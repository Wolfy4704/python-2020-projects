#pickling data
#brayden woodard
#12/20


#imports
import pickle, shelve

variety = ["sweet", "hot", "dill",  "bread and butter", "sour"]
shape = ["chips", "spear", "chuncks", "gherkins", "salad cubes"]
brand = ["kroger", "vlasic", "private selection", "boars head", "mt olive"]

##file = open("C:/Users/brayden.woodard/Desktop/read_write/assets/saved_data/pickles1.dat", "wb")
##pickle.dump(variety,file)
##pickle.dump(shape,file)
##pickle.dump(brand,file)
##
##file.close()
##
##file = open("C:/Users/brayden.woodard/Desktop/read_write/assets/saved_data/pickles1.dat", "rb")
##
##brand = pickle.load(file)
##shape = pickle.load(file)
##variety = pickle.load(file)
##
##print(brand)
##print(shape)
##print(variety)
##
##file.close()

try:
    sFile = shelve.open("C:/Users/brayden.woodard/Desktop/read_write/assets/saved_data/pickles2.dat")

except IOError as e:
    print("something went wrong")
    sys.exit()
except IndexError as i:
    print("something went wrong")
    sys.exit()
else:
    quit()
    
sFile["variety"] = variety
sFile["shape"] = shape
sFile["brand"] = brand
sFile.sync()

brand = sFile["brand"]
shape = sFile["shape"]
variety = sFile["variety"]

print(brand)
print(shape)
print(variety)

sFile.close()







                    
