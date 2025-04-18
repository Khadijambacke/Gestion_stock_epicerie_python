ensinv={"khadija","faatou","momy","hidayat","cheikh","bintou","ndella"}
conf={"khadija","faatou","momy"}
#noc={"cheikh","bintou","ndella"}
ensall={"faatou","momy","hidayat","ndella"}
#conf qui sont all
confall=conf.intersection(ensall)
print(confall)
#confir et sans all
confsall=conf-confall
print(confsall)
res=confsall.count()
print(res)