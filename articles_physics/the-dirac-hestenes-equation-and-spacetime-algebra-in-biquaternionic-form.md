# __The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form__

## Introduction

**Spacetime algebra** (STA) is the real algebra $\mathrm{Cl}_{1,3}(\mathbb R)$ of Minkowski space. David Hestenes and others use it as a coordinate-free language for relativistic physics, written in the algebra itself and never in an array. In STA the Dirac equation becomes one real equation for a field of the algebra,

$$
\tilde\nabla\psi\,\omega-eA\psi=m\psi v_0 ,
$$

where $\tilde\nabla$ is the corpus gradient, $\psi$ is an **even element**, $\omega=-\vec e_z$ is the source's imaginary unit with $\omega^2=-e_t$, and $v_0$ is a fixed timelike vector with $v_0^2=+1$. The equation is real: no complex number is introduced beyond the coefficients, no array is used, and the imaginary unit of the four-component equation of the older literature is replaced, on the field, by right multiplication by the fixed element $\omega$. Hestenes reads $\psi$ as a rotation times a density, so the eight real components of the field are the six parameters of a rotation plus a density and an angle. The electron's spin is then a geometric rotation, and the current is a geometric vector.

**Every derivative in this article is the corpus gradient**, cited and not restated. The gradient, its conjugate and its scalar square $\Box$ are fixed once for the series in *Conventions of the Operators and the Calculus*, §*The Gradient*, and the article adds no second derivative of its own. A free equation is therefore first order in one field, $\tilde\nabla\tilde F=0$; a mass is carried by the chiral pair

$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,
\qquad
\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R,
$$

which is the corpus's own equation; and no one-field first-order massive equation is written here, because the gradient cannot supply one.

The connection to the biquaternion framework is closer than for any other topic in this series. The **even part** of the spacetime algebra is, as a real algebra, the **biquaternion algebra** $\mathbb{B}=\mathbb{C}\otimes_\mathbb R\mathbb H$ of the companion articles. The field $\psi$ is an even element; it *is* an element of $\mathbb B$, with the same eight real components as the framework's field. The source's letters are kept, and their values are fixed once and used throughout: the spin plane that multiplies the field is $\omega=-\vec e_z$ with $\omega^2=-e_t$, an element of $\mathbb B$, and the fixed timelike vector is $v_0$, with $v_0^2=+1$, an odd element that $\mathbb B$ does not contain. The pseudoscalar of the spacetime algebra is central on the even part and of square $-e_t$: it is the corpus's central imaginary $i$, and the two are one element. The spin plane is not: it anticommutes with $\vec e_x$ and $\vec e_y$, commutes with $\vec e_z$ and $e_t$, and acts on the two parts of the field as $\mp i$. The central $i$ therefore stays free, and the imaginary unit of the equation is the spin plane and not the centre of $\mathbb B$. The Dirac–Hestenes equation and the framework's equation are two readings of the same algebra, and this article identifies where they agree and where they do not.

The article keeps three equations apart, because the corpus now carries more than one and they must not be read as one. The corpus's own equation is the **one-sided chiral pair**, in which the gradient acts on the left and the field is split into its two chirality parts $\tilde\Psi_L$ and $\tilde\Psi_R$. Kravchenko's equation is **two-sided**, with the derivative on the left, the mass on the right through a fixed direction, and a conjugation in the mass term. The Dirac–Hestenes equation is a third form: its derivative acts on the left, but its spin plane and its mass act on the right. It is the spacetime-algebra face of the chiral formulation, not a rewriting of Kravchenko's equation. The two-sided structure is the subject of the section *The Two Equations of the Corpus*.

What this buys the framework is a sharper statement of one of its open questions. The Dirac–Hestenes equation is not written with a left multiplication alone: the terms $\psi\omega$ and $m\psi v_0$ multiply the field on the **right**, by the fixed spin plane and by the fixed **odd** vector $v_0$. The companion article on minimal coupling records, as an unresolved choice, whether the framework's matter field sits with the gradient on the left or on the right, and records that the conserved current needs an odd element. The Dirac–Hestenes equation is the standard formulation in which exactly that structure is explicit. This article does not resolve the framework's choice; it exhibits the formulation in which the choice is forced.

The article is organised as follows. The next section introduces the spacetime algebra. The third states the Dirac–Hestenes equation and writes its current and its spin. The fourth sets it beside the corpus's one-sided and two-sided equations. The fifth treats the symmetries and the zitterbewegung reading. The sixth works out the relation to the biquaternion framework in detail. The closing sections are the open questions, the summary, the notation table and the literature.

## Spacetime Algebra

### The algebra and its grades

The spacetime algebra is the real algebra generated by four vectors $v_\mu$ with

$$
v_\mu v_\nu+v_\nu v_\mu=2\varepsilon_\mu\delta_{\mu\nu},
$$

with $\varepsilon=(1,-1,-1,-1)$, so that $v_0^2=+1$ and $v_k^2=-1$ for $k=1,2,3$. It is $\mathrm{Cl}_{1,3}(\mathbb R)$; an array display is a convenience, not part of the structure, and this article uses none. A general element is a **multivector** with components of grades zero to four:

| Grade | Elements | Count |
|---|---|---|
| $0$ | scalar | $1$ |
| $1$ | vectors $v_\mu$ | $4$ |
| $2$ | bivectors $v_\mu v_\nu$ | $6$ |
| $3$ | trivectors, the products $v_0v_1v_2v_3\,v_\mu$ | $4$ |
| $4$ | pseudoscalar $v_0v_1v_2v_3$ | $1$ |

The pseudoscalar $v_0v_1v_2v_3$ squares to $-e_t$. It **commutes with every even element** and **anticommutes with every odd element**. That single fact is what makes the even part a complex algebra in its own right: on it, $v_0v_1v_2v_3$ is a commuting element of square $-1$, that is the central imaginary of the even algebra, and the centre of the even part is spanned by $e_t$ and by it.

### The even part and the field

The even elements — scalars, bivectors and the pseudoscalar — form a subalgebra isomorphic to $\mathrm{Cl}_{3,0}(\mathbb R)$, the algebra of the three spatial directions taken on their own. As a real algebra, $\mathrm{Cl}_{3,0}(\mathbb R)$ is $\mathbb C\otimes_\mathbb R\mathbb H$, which is the **biquaternion algebra of the framework**, with the units $e_t,\vec e_x,\vec e_y,\vec e_z$ of *Conventions in the Biquaternion Universe*. The field of the equation is an even element,

$$
\psi=\psi_0+\sum_{0\le\mu<\nu\le3}\psi_{\mu\nu}v_\mu v_\nu+\psi_4\,v_0v_1v_2v_3 ,
$$

with eight real components, and those eight are the eight real components of an element of $\mathbb B$. The source writes them in the basis of the grades; the article writes them in the units of the algebra.

**The imaginary unit.** Two objects square to $-1$ and are kept apart. The pseudoscalar $v_0v_1v_2v_3$ is central on the even part, so it is the corpus's central $i$: one element read twice. The spin plane is the source's other square root of $-1$, it is not central, and it is the phase generator of the equation. The source writes the pseudoscalar as $i$ and never uses it alone in the equation: it appears only multiplied by the third spatial plane, so what meets the field is the product, the spin plane.

**The source's letter.** This article writes $\omega$ for that product, the imaginary unit of the equation, and fixes its value in the biquaternion algebra once:

$$
\omega=-\vec e_z,\qquad \omega^2=-e_t .
$$

It is the source's imaginary unit and not the corpus's central $i$; the central $i$ stays free in this article. $\omega$ anticommutes with $\vec e_x$ and $\vec e_y$, commutes with $\vec e_z$ and $e_t$, and acts on the two parts of the field as $\mp i$, so it is the central imaginary up to the sign that the chirality fixes. Two factors of $\omega$ give $-e_t$, so a double $\omega$ in any display below is a sign.

**The decomposition.** Hestenes decomposes the field as a rotation, a density and an angle, and in the biquaternion alphabet the decomposition is the polar word of *Conventions of the Norms and the Pairings* read with a central phase:

$$
\boxed{\;\psi=\sqrt{\rho}\,e^{i\theta/2}R\;},\qquad R\tilde R=e_t,
$$

where $R$ is a **rotor**, that is a rotation of norm one, $\tilde R$ is its reverse — for an even element the reverse is the quaternion conjugate $R^{\natural}$, a derived form the source's letter $\tilde{}$ requires and the article states here rather than importing — $\rho\ge0$ is a scalar **density**, and $\theta$ is a scalar angle, the Yvon–Takabayasi angle, zero for a pure electron state. The source writes the phase factor with the pseudoscalar, $(\rho e^{\theta v_0v_1v_2v_3})^{1/2}$, which is the same factor: the pseudoscalar is the central imaginary, so $e^{\theta v_0v_1v_2v_3}=e^{i\theta}$, and the factor is central, commutes with $R$, and leaves the order of the two factors immaterial. The counting is exact: $R$ has the six parameters of a rotation, $\rho$ and $\theta$ add two, and the total is the eight real components of the field. The **physical interpretation** is that the electron's spin and its kinematic frame are rotations in spacetime, and the density is a probability density.

## The Dirac–Hestenes Equation

### The equation

Hestenes' form of the Dirac equation for an electron in an electromagnetic four-potential $A=\sum_{\mu=0}^{3}A_\mu v_\mu$ is the source's own equation, written here with the corpus's gradient and the source's letters:

$$
\boxed{\;\tilde\nabla\psi\,\omega-eA\psi=m\psi v_0\;},
\qquad
\omega=-\vec e_z,\qquad
\omega^2=-e_t,\qquad
v_0^2=+1 .
$$

These values are fixed once and used throughout. The source writes the derivative term with the spin plane on the right of the field, and in the biquaternion alphabet that factor is $\omega$, which multiplies the field on the right, $\psi\mapsto-\psi\vec e_z$. The mass multiplies the field on the right by $v_0$, and that right multiplication is the one ingredient of the equation the even algebra cannot hold: $v_0$ is odd and every element of $\mathbb B$ is even, so no element of the biquaternion algebra multiplies by it. Each term of the source's equation is odd, as it must be: the vector derivative, the potential and $v_0$ are vectors, while $\psi$ and the spin plane are even. In the biquaternion alphabet every element is even, and the mass is the only term whose right factor is odd. The equation is written in the algebra and not in an array display, and it is covariant under a change of frame

$$
\psi\mapsto R\psi,\qquad
A\mapsto R A\tilde R,\qquad
v_\mu\mapsto Rv_\mu\tilde R,\qquad
R\tilde R=e_t,
$$

with $\tilde R$ the reverse of the rotor. The frame is rotated with the field, so that the gradient transforms as $\tilde\nabla\mapsto R\tilde\nabla\tilde R$ and the derivative term of the transformed equation is the rotor times the original one.

### The four-component equation of the older literature

The four-component equation is the same equation read on a carrier of four components instead of on the algebra, and the passage between the two replaces each object of the algebra by the array of its action. Three arrays carry the whole of the difference: the array of the volume element, which the older display prints multiplied by the central $i$; the array of the chirality; and the array of the time direction, which is the mass's right factor read as a carrier. The two right multiplications of this article, by $\omega$ and by $v_0$, are those same objects in the algebra's own terms, and no fourth object is needed. The corpus fixes the display once, in *Conventions of the Matrix Models*, and a reader who needs an array finds it there; this article prints none, because the equation on the algebra is the same equation and carries every object of it as an element.

What survives the change of display is what the next subsection uses. The current, the spin density and the rotation are elements with a geometric meaning and not entries of an array, and the equation's right factors are elements of the algebra: the spin plane and the odd $v_0$. Those are the objects the corpus's own equation does not have, and they are the reason the two equations are compared at all.

### The field and its observables

The field is the one of the previous section, a rotation times a density and an angle, and its bilinear covariants are geometric multivectors. The Dirac current is the geometric vector

$$
\boxed{\;J=\psi v_0\tilde\psi\;},
\qquad
J_\mu=\mathrm{Sc}(J v_\mu),
\qquad
J=\sum_{\mu=0}^{3}\varepsilon_\mu J_\mu v_\mu ,
$$

with $J_\mu$ the components and $\tilde\psi$ the reverse of the field, which is $\psi^{\natural}$ on the even part. It is a pure vector, future-pointing and timelike, with $J^2=\rho^2>0$, and its time component is the probability density. The spin density is the bivector

$$
S=\psi\,\omega\tilde\psi ,
\qquad
\mathrm{Sc}(JS)=0 \quad(\theta=0),
$$

built with the same fixed plane that multiplies the derivative term of the equation, and orthogonal to the current for a pure electron state. The density bilinear is

$$
\psi\tilde\psi=\rho\,e^{i\theta}=\rho\cos\theta+\rho\sin\theta\,i ,
$$

whose scalar part is $\rho\cos\theta$ and whose central-imaginary part is $\rho\sin\theta$; the density is the modulus $\rho$, and $\theta$ is the Yvon–Takabayasi angle. The framework's current is the four-vector $\tilde J=ic\rho\,e_t+\vec J\in\mathbb M_-$ of the Maxwell article, and the minimal-coupling article records that it is not a product of two elements of $\mathbb B$: it needs one factor the even alphabet does not supply, written there as the right multiplication by $i\vec e_x$. The Dirac–Hestenes current $J=\psi v_0\tilde\psi$ is the same current written in the full algebra, where the odd fixed vector $v_0$ supplies exactly the ingredient the even algebra cannot hold.

## The Two Equations of the Corpus

The corpus carries two Dirac equations, and the Dirac–Hestenes equation must be placed against both. They are distinguished by which side the operator acts on and by what carries the chirality.

### The one-sided equation

The corpus's own equation is the **chiral pair**

$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,
\qquad
\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R,
$$

in which the gradient multiplies each chirality part of the field on the left, and the mass pairs the two parts across. The field is an element $\tilde\Psi$ of $\mathbb B$ with the two parts $\tilde\Psi_L$ and $\tilde\Psi_R$: the subscript is the chirality, the $L$ part the minus value and the $R$ part the plus value, and the convention that fixes it, together with the frame it depends on, is stated once in *Conventions of the Special Elements*, §*The Chirality Convention*. The operator is one-sided, and the two lines are the two parts of the field.

### The two-sided equation

Kravchenko's equation is a single equation on $\mathbb B$, written $\mathcal NF=0$. Split into its two sides, it reads

$$
\Bigl(i\frac{\partial}{\partial t'}+\sum_{k=1}^{3}\vec e_k\frac{\partial}{\partial Q_k}\Bigr)F=mi\,\overline F\,\vec e_z ,
$$

and the operator that collects the two sides is

$$
\mathcal NF=\Bigl(i\frac{\partial}{\partial t'}+\sum_{k=1}^{3}\vec e_k\frac{\partial}{\partial Q_k}\Bigr)F-mi\,\overline F\,\vec e_z .
$$

Here $t'$ is the physical time of the material sector, whose relation to the corpus's coordinate is fixed in *Conventions in the Biquaternion Universe*. The derivative is not a second letter for the gradient: Kravchenko's time derivative carries the sign opposite to the corpus's, and his spatial part is the spatial part of the corpus gradient unchanged. The sign is his convention for the time direction, and it is the only respect in which the two derivatives differ.

The left side is one-sided: the derivative acts from the left. The right side is the mass: the componentwise conjugation $\overline{\cdot}$ supplies the antilinear part, and the fixed direction $\vec e_z$ multiplies on the right. **The letter $\mathcal N$ is the whole two-sided operator and not a factor of it**: it is neither an element of the algebra nor a left or a right multiplication, since its action is a left derivative on one side and a conjugation followed by a right multiplier on the other. This is the **two-sided** equation of the corpus: two sides, one field, and no split of the field into parts. The two parts are there all the same, $F_L$ and $F_R$, and no term of the equation is written on them: the same unit $\vec e_z$ multiplies the conjugated field on the right.

### Where the Dirac–Hestenes equation sits

The Dirac–Hestenes equation is also two-sided, but its right factors are the fixed spin plane $\omega$ in the derivative term and the fixed timelike vector $v_0$ in the mass term. The spin plane is $\omega=-\vec e_z$ in the framework's units, so the two equations multiply by the same spatial unit and only the slot differs: Kravchenko puts $\vec e_z$ in the mass term, where a conjugation accompanies it, and the Dirac–Hestenes equation puts it in the derivative term, where it plays the part of the imaginary unit of the older display. The spin plane is the phase generator and not the chirality. The chirality is the volume element read with the central $i$, that is $i\omega=-i\vec e_z$, and it is the frame's volume cell of *Conventions of the Special Elements*, §*The Chirality Convention*; the two are different cells and are not interchangeable. The spin plane commutes with $v_0$ and the volume element anticommutes with it, because the volume element is even and $v_0$ is odd, and that is why the mass is the term that mixes the two parts of the field. What differs between the two equations is the company the unit keeps: Kravchenko's factor carries a conjugation and this one generates the phase. The mass itself is a right multiplication by an odd vector, not a conjugation together with a spatial direction. It is therefore the spacetime-algebra face of the **chiral** equation, not a rewriting of Kravchenko's. The word "two-sided" does not identify the two: it says only that a right action is present.

| | One-sided chiral pair | Dirac–Hestenes | Kravchenko two-sided |
|---|---|---|---|
| Equation | $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$, $\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R$ | $\tilde\nabla\psi\,\omega-eA\psi=m\psi v_0$ | $\mathcal NF=0$, with $\mathcal N$ as displayed |
| Field | $\tilde\Psi$, an element of $\mathbb B$, with the parts $\tilde\Psi_L$ and $\tilde\Psi_R$ | $\psi$, an even element, eight real components | $F\in\mathbb B$ |
| Derivative | left, by $\tilde\nabla$ and $\tilde\nabla^{\natural}$ | left, by $\tilde\nabla$ | left, by $\tilde\nabla$ with the $Q_t$ derivative reversed |
| Right factors | none | $\omega\,(=-\vec e_z)$ in the derivative, $v_0$ (odd, outside $\mathbb B$) in the mass | $\vec e_z$, on the right of the conjugated field |
| Mass | pairing of the two parts | right multiplication by the odd $v_0$ | $-mi\,\overline F\,\vec e_z$: a conjugation, then a right factor |
| Chirality | the two parts $\tilde\Psi_L$, $\tilde\Psi_R$ | the two parts $\psi_L$, $\psi_R$ | the two parts $F_L$, $F_R$, carried by no term |
| Use | the definition and the kinematics | the geometric STA form | the analytic dictionary and the integral representation |

The one-sided pair is the definition; the Dirac–Hestenes equation is the formulation in which the spin plane and the odd mass direction are explicit; Kravchenko's equation is the form in which the analytic machinery acts. The three carry the same eight real components and are related by changes of representation, not by changes of physics.

## Symmetries and the Zitterbewegung Interpretation

### Local phase symmetry

The Dirac–Hestenes equation is invariant under the local phase transformation

$$
\psi\mapsto \psi E,
\qquad
E=\exp\bigl(e\alpha(x)\,\omega\bigr),
\qquad
eA\mapsto eA-\tilde\nabla\alpha ,
$$

a **right** multiplication by the phase factor, accompanied by the gauge transformation of the potential, with $e$ the charge coupling constant of the equation. The side is forced by the equation: the phase must reach the derivative on the same side as the spin plane. The derivative term produces

$$
\tilde\nabla(\psi E)\,\omega
=(\tilde\nabla\psi)\,\omega E-e(\tilde\nabla\alpha)\,\psi E ,
$$

because $\partial E/\partial Q_\mu=e(\partial \alpha/\partial Q_\mu)\,\omega E$, because $E$ commutes with $\omega$, and because $\omega^2=-e_t$ turns the two factors of the spin plane into $-1$. The shifted potential produces $+e(\tilde\nabla\alpha)\psi E$, and the two cancel. The mass term is invariant as well, and this the source states in the spacetime algebra, where the phase generator is the spin plane and commutes with the vector $v_0$. A **left** multiplication by the phase does not work: it puts $\tilde\nabla\alpha$ between $\omega$ and $\psi$, where no rearrangement removes it, and a direct computation leaves a residual of order one. This is the left-versus-right matter-representation question that the minimal-coupling article records, and the STA equation answers it on the other side from the corpus's one-sided pair: the derivative acts on the left, and the phase, the spin plane and the mass all act on the right.

### The discrete symmetries

The discrete operations are not all of one kind, and they are not the right multiplications of the equation. The corpus's operations are

$$
P[\psi]=\psi(t',-\vec x)\,i\vec e_x,
\qquad
C[\psi]=-\vec e_y\,\psi^{*}\,\vec e_y,
\qquad
T[\psi]=-\vec e_y\,\psi^{*}(-t',\vec x),
$$

with $\vec x=x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ and $\psi^{*}$ the conjugation that is antilinear in the coefficients and reverses the order of a product, the antilinear map that carries one part of the field onto the other. **The three are not three of one kind, and none of them is a plain multiplication by a single element on one side.** Parity is a right multiplication by the fixed element $i\vec e_x$, which is odd. Charge conjugation multiplies on **both** sides, by $-\vec e_y$ on the left and by $\vec e_y$ on the right — the conjugation by $\vec e_y$ up to sign — and it is composed with $\psi^{*}$. Time reversal multiplies on the left by $-\vec e_y$ and is composed with the same $\psi^{*}$. Their characters and the side of each factor are collected in the table.

| Operation | Character | Action | Side of the factor | Chirality |
|---|---|---|---|---|
| Parity $P$ | linear | $\psi(t',-\vec x)\,i\vec e_x$ | right multiplication | exchanges $L$ and $R$ |
| Charge conjugation $C$ | antilinear | $-\vec e_y\,\psi^{*}\,\vec e_y$ | both sides | exchanges $L$ and $R$ |
| Time reversal $T$ | antilinear | $-\vec e_y\,\psi^{*}(-t',\vec x)$ | left multiplication | keeps $L$ and $R$ |

Parity is linear and is a one-sided multiplication. Charge conjugation and time reversal are **antilinear**, and each is a fixed factor composed with the conjugation $\psi^{*}$; charge conjugation is the one operation of the three that acts on both sides. This is why the right factors of the Dirac–Hestenes equation — the linear right multiplications by $\omega$ and by $v_0$ — are not the discrete operations: none of the three is that. The conventions, the signs and the composition $CPT$ are fixed in *The CPT Theorem in Biquaternionic Form* and *Parra's Four Options of the Dirac Equation and the Discrete Symmetries*.

### Zitterbewegung

Hestenes' interpretation reads the field's rotation as a physical rotation of a local frame, and the rapid oscillatory motion of a relativistic wave packet — zitterbewegung — as the rotation of the electron's frame along its world line. The framework's own companion article *Zitterbewegung in Biquaternionic Form* treats the same effect algebraically, through the structure of the velocity operator. The STA interpretation is the geometric counterpart, and the two share the observation that the oscillating quantity is a rotation.

## Relation to the Biquaternion Framework

### The eight-component match

The correspondence begins with a dimension count that is exact, not approximate. An even element of $\mathrm{Cl}_{1,3}$ has **eight real components**, and $\mathrm{Cl}_{1,3}^{+}\cong\mathbb C\otimes_\mathbb R\mathbb H$. The biquaternion field of the framework also has **eight real components**. The field $\psi$ is therefore an element of the biquaternion algebra, and the framework's field is the same object. This is the strongest correspondence in the series: not a transcription of coefficients, but an identity of the underlying real algebra.

### The two imaginaries

The framework carries a **central** imaginary unit $i$, commuting with everything; its basis is $e_t=1,\vec e_x,\vec e_y,\vec e_z$ over the complex numbers. The source carries an imaginary unit of its own, the spin plane that multiplies the field on the right; this article writes it $\omega=-\vec e_z$, with $\omega^2=-e_t$. The pseudoscalar of the spacetime algebra is a third symbol in the source's pages, and it is not a third object: it is the corpus's central $i$.

The spin plane and the central $i$ are **not** one object, and the difference is the whole of the translation. The source's $\omega$ is not central: it anticommutes with $\vec e_x$ and $\vec e_y$, commutes with $\vec e_z$ and $e_t$, and acts on the two parts of the field as $\mp i$. It is the central imaginary up to the sign that the chirality fixes, and the central $i$ of the framework stays free. What the comparison gives is therefore narrower and sharper than an identification: the equation's imaginary unit is a geometric object whose action is $\mp i$ on the two parts, and not a scalar. This is why the framework's complexification is natural rather than an extraneous addition: the source's imaginary unit was always geometric, and the corpus's central $i$ is what remains when the chirality is forgotten. The chirality itself is the volume element read with the central $i$, $i\omega=-i\vec e_z$, a root of $+1$.

### The odd vector $v_0$ and the right action

The two places where the Dirac–Hestenes equation differs in shape from the framework's one-sided equation are the two places the companion articles flag as subtle.

First, the equation is **not** a pure left-action equation. The terms $\psi\omega$ and $m\psi v_0$ multiply the field on the right by fixed algebra elements. The corpus's one-sided equation is written in terms of the gradient acting on the left, and the minimal-coupling article records the left-action and right-action constructions as two consistent covariant options whose choice is an unresolved matter representation. The Dirac–Hestenes equation is a standard formulation in which the right action is essential, and the fixed element in the mass term is $v_0$, which selects a rest frame. The gauge phase of the section above acts on the same side.

Second, the mass term uses an **odd** vector. The framework's mass is the linear pair of terms, derived from the gradient and the conjugate gradient, that couples the two parts of the field, and the minimal-coupling article notes that the conserved current requires an odd element that a product of two even factors does not supply. In the STA form the odd element is explicit and unavoidable: $m\psi v_0$ is odd because $v_0$ is odd, and the current $J=\psi v_0\tilde\psi$ carries the same $v_0$. That vector has no image in $\mathbb B$, which holds only even elements; what the alphabet records of it is the one odd factor that the current of the minimal-coupling article needs, the right multiplication by $i\vec e_x$. The framework's observation and the STA structure are the same statement in two languages: the current needs one odd factor, and the mass term here is built on one.

The distinction from Kravchenko's equation is the direction of the mass and the slot of the direction. In the Dirac–Hestenes equation the mass multiplies by the timelike $v_0$, and the spatial $\vec e_z$ sits in the derivative term as the spin plane; in Kravchenko's the mass multiplies by that same $\vec e_z$ and carries a conjugation. The two are different representations of the same mass term, and the table of the preceding section separates them.

### What the framework does not gain

The Dirac–Hestenes equation is an **equivalent rewriting** of the Dirac equation. It is real, free of arrays, and geometric, and those are real advantages of exposition and interpretation; they are not new physics. In particular it neither resolves the framework's left-versus-right representation question nor supplies an empirical prediction. It does, however, tell the framework what a resolution of that question looks like in the standard formulation, and it identifies the source's imaginary unit with a geometric element of the algebra whose action is $\mp i$ on the two parts of the field — a clarifying rather than a predictive result.

### The algebra of physical space and the spacetime algebra

The biquaternion framework is one of two readings of the same even algebra, and the other reading — the **algebra of physical space** of Baylis (*Relativity in Introductory Physics*, §VI; *Paravectors and the Geometry of Spacetime*) — is worth setting beside the spacetime algebra here, because the comparison is the reason the series prefers the smaller algebra.

Both are $\mathrm{Cl}_{3,0}$, the even part of $\mathrm{Cl}_{1,3}$, and both therefore have **eight** real independent elements against the **sixteen** of the full spacetime algebra. The three vectors of the algebra of physical space, which square to $+1$, are the three planes that the time direction spans with the three spatial directions, and the two volume elements are one element. That is the algebraic content of the corpus's statement that the biquaternion algebra is the even part of $\mathrm{Cl}_{1,3}$.

**Two structural differences follow.** First, the volume element. In the algebra of physical space the volume element is the product of three vectors, and because the underlying dimension is odd it is **central**: it commutes with the vectors as well as with the bivectors, so it can be treated as the scalar imaginary of a complexification and the algebra is literally $\mathbb C\otimes_\mathbb R\mathbb H$. In the spacetime algebra the pseudoscalar $v_0v_1v_2v_3$ commutes with the even elements but **anticommutes with the four vectors** $v_\mu$. On the even part it too is a central element of square $-1$, but on the full algebra it is an oriented volume element rather than a scalar imaginary, and this is why the spacetime algebra is normally presented as a real algebra where the complex structure appears only on restriction. Second, the presentation. The spacetime algebra is usually developed through the outer product and the decomposition into grades of its sixteen dimensions; the algebra of physical space works with the product alone, the outer product being the bivector part of a product and the duality being multiplication by the volume element, so that no separate exterior calculus has to be carried.

**The compensating cost and gain.** The algebra of physical space needs an extra conjugation to express the Minkowski form of a paravector, one that reverses the order of a product and flips the sign of the vector part, and on a paravector $p=p_0+\vec p$ it acts as $p_0-\vec p$; the spacetime algebra gets the same form from its indefinite signature directly. That map is not one of the four maps of the biquaternion alphabet, and a reader who takes the algebra of physical space for the spacetime algebra will read one more conjugation than there is. In exchange it gives the paravector identity $p(p_0-\vec p)=p_0^2-\vec p^2$ *inside* a definite algebra, and with it a metric relation that the spacetime algebra cannot state in the same way: the **measured** (Euclidean) length of a displacement on a spacetime diagram is the modulus of the paravector, while the **Minkowski** length is the same modulus combined with a hyperbolic angle read off from the diagram — the source's §III.C result. The series uses the biquaternion algebra, which is the algebra of physical space with the generators chosen to square to $-1$; the comparison above is the whole of the difference between them.

### The space-algebra formulation and the equivalence of the three

The STA formulation is one of three equivalent real rewritings of Dirac theory that the series records; the other two are the corpus's biquaternion chiral pair and the space formulation of Daviau, which writes the equation on the full algebra of physical space with a conjugation in the mass term. The equation is the companion article's:

$$
\tilde\nabla\varphi\,\omega_1=m\varphi^{*}+qA\varphi ,
$$

where $\varphi$ is an element of the algebra on the same eight real parameters, $\omega_1=-\vec e_x$ is the fixed unit of that equation — the spin plane taken along the first spatial direction — $\varphi^{*}$ is the star of that article, a conjugation composed with a two-sided multiplication by a fixed unit, $q$ is the charge as that article writes it, and the gradient is cyclically permuted over the space directions. The charge $q$ is $-e$ in the sign convention of the equation above, and the mass enters with the opposite sign. The three formulations are related by the sign of the mass, a cyclic relabelling of the space directions, and the star. In particular the Dirac–Hestenes equation is Parra's option $\{2\}$ and the Daviau equation is Parra's option $\{1\}$, two of the four inequivalent sign conventions of one equation, permuted by the discrete group $\Gamma_{1,3}/\Gamma^+_{1,3}$. The details, the dictionary and the equivalence are in the two companion articles.

## Open Questions

1. **Which fixed direction?** The standard formulation fixes the timelike vector $v_0$, and the mass and the current are both built on it. Does the framework's field select a fixed timelike direction of its own, and is it the same one? The corpus's own equations carry no such vector, and the question is whether one is forced by the algebra or chosen by the display.

2. **The right action.** If the physical Dirac field is the STA field, then the framework's equation must be rewritten to act on the right for the spin plane, the mass and the gauge phase. What, algebraically, distinguishes the left from the right action here, and does the framework's sector split select one? The two-sided form of Kravchenko's equation is the other side of the same question.

3. **The decomposition.** Hestenes' $\psi=\sqrt{\rho}\,e^{i\theta/2}R$ singles out a rotation, a density and an angle as the physical content. Does the framework's field admit the same decomposition, and does its norm $\langle\tilde Q\rangle_{\natural}$ play the role of the density $\rho$?

4. **Charge conjugation.** Charge conjugation is antilinear, and its factor is the one operation of the three that multiplies on both sides, $-\vec e_y(\cdot)\vec e_y$; the parity's factor is the one-sided right multiplication by $i\vec e_x$. The framework's conjugation articles build charge conjugation from the real structure $\flat$. Are the two the same operation in different normalisations?

5. **Zitterbewegung.** The two interpretations — the algebraic one of the framework's zitterbewegung article and the geometric one of STA — should be compared directly; the corpus does not yet contain the comparison.

6. **Empirical contact.** As everywhere, an equivalent rewriting carries no prediction. The question is whether the identification of the source's imaginary unit with the frame's spin plane lets the framework import any of STA's structural results, and if so whether any of them is testable.

## Summary

Spacetime algebra is the real algebra $\mathrm{Cl}_{1,3}(\mathbb R)$ of Minkowski space, and the Dirac–Hestenes equation

$$
\tilde\nabla\psi\,\omega-eA\psi=m\psi v_0
$$

is the Dirac equation rewritten in it as one real equation for an even element. The field has eight real components; it decomposes as $\psi=\sqrt{\rho}\,e^{i\theta/2}R$ into a rotation, a density and an angle; and the current is the geometric vector $J=\psi v_0\tilde\psi$. The older four-component display is the same equation read on a carrier of four components, and it is fixed once in *Conventions of the Matrix Models*; this article prints no array.

The corpus carries two Dirac equations, and the Dirac–Hestenes equation is a third form placed against both. The **one-sided chiral pair** $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$, $\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R$ carries the field in its two parts. **Kravchenko's two-sided equation** $\mathcal NF=0$ carries the derivative on the left, the mass on the right through $\vec e_z$, and a conjugation in the mass term. The Dirac–Hestenes equation carries the derivative on the left and the spin plane and the mass on the right, and it is the STA face of the chiral equation, not a rewriting of Kravchenko's.

The correspondence with the biquaternion framework is the closest in this series and is exact at the level of the algebra: the even part of $\mathrm{Cl}_{1,3}$ is the biquaternion algebra $\mathbb C\otimes_\mathbb R\mathbb H$, so the field $\psi$ *is* a biquaternion with the framework's eight real components. The equation's imaginary unit is not the corpus's central $i$: it is the spin plane $\omega=-\vec e_z$, of square $-e_t$, which anticommutes with $\vec e_x$ and $\vec e_y$ and acts as $\mp i$ on the two parts of the field, so the central $i$ stays free. The equation's two characteristic features — the **right** action of the spin plane and of the mass, and the **odd** $v_0$ that carries the mass and the current, an element the even algebra does not contain — are exactly the structures the framework's companion articles flag as subtle, the left-versus-right matter representation and the odd element the current requires. The equation's gauge phase acts on the right, with the spin plane, while the derivative acts on the left; that is the answer the standard formulation gives to the representation question. The Dirac–Hestenes equation is an equivalent rewriting and carries no new prediction, but it is the standard formulation in which the structures behind the framework's open questions are explicit in the language of the full spacetime algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Cl}_{1,3}(\mathbb R)$ | Spacetime algebra, $v_0^2=+1$, $v_k^2=-1$ |
| $v_0v_1v_2v_3$ | Pseudoscalar of the spacetime algebra; square $-1$, central on the even part, the corpus's central $i$ |
| $\tilde\nabla$, $\tilde\nabla^{\natural}$, $\Box$ | Corpus gradient, its conjugate, and the scalar square; cited to *Conventions of the Operators and the Calculus* |
| $\omega=-\vec e_z$ | The source's imaginary unit, the spin plane; $\omega^2=-e_t$, right multiplication, even |
| $i\omega=-i\vec e_z$ | The chirality, the frame's volume cell; the two parts of the field are its two values |
| $\psi$ | The field of the Dirac–Hestenes equation, an even element |
| $\psi_L$, $\psi_R$ | Its two parts; their values are the minus one and the plus one |
| $\psi=\sqrt{\rho}\,e^{i\theta/2}R$ | Rotation, density and angle; $R\tilde R=e_t$ |
| $v_0$ | Fixed timelike vector, $v_0^2=+1$; odd, so not an element of $\mathbb B$; mass and current, right multiplication |
| $J=\psi v_0\tilde\psi$ | Dirac current, a vector with $J^2=\rho^2$ |
| $S=\psi\,\omega\tilde\psi$ | Spin density, a bivector with $\mathrm{Sc}(JS)=0$ at $\theta=0$ |
| $\mathbb B=\mathbb C\otimes_\mathbb R\mathbb H$ | Biquaternion algebra $=$ even part of $\mathrm{Cl}_{1,3}$ |
| $i$ | Framework's central imaginary unit, kept free; the source's unit is $\omega$ |

## Further Reading

- D. Hestenes, *Space–Time Algebra* (Gordon and Breach, 1966; reprinted Birkhäuser, 2015), for the original formulation.
- D. Hestenes, "Real spinor fields," *Journal of Mathematical Physics* **8** (1967) 798–808, for the field and its observables.
- C. Doran and A. Lasenby, *Geometric Algebra for Physicists* (Cambridge University Press, 2003), chapters 8 and 9, for the Dirac equation in STA and the field of the algebra.
- C. Doran, A. Lasenby, S. Gull and S. Somaroo, "Spacetime algebra and electron physics," *Advances in Imaging and Electron Physics* **95** (1996) 271–386, for the systematic treatment.
- S. Gull, A. Lasenby and C. Doran, "Imaginary numbers are not real — the geometric algebra of spacetime," *Foundations of Physics* **23** (1993) 1175–1201, for the pedagogic account of the pseudoscalar and the imaginary unit.
- D. Hestenes, "Zitterbewegung in quantum mechanics," *Foundations of Physics* **40** (2010) 1–54, for the rotor interpretation of the oscillatory motion.
- W. E. Baylis (ed.), *Clifford (Geometric) Algebras with Applications in Physics, Mathematics and Engineering* (Birkhäuser, 1996), for the broader context.
- B. Fauser, "On the equivalence of Daviau's space Clifford algebraic, Hestenes' and Parra's formulations of (real) Dirac theory," arXiv:hep-th/9908200, 1999, for the equivalence of this formulation with the space and Parra formulations used in the subsection above.
- The companion articles of this series: [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), [The Daviau Map and the Space Clifford Formulation of the Dirac Equation](the-daviau-map-and-the-space-clifford-formulation-of-the-dirac-equation.html), [Parra's Four Options of the Dirac Equation and the Discrete Symmetries](parras-four-options-of-the-dirac-equation-and-the-discrete-symmetries.html), [Zitterbewegung in Biquaternionic Form](zitterbewegung-in-biquaternionic-form.html), [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html), [The CPT Theorem in Biquaternionic Form](the-cpt-theorem-in-biquaternionic-form.html), and [The Dirac–Kähler Equation](../articles_maths/the-dirac-kahler-equation.html).
