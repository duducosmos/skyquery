#!/usr/bin/env python
__title__ = "QuasarSubSampleSDSS"
__author__ = "Eduardo S. Pereira"
__email__ = "pereira.somoza@gmail.com"
__data__ = "08/01/2012"
__versio__ = "0.1"

"""
This Script perform an query into the SkyServer of 
SDSS and return a statistical subsample os quasar based into the
work of Richards et al. (2006). See appendix of the article of these 
author.
The SQL Query is storage into the myquery variable. The query access
The SDSS DR7 and there are some correction into this query with respect
to presented by Richrds et al. (2006).

Also, it is used the data from DR7 quasar catalog ( Schneider et al. 2010) and 
DR7 quasar properties catalog (Shen et al. 2011) in order to produce a 
subsample of quasar and informations of these objects.


Bibliografy:
Richards et al. 2006. AJ, 131, 2760-2787.
Shen et al. 2011, AJ, 194,45.
Schneider et al. arXiv:1004.1167v1, 2010.
"""


from BeautifulSoup import BeautifulSoup
from string import replace
import sys
import urllib2
import sqlcl

class skyQuery:
    
    def __init__(self):
        self.defaultQuery = """SELECT  %s t.SpecObjID, t.ra, t.dec, mjd,plate,
fiberID,z,zErr,zConf,specClass
FROM Target as t
--Match to the tables with geometry and version information
inner JOIN Region as r on t.regionid = r.regionid
inner JOIN TargetInfo as ti on t.targetId = ti.targetid
-- Extract the TARGET photometry
inner JOIN TARGDR7..PhotoTag as p on ti.targetObjId = p.objID
-- Match to objetcs with spectroscopy
LEFT OUTER JOIN specObj as s on s.targetid = t.targetId
WHERE(
-- Restrict sample to target selection version v3_1_0
     r.regionid in (
         SELECT b.boxid FROM region2box as b, tilinggeometry as g
         WHERE b.boxtype = 'SECTOR'
         AND b.regiontype = 'TIPRIMARY' 
         AND b.id = g.tilinggeometryid 
         GROUP BY b.boxid
         HAVING MIN(g.targetversion) >= 'v3_1_0'
     )
     AND
     -- Include only primary objects
         ((p.mode =1) AND (p.status & 0x10) > 0) AND ((p.status & 0x2000) > 0) 
     AND
     -- Include only explicit quasar targets
         ((p.primTarget & 0x0000001f) >0)
     AND 
     -- Include only quasar confirmed by spectral analisys
         (s.SpecClass > 2)
    AND
         (s.SpecClass < 5)
     AND
         (s.zConf > 0.3)
    AND
        (s.z > 0.0)
)
""" %''
    def progress_bar(self, value, max, barsize):
        """Implementa barra de progressos em modo texto:
    Exemplo de uso:
    
    >>print "processing..."
    >>for i in xrange(11):
       progress_bar(i, 10, 40)
       time.sleep(1)
    >>print "ok"
    >>raw_input()
        """
        chars = int(value * barsize / float(max))
        percent = int((value / float(max)) * 100)
        sys.stdout.write("#" * chars)
        sys.stdout.write(" " * (barsize - chars + 2))
        if value >= max:
            sys.stdout.write("done. \n\n")
        else:
            sys.stdout.write("[%3i%%]\r" % (percent))
            sys.stdout.flush()
    
    def dataExtraction(self, tables):
        """Given a HTML table int the format of the data from SkyServer of SDSS, return all the values into a python list
        >>> table = ''' <table border='1' BGCOLOR=cornsilk>
    <tr align=center><td><font size=-1>targetID</font></td></tr>
    <tr align=center BGCOLOR=#eeeeff><td nowrap><font size=-1>1</font></td></tr>
    </table>'''
        >>> dataExtraction(table)
        [['targetID'],['1']]
        """
        print 'Extracting data obtained from SkyServer'
        html2 = '''<html><head>
        <title>SDSS Query Results</title>
        </head><body bgcolor=white>
        %s
        </BODY></HTML>
        ''' %tables[0]
        soup2 = BeautifulSoup(html2)
        
        line = 0
        Sample = []
        #Sample2 = ""
        rows = soup2.findAll("tr")
        lendata = len(rows)
        self.progress_bar(line, lendata, 40)
        for row in  rows:
            if (line == 0):
                data = replace(str(row), "<tr align=\"center\">", '')
                data = replace(data, '</tr>', '')
                data = replace(data, '<td><font size=\"-1\">', '')
                data= replace(data, '</font>', '')
                data = replace(data, '</td>', ';')
                Sample.append(data.split(';')[:-1])
                line+=1
            else:
                data = replace(str(row), "<tr align=\"center\" bgcolor=\"#eeeeff\">", '')
                data = replace(data, '</tr>', '')
                data = replace(data, '<td nowrap=\"nowrap\"><font size=\"-1\">', '')
                data= replace(data, '</font>', '')
                data = replace(data, '</td>', ';')
                data = replace(data, '\t', '')
                data = replace(data, '\r\n', ' ')
                data = replace(data,'<td nowrap><font size=\"-1\">','')
                Sample.append(data.split(';')[:-1])

            self.progress_bar(line, lendata, 40)
        
        #arq = open('subsample.dat', 'w')
        #arq.write(Sample2)
        #arq.close()
        print 'Finished...'
        return Sample
        
    def dataQuery(self, myquery):
        """ Return a table or print a error of data query from SkyServer of SDSS.
        """
        print 'Quering the SkySever'
        page =  sqlcl.query(myquery, fmt='html').read()
        soup = BeautifulSoup(page)
        tables = [table for table in soup.findAll("table")]    
        if (len(tables) >=1):
            print 'Data recived'
            return tables
        else:
            h3 = [h for h in soup.findAll("h3")]
            error =  str(h3[1])
            error = replace(error,'<h3 bgcolor=\"pink\"><font color=\"red\">', '' )
            error = replace(error,'</font></h3>', '' )
            error = replace(error, '<br />', '\n')
            print error
            return (None,error)
