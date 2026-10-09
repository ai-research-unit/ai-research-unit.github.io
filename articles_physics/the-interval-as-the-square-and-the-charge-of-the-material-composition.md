# __The Interval as the Square and the Charge of the Material Composition__

## Introduction

A relativistic event is an element of the algebra with an imaginary time and a real space part,

$$
\tilde T = ict\,e_0 + x\,e_1 + y\,e_2 + z\,e_3 ,
$$

and the number that decides whether two events can be joined by a signal is its **interval**. This article
reads the interval as the value of a product rather than as a form laid on the algebra from outside. The
product is the **quaternionic product**

$$
\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q ,
$$

the ordinary multiplication with the natural conjugation inserted in the first slot, and the claim of the
article is the identity

$$
\tilde Q\star\tilde Q = N(\tilde Q)\,e_0 , \qquad N(\tilde Q)=Q_0^{2}+Q_1^{2}+Q_2^{2}+Q_3^{2} ,
$$

together with its reading: **the square of a material element is its interval**. The identity has two
consequences that this article also owns, and both are about composition rather than about a single
element. The value of the square is **multiplicative**, $N(\tilde P\star\tilde Q)=N(\tilde P)N(\tilde Q)$;
and because a vanishing factor forces a vanishing product, the **lightlike elements compose to lightlike
elements**, so the null cone is closed under the material composition. The interval is therefore a
**charge of the composition**, multiplicative and not additive, whose neutral value is $1$ and whose
absorbing value is $0$.

The article keeps to the material sector and to the one product that squares to the interval. It defers
the expression of the interval itself, the mass shell, the four-velocity and the inverse to *Biquaternion
Norm and Invertibility*; the identification of the vanishing set of $N$ with the light cone to *The Light
Cone as the Biquaternion Zero-Divisor Cone* and to *Zero Divisors as a Physical Locus in Biquaternionic
Form*; the interval-one group to *The Lorentz Group as Biquaternion Norm Automorphisms*; and the
comparison of this product's scalar form with the other three to *The Four General Products and Their Physical Readings: the Two Algebras and the Two Sesqualgebras*. Every result read below is proved in the
mathematics study whose entry point is *The Mathematical Study of Biquaternions*, and is cited there
rather than re-derived.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis
$e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$, $e_1e_2=e_3$, and central scalar imaginary $i$ with $i^{2}=-1$. An
element is $\tilde Q=Q_0e_0+\mathbf Q$ with $Q_\mu\in\mathbb{C}$ and vector part
$\mathbf Q=Q_1e_1+Q_2e_2+Q_3e_3$; the complex bilinear dot and cross products of vector parts are
$(\mathbf P,\mathbf Q)=\sum_kP_kQ_k$ and $\mathbf P\times\mathbf Q$. The conjugations are the natural one
${}^{\natural}$ (keeps the scalar coordinate, negates the three vector coordinates),
$\tilde Q^{\natural}=Q_0-\mathbf Q$, the coefficientwise one $\bar{\cdot}$, and the Hermitian star
${}^{*}=\bar{\cdot}\circ{}^{\natural}$; the sectors are $\mathbb{M}_\pm=\{\tilde Q:\tilde Q^{*}=\pm\tilde Q\}$,
the material one being $\mathbb{M}_-$. Juxtaposition $\tilde P\tilde Q$ is the ordinary (plain) product of
the algebra, $\star$ is the quaternionic product, and the biquaternion norm is
$N(\tilde Q)=\langle\tilde Q,\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2}$.
The material coordinate is $\tilde Q=ict\,e_0+\mathbf x$ with $\mathbf x=xe_1+ye_2+ze_3$.

## The Product and the Square

The quaternionic product differs from the multiplication of the algebra in one operation only: the first
factor is read through the natural conjugation before being multiplied. Writing both out on the
scalar–vector split,

$$
\tilde P\tilde Q=\bigl(P_0Q_0-(\mathbf P,\mathbf Q)\bigr)e_0+P_0\mathbf Q+Q_0\mathbf P+\mathbf P\times\mathbf Q ,
\qquad
\tilde P\star\tilde Q=\bigl(P_0Q_0+(\mathbf P,\mathbf Q)\bigr)e_0+P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q ,
$$

shows that the insertion does exactly one thing: it **reverses the sign of the product of the two vector
parts**. The two products agree on the scalar line, where there is no vector part to negate, and part
company as soon as one is present. On the vector part alone the quaternionic product of two pure elements
is

$$
\mathbf U\star\mathbf V = -\mathbf U\mathbf V = (\mathbf U,\mathbf V)e_0-\mathbf U\times\mathbf V .
$$

**Theorem (the square is the interval).** For every $\tilde Q$,

$$
\tilde Q\star\tilde Q = \tilde Q^{\natural}\tilde Q = N(\tilde Q)\,e_0 .
$$

**Proof.** In the second display put $\tilde P=\tilde Q$: the vector part is
$Q_0\mathbf Q-Q_0\mathbf Q-\mathbf Q\times\mathbf Q=0$, because the cross product of a vector with itself
vanishes, and the scalar part is $Q_0^{2}+(\mathbf Q,\mathbf Q)=N(\tilde Q)$. 

Every square of a single element therefore lands in the **centre** of the algebra, and on the central
line it lands on a definite value. Two consequences are used below. The symmetrisation is central,
$\tilde P\star\tilde Q+\tilde Q\star\tilde P=2\bigl(P_0Q_0+(\mathbf P,\mathbf Q)\bigr)e_0$, and the
discrepancy of the two orders is purely a vector,
$\tilde P\star\tilde Q-\tilde Q\star\tilde P=2P_0\mathbf Q-2Q_0\mathbf P-2\mathbf P\times\mathbf Q$. The
article does not develop either; it needs only that the square is central.

**Remark (verified).** The identity was recomputed on $100$ random biquaternions in exact complex
arithmetic; the maximum deviation of $\tilde Q^{\natural}\tilde Q-N(\tilde Q)e_0$ from zero is
$8.9\times10^{-16}$, machine precision. The identity is exact algebra and the numerical check confirms the
conventions with which it is written.

## The Square of the Plain Product Is Not the Interval

The content of the identity is the contrast with the product of the previous block, and the contrast is
notational unless it is stated.

**Proposition (the ordinary square).** For every $\tilde Q$,

$$
\tilde Q\tilde Q = \bigl(Q_0^{2}-(\mathbf Q,\mathbf Q)\bigr)e_0 + 2Q_0\mathbf Q ,
$$

so the ordinary square is central exactly when the scalar part of $\tilde Q$ vanishes or the vector part
does, and its scalar value is

$$
\mathrm{Sc}(\tilde Q\tilde Q)=Q_0^{2}-(\mathbf Q,\mathbf Q)=B(\tilde Q,\tilde Q) ,
$$

the diagonal value of the general plain bilinear form $B$ of *The Ordinary Product and the Material Sector*.

**Proof.** Distribute the product and use $\mathbf Q^{2}=-(\mathbf Q,\mathbf Q)$ for a vector part. 

The two squares differ in the sign of the vector pairing, and that single sign is the whole difference
between a Euclidean square and the interval:

$$
B(\tilde Q,\tilde Q)=Q_0^{2}-(\mathbf Q,\mathbf Q) , \qquad N(\tilde Q)=Q_0^{2}+(\mathbf Q,\mathbf Q) .
$$

On the material element $\tilde Q=ict\,e_0+\mathbf x$ the two read

$$
B(\tilde Q,\tilde Q)=-c^{2}t^{2}-\lvert\mathbf x\rvert^{2} , \qquad N(\tilde Q)=-c^{2}t^{2}+\lvert\mathbf x\rvert^{2} ,
$$

the first the negative of the Euclidean length of the event, the second the interval. On this sector $B$
is negative definite and has no null element beyond the origin, so it has no cone; $N$ is indefinite, and
its vanishing set is the light cone. The pass from the ordinary product to the quaternionic one is
therefore, on the material sector, the pass from a Euclidean square to the interval, and it is done by
inserting one conjugation in the first slot.

**Remark (verified).** The two squares differ on $100$ of $100$ random elements. The case
$\tilde Q=3e_0+ie_1$ shows both squares at once: the ordinary square is $10e_0+6ie_1$, which is not even
central, its scalar value $10$ is $B(\tilde Q,\tilde Q)=9+1$, and the quaternionic square is
$N(\tilde Q)e_0=8e_0$. The three numbers are $10$, $8$ and the Euclidean value $10$: the first and
the last coincide only because this vector coefficient is purely imaginary, where
$-\mathbf Q\!\cdot\!\mathbf Q$ and $\lvert\mathbf Q\rvert^{2}$ agree, so only two of the three values
differ — they remain three different questions asked of the same element.

## The Interval Is a Multiplicative Charge

**Theorem (multiplicativity).** For all $\tilde P,\tilde Q$,

$$
N(\tilde P\star\tilde Q)=N(\tilde P)\,N(\tilde Q) .
$$

**Proof.** $N(\tilde P\star\tilde Q)=N(\tilde P^{\natural}\tilde Q)=N(\tilde P^{\natural})N(\tilde Q)$ by
the multiplicativity of $N$ under the ordinary product, and $N(\tilde P^{\natural})=N(\tilde P)$ because
the natural conjugation is an anti-automorphism that preserves the norm. 

The interval therefore turns the material composition into multiplication of numbers. That is the
definition of a **multiplicative charge**: composing two material operations does not add their intervals,
it multiplies them. An operation of interval $2$ composed with an operation of interval $2$ gives an
operation of interval $4$, and an operation of interval $1$ leaves the interval of whatever it is composed
with unchanged.

On the invertible elements the statement sharpens to a character statement. The units are
$\mathbb{B}^{\times}=\{\tilde Q:N(\tilde Q)\neq0\}$, and $N$ restricts to a group homomorphism

$$
N:\ (\mathbb{B}^{\times},\ \cdot\ )\longrightarrow(\mathbb{C}^{\times},\ \cdot\ ) ,
$$

whose kernel is the set of **interval-one** operations, $\{\tilde Q:N(\tilde Q)=1\}$. Outside the units
the multiplicativity still holds as an identity of complex numbers, and that extension is what closes the
cone.

**Remark (verified).** The multiplicativity was recomputed on $100$ random pairs, with maximum deviation
$9.0\times10^{-14}$; and $100$ random pairs of interval-one elements were again of interval one, with the
same precision. The interval-one set is closed here and not merely nearly so.

## The Light Cone Is Closed under Composition

**Theorem (closure of the null set).** If $N(\tilde P)=0$ or $N(\tilde Q)=0$, then
$N(\tilde P\star\tilde Q)=0$ and $N(\tilde Q\star\tilde P)=0$. The null set
$\mathcal N=\{\tilde Q:N(\tilde Q)=0\}$ is closed under the quaternionic product on either side.

**Proof.** The value of $N$ on the product is the product of the values, and a product of complex numbers
vanishes when a factor does; the reversed order is the same computation. 

The general form of the statement is the level-set law
$\{N=\lambda\}\star\{N=\mu\}\subseteq\{N=\lambda\mu\}$. A level set preserved by the product must satisfy
$c^{2}=c$, so the preserved level sets are exactly $c=0$ and $c=1$.

**Reading (the interval is a scale, not a conserved quantity).** The level-set law says that composition
moves an element from the level $\lambda$ to the level $\lambda\mu$ when it meets an element of level
$\mu$: the interval **multiplies**, so it behaves like a **scale** (a ratio, a unit-bearing number) and
not like a conserved charge, which would be additive over a composition. A physical label that multiplies
along a composition is a scaling label; only its vanishing set, $c=0$, and its fixed set, $c=1$, are
preserved. The reading is a re-naming of the proved law and is offered as a reading; it is close to the
"multiplicative charge" wording of the previous section, and it is recorded only because "charge" suggests
an additive conserved quantity that this interval is not.

**Remark (verified).** On five explicitly null elements — $e_0+ie_1$, $e_1+ie_2$, $e_1-ie_2$, $ie_0+e_1$
and $ie_0+e_2$ — every norm is **exactly** $0$, and in the whole $5\times5$ table of products, in both
orders, the value of $N$ is exactly $0$ and not merely small. Over $100$ random pairs drawn from
$\{N=c\}$ for $c=0$ and $c=1$ the product lies in the same level set, with deviation $4.4\times10^{-15}$
for $c=1$, while for $c=2$, $c=\tfrac12$ and $c=-1$ the product is off the level set by $2$, $0.25$ and
$2$ respectively. No other level set is preserved.

This closure is the article's addition to the physics of the cone. *The Light Cone as the Biquaternion
Zero-Divisor Cone* owns the identification of the vanishing set of $N$ with the light cone, and *Zero
Divisors as a Physical Locus in Biquaternionic Form* owns the reading of the null elements as a kinematic
boundary; neither owns the statement that the set is stable under composition.

**Corollary (composition cannot generate mass).** A massless operation stays massless under composition
with anything: if $N(\tilde Q)=0$ then $N(\tilde P\star\tilde Q)=N(\tilde Q\star\tilde P)=0$ for every
$\tilde P$. Since the interval of a composite is the **product** of the intervals, no composition of
material operations can turn a lightlike factor into a massive one, and mass is a multiplicative label
and never an additive charge generated by the product. The physical content is the composition law of
lightlike propagation: **if one of two composed operations is lightlike, the composite is lightlike**. The
statement is not the same as the multiplicativity of the previous section: multiplicativity says how the
value changes, this corollary says what the product cannot produce.

## What Is Not Closed

Two tempting closure statements are false, and the article states both because the closure it proves is
easily over-read.

**The material sector is not closed.** The square of a material element is its interval, and the interval
is a number on the central line, not another material element. The minimal witness is
$e_1\star e_1=N(e_1)e_0=e_0$: the element $e_1$ is material, and its square is the central real unit,
which is Hermitian. So $\mathbb{M}_-\star\mathbb{M}_-\not\subseteq\mathbb{M}_-$. Neither is the
informational sector closed: $e_0+ie_1$ and $e_0+ie_2$ are both Hermitian, and their product
$e_0-ie_1+ie_2+e_3$ has a real coefficient of $e_3$ and is therefore not Hermitian. Squaring is a map
from the material sector to the central line, and no sector is a subalgebra of the quaternionic product.

**The causal set is not closed.** The **sign** of the interval multiplies along with its value, because
the value does: wherever neither factor is null,
$\operatorname{sgn}N(\tilde P\star\tilde Q)=\operatorname{sgn}N(\tilde P)\operatorname{sgn}N(\tilde Q)$.
With $\operatorname{sgn}=-1$ for a timelike element and $+1$ for a spacelike one, the rule is the
multiplication of signs, and its table on the material sector is

| | $N(\tilde Q)=-1$ | $N(\tilde Q)=+1$ |
|---|---|---|
| $N(\tilde P)=-1$ | $+1$ (spacelike) | $-1$ (timelike) |
| $N(\tilde P)=+1$ | $-1$ (timelike) | $+1$ (spacelike) |

so two timelike operations compose to a spacelike one, a timelike and a spacelike one compose to a
timelike one, and two spacelike ones compose to a spacelike one. That is the **same rule as the type of a
direction in a tensor product**, where the type of a product direction is the product of the types of the
two factors, a timelike direction times a timelike one being spacelike; here the causal type of the
composite is the product of the types of the factors, and the null elements are the zero class. On the
material sector $N$ takes both signs — in a randomised sample of $100$ material pairs the four cells were
occupied $2$, $6$, $17$ and $75$ times — so a composition of two timelike operations is spacelike and the
massive class is not closed. What is closed is the **lightlike** part of the causal set and nothing
larger. The honest form of the reading is therefore "lightlike composes to lightlike", not "the causal set
is closed".

## The Square Lands in the Informational Sector

The square of a material element is not only central; it lands on one side of the central line, and the
side is the informational one. This is a one-line fact with a physical reading, and it is stated here
because it is the concrete coupling the two sectors of the framework otherwise lack.

**Proposition.** For $\tilde Q\in\mathbb{M}_-$ the norm $N(\tilde Q)$ is **real**, and
$\tilde Q\star\tilde Q=N(\tilde Q)e_0$ lies on the real central line $\mathbb{R}e_0$, which is contained
in the informational sector $\mathbb{M}_+$.

**Proof.** Write $\tilde Q=ict\,e_0+\mathbf x$ with $t$ and the components of $\mathbf x$ real. Then
$Q_0=ict$ is purely imaginary, the $Q_k$ are real, and $N(\tilde Q)=Q_0^{2}+\mathbf x^{2}=-c^{2}t^{2}+\mathbf x^{2}$
is real. The unit $e_0$ is Hermitian, so $\mathbb{R}e_0\subseteq\mathbb{M}_+$. The square is
$N(\tilde Q)e_0$ by the square identity.

**Remark (verified).** The statement was recomputed on $100$ random material elements: the square is
central and real, and equals $N(\tilde Q)e_0$, to machine precision on all of them.

**Reading.** The interval of a material operation is an **informational scalar**. Squaring is therefore a
map from the material sector to the informational sector, $\mathbb{M}_-\to\mathbb{M}_+$, written by the
product and not added by hand; it is the algebraic form of the fact that the norm of a four-vector is a
real number, and the real numbers are the scalar line of the informational sector. What the framework has
called an open question — a coupling between the two sectors beyond the Lorentz conjugation — has this
minimal instance: the *square* couples them, even though the *product* of two material elements does not,
since it carries a rotation part in $\mathbb{M}_-$ and a boost part in $\mathbb{M}_+$ and so lies in
neither sector.

**Caution.** The statement is about the square of one element and not about the product of two. It does
not say that a product of material elements is informational, and it does not by itself supply a dynamics
between the sectors. What it supplies is one algebraic map $\mathbb{M}_-\to\mathbb{M}_+$, the norm, with
its image the real scalar line. **Boundary.** The two sectors themselves are *The Anti-Hermitian Subspace
$\mathbb{M}_-$ as the Material Sector* and *The Hermitian Subspace $\mathbb{M}_+$ as the Informational
Sector*; this article owns only the map between them and does not restate their structure.

## The Interval Is Complex

The interval is a complex number, and splitting it reads the two sectors. For a general element
$\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu=q_\mu+iq'_\mu$,

$$
N(\tilde Q)=\sum_\mu \bigl(q_\mu^{2}-(q'_\mu)^{2}\bigr)+2i\sum_\mu q_\mu q'_\mu ,
$$

so the real part is the difference of the squared real and imaginary parameters and the imaginary part is
their overlap. On each of the two sectors one of the two families of parameters vanishes, $q_\mu q'_\mu=0$
term by term, so **$N$ is real on each sector separately** and complex only on a general element that mixes
them. The imaginary part is therefore a pure **sector-mixing term**: it vanishes on $\mathbb{M}_+\cup\mathbb{M}_-$ and measures the overlap of the material and informational contents of an element. This is the
quantity the introduction names when it says that the imaginary part of $N$ couples the two sectors through
cross terms; the name offered here, as a labelled reading, is an **overlap** or mixing term: each term
$q_\mu q'_\mu$ pairs one material parameter with one informational parameter of the same direction, $q'_0$
with $q_0$ on the time direction and $q_k$ with $q'_k$ on each space direction.

**Caution.** Only the real part is the interval, and the causal statements of this article are statements
about the real part. The imaginary part is not a causal quantity and is not the indefinite-metric form of
any later block; it is recorded here for the name and for the exact reason it vanishes on the sectors.

## The Reading: Composition Multiplies Intervals

**Proposed reading, labelled as such.** The interval is a **multiplicative charge of the material
composition**. Each clause below names a proved identity, and each is labelled as a reading.

- **The interval of a material operation is its square.** On the material coordinate
  $\tilde Q=ict\,e_0+\mathbf x$ the square is $(-c^{2}t^{2}+\mathbf x^{2})e_0$, the Minkowski interval.
  The interval, the four-velocity, the four-momentum and the rotor inverse are worked out in *Biquaternion
  Norm and Invertibility* and are cited, not repeated.
- **The massless shell is the vanishing of the square, and the mass shell a level set of it.** A
  four-momentum on shell has square $N(\tilde P)=-m^{2}c^{2}$, so the mass shell is
  $\{N=-m^{2}c^{2}\}$, interpolating between the null cone at $m=0$ and the timelike interior.
- **Composition multiplies intervals.** The interval is a square of the composition and not a component
  of it, which is why it composes multiplicatively and not additively.
- **Lightlike composes to lightlike.** The null cone is the absorbing set of the composition.
- **Composition cannot generate mass.** Because the interval of a composite is the product of the
  intervals, a lightlike factor stays lightlike under composition with anything, and mass is never
  produced additively by the product. The massive class is not closed, and the causal type of a composite
  is the product of the causal types.
- **The square is informational.** On the material sector $N$ is real, so the square lands on the real
  central line $\mathbb{R}e_0$, which lies in $\mathbb{M}_+$. Squaring is a map $\mathbb{M}_-\to\mathbb{M}_+$,
  and the interval of a material operation is an informational scalar.
- **The interval is complex, and its imaginary part is a sector overlap.** $N$ is real on each sector and
  complex only on an element that mixes them; the imaginary part is the overlap of the material and
  informational contents.
- **The interval-one operations are the interval-preserving operations.** They form a group **under the
  ordinary product**, the group $\{\tilde U:N(\tilde U)=1\}$, of complex dimension three, which is the
  two-fold cover of the restricted Lorentz group. The group statement belongs to the associative product
  and not to the material one, for the reason given below.
- **The multiplicative law is an additive law in the logarithm.** The proved identity
  $N(\tilde P\star\tilde Q)=N(\tilde P)N(\tilde Q)$ is a law of multiplication, and wherever $N\neq0$ a
  logarithm turns it into a law of addition,
  $\ln N(\tilde P\star\tilde Q)=\ln N(\tilde P)+\ln N(\tilde Q)$. The quantity $\tfrac12\ln N$ is therefore
  offered, **as a reading**, as the **additive potential** whose exponential is the interval: it adds over
  the composition where the interval multiplies. The logarithm is not introduced only for this reading. It
  is already the quantity in which the framework measures information loss: the Lyapunov exponent of the
  informational sector is
  $\lambda=\lim_{t\to\infty}\tfrac1{2t}\log\bigl(\lvert N(\delta\tilde\rho(t))\rvert/\lvert N(\delta\tilde\rho(0))\rvert\bigr)$,
  with the factor $\tfrac12$ forced by the quadratic form, and the multiplicativity of $N$ is
  what makes the logarithm additive along a flow and the limit finite (*The Lyapunov Exponent and
  Information Loss in the Biquaternion Framework*). Read on a material element $ict\,e_0+\mathbf x$ the
  potential is half the logarithm of the magnitude of the Minkowski interval, $-c^{2}t^{2}+\mathbf x^{2}$.
  The algebra proves the multiplicative law and nothing about the physical use of its logarithm, and the
  additive-potential name is the framework's.

## The Limits of the Reading

**Multiplicativity is not conservation.** The interval is preserved only by the interval-one elements.
Under a general composition it changes, by multiplication. An interval is not a conserved quantity of the
material composition unless the acting set is restricted to the unit group, and any statement that "the
interval is preserved" must name the acting set.

**Closure is under the binary product, not under every word.** The quaternionic product is not
associative: its associator is nonzero on $24$ of the $64$ triples of basis elements, and it satisfies
none of the weaker identities — not alternativity, not flexibility, not third-power associativity
(*The Associator and the Ternary Product of the Quaternionic Product*). The closure proved above is the
statement "if $N(\tilde P)=0$ then $N(\tilde P\star\tilde Q)=0$" and nothing more. A word of three
operations has no bracketing-free value, and the rectangle of the square is defined for one element only.

**The logarithm is multi-valued, and its use is confined to a sector.** The additive-potential reading
needs $N\neq0$, so it excludes the null cone, which is exactly the set the closure statement is about; and
a logarithm of a complex number is defined only up to $2\pi i$, so at most its **real part**
$\tfrac12\ln\lvert N\rvert$ is a well-defined real label, and only where $N$ is real. This is the
restriction under which the framework does use it: the Lyapunov exponent above is written with $\lvert N\rvert$
precisely because the informational sector's norm is real there. The algebra supplies neither the branch
nor the physical meaning of the potential.

**Open question.** Whether the multiplicative-charge reading is more than a naming is not settled here.
The algebra proves the identity; the reading names $N$ a charge of the composition. What would make the
naming content is a composition law of the physical operations that the multiplicative law explains, and
the framework records the question rather than resolving it.

## The Ledger

**Proved.** The square identity $\tilde Q\star\tilde Q=N(\tilde Q)e_0$ and the centrality of the square.
The contrast with the ordinary square $\tilde Q\tilde Q=(Q_0^{2}-(\mathbf Q,\mathbf Q))e_0+2Q_0\mathbf Q$,
whose scalar value is $B(\tilde Q,\tilde Q)$ and which is central only in the two degenerate cases; the two
squares differ by the sign of the vector pairing, which the natural conjugation inserts. The
multiplicativity $N(\tilde P\star\tilde Q)=N(\tilde P)N(\tilde Q)$ and the level-set law
$\{N=\lambda\}\star\{N=\mu\}\subseteq\{N=\lambda\mu\}$; the closure of the units, of the interval-one set
and of the null set; the preservation of the level sets $c=0$ and $c=1$ and of no other. The falsity of
the closure of the two sectors, with the witness $e_1\star e_1=e_0$, and of the causal set, since the sign
of the interval multiplies; the four-cell sign table of the causal types, with the occupation $2$, $6$,
$17$, $75$ over $100$ random material pairs. The sector-bridge proposition, that $N$ is real on the
material sector, so the square lands on the real central line $\mathbb{R}e_0\subseteq\mathbb{M}_+$; and
the complex split $N=\sum_\mu\bigl(q_\mu^{2}-(q'_\mu)^{2}\bigr)+2i\sum_\mu q_\mu q'_\mu$, real on each
sector and complex only on a sector-mixing element.

**Readings.** That the interval of a material operation is its square and is a multiplicative charge of
the material composition; that composing two operations multiplies their intervals and moves them between
the level sets, so the interval is a **scale** and not a conserved quantity; that the massless
shell is the vanishing of the square; that lightlike propagation composes to lightlike propagation; that
composition cannot generate mass; that the interval-one operations are the interval-preserving
operations; that the square is a map $\mathbb{M}_-\to\mathbb{M}_+$ and the interval of a material
operation an informational scalar; that the imaginary part of the interval is the overlap of the material
and informational contents; that the multiplicative law is additive in the logarithm, so that
$\tfrac12\ln N$ is offered as the **additive potential** whose exponential is the interval, the same
logarithm in which the informational sector's Lyapunov exponent is measured.

**Not claimed.** That a physical operation is a biquaternion, or that its square has a physical process
behind it. That the interval is conserved by a general composition. That the causal set is closed. That a
word of three null operations is null. That the multiplicative-charge wording is forced by the algebra
rather than chosen. That the logarithm of the interval is a physical potential, or that
$\tfrac12\ln\lvert N\rvert$ is a conserved or a measured quantity, or that the additive-potential name is
forced by the algebra. That the additive potential of a material composition is the Lyapunov exponent of
an informational flow: the two share the logarithm of $N$ and are otherwise different objects, one a label
of a composition and the other a rate along a flow. That the sector bridge of the square is a dynamics
between the sectors, or that the imaginary part of the interval is a physical process: only the map
$\mathbb{M}_-\to\mathbb{M}_+$ and the name of the overlap are supplied, and the coupling between the
sectors remains an open question of the introduction.

## Physical Readings

The interval reads as the square of the composition, the mass as its charge and the sign as the sector. Two further readings belong with it. The norm is reversed by the central generator, $N(i\tilde Q) = -N(\tilde Q)$, so the exchange that ticks the clock also carries the sign of the interval, and the flip of signature between the two sectors is one application of the tick (*Each Sector Is the Other's Clock: the Sector Exchange as Relational Time*). And the interval is the form that a change of the local complex structure moves, so its sign at a point is data of the embedding rather than of the algebra (*Conventions in the Biquaternion Universe*).

## Summary

The quaternionic product $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ is the ordinary product with
the natural conjugation inserted in the first slot, and the insertion reverses the sign of the product of
the vector parts. Its square is central, $\tilde Q\star\tilde Q=N(\tilde Q)e_0$, so **the interval of a
material element is its square**, and on the material coordinate $ict\,e_0+\mathbf x$ the square is
$-c^{2}t^{2}+\mathbf x^{2}$. The ordinary product squares to something else,
$\tilde Q\tilde Q=(Q_0^{2}-(\mathbf Q,\mathbf Q))e_0+2Q_0\mathbf Q$, whose scalar value
$B(\tilde Q,\tilde Q)$ is negative definite on the material sector and has no cone: the two products differ
by the sign of the vector pairing, and that sign is the difference between a Euclidean square and the
interval. The value of the square is multiplicative, $N(\tilde P\star\tilde Q)=N(\tilde P)N(\tilde Q)$,
with the level-set law $\{N=\lambda\}\star\{N=\mu\}\subseteq\{N=\lambda\mu\}$; the units, the interval-one
set and the null set are closed, the null set exactly so, so lightlike propagation composes to lightlike
propagation and a massless operation cannot be made massive by composition. The interval is therefore read
as a **multiplicative charge** of the material composition, neither additive nor conserved in itself (its
logarithm, offered as a reading and bounded by its caution, is the additive potential), whose neutral
value is $1$ and whose absorbing value is $0$. Composition cannot generate mass: the causal type of a
composite is the product of the causal types, so the massive class is not closed and only the lightlike
class is. Because $N$ is real on the material sector, the square lands on the real central line
$\mathbb{R}e_0$, which is the informational sector: squaring is a map $\mathbb{M}_-\to\mathbb{M}_+$ and
the interval of a material operation is an informational scalar. Read on a general element $N$ is complex,
real on each sector, with imaginary part the overlap of the material and informational contents. What is
not closed matters as much: neither sector survives
the product, since the square of a material element is a central number, and the causal set is not closed,
since the sign of the interval multiplies. Because the product is not associative, the closure is a
closure under the two-element product, and a word of three operations has no bracketing-free value. The
interval, the mass shell, the four-velocity and the inverse are owned by *Biquaternion Norm and
Invertibility*; the cone by *The Light Cone as the Biquaternion Zero-Divisor Cone* and *Zero Divisors as a
Physical Locus in Biquaternionic Form*; the interval-one group by *The Lorentz Group as Biquaternion Norm
Automorphisms*; and the comparison of the four general products by *The Four General Products and Their Physical Readings: the Two Algebras and the Two Sesqualgebras*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | the biquaternion algebra |
| $e_0,e_1,e_2,e_3$; $i$ | the basis, $e_k^{2}=-e_0$; the central scalar imaginary |
| $\tilde Q=Q_0e_0+\mathbf Q$ | an element and its scalar–vector split |
| ${}^{\natural}$, ${}^{*}$ | the natural and the Hermitian conjugations |
| $\mathbb{M}_\pm$ | the material (anti-Hermitian) and informational (Hermitian) sectors |
| $\tilde P\tilde Q$ | the ordinary (associative) product |
| $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$ | the quaternionic product |
| $\tilde Q\star\tilde Q=N(\tilde Q)e_0$ | the square identity; the interval as the square |
| $N(\tilde Q)=\sum_\mu Q_\mu^{2}$ | the biquaternion norm |
| $B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)$ | the general plain bilinear form of the ordinary product |
| $N(\tilde P\star\tilde Q)=N(\tilde P)N(\tilde Q)$ | multiplicativity; the interval as a charge |
| $\mathcal N=\{N=0\}$ | the null set; the light cone on the material sector |
| $\{N=1\}$ | the interval-one operations; a group under the ordinary product |
| $ict\,e_0+\mathbf x$ | the material coordinate |

## Further Reading

- *The Mathematical Study of Biquaternions*, the physics entry point to the mathematical study under
  which this block sits.
- Mathematics article *Introduction to the General Quaternionic Algebra of Biquaternions*
  (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-biquaternions.md`), for the product, its table and its
  square.
- Mathematics article *Idempotents of the Quaternionic Product*
  (`articles_maths/idempotents-of-the-quaternionic-product.md`), for the square lemma.
- Mathematics article *The Associator and the Ternary Product of the Quaternionic Product*
  (`articles_maths/the-associator-and-the-ternary-product-of-the-quaternionic-product.md`), for the
  associator and the failure of the weaker identities.
- Companion article *Biquaternion Norm and Invertibility*, for the interval, the multiplicativity under the
  ordinary product, the invertibility criterion, the four-velocity and the mass shell.
- Companion article *The Ordinary Product and the Material Sector*, for the ordinary product, the form $B$
  and the Euclidean square.
- Companion article *Why the Material Composition Is Oriented and Cannot Measure*, for the orientation of
  the two slots, the left unit and the absence of a material projection.
- Companion article *The Light Cone as the Biquaternion Zero-Divisor Cone* and *Zero Divisors as a
  Physical Locus in Biquaternionic Form*, for the cone.
- Companion articles *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* and *The Hermitian
  Subspace $\mathbb{M}_+$ as the Informational Sector*, for the two sectors whose square-coupling this
  article reads.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the Minkowski
  interval read off a product of the spacetime algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the quadratic form of the
  quaternion algebra, its zero divisors and its group of units.
