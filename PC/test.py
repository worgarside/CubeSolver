# """\
# ------------------------------------------------------------
# USE: python <PROGNAME> (options)
# OPTIONS:
#     -h : print this help message
#     -s : use "with stoplist" configuration (default: without)
#     -p : use "with stemming" configuration (default: without)
#     -w LABEL : use weighting scheme "LABEL" (LABEL in {binary, tf, tfidf}, default: binary)
#     -o FILE : output results to file FILE (default: output to stdout)
# ------------------------------------------------------------\
# """
#
# import getopt
# import re
# import sys
#
#
#
#
# def printHelp():
#     help = __doc__.replace('<PROGNAME>', sys.argv[0], 1)
#     print(help, file=sys.stderr)
#     sys.exit()
#
#
#
# if __name__ == '__main__':
#
#     opts, args = getopt.getopt(sys.argv[1:], 'hspw:o:')
#
#     opts = dict(opts)
#     print(opts)
#     exit()
#     if '-h' in opts:
#         printHelp()
#
#     if len(args) > 0:
#         print("*** ERROR: no arg files - only options! ***", file=sys.stderr)
#         printHelp()
#
#     if '-w' in opts:
#         if opts['-w'] in ('binary', 'tf', 'tfidf'):
#             termWeighting = opts['-w']
#         else:
#             warning = (
#                 "*** ERROR: term weighting label (opt: -w LABEL) not recognised! ***\n"
#                 " -- must be one of: binary / tf / tfidf")
#             print(warning, file=sys.stderr)
#             printHelp()
#     else:
#         termWeighting = 'binary'
#
#     if '-o' in opts:
#         outfile = opts['-o']
#     else:
#         outfile = None
#
#     if '-s' in opts and '-p' in opts:
#         indexFile = 'index_withstoplist_withstemming.txt'
#         queriesFile = 'queries_withstoplist_withstemming.txt'
#     elif '-s' in opts:
#         indexFile = 'index_withstoplist_nostemming.txt'
#         queriesFile = 'queries_withstoplist_nostemming.txt'
#     elif '-p' in opts:
#         indexFile = 'index_nostoplist_withstemming.txt'
#         queriesFile = 'queries_nostoplist_withstemming.txt'
#     else:
#         indexFile = 'index_nostoplist_nostemming.txt'
#         queriesFile = 'queries_nostoplist_nostemming.txt'


print('testing')