**CS-340_SNHU**
**Client/Server Development**

# Grazioso Salvare Animal-Shelter Dashboard

This is a full-stack web dashboard I built for **CS-340: Client/Server Development**. It lets Grazioso Salvare — a search-and-rescue animal training company — dig through the Austin Animal Center data and quickly find dogs that fit different kinds of rescue work.

**Tech stack:** Python · MongoDB · PyMongo · Dash / JupyterDash · Plotly Express · Dash Leaflet · pandas

**Design pattern:** Model-View-Controller (MVC)
- **Model** — MongoDB (`aac` database, `animals` collection), accessed through my CRUD Python module
- **View** — the Dash widgets: a logo header, radio-button filters, an interactive data table, a breed pie chart, and a geolocation map
- **Controller** — the Dash callbacks that react to clicks and update the widgets

**Features**
- Filter by rescue type (Water Rescue, Mountain/Wilderness Rescue, Disaster/Individual Tracking), plus a Reset
- An interactive data table with sorting, column filters, single-row selection, and pagination
- A pie chart and a map that both update on the fly when you change the filter

**What's in here**
- `ProjectTwoDashboard.ipynb` — the dashboard code
- `CRUD_Python_Module.py` — the `AnimalShelter` CRUD module from Project One
- `README` (Word doc) — the full project write-up with screenshots

---

## Reflection

### How do you write programs that are maintainable, readable, and adaptable?

For me it comes down to keeping things separated. The best example is the CRUD module I wrote in Project One: all the database stuff — connecting, logging in, and the create/read/update/delete operations — lives inside one `AnimalShelter` class. The dashboard never touches MongoDB directly; it just calls the module's methods and uses whatever comes back. That clean line between "getting the data" and "showing the data" is what kept both pieces easy to work with.

The payoff was obvious as soon as I started Project Two. Since the module was already written and commented, I didn't have to touch any database code — I just imported it, connected once, and every filter handed a different query to the same `read()` method. Everything came back in the same shape (a list of records that drops right into a pandas DataFrame), so the callbacks stayed short. It made fixing things way easier, too: when I had to correct the filter queries later, I was editing one spot instead of digging through database code tangled up in the UI.

And I can reuse this thing. The module doesn't assume anything about what's calling it, so I could drop it into a command-line tool, a REST API, or a totally different dashboard and it'd just work. Anything that needs to talk to that collection can grab it as-is. That reusability is really the whole point of writing it this way.

### How do you approach a problem as a computer scientist?

I like to start from what the client actually needs and work down to the data first, then build back up to the interface. For Grazioso Salvare, that meant taking their real goal — find rescue-candidate dogs by breed, sex, and age — and turning it into the MongoDB queries before I wrote a single line of UI. Once the queries were pulling the right records, I built the widgets on top and wired up the callbacks.

This one felt different from past assignments for a couple of reasons. It was full-stack and driven by a client's spec instead of a tidy exercise with a known answer, so I had to think about the whole pipeline — database, queries, and display — and about a real person who needs the interface to be easy and hard to mess up. It also taught me to actually check the data instead of trusting the spec. The preferred-breed table had clean names like "Doberman Pinscher" and "Chesapeake Bay Retriever," but the data stored them as "Doberman Pinsch" and "Chesa Bay Retr Mix." Since `$in` matches exact strings, my first queries quietly came back missing records. Auditing the breed column against the real data and fixing the strings cleared it up — and it's the kind of double-check I'll definitely keep doing.

The same game plan would carry over to any other client: pin down the requirements, model the data around them, build and test the queries on their own, check them against the actual data, and only then put the interface on top. Keeping the data code modular means I can test and change each layer without breaking the others.

### What do computer scientists do, and why does it matter?

The way I see it, computer scientists take real problems and build systems that solve them — turning big, messy piles of data into tools that help people make better calls. The code isn't the point; what people can *do* with it is.

For a company like Grazioso Salvare, that's pretty concrete. They need to find the right dogs for life-saving rescue work, and there's no way to eyeball thousands of records by breed, age, sex, and outcome by hand. This dashboard takes that exact same data and turns it into something they can act on in seconds: pick a rescue type and instantly see which animals qualify, how the breeds break down, and where they are on a map. Making that fast, accurate, and easy to get through saves them time, cuts down on mistakes, and helps them do the thing that actually matters — getting good rescue dogs out into the field.
