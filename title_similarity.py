import numpy as np

# lowercase word, remove punctuation, optionally return nothing if word is 
# a stopword, optionally reduce word to its root
def process(word, stopwords=True, stemming=True):
		#lowercase all words			
		word = word.lower()
		punctuation = {
			'"', '!', '?', ',', ':', ';','/', '<', '>', '.', '`', '~', '[', ']',
			'$', '&', '_', '@', '(', ')', '{', '}', '|', '%', '#', '^', '=', '+',
		}
		for el in punctuation:
			if el in word:
				return word.replace(el, '')
		stopwords = [
			"a","able","about","above","abst","accordance","according","accordingly","across","act","actually","added","adj","affected","affecting",
			"affects","after","afterwards","again","against","ah","all","almost","alone","along","already","also","although","always","am","among",
			"amongst","an","and","announce","another","any","anybody","anyhow","anymore","anyone","anything","anyway","anyways","anywhere","apparently",
			"approximately","are","aren","arent","arise","around","as","aside","ask","asking","at","auth","available","away","awfully","b","back","be",
			"became","because","become","becomes","becoming","been","before","beforehand","begin","beginning","beginnings","begins","behind","being",
			"believe","below","beside","besides","between","beyond","biol","both","brief","briefly","but","by","c","ca","came","can","cannot","can't",
			"cause","causes","certain","certainly","co","com","come","comes","contain","containing","contains","could","couldnt","d","date","did","didn't",
			"different","do","does","doesn't","doing","done","don't","down","downwards","due","during","e","each","ed","edu","effect","eg","eight","eighty",
			"either","else","elsewhere","end","ending","enough","especially","et","et-al","etc","even","ever","every","everybody","everyone","everything",
			"everywhere","ex","except","f","far","few","ff","fifth","first","five","fix","followed","following","follows","for","former","formerly","forth",
			"found","four","from","further","furthermore","g","gave","get","gets","getting","give","given","gives","giving","go","goes","gone","got","gotten",
			"h","had","happens","hardly","has","hasn't","have","haven't","having","he","hed","hence","her","here","hereafter","hereby","herein","heres",
			"hereupon","hers","herself","hes","hi","hid","him","himself","his","hither","home","how","howbeit","however","hundred","i","id","ie","if",
			"i'll","im","immediate","immediately","importance","important","in","inc","indeed","index","information","instead","into","invention","inward",
			"is","isn't","it","itd","it'll","its","itself","i've","j","just","k","keep	keeps","kept","kg","km","know","known","knows","l","largely",
			"last","lately","later","latter","latterly","least","less","lest","let","lets","like","liked","likely","line","little","'ll","look","looking",
			"looks","ltd","m","made","mainly","make","makes","many","may","maybe","me","mean","means","meantime","meanwhile","merely","mg","might",
			"million","miss","ml","more","moreover","most","mostly","mr","mrs","much","mug","must","my","myself","n","na","name","namely","nay","nd",
			"near","nearly","necessarily","necessary","need","needs","neither","never","nevertheless","new","next","nine","ninety","no","nobody","non",
			"none","nonetheless","noone","nor","normally","nos","not","noted","nothing","now","nowhere","o","obtain","obtained","obviously","of","off",
			"often","oh","ok","okay","old","omitted","on","once","one","ones","only","onto","or","ord","other","others","otherwise","ought","our","ours",
			"ourselves","out","outside","over","overall","owing","own","p","page","pages","part","particular","particularly","past","per","perhaps",
			"placed","please","plus","poorly","possible","possibly","potentially","pp","predominantly","present","previously","primarily","probably",
			"promptly","proud","provides","put","q","que","quickly","quite","qv","r","ran","rather","rd","re","readily","really","recent","recently",
			"ref","refs","regarding","regardless","regards","related","relatively","research","respectively","resulted","resulting","results","right",
			"run","s","said","same","saw","say","saying","says","sec","section","see","seeing","seem","seemed","seeming","seems","seen","self","selves",
			"sent","seven","several","shall","she","shed","she'll","shes","should","shouldn't","show","showed","shown","showns","shows","significant",
			"significantly","similar","similarly","since","six","slightly","so","some","somebody","somehow","someone","somethan","something","sometime",
			"sometimes","somewhat","somewhere","soon","sorry","specifically","specified","specify","specifying","still","stop","strongly","sub",
			"substantially","successfully","such","sufficiently","suggest","sup","sure	t","take","taken","taking","tell","tends","th","than","thank",
			"thanks","thanx","that","that'll","thats","that've","the","their","theirs","them","themselves","then","thence","there","thereafter","thereby",
			"thered","therefore","therein","there'll","thereof","therere","theres","thereto","thereupon","there've","these","they","theyd","they'll",
			"theyre","they've","think","this","those","thou","though","thoughh","thousand","throug","through","throughout","thru","thus","til","tip","to",
			"together","too","took","toward","towards","tried","tries","truly","try","trying","ts","twice","two","u","un","under","unfortunately","unless",
			"unlike","unlikely","until","unto","up","upon","ups","us","use","used","useful","usefully","usefulness","uses","using","usually","v","value",
			"various","'ve","very","via","viz","vol","vols","vs","w","want","wants","was","wasnt","way","we","wed","welcome","we'll","went","were","werent",
			"we've","what","whatever","what'll","whats","when","whence","whenever","where","whereafter","whereas","whereby","wherein","wheres","whereupon",
			"wherever","whether","which","while","whim","whither","who","whod","whoever","whole","who'll","whom","whomever","whos","whose","why","widely",
			"willing","wish","with","within","without","wont","words","world","would","wouldnt","www","x","y","yes","yet","you","youd","you'll","your",
			"youre","yours","yourself","yourselves","you've","z","zero"]
		if stopwords == True:
			if word in stopwords:
				return None
		#stemming, only apply to 4 letter words or greater
		if stemming == True:
			if len(word) > 3:
				suffixes = {
					#'iest', 'sion', 'tion', 'ative', 'able',
					'ary', 'ate', 'ful', 'ine', 'ing', 'ily', 'ade', 'age',
					'ty', 'en', 'es', 'ed', 'al', 'cy', 'ee', 'er','y', 's',
					#'ingly', 'ency', 'ment',
					'ing', 'ly', 'ed', 'es', 'le', 's', 'y'
				}
				exceptions = {
					"'",
					"-",
				}
				#ignore stemming on words with the exceptions
				for el in exceptions:
					if el in word:
						return word
				#look for endings to stem
				if word[-5:] in suffixes:
					return word[:-5]
				elif word[-4:] in suffixes:
					return word[:-4]
				elif word[-3:] in suffixes:
					return word[:-3]
				elif word[-2:] in suffixes:
					return word[:-2]
				elif word[-1:] in suffixes:
					return word[:-1]
				else:
					return word
			#word too short to stem
			else:
				return word
		return word

def cosine_similarity(vect1, vect2):
	dot_product = np.dot(vect1, vect2)
	norm_1 = np.linalg.norm(vect1)
	norm_2 = np.linalg.norm(vect2)
	return dot_product / (norm_1 * norm_2)

def vectorize(title1, title2, stopwords=True, stemming=True):
	print ('Title 1: ', title1)
	print ('Title 2: ', title2)
	t1 = title1.split()
	t2 = title2.split()
	tf_1 = {}
	tf_2 = {}
	for word in t1:
		word = process(word, stopwords=bool(stopwords), stemming=bool(stemming))
		if word is None:
			continue
		if word in tf_1:
			tf_1[word] += 1
		else:
			tf_1[word] = 1
	for word in t2:
		word = process(word, stopwords=bool(stopwords), stemming=bool(stemming))
		if word is None:
			continue
		if word in tf_2:
			tf_2[word] += 1
		else:
			tf_2[word] = 1

	all_words = set(tf_1.keys()).union(set(tf_2.keys()))
	vect1 = []
	vect2 = []
	for word in all_words:
		if word in tf_1:
			vect1.append(tf_1[word])
		else:
			vect1.append(0)
		if word in tf_2:
			vect2.append(tf_2[word])
		else:
			vect2.append(0)
	return np.array(vect1), np.array(vect2)


title1 = "Tyson recalls 36,000 pounds of chicken nuggets after complaints about rubber in product"
title2 = "Tyson Foods recalls more than 36,000 pounds of chicken nuggets after possible rubber contamination"
title3 = "Polar Vortex Live Updates: Extreme Cold Weather Grips Midwest"

vect1, vect2 = vectorize(title1, title2, stopwords=False, stemming=False)
sim = cosine_similarity(vect1, vect2)

if sim > 0.6:
	print ('Titles are similar: ', sim)
else:
	print ('Title are not similar: ', sim)