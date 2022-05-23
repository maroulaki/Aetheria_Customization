from random import randint as rand

#Gemstones rolling tables from DMG
gems_10gp_d12 = ["Azurite (opaque mottled deep blue)", "Banded agate (translucent striped brown, blue, white, or red)", "Blue quartz (transparent pale blue)", "Eye agate (translucent circles of gray, white, brown, blue, or green)", "Hematite (opaque gray-black)", "Lapis lazuli (opaque light and dark blue with yellow flecks)", "Malachite (opaque striated light and dark green)", "Moss agate (translucent pink or yellow-white with mossy gray or green markings)", "Obsidian (opaque black)", "Rhodochrosite (opaque light pink)", "Tiger eye (translucent brown with golden center)", "Turquoise (opaque light blue-green)"]

gems_50gp_d12 = ["Bloodstone (opaque dark gray with red flecks)", "Carnelian (opaque orange to red-brown)", "Chalcedony (opaque white)", "Chrysoprase (translucent green)", "Citrine (transparent pale yellow-brown)", "Jasper (opaque blue, black, or brown)", "Moonstone (translucent white with pale blue glow)", "Onyx (opaque bands of black and white, or pure black or white)", "Quartz (transparent white, smoky gray, or yellow)", "Sardonyx (opaque bands of red and white)", "Star rose quartz (translucent rosy stone with white star-shaped center)", "Zircon (transparent pale blue-green)"]

gems_100gp_d10 = ["Amber (transparent watery gold to rich gold)", "Amethyst (transparent deep purple)", "Chrysoberyl (transparent yellow-green to pale green)", "Coral (opaque crimson)", "Garnet (transparent red, brown-green, or violet)", "Jade (translucent light green, deep green, or white)", "Jet (opaque deep black)", "Pearl (opaque lustrous white, yellow, or pink)", "Spinel (transparent red, red-brown, or deep green)", "Tourmaline (transparent pale green, blue, brown, or red)"]

#Art Objects rolling tables from DMG
art_25gp_d10 = ["Silver ewer", "Carved bone statuette", "Small gold bracelet", "Cloth-of-gold vestments", "Black velvet mask stitched with silver thread", "Copper chalice with silver filigree", "Pair of engraved bone dice", "Small mirror set in a painted wooden frame", "Embroidered silk handkerchief", "Gold locket with a painted portrait inside"]

art_250gp_d10 = ["Gold ring set with bloodstones", "Carved ivory statuette", "Large gold bracelet", "Silver necklace with a gemstone pendant", "Bronze crown", "Silk robe with gold embroidery", "Large well-made tapestry", "Brass mug with jade inlay", "Box of turquoise animal figurines", "Gold bird cage with electrum filigree"]

#Magic Item tables
A = {
	"1-50":"Potion of healing",
	"51-60":"Spell scroll (cantrip)",
	"61-70":"Potion of climbing",
	"71-90":"Spell scroll (1st level)",
	"91-94":"Spell scroll (2nd level)",
	"95-98":"Potion of greater healing",
	"99":"Bag of holding",
	"00":"Driftglobe"
}

B = {
	"01-15":"Potion of greater healing",
	"16-22":"Potion of fire breath",
	"23-29":"Potion of resistance",
	"30-34":"+1 ammunition",
	"35-39":"Potion of animal friendship",
	"40-44":"Potion of hill giant strength",
	"45-49":"Potion of growth",
	"50-54":"Potion of water breathing",
	"55-59":"Spell scroll (2nd level)",
	"60-64":"Spell scroll (3rd level)",
	"65-67":"Bag of holding",
	"68-70":"Keoghtom's ointment",
	"71-73":"Oil of slipperiness",
	"74-75":"Dust of disappearance",
	"76-77":"Dust of dryness",
	"78-79":"Dust of sneezing and choking",
	"80-81":"Elemental gem",
	"82-83":"Philter of love",
	"84":"Alchemy jug",
	"85":"Cap of water breathing",
	"86":"Cloak of the manta ray",
	"87":"Driftglobe",
	"88":"Goggles of night",
	"89":"Helm of comprehending languages",
	"90":"Immovable rod",
	"91":"Lantern of revealing",
	"92":"Mariner's armor",
	"93":"Mithral armor",
	"94":"Potion of poison",
	"95":"Ring of swimming",
	"96":"Robe of useful items",
	"97":"Rope of climbing",
	"98":"Saddle of the cavalier",
	"99":"Wand of magic detection",
	"00":"Wand of secrets",
}

C = {
	"01-15":"Potion of superior healing",
	"16-22":"Spell scroll (4th level)",
	"23-27":"+2 ammunition",
	"28-32":"Potion of clairvoyance",
	"33-37":"Potion of diminution",
	"38-42":"Potion of gaseous form",
	"43-47":"Potion of frost giant strength",
	"48-52":"Potion of stone giant strength",
	"53-57":"Potion of heroism",
	"58-62":"Potion of invulnerability",
	"63-67":"Potion of mind reading",
	"68-72":"Spell scroll (5th level)",
	"73-75":"Elixir of health",
	"76-78":"Oil of etherealness",
	"79-81":"Potion of fire giant strength",
	"82-84":"Quaal's feather token",
	"85-87":"Scroll of protection",
	"88-89":"Bag of beans",
	"90-91":"Bead of force",
	"92":"Chime of opening",
	"93":"Decanter of endless water",
	"94":"Eyes of minute seeing",
	"95":"Folding boat",
	"96":"Heward's handy haversack",
	"97":"Horseshoes of speed",
	"98":"Necklace of fireballs",
	"99":"Periapt of health",
	"00":"Sending stones",
}

F = {
	"01-15":"+1 weapon",
	"16-18":"+1 shield",
	"19-21":"Sentinel shield",
	"22-23":"Amulet of proof against detection and location",
	"24-25":"Boots of elvenkind",
	"26-27":"Boots of striding and springing",
	"28-29":"Bracers of archery",
	"30-31":"Brooch of shielding",
	"32-33":"Broom of flying",
	"34-35":"Cloak of elvenkind",
	"36-37":"Cloak of protection",
	"38-39":"Gauntlets of ogre power",
	"40-41":"Hat of disguise",
	"42-43":"Javelin of lightning",
	"44-45":"Pearl of power",
	"46-47":"+1 rod of the pact keeper",
	"48-49":"Slippers of spider climbing",
	"50-51":"Staff of the adder",
	"52-53":"Staff of the python",
	"54-55":"Sword of vengeance",
	"56-57":"Trident of fish command",
	"58-59":"Wand of magic missiles",
	"60-61":"+1 wand of the war mage",
	"62-63":"Wand of web",
	"64-65":"Weapon of warning",
	"66":"Adamantine chain mail",
	"67":"Adamantine chain shirt",
	"68":"Adamantine scale mail",
	"69":"Bag of tricks, gray",
	"70":"Bag of tricks, rust",
	"71":"Bag of tricks, tan",
	"72":"Boots of the winterlands",
	"73":"Circlet of blasting",
	"74":"Deck of illusions",
	"75":"Eversmoking bottle",
	"76":"Eyes of charming",
	"77":"Eyes of the eagle",
	"78":"Figurine of wondrous power, silver raven",
	"79":"Gem of brightness",
	"80":"Gloves of missile snaring",
	"81":"Gloves of swimming and climbing",
	"82":"Gloves of thievery",
	"83":"Headband of intellect",
	"84":"Helm of telepathy",
	"85":"Instrument of the bards, doss lute",
	"86":"Instrument of the bards, fochlucan bandore",
	"87":"Instrument of the bards, mac-fuirmidh cittern",
	"88":"Medallion of thoughts",
	"89":"Necklace of adaptation",
	"90":"Periapt of wound closure",
	"91":"Pipes of haunting",
	"92":"Pipes of the sewers",
	"93":"Ring of jumping",
	"94":"Ring of mind shielding",
	"95":"Ring of warmth",
	"96":"Ring of water walking",
	"97":"Quiver of ehlonna",
	"98":"Stone of good luck",
	"99":"Wind fan",
	"00":"Winged boots",
}

G ={
	"01-11":"+2 weapon",
	"12-14":"Figurine of Wondrous Power",
	"15":"Adamantine breastplate",
	"16":"Adamantine splint armor",
	"17":"Amulet of health",
	"18":"Armor of vulnerability",
	"19":"Arrow-catching shield",
	"20":"Belt of dwarvenkind",
	"21":"Belt of hill giant strength",
	"22":"Berserker axe",
	"23":"Boots of levitation",
	"24":"Boots of speed",
	"25":"Bowl of commanding water elementals",
	"26":"Bracers of defense",
	"27":"Brazier of commanding fire elementals",
	"28":"Cape of the mountebank",
	"29":"Censer of controlling air elementals",
	"30":"+1 chain mail",
	"31":"Chain mail of resistance",
	"32":"+1 chain shirt",
	"33":"Chain shirt of resistance",
	"34":"Cloak of displacement",
	"35":"Cloak of the bat",
	"36":"Cube of force",
	"37":"Daern's instant fortress",
	"38":"Dagger of venom",
	"39":"Dimensional shackles",
	"40":"Dragon slayer",
	"41":"Elven chain",
	"42":"Flame tongue",
	"43":"Gem of seeing",
	"44":"Giant slayer",
	"45":"Glamoured studded leather",
	"46":"Helm of teleportation",
	"47":"Horn of blasting",
	"48":"Horn of Valhalla",
	"49":"Instrument of the bards, canaith mandolin",
	"50":"Instrument of the bards, cli lyre",
	"51":"Ioun stone, awareness",
	"52":"Ioun stone, protection",
	"53":"Ioun stone, reserve",
	"54":"Ioun stone, sustenance",
	"55":"Iron bands of bilarro",
	"56":"+1 leather armor",
	"57":"Leather armor of resistance",
	"58":"Mace of disruption",
	"59":"Mace of smiting",
	"60":"Mace of terror",
	"61":"Mantle of spell resistance",
	"62":"Necklace of prayer beads",
	"63":"Periapt of proof against poison",
	"64":"Ring of animal influence",
	"65":"Ring of evasion",
	"66":"Ring of feather falling",
	"67":"Ring of free action",
	"68":"Ring of protection",
	"69":"Ring of resistance",
	"70":"Ring of spell storing",
	"71":"Ring of the ram",
	"72":"Ring of x-ray vision",
	"73":"Robe of eyes",
	"74":"Rod of rulership",
	"75":"+2 rod of the pact keeper",
	"76":"Rope of entanglement",
	"77":"+1 scale mail",
	"78":"Scale mail of resistance",
	"79":"+2 shield",
	"80":"Shield of missile attraction",
	"81":"Staff of charming",
	"82":"Staff of healing",
	"83":"Staff of swarming insects",
	"84":"Staff of the woodlands",
	"85":"Staff of withering",
	"86":"Stone of controlling earth elementals",
	"87":"Sun blade",
	"88":"Sword of life stealing",
	"89":"Sword of wounding",
	"90":"Tentacle rod",
	"91":"Vicious weapon",
	"92":"Wand of binding",
	"93":"Wand of enemy detection",
	"94":"Wand of fear",
	"95":"Wand of fireballs",
	"96":"Wand of lightning bolts",
	"97":"Wand of paralysis",
	"98":"+2 wand of the war mage",
	"99":"Wand of wonder",
	"00":"Wings of flying"
}

#GEM ROLLING FUNCTIONS
def roll_gems_10(gems):
	times = 2*rand(1,6)
	gems_10gp_d12.shuffle()
	for i in range(0,times):
		gems.append(gems_10gp_d12.pop())

def roll_gems_50(gems):
	times = 2*rand(1,6)
	gems_50gp_d12.shuffle()
	for i in range(0,times):
		gems.append(gems_50gp_d12.pop())

def roll_gems_100(gems):
	times = 3*rand(1,6)
	pool.extend(gems_100gp_d10)
	pool.extend(gems_100gp_d10)
	pool.shuffle()
	for i in range(0,3):
		gems.append(pool.pop())

#ART OBJECT ROLLING FUNCTIONS
def roll_art_25(art):
	times = 2*rand(1,4)
	art_25gp_d10.shuffle()
	for i in range(0,times):
		art.append(art_25gp_d10.pop())

def roll_art_250(art):
	times = 2*rand(1,4)
	art_250gp_d10.shuffle()
	for i in range(0,times):
		art.append(art_250gp_d10.pop())

#GOLD FOR CHART 1 ONLY
#For coins, a 4-position list is used as follows: gold=[PP,GP,SP,CP]
def roll_gold1(gold):
	gold.append(0)
	gold.append(10*2*rand(1,6))
	gold.append(100*3*rand(1,6))
	gold.append(100*6*rand(1,6))
#---------------COMMAND START----------------------
gold = []
gems = []
art = []

roll_gold1(gold)

dice = rand(1,100)
