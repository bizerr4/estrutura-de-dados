#10 (FB=-2)
# \
#  20 (FB=-1)
#   \
#    30

#rotação direita-direita

#  20
# /  \
#10   30


# 20 (FB=-2)
# /  \
#10   30 (FB=-1)
#     \
#      40 (FB=-1)
#       \
#        50

#rotação direita-direita
#
#   20
# /  \
#10   40
#    /  \
#   30   50

#       20 (FB=-2)  <- Desbalanceado
#     /  \
#    10   40 (FB=1)
#        /  \
#       30   50
#      /
#     25   

#direita-esquerda

#      20
#     /  \
#    10   30
#        /  \
#       25   40
#            \
#             50

#arvore final
#       30 (FB=0)
#       /  \
#   20 (FB=0)   40 (FB=-1)
#  / \        \
#10  25       50