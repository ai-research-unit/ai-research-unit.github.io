# __The Cayley–Dickson Construction of the Quaternion Algebra__

## Introduction

**A note on the order of the corpus.** This article is not the preferred construction of the algebra, and it is kept for the questions only it can answer. It begins by naming one vector unit, $\vec e_z$, as the imaginary unit of a base field, and a second, $\vec e_x$, as the unit that is adjoined; the third is then computed, $\vec e_y=\vec e_z\vec e_x$. Three units that the algebra treats alike therefore enter the construction in three different roles, a field, a generator and an output, and the equality of the three squares, the cyclic symmetry of the table and the absence of a privileged third unit must all be derived from an axiom set that already ranks them. Nothing here is wrong, and the derivation is complete. What the presentation carries is a choice of direction that the algebra does not contain: a reader cannot tell from this page which features of the table belong to the algebra and which belong to the route.

**The preferred route.** It is *The Axis-Free Construction of the Quaternion Algebra*, before this article in this category. It declares the four units with three equal squares and one rule of anticommutation, derives the same sixteen products, proves associativity inside the coefficient display, and leaves one bit, the orientation, which the conjugation absorbs. The two articles prove different things about one object, and neither replaces the other. What this article supplies and that one cannot is the reason for the signs: that the twist is forced by the absence of zero divisors, that the third unit is computed rather than assumed, and that the ladder has a next rung, where associativity fails.

**The subject.** This article builds the algebra of *Quaternion Algebra*, above this article in this category, from the complex algebra by one doubling step. The multiplication table of that article is stated there and derived here, from the single rule that defines the doubling.

**What the construction uses.** The base units only: the scalar unit $e_t$ and the three vector units $\vec e_x,\vec e_y,\vec e_z$. The only imaginary unit is $\vec e_z$, and it is the complex unit of the base. The third vector unit is not introduced independently: it is computed, $\vec e_y=\vec e_z\vec e_x$.

**What the construction does not use.** No array, no representation, no second triple of units, and no symbol of its own for the complex unit.

**Why the step is worth writing out.** A table stated is not a table explained, and one feature of the quaternion table invites the reading that it is a convention: the signs of the ordered products. The doubling shows that one sign and one twist produce the whole table with no freedom left. The sign is the square of the new unit, $\vec e_x^2=-e_t$. The twist is the rule that the new unit passes to the other side of a base element conjugated, $\vec e_xw=\bar w\vec e_x$. Those two choices are made in §*The Doubling Step*, they are cashed in §*Hamilton's Rules*, and the second of them is shown in §*The Twisting Rule* to be what keeps the algebra free of zero divisors.

**Boundaries.** The base is *Complex Algebra*, in the complex category; the general doubling, its recursion, the saturation at the octonions and the Hurwitz theorem are *Quadratic Forms over Algebras and Norms*, §*The Cayley–Dickson Doubling*, and are cited and not repeated. The table, the conjugations and the subspaces are *Quaternion Algebra*, above this article in this category; the classes of element are *The Specificities of the Quaternion Algebra*, below; and the norm, its multiplicativity and the invertibility criterion it supplies are *Norm and Invertibility in the Quaternion Algebra*, below. The same step taken with the other sign gives the split quaternions, and it is *Split-Quaternion Algebra*. The same construction taken one layer up, where the step from $\mathbb{H}$ to $\mathbb{B}$ is a scalar extension rather than a rung, is *The Cayley–Dickson Construction of the Biquaternion Algebra*, in the Biquaternions category.

## The Base and Its Units

### The Units and the Coefficients

**One unit to a direction.** The base is written with the letter $e$, one unit to a direction. The scalar unit is $e_t=1$. The three vector units are $\vec e_x,\vec e_y,\vec e_z$. The arrow is the only mark that separates the scalar unit from a vector unit.

**The base letter and the unit-element letter.** The base letter is $e$ and the unit-element letter is $u$, and the two are never exchanged. The unit element of the doubled layer is written $\tilde u$, and it is $e_t$. Because the base units carry $e$, the letter $e$ is not available for the exponential, which is written $\exp(\cdot)$.

**The coefficients.** A coefficient carries the name of the direction it multiplies. The coefficient $q_x$ multiplies $\vec e_x$, the coefficient $q_y$ multiplies $\vec e_y$, and the coefficient $q_z$ multiplies $\vec e_z$. The label on the unit names the direction, and the label on the coefficient names the same direction, so the pair reads without ambiguity.

**The three vector units are the quaternion units**, the corpus's replacement for the three classical imaginaries. In the quaternion layer each squares to the negative of the scalar unit, $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$, and §*Hamilton's Rules* derives exactly this.

### The Generic Element and the Pure Element

**The glyphs.** The case and the tilde of the glyph are fixed first, and the element is written after. The tilde marks the quaternionic factor, that is the presence of the doubling unit $\vec e_x$; a base element carries none, and it is written with the letter $w$.

| Layer | Element | Scalar part | Vector part |
|---|---|---|---|
| $\mathbb{C}$ | $w=u+v\vec e_z$ | $u$, real | none |
| $\mathbb{H}$ | $\tilde q=q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ | $q_t$, real | $q_x\vec e_x$, $q_y\vec e_y$, $q_z\vec e_z$, real |

**One family of letters.** The generic element of the doubled layer is $\tilde q$, and no letter outside that family stands for an arbitrary element of the algebra. A statement that holds for every element is written with $\tilde q$; a statement that needs two elements writes them $\tilde q_1$ and $\tilde q_2$, and a third takes the next number. The number counts the element and never names a direction; a letter names the direction. A letter outside the family names a specific object, or an element bound where it is introduced — the coefficients $a,b,c,d$ of §*The Doubling Step* are of that kind.

**The pure element.** The element is a scalar part plus, in the doubled layer, a vector part,

$$
\tilde q=q_te_t+\vec q .
$$

A pure element is one with no scalar part, and it is written with the arrow of the vector part: $\vec q$ is the pure element of the quaternion layer. The arrow marks purity, not magnitude, so a pure element is of arbitrary magnitude; the unit pure element, the axis of a rotation, is written $\vec u$, and its unit length is carried by the construction that names it. The arrow and the tilde are never stacked: the arrow replaces the tilde rather than being laid on it, so a pure element is $\vec q$ and never an arrowed $\tilde q$.

## The Base Algebra

**The base.** The complex algebra of the doubling is the plane spanned by $e_t$ and $\vec e_z$,

$$
\mathbb{C}=\mathbb{R}[\vec e_z]=\{\,u+v\vec e_z:u,v\in\mathbb{R}\,\},\qquad \vec e_z^2=-e_t ,
$$

with the product read off the square and the commutativity of the two units,

$$
(u+v\vec e_z)(u'+v'\vec e_z)=(uu'-vv')+(uv'+vu')\vec e_z .
$$

The algebra is that of *Complex Algebra*, in the complex category, written in the base units of this one.

**No second imaginary symbol.** The complex unit of the doubling is the vector unit $\vec e_z$, and the base is written with it. The coefficient field of the doubling is therefore the plane itself, and the construction needs no symbol of its own for its imaginary unit: the only imaginary unit in this article is $\vec e_z$.

### The Conjugation of the Base

**The bar.** The conjugation of the base flips the vector unit and fixes the scalar unit,

$$
\bar w=u-v\vec e_z,\qquad \overline{\vec e_z}=-\vec e_z,\qquad \overline{e_t}=e_t ,
$$

so that

$$
w\bar w=u^2+v^2\in\mathbb{R}_{\geq0} .
$$

**The bar is an involution.** Applying it twice returns the element, $\overline{\bar w}=w$, because the two signs cancel. It reverses the order of a product, $\overline{ww'}=\bar w'\bar w$, and the base is commutative, so the reversal is invisible and the bar reads as an automorphism of the product as well. That reversal is not invisible on the doubled layer, where it is the content of §*Conjugation, the Norm and the Inverse*.

**The coefficients of the doubling rule.** In the product rule of §*The Doubling Step* the coefficients of the base are written $a,b,c,d$. They are bound at the point of use, they are elements of the base and not of the doubled algebra, and $\bar a,\bar b,\bar c,\bar d$ are their bar-conjugates.

## The Doubling Step

### The Space

**The double.** The doubled algebra is the real vector space of pairs of base elements,

$$
\mathbb{H}=\mathbb{C}\oplus\mathbb{C}\vec e_x=\{\,a+b\vec e_x:a,b\in\mathbb{C}\,\},
$$

made into an algebra by the product rule of the next subsection. The new symbol $\vec e_x$ names a vector direction, and it carries the arrow for that reason. The real basis is

$$
e_t,\qquad \vec e_z,\qquad \vec e_x,\qquad \vec e_z\vec e_x ,
$$

which is four elements because $1,\vec e_z$ is a basis of the base and $b\vec e_x=(u+v\vec e_z)\vec e_x=u\vec e_x+v\vec e_z\vec e_x$ for a base element $b=u+v\vec e_z$. The dimension doubles, as the doubling requires.

### The Product Rule

**The rule.** For $a,b,c,d$ in the base,

$$
(a+b\vec e_x)(c+d\vec e_x)=(ac-b\bar d)+(ad+b\bar c)\,\vec e_x .
$$

**The two generating rules.** The product rule is equivalent to the pair

$$
\vec e_x^2=-e_t,\qquad \vec e_x\,w=\bar w\,\vec e_x\ \text{ for every }w\in\mathbb{C} .
$$

*Proof.* Assume the two rules and expand the left side of the product rule:

$$
(a+b\vec e_x)(c+d\vec e_x)=ac+ad\vec e_x+b\vec e_xc+b\vec e_xd\vec e_x .
$$

The third term is $b\bar c\vec e_x$ by the twisting rule applied to $c$, and the fourth is $b\bar d\vec e_x^2=-b\bar d$ by the twisting rule applied to $d$ and then the square. Collecting, $ac-b\bar d+(ad+b\bar c)\vec e_x$. Conversely, $a=c=0$ and $b=d=e_t$ in the product rule give $\vec e_x^2=-e_t$, and $a=d=0$, $b=e_t$, $c=w$ give $\vec e_xw=\bar w\vec e_x$. The two forms are therefore the same rule.

**The heart of the construction.** The rule $\vec e_xw=\bar w\vec e_x$ is the twisting rule, and it is what makes the doubled algebra non-commutative. Its effect on the base unit is the sign flip $\vec e_x\vec e_z=-\vec e_z\vec e_x$, which is step 3 of §*Hamilton's Rules* and the source of every sign in the table.

### The Twisting Rule

**Why the twist and not the plain rule.** The plain rule $\vec e_xw=w\vec e_x$ is available, and it must be excluded by an argument and not by a choice of notation. Under the plain rule the element $\vec z=\vec e_z\vec e_x$ has square

$$
\vec z^2=\vec e_z\vec e_x\vec e_z\vec e_x=\vec e_z^2\vec e_x^2=(-e_t)(-e_t)=e_t ,
$$

where the middle equality is the plain rule itself: the second $\vec e_x$ passes $\vec e_z$ unchanged, and the two copies of $\vec e_x$ meet. Then

$$
\pi_\pm=\tfrac12\bigl(e_t\pm\vec z\bigr),\qquad \pi_\pm^2=\tfrac14\bigl(e_t\pm2\vec z+\vec z^2\bigr)=\tfrac12\bigl(e_t\pm\vec z\bigr)=\pi_\pm,\qquad \pi_+\pi_-=\tfrac14\bigl(e_t-\vec z^2\bigr)=0 .
$$

Neither idempotent is zero: $\vec z=\vec e_z\vec e_x$ has no scalar part, so $\vec z\neq\pm e_t$, and $\pi_\pm$ does not vanish. So the algebra carries two non-zero orthogonal idempotents and their product vanishes: it has zero divisors, and no element of the form $\pi_+$ is invertible. Under the twisting rule the same computation gives $\vec z^2=-e_t$ instead, as step 4 of §*Hamilton's Rules* shows, and no element of the algebra is a zero divisor, as §*Conjugation, the Norm and the Inverse* proves. The twist is therefore not a stylistic preference: it is the difference between a division algebra and an algebra with two complementary ideals.

**Why the sign of the square.** The new unit squares to $-e_t$, the same sign as at the first rung, where the base unit $\vec e_z$ was adjoined to $\mathbb{R}$ with $\vec e_z^2=-e_t$. The opposite sign at this second rung gives the split quaternions of *Split-Quaternion Algebra*, and the two constructions differ in that sign alone. The choice made here is the one that keeps the squared norm a sum of squares, and the four-square identity is what the doubling is built to preserve.

## Naming the Units

**The third unit is computed.** Set

$$
\vec e_z:=\vec e_z,\qquad \vec e_x:=\vec e_x,\qquad \vec e_y:=\vec e_z\vec e_x .
$$

The two units of the doubling carry their own names, and the third is defined as their product. It is not introduced independently, and this is the point at which the construction fixes the third unit.

**Why this order and not the other.** The two orders of the two new units differ by a sign, $\vec e_x\vec e_z=-\vec e_z\vec e_x$, so the definition $\vec e_y=\vec e_x\vec e_z$ would give $-\vec e_y$ instead. The order is fixed by the triple product: with $\vec e_y=\vec e_z\vec e_x$ one has

$$
\vec e_z\vec e_x\vec e_y=\vec e_y\vec e_y=-e_t ,
$$

whereas the other order gives $+e_t$. The cyclic form of the table is exactly the statement that the three units in the order $z,x,y$ multiply to $-e_t$, and that order is the one the definition must respect.

**The general element.** With the three vector units named,

$$
\tilde q=q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z,\qquad q_\mu\in\mathbb{R},
$$

the coefficient carrying the label of its direction. The base sits inside the doubled algebra as the subspace of the elements with $b=0$, that is as $\operatorname{span}\{e_t,\vec e_z\}$.

**The doubling order is not the display order.** Read as a pair, the element is

$$
\tilde q=\bigl(q_te_t+q_z\vec e_z\bigr)+\bigl(q_x+q_y\vec e_z\bigr)\vec e_x ,
$$

so the base part carries the coordinates $t,z$ and the second slot the coordinates $x,y$. The corpus writes the four coordinates in the order $t,x,y,z$, and that order is a display convention of *Quaternion Algebra*, not the order in which the doubling produces them.

## Hamilton's Rules

**The programme.** The two generating rules and the definition of the third unit determine every product. The nine steps below compute them, in the order in which the construction supplies them, and no step uses anything but $\vec e_z$, $\vec e_x$, $\vec e_y=\vec e_z\vec e_x$ and the twisting rule.

### The Two Squares

**Step 1.** The base unit squares to $-e_t$ by the definition of the base,

$$
\vec e_z^2=-e_t .
$$

**Step 2.** The doubling unit squares to $-e_t$ by the first generating rule,

$$
\vec e_x^2=-e_t .
$$

The two squares carry the same sign. The whole sign pattern of the table follows from that agreement together with the twist, and the next subsection applies it.

### The Sign Flip

**Step 3.** The two new units anticommute. Apply the twisting rule with $w=\vec e_z$ and use $\overline{\vec e_z}=-\vec e_z$:

$$
\vec e_x\vec e_z=\overline{\vec e_z}\,\vec e_x=-\vec e_z\vec e_x .
$$

This is the only place in the article where the bar enters the multiplication table, and it enters as a sign.

### The Third Unit

**Step 4.** The third unit squares to $-e_t$. By the definition $\vec e_y=\vec e_z\vec e_x$, by the associativity of the product, and by step 3,

$$
\vec e_y^2=(\vec e_z\vec e_x)(\vec e_z\vec e_x)=\vec e_z(\vec e_x\vec e_z)\vec e_x=\vec e_z(-\vec e_z\vec e_x)\vec e_x=-\vec e_z^2\vec e_x^2=-(-e_t)(-e_t)=-e_t .
$$

The associativity used in the middle is not an extra assumption: the product of the double is associative because the base is associative and commutative, which is §*Associativity and the Ladder*.

### The Six Ordered Products

**Step 5.** The two orders of the doubling units are fixed by step 3 and by the definition of the third unit:

$$
\vec e_z\vec e_x=\vec e_y,\qquad \vec e_x\vec e_z=-\vec e_y .
$$

**Step 6.** The first unit times the third. Substitute the definition of $\vec e_y$ and apply step 3:

$$
\vec e_x\vec e_y=\vec e_x(\vec e_z\vec e_x)=(\vec e_x\vec e_z)\vec e_x=(-\vec e_z\vec e_x)\vec e_x=-\vec e_z\vec e_x^2=\vec e_z .
$$

**Step 7.** The third unit times the first:

$$
\vec e_y\vec e_x=(\vec e_z\vec e_x)\vec e_x=\vec e_z\vec e_x^2=-\vec e_z .
$$

**Step 8.** The third unit times the base unit:

$$
\vec e_y\vec e_z=(\vec e_z\vec e_x)\vec e_z=\vec e_z(\vec e_x\vec e_z)=\vec e_z(-\vec e_z\vec e_x)=-\vec e_z^2\vec e_x=\vec e_x .
$$

**Step 9.** The base unit times the third:

$$
\vec e_z\vec e_y=\vec e_z(\vec e_z\vec e_x)=\vec e_z^2\vec e_x=-\vec e_x .
$$

### The Table

**The collected rules.** The three squares and the six ordered products of the steps are, with $e_t$ the unit,

$$
\vec e_z^2=\vec e_x^2=\vec e_y^2=-e_t ,
$$

$$
\vec e_z\vec e_x=\vec e_y,\quad \vec e_x\vec e_z=-\vec e_y,\qquad
\vec e_x\vec e_y=\vec e_z,\quad \vec e_y\vec e_x=-\vec e_z,\qquad
\vec e_y\vec e_z=\vec e_x,\quad \vec e_z\vec e_y=-\vec e_x .
$$

**The full table.** Written as a table of the sixteen products, with the left factor on the row and the right factor on the column:

| | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $-e_t$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $\vec e_y$ | $-\vec e_z$ | $-e_t$ | $\vec e_x$ |
| $\vec e_z$ | $\vec e_z$ | $\vec e_y$ | $-\vec e_x$ | $-e_t$ |

The table is the multiplication table of *Quaternion Algebra*, above this article in this category.

### The Cyclic Form

**The cyclic triple.** The six ordered products are three cyclic relations and their three negations:

$$
\vec e_z\vec e_x=\vec e_y,\qquad \vec e_x\vec e_y=\vec e_z,\qquad \vec e_y\vec e_z=\vec e_x ,
$$

$$
\vec e_x\vec e_z=-\vec e_y,\qquad \vec e_y\vec e_x=-\vec e_z,\qquad \vec e_z\vec e_y=-\vec e_x .
$$

**The triple product.** The cyclic relations compose to one identity, and it is the sharpest single statement of the table:

$$
\vec e_z\vec e_x\vec e_y=-e_t .
$$

*Proof.* $\vec e_z\vec e_x\vec e_y=\vec e_y\vec e_y=-e_t$ by the definition of $\vec e_y$ and step 4. The other orders do not give the same sign: $\vec e_x\vec e_z\vec e_y=+e_t$, because the transposition of the first two factors costs one sign and the sign of the triple is odd under a transposition.

**These are Hamilton's relations.** The three cyclic relations with the three negations are the classical quaternion relations, with $(\vec e_z,\vec e_x,\vec e_y)$ in the role of the classical triple. The construction has produced them and has not assumed them: the only inputs are $\vec e_z^2=-e_t$, the twist, and the definition of the third unit as the product of the other two.

## Associativity and the Ladder

**Associativity.** The product of the double is associative. The associator

$$
A(\tilde q_1,\tilde q_2,\tilde q_3)=(\tilde q_1\tilde q_2)\tilde q_3-\tilde q_1(\tilde q_2\tilde q_3)
$$

is trilinear, because the product is bilinear, so it vanishes identically once it vanishes on the sixty-four triples of units. On those triples it vanishes: the four units are monomials in $\vec e_z$ and $\vec e_x$ with signs — $e_t$ is the empty monomial, $\vec e_z$ and $\vec e_x$ are the letters, and $\vec e_y=\vec e_z\vec e_x$ is the product of the two — the product of two units is again a signed unit, and the two bracketings of three such monomials reduce to the same signed monomial. The general criterion gives the same answer without a computation: the double of an associative algebra is associative exactly when the doubled algebra is associative and commutative, which is *Quadratic Forms over Algebras and Norms*, §*The Cayley–Dickson Doubling*, and the base is both.

**Non-commutativity.** The product is not commutative, because $\vec e_x\vec e_y=\vec e_z$ while $\vec e_y\vec e_x=-\vec e_z$. This is the property the second rung loses, and it is also the reason the third rung is not associative: the criterion above fails at the next doubling, since the doubled algebra is no longer commutative, and the octonions lose associativity. The whole ladder is $\mathbb{R}\to\mathbb{C}\to\mathbb{H}\to\mathbb{O}$ with the same sign at each step, and $\mathbb{H}$ is its last associative division algebra.

**The division property.** Every non-zero element is invertible, so the algebra has no zero divisor. That is §*Conjugation, the Norm and the Inverse*, and it is the property the twist secured in §*The Twisting Rule*. With it the doubled algebra is a division algebra, and by the theorem of Frobenius it is one of the three finite-dimensional associative real division algebras, the others being $\mathbb{R}$ and $\mathbb{C}$; the statement is *The Specificities of the Quaternion Algebra*, below this article in this category.

### The Choice of the Doubling

**The ingredients in one table.**

| CD ingredient | Choice for $\mathbb{H}$ |
|---|---|
| Base field | $\mathbb{R}$ |
| First doubling | $\mathbb{C}=\mathbb{R}[\vec e_z]$, $\vec e_z^2=-e_t$ |
| Second doubling | $\mathbb{H}=\mathbb{C}\oplus\mathbb{C}\vec e_x$ |
| New unit | $\vec e_x$, with $\vec e_x^2=-e_t$ |
| Twisting | $\vec e_xw=\bar w\vec e_x$ for all $w\in\mathbb{C}$ |
| Units | $\vec e_z$, $\vec e_x$, $\vec e_y=\vec e_z\vec e_x$ |
| Product | $\vec e_z^2=\vec e_x^2=\vec e_y^2=\vec e_z\vec e_x\vec e_y=-e_t$ |

**What is not in the table.** No sign of an ordered product appears, and no coordinate. The six ordered products of §*The Six Ordered Products* are consequences of the five rows above, and the fifth of them is the one that carries the non-commutativity.

## Conjugation, the Norm and the Inverse

### The Conjugation

**The rule of the double.** The conjugation of the double is the bar on the base part together with a sign on the second part,

$$
(a+b\vec e_x)^{\natural}=\bar a-b\vec e_x .
$$

This is the conjugation of the Cayley–Dickson step, *Quadratic Forms over Algebras and Norms*, §*The Cayley–Dickson Doubling*, and it is an involution that reverses the order of a product.

**In the corpus display.** With $a=q_te_t+q_z\vec e_z$ and $b=q_x+q_y\vec e_z$, so that $b\vec e_x=q_x\vec e_x+q_y\vec e_y$,

$$
\tilde q^{\natural}=\bar a-b\vec e_x=q_te_t-q_z\vec e_z-q_x\vec e_x-q_y\vec e_y
=q_te_t-q_x\vec e_x-q_y\vec e_y-q_z\vec e_z .
$$

So the quaternion conjugation flips the sign of all three vector units, the base unit $\vec e_z$ included, and it fixes the scalar unit. The display is the one of *Quaternion Algebra*.

**The order is reversed.** For two elements,

$$
(\tilde q_1\tilde q_2)^{\natural}=\tilde q_2^{\natural}\,\tilde q_1^{\natural}.
$$

*Proof.* Both sides are bilinear, so it suffices to check the sixteen pairs of units. A product of two units is a signed unit, $\vec e_\mu\vec e_\nu=\varepsilon\vec e_\gamma$ with $\varepsilon=\pm1$, and the conjugation sends each unit to a signed copy of itself, $\vec e_\mu^{\natural}=\sigma_\mu\vec e_\mu$ with $\sigma_t=+1$ and $\sigma_x=\sigma_y=\sigma_z=-1$. The left side is then $\varepsilon\sigma_\gamma\vec e_\gamma$ and the right side is $\sigma_\nu\sigma_\mu\varepsilon\vec e_\gamma$, so the identity holds once $\sigma_\gamma=\sigma_\mu\sigma_\nu$. The four cases exhaust the sixteen pairs: two scalar units, one scalar and one vector, two distinct vector units with the third as their product, and one vector unit twice with the scalar unit as its square. In each the sign of the product unit is the product of the signs of the two factors. Bilinearity extends the identity to the algebra.

**The bar is the restriction.** On the base, the second part vanishes and the conjugation reads $(w+0\vec e_x)^{\natural}=\bar w$. So the bar of §*The Conjugation of the Base* is the restriction of $\natural$ to the base, and the two signs are one sign. The distinction to keep is that the bar is written on a base element $w$ and $\natural$ on an element $\tilde q$ of the doubled algebra; the marks are different because the objects are.

### The Norm

**Theorem (the norm of the double is the sum of the norms).** For every element,

$$
\tilde q\,\tilde q^{\natural}=N(\tilde q)\,e_t,\qquad N(\tilde q)=q_t^2+q_x^2+q_y^2+q_z^2\in\mathbb{R}_{\geq0} .
$$

*Proof.* Write $\tilde q=a+b\vec e_x$ with $a=q_te_t+q_z\vec e_z$ and $b=q_x+q_y\vec e_z$. The product rule is applied with $c=\bar a$ and $d=-b$, so that $\bar c=a$ and $\bar d=-\bar b$, and it gives

$$
(a+b\vec e_x)(\bar a-b\vec e_x)=\bigl(a\bar a+b\bar b\bigr)+\bigl(-ab+ba\bigr)\vec e_x .
$$

The scalar part is the sum of the two base norms, $a\bar a=q_t^2+q_z^2$ and $b\bar b=q_x^2+q_y^2$ by §*The Conjugation of the Base*, that is $q_t^2+q_x^2+q_y^2+q_z^2$. The coefficient of $\vec e_x$ is $-ab+ba$, which vanishes because the base is commutative. The result is $N'(a,b)=N(a)+N(b)$ of the general doubling, computed in the coordinates of this base.

**The norm is definite.** It is a sum of four squares, so it vanishes only at the origin and is positive on every other element. The doubling has therefore preserved the definiteness of the base norm. Its multiplicativity, cited in §*The Inverse*, is the four-square identity: a product of two sums of four squares is again a sum of four squares.

### The Inverse

**Every non-zero element is a unit.** Let $\tilde q\neq0$. Then $N(\tilde q)>0$ is a real number, and

$$
\tilde q^{-1}=\frac{\tilde q^{\natural}}{N(\tilde q)} ,
$$

because $\tilde q\tilde q^{\natural}=N(\tilde q)e_t$ and the norm is a scalar. The inverse is two-sided, since $\tilde q^{\natural}\tilde q=N(\tilde q)e_t$ by the same computation on the other side.

**The division algebra.** No product of non-zero elements vanishes, because $N(\tilde q_1\tilde q_2)=N(\tilde q_1)N(\tilde q_2)$ by the multiplicativity of the norm, *Norm and Invertibility in the Quaternion Algebra*, below this article in this category, and a product of positive numbers is positive. So $\mathbb{H}$ is a division algebra, and the theorem of Frobenius places it among the three.

**The star.** In the biquaternion layer the star is the composite of the coefficient bar and the quaternion sign, $\star=\bar{}\circ\natural$. In the quaternion layer the coefficients are real, the bar is the identity on them, and the star coincides with $\natural$. The biquaternion layer is not developed here.

## Summary

1. The quaternion algebra is the double of the complex algebra, $\mathbb{H}=\mathbb{C}\oplus\mathbb{C}\vec e_x$, with the base $\mathbb{C}=\mathbb{R}[\vec e_z]$.
2. The product is fixed by the square of the new unit and by the twisting rule: $\vec e_x^2=-e_t$ and $\vec e_xw=\bar w\vec e_x$ for every base element $w$.
3. The twisting rule is the heart of the construction. Without it the element $\vec e_z\vec e_x$ squares to $+e_t$, the algebra carries the two idempotents $\tfrac12(e_t\pm\vec e_z\vec e_x)$, and it has zero divisors.
4. The third vector unit is not introduced: it is computed, $\vec e_y=\vec e_z\vec e_x$, and that order and not the other is the one that gives $\vec e_z\vec e_x\vec e_y=-e_t$.
5. The nine derivations of §*Hamilton's Rules* produce the squares, the sign flip and the six ordered products, that is the multiplication table of the quaternion algebra, from the two generating rules alone.
6. The result is associative, because the base is associative and commutative, and non-commutative, because the two new units anticommute.
7. The conjugation $\tilde q^{\natural}=q_te_t-q_x\vec e_x-q_y\vec e_y-q_z\vec e_z$ reverses the order of a product, and it restricts to the bar on the base.
8. The norm is the sum of the four squares of the coordinates, it is definite, and it gives the inverse $\tilde q^{-1}=\tilde q^{\natural}/N(\tilde q)$; every non-zero element is a unit, and the algebra is a division algebra.
9. The ladder is $\mathbb{R}\to\mathbb{C}\to\mathbb{H}$, with the same sign choice at each rung; the next doubling gives the octonions and loses associativity, so $\mathbb{H}$ is the last associative division algebra of the sequence.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $e_t$ | the scalar unit, $e_t=1$ | this article |
| $\vec e_x,\vec e_y,\vec e_z$ | the three vector units, each of square $-e_t$ | *Quaternion Algebra* |
| $w=u+v\vec e_z$ | the generic element of the base $\mathbb{C}$ | this article |
| $\bar w$ | the conjugation of the base, $u-v\vec e_z$ | this article |
| $a,b,c,d$ | the coefficients of the doubling rule, bound at the point of use | this article |
| $\tilde q$ | the generic element of $\mathbb{H}$, $q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ | *Quaternion Algebra* |
| $\vec q$ | the pure element, the vector part | *Quaternion Algebra* |
| $\vec u$ | the unit pure element, the axis of a rotation | *Quaternion Algebra* |
| $\tilde u$ | the unit element of the layer, equal to $e_t$ | this article |
| $\natural$ | the quaternion conjugation, $q_te_t-\vec q$ | *Quaternion Algebra* |
| $\star$ | the composite $\bar{}\circ\natural$, equal to $\natural$ on this layer | *Quaternion Algebra* |
| $N(\tilde q)$ | $\tilde q\tilde q^{\natural}=q_t^2+q_x^2+q_y^2+q_z^2$ | *Norm and Invertibility in the Quaternion Algebra* |

## Further Reading

- William Rowan Hamilton, *On Quaternions* (Proceedings of the Royal Irish Academy, 1844) and *Lectures on Quaternions* (1853), for the table as it was first stated.
- Leonard E. Dickson, *On Quaternions and Their Generalization and the History of the Eight Square Theorem* (Annals of Mathematics, 1919), for the doubling as a construction.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Dover, 1995), for the doubling, the criterion for associativity and the ladder.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the doubling read through the arithmetic of the units.
- John C. Baez, *The Octonions* (Bulletin of the American Mathematical Society, 2002), for the ladder, the lost properties at each rung and the place of the quaternions in it.
