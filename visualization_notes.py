'''
Created by Stephen Mendoza Jr. @stevemendozajr
Last updated 08-09-19
'''

'''
Seaborn Coloring
'''

####### default color palettes
deep, muted, bright, pastel, dark, colorblind

####### to view your current color pallete
current_palette = sns.color_palette()
sns.palplot(current_palette)

####### to set a permanent palette
sns.set_palette()

####### to temporarily set your color pallete
#8 colors you will have
temp_palette = sns.color_palette("hls", 8)
#to view your palette
sns.palplot(temp_palette)

#using husl palette
#hsl are floates between 0 and 1
sns.palplot(sns.husl_palette(10, h=.5)

###### crayola colors
sns.crayon_palette(colors)

#xkcd colors
colors = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
sns.palplot(sns.xkcd_palette(colors)

#favorite xkcd colors
"cerulean" #blue hue
"ocean blue" #blue hue
"coral" #orange hue
"electric blue" #blue hue
"reddish orange" #orange hue
"bright orange" #orange hue
"lightish blue" #blue hue
"blood orange" #orange hue
"rich blue" #blue hue
"electric lime" #green hue
"toxic green" #green hue


#to temporarily set your color palette with a with statement
with sns.color_palette("coolwarm"):
    distplot()

###### to choose specific hex color codes to use
my_color_list = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
sns.color_palette(flatui)

####### for blue sequential color
#from light blue to dark blue
#uses the color brewer names
#adding _r after color name will reverse order from dark to light
sns.palplot(sns.color_palette("Blues")


####### for custom sequential colors
sns.palplot(sns.light_palette("green")
#for darks
sns.palplot(sns.dark_palette("purple")


####### for a diverging color palette
#coolwarm is a built in diverging palette. this is not customized
#blue on end, white in middle, red on end
sns.palplot(sns.color_palette("coolwarm", 7)

####### for a custom diverging color palette
sns.palplot(sns.diverging_palette(220, 20, n=7)



#quick histogram of an attribute using matplotlib
plt.figure(figsize=(12,8))
plt.hist(df['Column_Name'], color='green',bins=10)
plt.xlabel('Column_Name')
plt.ylabel('Frequency')
plt.title("title goes here histogram")
plt.show()

#Seaborn Stuff

#histogram defaults
seaborn.distplot(df[Column_Name], 
bins=None, 
hist=True, 
kde=True, 
rug=False, 
fit=None, 
hist_kws=None, 
kde_kws=None, 
rug_kws=None, 
fit_kws=None, 
color=None, 
vertical=False, 
norm_hist=False, 
axlabel=None, l
abel=None, 
ax=None)

#jointplot defaults
seaborn.jointplot(x, y, 
data=None, 
kind='scatter', 
stat_func=None, 
color=None, 
height=6, r
atio=5, 
space=0.2, 
dropna=True, 
xlim=None, 
ylim=None, 
joint_kws=None, 
marginal_kws=None, 
annot_kws=None, 
**kwargs)

#pairplot defaults
seaborn.pairplot(data, 
hue=None, 
hue_order=None, 
palette=None, 
vars=None, 
x_vars=None, 
y_vars=None, 
kind='scatter', 
diag_kind='auto', 
markers=None, 
height=2.5, 
aspect=1, 
dropna=True, 
plot_kws=None, 
diag_kws=None, 
grid_kws=None, 
size=None)

#histogram - using seaborn to make a histogram
#with a kernel density estimate
sns.distplot(df[Column_Name], kde=True, rug=True, color="y");

#histogram with line distrubtion only
#kernel density estimate only
sns.distplot(x, hist=False, rug=True);


#bivariate distribution 
# scatter plot with regression line in the middle
# histogram of 2 attributes on the outside borders
sns.jointplot(x="Column_Name", y="Column_Name", data=df, kind="reg");

#pairwise plots
#bivariate plots of all numerical attributes in a dataframe
sns.pairplot(dataframe, hue="species", palette="husl");