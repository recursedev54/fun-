import math
from collections import Counter

def shannon_entropy(text):
    # Count the occurrences of each character in the text
    char_count = Counter(text)
    
    # Total number of characters in the text
    total_chars = len(text)
    
    # Calculate the probability of each character
    probabilities = [char_count[char] / total_chars for char in char_count]
    
    # Calculate Shannon entropy
    entropy = -sum(p * math.log2(p) for p in probabilities)
    
    return entropy

def find_top_words_with_entropy(corpus, num_words=100):
    words = corpus.split()
    
    word_entropies = []
    for word in words:
        entropy = shannon_entropy(word)
        word_entropies.append((word, entropy))
    
    # Sort the word_entropies list based on entropy in descending order
    word_entropies.sort(key=lambda x: x[1], reverse=True)
    
    return word_entropies[:num_words]

def main():
    corpus = r"""
1.
Press Space To Start - Boyfriend of the Year (free) 02:39
lyrics
download
2.
Someone Help Me, I Can't Find My Phone (And I Want To Go Home Now) (free) 05:44
3.
Untitled pt.1 (free) 05:20
4.
I Love You Like A Beach House Song But I Don't Know How To Tell You (free) 03:28
5.
The Western Song (Hell) (free) 06:08
6.
Epilogue (Heaven) (free) 09:37
Boyfriend of the Year (lyrics)
Congratulations you did it
Boyfriend of the year
You really saved your relationship
You really should cheer
I've tried confessing a thousand times before
In every situation, you close the goddamn door

Someone Help Me, I Can't Find My Phone (And I Want To Go Home Now) (lyrics)
they said we wouldn't last but here we are in each other's arms
the broken me's of the past are coming back to haunt me

I've got one that's drunk, one that's stoned, one that's barely alive
but the one that keeps me up at night is the one who keeps me going forward

I don't know why you hate the sound of your own voice on recording
I don't know why the weather changes, or gets so boring

and in the end, I knew no one was listening

someone help me I can't find my phone
and I wanna go home now
I'm so sick of my friends house
I'm getting sick of myself now

Hey mom, can you pick me up?
No, I don't wanna drive, can you pick me up?
No, I'm not on drugs, can you pick me up?
Yes, I'll go to college, can you pick me up?

I've got this feeling and it won't go away
fear about the future and it wont go away
losing all my friends and it wont go away
all day and it wont go away

I'm feeling nervous and it wont go away
please don't talk while I drive and it wont go away
I'm acting happy it won't go away
I'm acting and it wont go away

hey dad, can you pick me up?
no, I'm not on drugs, can you pick me up?
no, I'm not on drugs, can you pick me up?
no, I don't want to drive, can you pick me up?
yes, i'll go to college, can you pick me up?
no, I'm not on drugs, can you pick me up?
Oh God
Untitled pt.1 (lyrics)
another empty platitude
that I used to calm you down
I never was good at calming you down

Another empty platitude
that I used to disengage the bomb
I never was good at calming you down

and that was my fatal mistake
I didn't know how long it takes
This was where I went wrong
I'd assumed you wouldn't do it again

Ill tell you this, night after night
if I have to
(that I love you)
don't you worry
ill still be here you wake up and you're not angry

Another empty Platitude
that I used to make you feel
a certain way about me

another empty thing you said but you meant it
and my brain
is just working against me

do you mean to feel this way?
'Cause I will guide you
and I will fight for you

and did you mean all the things that you didn't say?
(is everything really the same?)
((is everything really okay?))

(cause that's what I been thinking lately)
I was worried back then that I wouldn't have relationship problems to talk about

We can talk about this when its not 4am when its not on our phones cause I deleted snapchat
(and I know this is hard for the both of us, don't you worry, I have no where to go)
((We can phone at 4am, when our phone are nearly almost dead and we really just wana go to bed but you))

and that was my fatal mistake
(will it always be this way?)

I didnt know when I would break
(all these thoughts just ruling my head)

we've been going at this for so long
(I dont know how much longer I can take it)
((In the light of the moon, we are dancing))

will you be okay when im at
(and all my thoughts want me dead)
((and I can feel you next to my side))

I Love You Like A Beach House Song But I Don't Know How To Tell You (lyrics)
I mustn't feel any way about this
I can not feel, all of my nerves have become numb
I cannot sing like Victoria Legrand
But I can sing this song
	
The Western Song (Hell) (lyrics)
if any sense goes to rational thinking, then
every time I think of you, it's like a prayer
If anyone listening wants
a rational way of thinking about
the way it is
ill tell you what i told the others
its not you that i fighting for
its him
its that simple
its just him

if anyone wants to get an abortion, you better act fast
my college professor will kick your ass
I'm an american

What is this?
modern country pop production?
What is this?
Chillin at the beach with a 'rona?
What is this?
What am I supposed to do? keep listening to this song even though terrible?

Shut the fuck up, I can tell when you're lying
Shut the fuck up, I can tell when you're lying to me

The one thing missed by the rational mind is that its happening all the time

Epilogue (Heaven) (lyrics)
this is the end, its finished
thank you for stopping by
I sincerely thank you
this is not an act, this is just me

one thing that frequently comes to mind is
am i doing this right
I know there is a somewhere out there
that knows what i'm talking about

It's you, up there
yeah
not you, but him,
but its you, you know what im talking about?

Take me anywhere but here
I wish to be anywhere else but here, but now im here, so I might as well make the most of it

was it an illusion, or was it always this way
I didn't expect the cold shoulders, but I got them anyway
I never learned how to write, write a song properly
this is all I know how to do

I want this to be something
I want this to mean something
I want this to be something
I want us to be something

more than just the sum of two parts

Was it the answer?
did you get real far?
did you die happy?
did it matter in the morning?

did it matter what you did with your day?
did it matter what you did with your life?
does it matter that now, you're taking the time, to listen to mine?

Is it all going to be okay?

Did the Bible say that?

I think the Bible says that

As long as you don't sin

Take me anywhere but here
I wish to be anywhere but here
But now i'm here, so I might as well make the most of it

Was it too loud? did you finally realize, what i'm talking about?
Did you read the lyrics?
I knew, sooner or later, our van would come to a crash, then I would ask
was it worth it?

and he said yes
I'm glad I was alive
he said yes
i'm glad when i sad when i died

and he said yes
it wasn't therapy for me
it was just a way out

was it love
that could save him?
it couldn't be love, after all
that's too mainstream

This isn't really me
its just my voice

Hey! Calm down! We're not trying to make a loud sound, we just wanna, keep them quiet, keep them buying, and keep them compliant
we're not trying to take away you're freedom,
we just don't know why you need it

I think it's love
I took the blank verses to think about it
this song is getting long
its time for me to turn off the mic and say, atleast for now,

the song is over, and
I hope you have a goodnight.1. press space to start
2. baby blue (beat to death)
You're wasting your life
You're wasting your life
You're wasting your life
You're wasting your life
--
You're wasting your life
You're wasting your life
--
You're wasting your life
You're wasting your life
You're wasting your life
You're wasting your life
--
You're wasting your life
You're wasting your life
--
I want to let some anger out
is that on the schedule for today?
for todaaayyyy
I want to write my feelings down
but every time I try its just more of the same
more of the saaaammeee
"Hide The Blue"
"You're Not Trying To"--"Improooovveee Your Life"
I get told what to do 
I get told whats true
what am I supposed to do with me?
Baby blue, You're not trying to
improoooooooooooooove your life
I get told what to do
we're just trying to help you
what am I supposed to do
with him..... ^
Whoooooooo is it? Hauling around????? THHIS???? 
PILE OF FLESH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
THATTTTTTTTTSSSS WHAT I"D ASK YOU
BEFORE IIIIII REALIZED IT
Its just you.
And me 
now im struggling with bpd
my eyes can see what the future brings I feel so weak
---
sitting in the class with my face down in my mask
a dreaming youth is wanting more than covid asks
I get told by the man
"I'll never amount to nothing anand"
When the HELL did I start. to. as. YOoouuU?
Baby Blue I know you're out there on the 
moon
will you shine some starlight?
it would help me in this hard time
baby true I know you're out there feeling blue
well I feel sadness too.
Baby Blue You try your best its all you can do
you're eyes they shine like the morning dew I can feel its true
i get help from my friends when I don't know what is next
and that is all i've been expecting
for now
i get
HELP. FROM MY FRIENDS. WHEN I DONT KNOW WHAT IS NEXT.
AND THAT IS ALL I'VE BEEN EXPECTING FOR NOW
i get 
HELP. FROM MY FRIENDS. WHEN I DONT KNOW WHAT IS NEXT.
AND THAT IS ALL I'VE BEEN EXPECTING FOR NOW
You've got no right right right right right to feel this sad sad sad sad sad
You've got to fight fight fight fight fight to keep whats yours yours yours alive
or it will die
your favorite thing will die.
3. Judetv (Directors cut)
Jude walks home from school in the evening
'Cause jude can't drive, he hasnt got the
Time to learn, he's all caught up in his head
'Bout the new world order, and getting older
Jude gives all he can and it's not that much to give
And yet he lives on
Just scraping by with his small slice of pie, but he can't see the light
--
Jude goes back and fourth inbetween feeling his absolute best and totally helpless
he streams the world from right behind his two eyes
and his inner voice says he's a total idiot
Jude goes back and fourth inbetween feeling his absolute best and total depression
he skirts the line between having it all, and having total downfall, a total spiral
Jude goes back and fourth inbetween throwing up your breakfast, and totally selfless
he tries his best but never passes the test, because you get what you give and you give what you get and
Jude got up to turn off the tv at the end of the song, why does this feel so wrong and
na na na na na , na na na na, na, na na na, na na, na na na, na na.
da da da da da...
4. Patient 19
What is the machine
You never answered this for me
What was the answer
I nearly went crazy
Just trying to find it
But you wouldn′t text me
I called up your phone I
Was just a bit manic
Was speaking in nonsense
Thought you'd understand it
Let′s sit down for a second
Let's take it all it in
You know you're something special
Will you stick around for a while
When you leave it′s so quiet
Yet something pulls me toward you
Will you be my lover for the rest of our lives?
Say yes please god ′cause I need to know
'Cause I′m sitting here crying in a hospital bed
And I don't know why they won′t turn the lights off yet
What'd you do to me
I can′t focus on anything
What was the lesson
It all seemed so pointless
Your manic depression
Is keeping you up late
I called up their drummer was speaking in nonsense
Said something 'bout mirrors
Thought he'd understand it
Let′s sit down for a second
Let′s take it all it
You know you're something special
Will you stick around for a while
When you leave it′s so quiet
Yet something pulls me toward you
Will you be my lover for the rest of our lives?
Say yes please god 'cause I need to know
′Cause I'm sitting here crying in a hospital bed
And I don′t know why they won't turn the lights off yet
What is with this dream?
I couldn't tell you what it means (All these places that I′ve seen)
What was the lesson (It′s my new obsession)
Did you end up in heaven (your facial expressions)
Did you try to speak up (I want to speak up)
But no one would listen (But I learned my lesson)
We flew down to Reno
Was hot as the desert
Wasn't used to the heat
I packed like ten sweatshirts
Let′s sit down for a second
Let's take it all it in
You know you′re something special
Will you stick around for a while
When you leave i'm so quiet
Yet something pulls me toward you
Will you be my lover for the rest of our lives?
Say yes please god ′cause I need to know
'Cause I'm sitting here crying and you′re like four hours away
And I don′t know if I can take this pressure
5. bill's theme (famous)
"zack!!!!!"
"You're gonna pay for this...."
"zack: move it drew..."
"NOT NOT"
"NOT NOT"
"NOT NOT"
"NOT NOT"
"NOT NOT"
"NOT NOT"
when
i look at "NOT NOT" you
i feel so blue "NOT NOT"
Thom yorke: alright
cause its a man's world...."NOT NOT"
and you gotta get"NOT NOT" through 'em all....
*werid solo*
help me....."NOT NOT"
Trust me....
"NOT NOT"
Not be the way I was once was
cause its a bill's world
and you gotta get through 'em all
6. Shut Up, Space Hippie.
*Spaced Out Bass Plus Reverb Drunched Drums*
Peer outside the capsule
breath the martian air
power on your heatsuit
cause its too cold to bear
why am I still doing this?
I practically abuse my body
zack: "that's not the right volume..."
walking down the sidewalk
looking up at space
knowing i'll never get there 'cause of allergies or grades
why am I still laughing?
I practically abuse my body...
*flute solo drenched, slow and ticking like a clock*
--
Shut Up, Space Hippie, you don't know what its like down here
When Your eyeballs start to bleed 
and you have oxygen but you cant see
shut up, space hippie, you know David had the truth
we're all blackstars just like you
It'll be okay
---
Step out into starlight
mend your broken face
quanitfy the milky way
andromeda and space
why am i still hurting?
I only want to heal my body
*police sirens*
turning off the engine
feeling very still
getting locked in jude space
escape to no avail
why am I still wandering?
I know the answers out there somewhere
*second flute solo, still drenchedand ticking slow like a clock along with the drums*
---
Shut Up, Space Hippie, you don't know what its like down here
When Your eyeballs start to bleed 
and you have oxygen but you cant breath
shut up, space hippie, you missed covid by a year
you played a black a note in our ear, and now we're here.
--
Shut Up, Space Hippie, you don't know what its like down here
When Your eyeballs start to bleed 
and you have oxygen but you cant breath
shut up, space hippie, you missed covid by a year
we're all blackstars just like you
It'll be okay
--
Shut Up, Space Hippie, you don't know what its like down here
When Your eyeballs start to bleed 
and you have oxygen but you cant breath
shut up, space hippie, you know David had the truth
we're all blackstars just like you
It'll be okay
--
Shut Up, Space Hippie, you don't know what its like down here
When Your eyeballs start to bleed 
and you have oxygen but you cant breath
shut up, space hippie, you missed covid by a year
you played a black a note in our ear, and now we're here.
7. untitled pt. 2
I can't stop your mentions
I don't know whats your dimension
I'd really to mention the way I feel.........
And of course im going to sleep
zack: what the fuck would i be doing if I wasnt sleeping
what the hell would i be doing
at 12:44 am
zack: I seriously cannot.. believe you said that
what the hell am i doing?
We can talk another time when its not four am. 
When its not on our phones cause I deleted snapchat
It just comes and it goes and (intelligeible)
(intelligible)
it just comes and it goes (unintelligible)
and i realized lately that consciousness is an illusion
and it goes like:
Run kids run, but not in traffic
You'll find me where you least expect it
I'll meet you out by the western front
you know the spot
you know what i want
I can live without life's simple pleasures
I don't know why the things I say
make you so twisted!
--
 Zack: can we try that one again please?
It's like we never actually communicated!
Zack: uh- I guess-
zack: I guess thats the take..-
--
hey man you,
yeah you know what to do
gotta crank it to 11
gotta get all the views
there is bitches there is money just waiting for you
and all you have to do is buy my seminar
zack: you see, i know people, so,.... basically.... if you want to go places in this business.... so ... so basically the music business
8. thank god we tried
Sara and Zack: The longer we go, the better off we'll be
I know 'cause mom fight all the time
when I look. in your eyes. and I want to see the light
but I know sometimes we're
'stuck in my room all night
and yes we have our issues
and yes we have our fights
but at the end of the night
I just want to know you're alive
and I now that you're scared
that one day we will die
but I've got this feeling you will be alright
and I know that you're scared that one day you will die
but i know we will look back saying
"Thank god we tried"
Sara: I know that you're scared that one day you will die, but I swear to god that you will be alright, be alright
Zack: "Thank god we tried"
Sara: I know that you're scared that one day you will die, but I swear to god that you will be alright, be alright
Zack: "Thank god we tried"
Sara: I know that you're scared that one day you will die, but I swear to god that you will be alright, be alright
9. was it love?
make me a god
that's what I want to be
make me a god
that's where I wanna be
was it love?
that could save him?
It couldnt be "love"
no
.....
After all...
That's Too MainStream
The Ballad Of Psychidelic Sarah: (Sarah Rejoyce): and someone else is trying to tell them something that maybe they didnt know before, they're not gonna even see it. they're gonna be like "THATS FALSE" or like  "THATS THE WORK OF THE DEVIL" you know what I mean? they cant` feel threatened their ego feels threatened becuase they want to think that they know everything that they're already perfect, so the fact that you've chosen to say "hey maybe the live I was living before WAS an illusion and i did not know everything (unintelligible) suffering through the mind and im *not* healed and im not perfect, and the- i dont know everything` fact that you've even been open to awakening and becoming better and learning new things (unintelligible) a spiritual journey)
zack: Divided by one.....
make me a god
zack: Divided by one.....
thats what I want to be
this isnt love.....
this isnt love
its just another mask that im putting on
its just a mask that im putting on
now im sitting here broken
i've been broken for so long
I dont know what to do
I dont know where to go
Sara: *coughs*
when Im not with you
Psychidelic Sarah: (Sarah Rejoyce): learning some truths about reality and you dont really know to start living those dreams , you know how to stay centered
zack: its so much colder, underneath the covers
Psychidelic Sarah: (Sarah Rejoyce): ill just start off by saying Sara: *cough* the fact that you've chosen to wake up, the universe is already on your side - your sould main purpose is to wake up maybe not in this lifetime but we are getting closer and closer as a human on earth, so the fact that you've chosen to wake up is a big step and the universe is already on your side, its giving you signs, and giving you the tools you need to (unintelligible) so i think the main reason people dont want to wake up is they want to believe that "OH SCIENCE is the only thing thats real and im superior and im smarter than you and i know everythiNG" and then
SOMEONE ELSE IS TRYING TO TELL THEM SOMETHING THAT MAYBE THEY DIDNT KNOW BEFORE
SOMEONE ELSE IS TRYING TO TELL THEM SOMETHING THAT MAYBE THEY DIDNT KNOW BEFORE
10. bills theme (humble)
"NOT"
"NOT"
"NOT"
"NOT"
--
"NOT"
"NOT"
"NOT"
--
"NOT NOT"

When i look
i feel like i shouldn't feel this way (this way)
Lazy we can't do this thing we're calling we
You and me lazy
--
I kept my mouth my mouth
shut for so long so long
But I cant cry cant cry
--
these tears these tears
I can't cry
so I spiral
--
feel betrayed I never hurt you hur tyou
I cant cry so I just spiral spiral
who's to say if i got anything right
burned your eyes your looking into the light the
--
you've battered down my heart
the mirrors broke for good I swears
and in my mind I see spirals
--
Shout out to bill
he made my spaceship.
11. Patient XX
What is the machine?
you never answer this for me
(cut off due to char limit)
With Love, from Locking.
by Press Space To Stop - LP III (2022)

1.
November 02:52
Quite restless, can't quite get this
Is this damn thing on?
Is anyone there?
Stayed up too late on Big Sleep
8k cry engine blue crab made of glass
2.
月クラゲ (Moon Jelly) 
3.
Moon Jelly Pt. 2
You know I'm out of breath
Ten feet of water over my head
You know I can't keep cool
The ocean water turning me blue
Looking up at the moon
The gelatin around me moves
And figures dance in green and blue around you
Think of some poignant thought
Impress the girl and win her love
Excite her heart and make her want to stay
We both know to keep this up
We'll have to call it less than love
So touch me please
I wanna feel this pain
You know I'm up at night
A bit of a lunatic but that's alright
I know I act a fool
But please believe me it was just to impress you
When you look up at the sky
do you think of me, or do you think of the sky?
And do you think of the moon jellies under the light
When you called me on the phone
For the last time I never felt more alone
'Cause I knew there way no way that I could call you back
Moon jelly, you're the one I envy
You lack the heart to feel my pain
I'm right here and things are crystal clear
And you can't get yourself off the sand
Moon jelly
You're half moon half jelly
See, you have no belly
Still, you're getting hungry
Moon jelly
You're half moon half jelly
Sting me if I hurt you please
There's a one in a million chance
It seems to find the one who'll dance
And laugh and sting you back to sleep
Moon jelly, you're the one I envy
You lack the heart to feel my pain
I'm right here and things are crystal clear
And you can't get yourself off the sand
Moon jelly, you're the one I envy
You lack the heart to feel my pain
I'm right here and things are crystal clear
And you can't get yourself off the sand
4.
It's Good
Much less than the blink of an eye it will find you
And it’s not what you're used to
Waiting on the crowds to approve
It’s good it’s good it’s good
Much worse than the concept of dying
Falling without ever trying
Ten years down the road you’ll be saying
good it’s good it’s good it’s good

Faster than inspiration leaves you
Darker than depressions perceived hue
The faces, they ask how it’s going
Good it’s good it’s good it’s good
Much worse than what you had in mind but
It’s alright
You can say you survived it
Ten years down the line you’ll look back and you’ll say
It’s good it’s good it’s good
Two stops then were homebound for Heaven
It’s a hard road, but you’ve got your new weapon
You're a black heart
Now you say it with faith it’s good
It’s good it’s good it’s good
5.
New OS
You're not the best well kempt
You're so depressed, your dogs are eating better than you
You can't get out of bed
So force a smile
Try some sitting still for a while

Three things you have to remember
1. No one is perfect
2. I can't remember the rest
I hate this body, give me something new

You got a new OS
Things will get better
Let your body heal over time
You got a new OS
Just keep on working
Keep on looking up to the stars

Now you're the best in class
You always were
things are different now than before
You got a new OS
You're not afraid
Now you're looking death in the face

But there's a crack in the wall
There's something wrong
The small mind it wont leave you alone
You're better now than you were
But lets be real
You don't know what you're doing at all

You got a new OS
Things will get better, let you're body heal overtime
You got a new OS
Can't tell for sure
But things feel different now than before

Now it's a mix of the two
Things could still be worse
And hey, you've got a new pair of shoes
Not quite the best in show
But that's okay
You see the ultraviolet rays

You got a new OS
Things will get better
Let your body heal over time
You got a new OS
Just keep on going
Take yourself right up to the stars

You got a new OS
You're not afraid
Now you're looking up to date
You got a new OS
Just making sure you're on the latest version of you
6.
Emory
Emory, I know it's not you, its me
I lose my mind to some degree
Will you bear with me?

Emory, the signs are written in the sand
The stars and moon all sing and dance and call your name

And when I'm tired I tend to think about you
So when I sleep my brain makes images of a girl with long hair
And when I wake up I don't see you anywhere
So go back to sleep, maybe ill see Emory
7.
(Little Boxcar to Waynesville)
8.
Spiderman 
You’re climbing up that wall
You’re flying through the town
No one can stop you now
You got your cape and suit
A mask they can’t see through
You’re feeling all brand new

You’re a superstar
You’ve got an iron heart
And no you can’t be stopped
You’re breaking down that wall
You’ve got a heart of gold
You’re a marvel

Your webs are running low
New York is getting cold
Now find you way back home

You’re feet are turning blue
This Costume isn’t warm
It seems like there’s no hope

You’re a superstar
You’ve got an iron heart
And no you can’t be stopped
You’re breaking down that wall
You’ve got a heart of gold
You’re really a marvel
9.
November Pt. 2 04:32
Sunshine and happy days
Blue skies and rainbows
Sunsets at 6pm
I might just off myself

Think of some happy thoughts
make it though winter
Things might be fucking hell
But at least we’ve got Autumn leaves

This might be the worst month
But at least we’ve got Autumn
Unless your names Vonnegut
Then it might be Locking

Think of some happy thoughts
Peer through the darkness
Things might be fucking hell
But at least we’ve got the silver moon

I’m already sick of November
Take me back to the first of September
Take me back to when things weren’t so different and I did more things than just sit on my phone and I
Can’t get off the clock app keeps ticking I
Stay in bed my body’s decaying I
Hate this time schedule who’s big idea was it
DLS can’t day light save my sanity
10.
Sean 
Sean got out of bed
Been thinking bout where his real mothers at
Start to see the truth
But it looks like an idol and it’s not speaking to you
Sean put down the pod
Hasn’t taken off his earbuds since 9am
Listen to the words
But be careful not to read to much
Sean was in a gown
Connected by wires like a robot clown
Sean felt like a fool
I’m never doing this thing again or before
And you know
It’s okay to feel good
It’s okay to feel bad
Every once in a while
Even god needs a healthy cry
And you know
Yeah you know
Sean’s got your back
11.
I Wanna Be Your Cat 2
I wanna be your cat
Oh to be the one you thinks all and that
Oh to be the one whose head you wanna pat
Oh to be the one you make up names for

I wanna live in and outside your doors
I’ll let you microchip my neck because I’m yours
I’ll let you rant about your day to me for hours

Cause you know
That I’m just waiting and daydreaming for the day you call me baby
Living in your laundry sleeping on top of your belly
And when I’m scared you’d go and talk right to me softly
I wanna be your cat so bad
12.
'Oumuamua 03:46
13.
Stay 05:03
Your back's against the wall
you don't even know what for
Your friends all live x hours away
and your ex girlfriend hopes that you're not dead
so just pretend
that things are dandy
so just pretend
that we're alright
so just pretend
that we can still make it
do you think that we'll make it?

You were in the backrooms, liminal space
I was getting worked up, I couldn't see your face
Meet me in the attic, we'll get stoned with the ghost
And then you can leave me in that same cloud of smoke
Won't you just stay?
Please God please stay
Even now I know
For us it's too late
Won't you just stay
Please God please stay
Even though I know
By now It's too late
14.
Vines 
They see
Everything
And they tap
Tap your name
You writhe
You infest
You can’t cure
The disease
So you crawl
And you grow
Up the walls
Down the window
To the place
They can’t see
What you don’t show them
When the joke’s done

You’re green
You have leaves
Poison leaves
Leaves of three
And you spread
Like a fire
Sickening heat
Fueled by desire
And you fall
And you bleed
Poison blood
And it burns
Through your skin
See your bones
Made of vines
15.
MADWRLD (QUETIAPINE) 
Woke up feeling lost in space
Just trying to forget that place
Just trying to forget that room
They wouldn’t turn the lights off for you

So what happens to the broken glass
And the mirror behind that fact
And the mirror behind that wall
And the one in the corner of the room
Cause every idol has an ounce of truth
You pick your poison and I pick mine too
But who’s picking the deadlier fruit?
And you’re acting like you ate the truth
Why would you do this to me?
Gave me that Quetiapine
And now I'm seeing things
When I'm trying to get to sleep
Make me take mysterious drugs
And then you say it's my fault
When I start seeing ghosts
Turns out you can’t trust your gut
But it’s still better than those fucking cunts
Overprescribe 'til it makes you cut
Overprice basic life saving drugs
You’d think it wouldn’t be this way
The smartest people in the worst array
And the pills make you feel even worse
More psychosis than you walked in the door with

Why would you do this to me?
Gave me that Quetiapine
And now I'm seeing things
When I'm trying to get to sleep

How could you send me to Hell?
And tell me that it's my fault
When I start burning up?
16.
? 01:41
17.
When I'm Strong 04:16
When
When I’m strong
I won’t have to sing this song
Because I’ll be so strong

When
When I’m tall
I won’t be scared at all
And I won’t be scared to fall

I been weak for so long
Can’t remember the last time I worked out
Baby can't we work this out

When I’m finally strong
Baby I’ll be the one
You want with you
And baby I’ll see you there

If
If by chance
Somehow I shake off this old skin
And become a better man

If
If honestly I try
To be the things you saw in me
To be a better guy than he was

I been weak for so long
Can’t remember the last time I worked out
Baby can't we work this out

When I’m finally strong
Baby I’ll be the one
You want with you
And baby I’ll see you there

I been weak for so long
Can’t remember the last pound I lifted
Don’t want to you to lift my weights

When I’m finally strong
You know I’ll be the one
And I’ll lift you
Up to the stars where you belong
18.
THC / Just Kill Me 03:46
Kill me, kill me
What did they put in this thing?
Kill me just kill me
I can’t get to sleep

I been high too long
And I ain’t coming down
And now my stomach hurts
THC is the worst

Call me a hypocrite
But I’m just trying to quit
So tired of feeling so tired
Just tired of getting bad highs

Not trying to rain the parade
I know that lynch smokes mj
I’m cool with smoking no doubt
But I keep greening out

Kill me, kill me
Kill me, just kill me
I’m done with thc
I want this out of my body

Kill me, kill me
Kill me, just kill me
I’m done with thc
I want this out of my

It was fine at first
It’s slowly getting worse
Don’t even talk to my friends
Just sitting stoned in my bed

Don’t even show me the bill
My wallets getting so low
My body’s getting so high
But still I just wanna die

Kill me, kill me
Kill me, just kill me
I’m done with THC
I want this out of my body

Kill me, kill me
Kill me, just kill me
I’m done with THC
I want this out of my body

Kill me, kill me
Kill me, just kill me
I’m done with THC
I want this out of my body

Kill me, kill me
Kill me, kill me
I’m done with THC
I want this out of my
19.
The Machine 09:39
One no longer bleeds
You just let off your heat
When you need to rethink
You can focus on one thing

It no longer bleeds
Watch the glowing heat sync
It no longer fears
Only wires up here

It works day after day
Marvel at the display
Watch the gears turning round
No it never slows down

See a piece that you like
You can have it full price
It can never be stopped
Press the space bar and watch

When will my body rest
When will my body reset
When will this pain be undone
When will this album end

When will my work be done
When will my grave be undug
When will the last note be sung
When will the wires be cut

When will my body rest
When will my body reset
When will this pain be undone
When will this album end

When will my work be done
When will my grave be undug
When will the last note be sung
When will the wires be cut

One no longer bleeds
Two just let off your heat
Three you need to rethink
Four and focus on one thing

It no longer bleeds
Watch the glowing heat sync
It no longer fears
Only wires up here

It works day after day
Marvel at the display
Watch the gears turning round
No it never slows down

See a piece that you like
You can have it full price
It can never be stopped
Press the space bar and watch

When will my body rest
When will my body reset
When will this pain be undone
When will this album be done

When will my work be done
My body’s way overclocked
Processors can’t keep up
So let the meltdown start

Countless lines of code
Compile as you sleep
More likely than you think
Rewriting as we speak
More likely than a ghost
An Ai overlord
In 2042
The thunderhead is you

How come he don’t bleed
He is just a machine
Pay no mind to him dear only wires up there
He can’t hear us speak
No ears no brain to think
Put your worries to rest
Only wires

If you get to sleep
Tell me what do you think
Of the quantum field
Anything goes in here
And If you wake up tired
I’ve got you covered full price
Take some of this caffeine
You know you’re just a machine

Countless lines of code
Compile as you sleep
More likely than you think
More likely than you'd know
More likely than a ghost
An Ai overlord
Who’s living in the clouds
The thunderhead
When will my body rest
When will my body reset
When will this pain be undone
When will the last note be sung
When will my work be done
My body’s way overclocked
Processors can’t keep up
So press the space bar to stop
Count the fleshy machines
Working hard for their queen
They don’t know of her goals
It’s a dog eat dog world
Pay your bills on time
Don’t dare to step out of line
Watch the red oil flow
It’s working hard for the ghost

Waste
Greed
Power
The machine
20.
Robin 03:31
You know better that most
You’re sweet but sharp like a rose

You’re brother's 5 foot forty
Carla might be your shorty
You’re the life of the party

You go to school at Greens
You’re dressing better than me
Now tell me one more thing,
How’s it feel to be queen?

While they’re holding their breath
You’re going for the kill
Now you’re out of second place
and you’re gunning for the gold
And they try to act tough wearing Adidas shorts
But you dress too well so go give them hell girl

You always stay on your toes
Eyes on the prize and the road
You know you’re way too cool
You froze the swimming pool
I wanna skate with you

You make me skip half a beat
Still dressing well
And if you think you can pull a fast one
Well she’s faster

While they’re holding their breath
You’re going for the kill
And you wanna win the race and you totally will
And they never saw the vision so they couldn’t come close
‘Cause you just dress to well so go give them hell girl
21.
In a Cherry Colored Funk (Bonus Track) 02:51
22.
Orange Lavaburst (Bonus Track) 05:22
Lazy
Why aren’t you calling me baby
Why do you look at me with those big sad eyes
I know lately
I’ve been acting so crazy
It must be so hard for you

So return
To what I know
I know loved me once
And I loved you too

And If I had a time machine
I wouldn’t change the truth
I’d only change the fact that I went mad in front of you

So turn on the thrusters
And set the year
We’re going back in style
Things will be different here

With no compromises
I’ll be like Marty mcfly
Fix our 2020
And Then we’ll fly off right into the sky

Softly singing subtle things to you as you fall asleep
and when you fall into that dream
You don’t have to worry about a thing
You don’t have to worry about the world
That’s cold and cruel
And twists your arm until you’re blue
And when you’re blue like baby blue
Do you feel so pink and helpless too
Do you feel so weak and helpless too
Do you feel so weak and helpless
Do you feel so weak and helpless too
Do you feel so weak and helpless

So turn on the thrusters
And set the year
We’re going back in style
Things will be different here

With no compromises
I’ll wipe away those tears
Fix our 2020
And I’ll make boyfriend of another year
23.
Gallows Pool (Bonus Track) 03:38
Maybe we could go for a dip
This snowy weather’s kinda making me sweat
And ok I’ll stop playing the fool
Or I would if I was closer to you
Cause I hate the holidays
The early evenings and the freezing rain
And if I could choose my town
I’d pick one closer so that we could hang out

And I know I’m hard to read
But that’s just ‘cause I mess up everything
So forgive this strange facade
I don’t want you to think that I’m odd
But I like your point of view
And I wish I lived closer to you
But until that time is here
I'll only see you on the darkened mirror

And I don’t care if it takes me all the way till next year
I’ll see you again
I’ll see you again
And I don’t care if I wake up swimming in the gallows pool
I’ll do what it takes
To see you
24.
It's The End Of The World Again (Bonus Track) 00:40
Please don't tell me you'll give up on the world
'Cause so many people already have
And please don't live the rest of your life
through the darkened mirror
I'm only asking this of you
I'm only asking this of you
I'm only asking this of you
25.
The Fool (Bonus Track) 03:36
It was late at night
Cards were all laid out and the tower fell
The seven chairs were set
I could partly tell just by the things you said
One thing two
Thing three and four
Now what do I do
I know I act so cool
Please believe me I know that I’m just a fool
Just a fool
A fool in ___ with you
A fool
A fool in ___ with you
26.
Sun Eyes (Bonus Track) 04:47
Looking back
Through the looking glass
Everything seems far away
Sitting in
The shadows of the sun
Everything
Has lost its fun

The curtains are drawn
The light is dim
He’s looking at me but
I’m looking through him

Sun Eyes Sun Eyes
Looking back through the looking glass
Sun Eyes Sun Eyes
Looking back through the looking glass
Sun Eyes Sun Eyes
Looking back through the looking glass
Sun Eyes Sun Eyes
Sun Eyes Sun Eyes

I'm a magician
I’m disappearing
I’m in the mirror
But I can't hear ya

The mirror is broken
It all falls apart
I’m looking at you
But you're looking at my heart
Looking at my heart
Looking at my heart
Looking at my heart
Looking at my

Sun Eyes Sun Eyes
Looking back through the looking glass
Sun Eyes Sun Eyes
Looking back through the looking glass
Sun Eyes Sun Eyes
Looking back through the looking glass
Sun Eyes Sun Eyes
Sun Eyes Sun Eyes

Standing on the edge of the world
A feeling I've never felt before
The feeling that my life's going wrong
I feel lost in space
in a dream turned sour

Sun Eyes Sun Eyes
Sun Eyes Sun Eyes
Sun Eyes Sun Eyes
Sun Eyes Sun Eyes
Sun Eyes Sun Eyes
Sun Eyes Sun Eyes
Sun Eyes Sun Eyes
1.
Trµe LµvµLite 01:40
2.
∷⨍our (free) 02:30
3.
venus venus flytrap!!!!! (burnt) (free) 05:04
4.
«ytpme_empty» (free) 04:06
5.
flower boy (free) 02:58
6.
∷⨍our - reprise 01:24
7.
𝖘ɤđ𝖓𝖊ɤ♎♎♎ (free) 07:45
8.
Blµe ★ LµvµLite (free) 02:02
9.
∷⨍our (remix) (bonus track) 02:31
...
four Four four Four.
I'm in my chest
no more voice inside my head
just last week she turned up dead
don't identify with that
Obsessed all day
Can't help feeling like im strange
booked a flight I never paid
1.
Trµe LµvµLite 01:40
2.
∷⨍our (free) 02:30
3.
venus venus flytrap!!!!! (burnt) (free) 05:04
4.
«ytpme_empty» (free) 04:06
5.
flower boy (free) 02:58
6.
∷⨍our - reprise 01:24
7.
𝖘ɤđ𝖓𝖊ɤ♎♎♎ (free) 07:45
8.
Blµe ★ LµvµLite (free) 02:02
9.
∷⨍our (remix) (bonus track) 02:31
...
∷⨍our (lyrics)
four Four four Four.
I'm in my chest
no more voice inside my head
just last week she turned up dead
don't identify with that
Obsessed all day
Can't help feeling like I'm strange
booked a flight I never paid
booked a flight I never paid- for
I can't help, Zack
You're too gone for even that
and the mirror starts to crack
and the mirror starts to crack
no sleep last night
and today feels like a storm
think I might be going home
think I might be going home- soon
What a nice day
Not too warm and not too grey
hope the weather stays this way
home the weather stays the same way
venus venus flytrap!!!!! (burnt) 
Stuck between some coals and a hot plate
This room is to much for me
I'm burning up as we speak
turn on the AC
and you can breathe in cold air
But you're still sunburnt when you strip down bare
You're hot- there's no stopping it
In the last verse things got a little out of hand
I started mumbling words
Pretty sure that part was in prose
And when my mind had been erased
I scanned the lines I turned the page
My face turned red I got so mad they pulled a gun and I said "SHOOT!"
In the dark like a bow through the heart
Stupid cupid's left a mark so don't tell me we're friends
I can tell what's in your head
But I'm in too deep
It's complete 
It's complete 
It's complete 
It's complete 
I got-
STOCKHOLM SYNDROME
I GOT STOCKHOLM SYNDROME
IM TRAPPED I GOT STOCKHOLM SYNDROME
IM TRAPPED I GOT STOCKHOLM SYNDROME
Fuckin' with a girl like that-
Oh, she's dangerous as heaven
Come on triple sevens
Fuckin' with a girl like that-
Oh, she's dangerous as heaven
So give me one more shot!
In the dark like a bow through the heart
Stupid cupid's left a mark so don't tell me we're friends
I can tell what's in your head
And I'm in too deep
It's complete 
It's complete 
It's complete 
It's complete 
I got-
Stockholm Syndrome
I got-
Stockholm Syndrome
I got-
Fuckin' with a girl like that-
Oh, she's dangerous
Fuckin' with a girl like that-
Oh, she's dangerous as heaven
FEEL YOUR HEAT
FEEL MY HEAT
Burn in down
Burn in down
Burn in down
Burn in down
Burn in down
Burn in down
Burn in down
Burn in down
Burn in down
Burn in down
Burn in down
Burn in down
Burn in down
Burn in down
Burn in down
Burn in down
Light it up
Light it up
Light it up
Light it up
Light it up
Light it up
Light it up
Light it up
Light it 
Burn It
Light it
Burn it
Fuck it
Fuck it
Fuck it
FUCK IT
FUCK IT
«ytpme_empty» (lyrics)
All lost
In time
And yet
No one
Today
Some
Feel okay
It's okay
flower boy (lyrics)
It was late, and getting cold
We ran right toward that artificial glow
You said "It's better off this way"
Fuck better, all I want is you
My baby, it's been a year now
I'm right here, but I won't be stayin' in town
I can see you got presence
So don't touch me with a 10 foot pole
I'm just kidding
You can't get there from here
No matter how you go
It's the thrill
Stay in the world just a second more
You won't win here like that
Little flower boy.
It's a shame
Be that as it may it'll all work out
It was late in mid October
I could sense the snow was fit to kill
You said "Its better off this way"
Fuck better, all I need is you my baby
It's been a year now
I'm right here
But
I wont be stayin' (I won't be stayin')
I can see you got presence
So lets leave that in the double room
I'm just kidding
You can't there from here
No matter how you go
It's the game
Be that as it may it'll all work
You won't win like that
Little flower boy
Oooo
∷⨍our - reprise (lyrics)
checked all the databases, there are four possible
Five, four, three, two
𝖘ɤđ𝖓𝖊ɤ♎♎♎ (lyrics)
The ice melt melts to slow
I'd rather we we're both here alone
The Coffee maker drips to slow
I'd rather we were both in the know
Sydney, will you even miss me
When you leave this town
I know you've got your own life
You live on your own time
And I do the same
You build me up and break me down
You burn and manifest our Love
You're all I'm needing right now
You're all I'm needing right now Sydney
And I don't blame you
For any reservation
You have with our relation
I'm pretty sure Indie Rock boyfriend is a red flag
I'm just going to ignore that
Anyways, shoegaze is where its at
Sydney, will you even miss me?
when you leave this town
I know you've got your own life
You live on your own time
And I do the same
You build me up and break me down
You burn and manifest our Love
You're all I'm needing right now
You're all I'm needing right now Sydney
Stuck in an airport
In New York city
The smog was so bad
I had to wear a mask
Sydney, will you even miss me
When you leave this town
I know you've got your own life
You live on your own time
And I do the same
You build me up and break me down
You burn and manifest our Love
You're all I'm needing right now
You're all I'm needing right now Sydney
All I'm needing right now
You're all I'm needing right now Sydney
You're all I'm needing right now
You're all I'm needing right now Sydney
Sydney, will you even miss me
When you leave this town
I know you've got your own life
You live on your own time
And I do the same
You build me up and break me down
You burn and manifest our Love
You're all I'm needing right now
You're all I'm needing right now Sydney
Blµe ★ LµvµLite (instrumental)
∷⨍our (remix) (bonus track) (lyrics)
Four Four Four Four () Four
I'm in my chest
No more voice inside my head
Just last week she turned up dead
Don't identify with that
Obsessed all day
Can't help feeling like I'm strange
booked a flight I never paid
booked a flight I never paid- for
I can't help, Zack
You're too gone for even that
and the mirror starts to crack
and the mirror starts to crack
no sleep last night
and today feels like a storm
think I might be going home
think I might be going home- soon
What a nice day
Not too warm and not too grey
hope the weather stays this way
home the weather stays the same way"""
    
    top_words = find_top_words_with_entropy(corpus)
    
    print("Top 100 words with highest Shannon entropy values:")
    for word, entropy in top_words:
        print("Word:", word, "| Shannon Entropy:", entropy)

if __name__ == "__main__":
    main()
