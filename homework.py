def text_lenght_calc():
    """
    Metin Uzunluğu Hesapma Fonksiyonu
    """    
    text = input("Enter the text: ")

    print(len(text))


def first_and_last_char():
    """
    Kullanıcı tarafından girilen bir metnin ilk iki ve son iki karakterini ekrana yazdıran Python programını yazınız.
    """

    text = input("Enter the text: ")

    print(text[:2],text[-2:])


def change_char():
    """
    Kullanıcıdan değişecek metin ve eski harf ve yeni harf bilgisini alarak girilen metin üzerinden değişikliği yapıp sonucu ekrana yazdıran Python programını yazınız.
    """

    text = input("Enter the text: ")
    old_char = input("Enter the old word: ")
    new_char = input("Enter the new word: ")

    print(text.replace(old_char,new_char))

def check_palindrome():
    """
    Kullanıcı tarafından girilen bir kelimenin palindrom olup olmadığını karşılaştırma operatöründen faydalanarak print() fonksiyonu ile ekrana yazdırınız.
    """

    text = input("Enter the text: ")
    text_no_space = text.replace(" ","")

    # one line if-else
    print("This is palindrome ") if text_no_space == text_no_space[::-1] else print("Not palindrome")

    # if text_no_space == text_no_space[::-1]:
    #     print ("true")
    # else:
    #     print ("false")



def last_char_multi_with_four():
    """
    Girilen bir metnin son 2 karakterini 4 defa çoğaltarak ekrana yazan Python programını yazınız. * aritmetik operatöründen faydalanabilirsiniz.
    """

    text = input("Enter the text: ") 

    print(text[-2:]*4)

def change_list():
    """
    5 elemanlı bir liste oluşturunuz. Bu liste içerisindeki 2. elemanı 100 ile değiştiren python kodu yazınız.
    """

    liste1 = [15,16,17,18,20]
    print(liste1)
    liste1[1] = 100
    print(liste1)

def conca_two_list():
    """
    İki farklı listede tutulan verileri tek bir listede  "+" operatörü ile birleştiren python kodunu yazınız.
    """
    # With "+"
    liste1 = [1,2,3,4,5]
    liste2 = [6,7,8,9,10]
    liste3 = liste1 + liste2
    print(liste3)

def conca_two_list_with_appe():
    """
    İki farklı listede tutulan verileri tek bir listede  append ile birleştiren python kodunu yazınız.
    """
    # With append ?
    liste1 = [1,2,3,4,5]
    liste2 = [6,7,8,9,10]
    
    for i in liste2:
        liste1.append(i)
    print(liste1)


def conca_two_list_with_exte():
    """
    İki farklı listede tutulan verileri tek bir listede extend  ile birleştiren python kodunu yazınız.
    """
    # With extend 
    liste1 = [1,2,3,4,5]
    liste2 = [6,7,8,9,10]
    liste1.extend(liste2)
    print(liste1)

def add_first_index():
    """
    Oluşturduğunuz 3 elemanlı bir liste içerisine ilk sıraya "Elma" kelimesini ekleyiniz.
    """
    liste1 = [1,2,3]
    liste1.insert(0,"Elma")
    print(liste1)

def remove_first_three():
    """
    liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23] yukarıdaki listeden ilk 3 sayısını silip ekrana yazdırınız.
    """
    liste = [1,2,3,4,5,6,7,1,3,3,3,2,2,1,23]

    liste.remove(3)

    print(liste)

def copy_add_list():
    """
    iste1 = ["1",1,2,"3"] Yukarıdaki listenin bir kopyasını alarak 250 sayısını listenin sonuna ekleyiniz,her iki listeyi ekrana yazdırınız.
    """
    liste1 = ["1",1,2,"3"]
    liste2 = liste1.copy()
    #liste2 = list(list1)
    liste2.append(250)
    print("Liste1 Çıktısı =>",liste1)
    print("Liste2 Çıktısı =>",liste2)

def conca_two_dict():
    """
    Aşağıdaki üç farklı sözlüğü tek sözlükte birleştiren python kodunu yazınız dict1={1:10, 2:20} dict2={3:30, 4:40} dict3={5:50,6:60} Beklenen Çıktı : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 
    """
    dict1 = {1:10, 2:20} 
    dict2 = {3:30, 4:40} 
    dict3 = {5:50, 6:60}
    print({**dict1,**dict2,**dict3})

def remove_last_ele_dict():
    """
    sozluk ={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} Sözlükteki en son elemanı silerek ekrana işlem sonucunu yazdırınız Beklenen Çıktı :(6,60)
    """
    sozluk = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    print(sozluk.popitem())

def add_item_to_dict():
    """
    dict1={1:10, 2:20} Yukarıdaki sözlüğe bir eleman ekleyiniz. Beklenen Çıktı :{1:10, 2:20, 3:30}
    """
    dict1 = {1:10, 2:20} 
    dict1[3] = 30
    print(dict1)

def list_to_dict():
    """
    liste=[1,2,3,4,5] a.Yukarıdaki listeden faydalanarak bir sözlük oluşturun b.sözlüğün her alamanının karşılığına değer olarak anahtarda bulunan sayısal değerin 10 katını eşitleyin. Beklenen Çıktı : a. {1:0,2:0,3:0,4:0,5:0} b. {1:10,2:20,3:30,4:40,5:50}
    """
    liste1 = [1,2,3,4,5]
    dict1 = {i: 0 for i in liste1}
    print(dict1)
    dict1 = {i: i*10 for i in dict1.keys()}
    print("*******")
    print(dict1)

def key_add_dict():
    """
    sozluk={1:10,2:20,3:30,4:40,5:50} Sözlük içerisine 6 sayısını anahtar olarak değeri 60 olacak şekilde setdefault fonksiyonunu kullanarak ekleyiniz
    """
    dict1 = {1:10,2:20,3:30,4:40,5:50}
    dict1.setdefault(6,60)
    print(dict1)

def list_in_dict_sort():
    """
    Bir listeyi bir sözlükte sıralamak için bir Python programı yazın
    Örnek Veri: num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
    """
    num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
    num = {key:sorted(value) for key,value in num.items()}
    print(num)

def rem_wspace_key():
    """
    sozluk = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
    ilgili sözlükten anahtar kısımlarında bulunan boşlukları temizleyen python kodu yazınız. 
    """
    sozluk = {'S 001': ['Math', 'Science'], 'S 002': ['Math', 'English']}
    sozluk = {key.replace(" ",""):value for key,value in sozluk.items()}
    print(sozluk)

def concatenate_two_list():
    """
    liste1=[1,2,3] liste2=[4,5,6,7,8] iki listeyi liste3 ile birleştiriniz.
    """
    liste1 = [1,2,3] 
    liste2 = [4,5,6,7,8]
    liste3 = liste1 + liste2
    print(liste3)

def del_el_list():
    """
    liste=[1,2,3,4,5,6] listesindeki 1. elemanı del komutu ile siliniz.
    """
    liste=[1,2,3,4,5,6]
    del(liste[0])
    print(liste)



def add_last_list():
    """
    liste=["elma" , "armut", "çilek"] listesine append komutu ile sona 3 elemanını ekleyiniz.
    """
    liste=["elma" , "armut", "çilek"]
    liste.append(3)
    print(liste)


def max_thre_value_list():
    """
    Girilen on sayı içerisinden en büyük üç sayıyı bulmak için bir Python fonksiyonu yazınız.
    """
    #num = list(map(int,input("Enter 10 number with ',' : ").split(",")))
    num = [int(input(f"{i+1} . number : ")) for i in range(10)]
    num.sort()
    print(num[-3:])

def low_up_letter():
    """
    Bir metin içerisindeki büyük ve küçük harflerin listesini yazdıran python programını yazınız.
    """
    text = input("Enter the text: ").replace(" ","")
    lower_letters = [i for i in text if i != str.upper(i)]
    upper_letters = [i for i in text if i == str.upper(i)]
    # for i in text:
    #     if i == str.upper(i):
    #         upper_letters.append(i)
    #     else:
    #         lower_letters.append(i)
    
    print(lower_letters)
    print(upper_letters)



def odd_or_even():
    """
    Kullanıcıdan alınan 10 sayının çift ve tek sayıların sayısını ekrana yazdıran programı yazınız. 
    """
    
    num = [int(input(f"{i+1} . number : ")) for i in range(10)]
    odd_num = [i for i in num if i % 2 !=0]
    even_num = [i for i in num if i % 2 ==0]
    print("Odd numbers : ",len(odd_num))
    print("Even numbers : ",len(even_num))

