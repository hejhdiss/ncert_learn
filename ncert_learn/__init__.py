# ncert_learn/__init__.py
__version__ = "2.7.2"

from .intfncs import checkprime,factors,len_fibonacci,checkarmstrong,reverse,checkpalindrome,checkstrong,checkniven,prime,armstrong,strong,niven,palindrome,len_armstrong,len_strong,len_niven,len_palindrome,checkeven,checkodd,checkzero,checknegative,checkpositive
from .stkdict import clearstackdict,createstackdict,pushstackdict,popstackdict,peekstackdict,displaymodestackdict# Import functions
from .stklist import createstacklst,clearstacklst,pushstacklst,popstacklst,peekstacklst,displaymodestacklst
from .dat import studyexamples,studyfunctions,studyshort,studymysqlpython,notes,basics,mysqlnotes
from .area import areaofcircle,areaofpolygon,areaofrectangle,areaofsquare,areaoftriangle
from .conversions import integertobinary,integertooctal,integertohexadecimal,binarytointeger
from .mysql import mysqlconnect,mysqlconnectwithdatabase,mysqlshowdatabases,mysqlcreatedatabase,mysqlshowtables,mysqlshowtablesfromdatabase,mysqldescribetable,mysqldescribetablefromdatabase,mysqlfetchalltable,mysqlfetchalltablefromdatabase,mysqlcreatetable,mysqltableinsert,mysqlrowcounttablefromdatabase,mysqlexecutequery
from .sort import bubblesort,insertionsort
from .text import istextfile,copytextfromonetoanother,opentextfile,addlinetofile,readtextfile,cleartextfile,readspecificline
from .os import getexecutablepath,cpucount,listdir,listdirfrompath,osname,processorname,isnetworkconnected,getpythoninterpreter
from .packageinstall import install_library,install_librariesfromlist
from .support import supportemail,feedbackemail,bugtrackerurl,githuburl,documentationurl,authorname
from .time import currenttime,processtime,monotonic,threadtime
# Optional: List functions to include in 'import *' calls
__all__ = ['mysqlconnectwithdatabase','exampleusage','checkprime','factors','len_fibonacci','checkarmstrong','reverse','checkpalindrome','checkstrong','checkniven','prime','armstrong','strong','niven','palindrome','len_armstrong','len_strong','len_niven','len_palindrome','checkeven','checkodd','checkzero','checknegative','checkpositive','clearstackdict','createstackdict','pushstackdict','popstackdict','peekstackdict','displaymodestackdict','createstacklst','clearstacklst','pushstacklst','popstacklst','peekstacklst','displaymodestacklst','studyexamples','studyfunctions','studyshort','studymysqlpython','notes','basics','extendednotes','mysqlnotes'
           ,'bubblesort','insertionsort','mysqlconnect','mysqlshowdatabases','mysqlcreatedatabase','mysqlshowtables','mysqlshowtablesfromdatabase','mysqldescribetable','mysqldescribetablefromdatabase','mysqlfetchalltable','mysqlfetchalltablefromdatabase','mysqlcreatetable','mysqltableinsert','mysqlrowcounttablefromdatabase','mysqlexecutequery',
           'integertobinary','integertooctal','integertohexadecimal','binarytointeger','areaofcircle','areaofpolygon','areaofrectangle','areaofsquare','areaoftriangle',
           'istextfile','copytextfromonetoanother','opentextfile','addlinetofile','readtextfile','cleartextfile','readspecificline',
           'getexecutablepath','cpucount','listdir','listdirfrompath','osname','processorname','isnetworkconnected','getpythoninterpreter',
           'install_library','install_librariesfromlist',
           'supportemail','feedbackemail','bugtrackerurl','githuburl','documentationurl','authorname',
           'currenttime','processtime','monotonic','threadtime']
