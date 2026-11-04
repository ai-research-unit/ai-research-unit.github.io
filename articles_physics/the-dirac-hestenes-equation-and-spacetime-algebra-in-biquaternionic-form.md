# __The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form__

## Introduction

**Spacetime algebra** (STA) is the real Clifford algebra $\mathrm{Cl}_{1,3}(\mathbb R)$ of Minkowski space. David Hestenes and others use it as a coordinate-free and matrix-free language for relativistic physics. In STA the Dirac equation becomes one real equation for a multivector field,

$$
\tilde\nabla\psi\,\omega-eA\psi=m\psi v_0 ,
$$

where $\tilde\nabla$ is the corpus gradient defined in the next paragraph, $\psi$ is an **even multivector**, $\omega=-\vec e_z$ is the source's imaginary unit with $\omega^2=-e_t$, and $v_0$ is a fixed timelike vector with $v_0^2=+1$. The equation is real: no complex number is introduced, no matrix representation is used, and the imaginary unit of the column equation is replaced, on the spinor module, by right multiplication by the fixed volume element $\omega$. Hestenes reads $\psi$ as a Lorentz rotor times a density, so the eight real components of the Dirac spinor are the six parameters of a Lorentz transformation plus a density and an angle. The electron's spin is then a geometric rotation, and the current is a geometric vector.

**Every derivative in this article is the corpus gradient**, and the article defines it once, here, with its conjugate and its scalar square. With the units $e_t,\vec e_x,\vec e_y,\vec e_z$ of *Algebra and Element Conventions* and the coordinates $Q_\mu$,

$$
\tilde\nabla=\sum_{\mu\in\{t,x,y,z\}}e_\mu\frac{\partial}{\partial Q_\mu},
\qquad
\tilde\nabla^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu e_\mu\frac{\partial}{\partial Q_\mu},
\qquad
\Box=\tilde\nabla\tilde\nabla^{\natural}=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q ,
$$

with $\varepsilon=(1,-1,-1,-1)$ and $\Delta_Q=\partial^2/\partial Q_x^2+\partial^2/\partial Q_y^2+\partial^2/\partial Q_z^2$. On the material sector $Q_t=ict'$, so the gradient reads $-\frac{i}{c}e_t\partial/\partial t'+\sum_k\vec e_k\partial/\partial q_k$ and $\Box$ reads $\Delta-c^{-2}\partial^2/\partial t'^2$. The gradient is an element with derivative coefficients, and it multiplies its argument on the left. Its square is not a scalar: $e_t$ commutes with the three spatial units, so the two orders of a mixed derivative add instead of cancelling, and

$$
\tilde\nabla^2=\Box-2\Delta-\frac{2i}{c}\sum_k\vec e_k\frac{\partial^2}{\partial t'\,\partial q_k}.
$$

The scalar second-order operator is the product with the conjugate, and only that product is the d'Alembertian. A free equation is therefore first order in one field, $\tilde\nabla\tilde F=0$; a mass is carried by the chiral pair

$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,
\qquad
\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R,
$$

which is the corpus's own equation; and no one-field first-order massive equation is written here, because the gradient cannot supply one.

The connection to the biquaternion framework is closer than for any other topic in this series. The **even subalgebra** of the spacetime algebra is, as a real algebra, the **biquaternion algebra** $\mathbb{B}=\mathbb{C}\otimes_\mathbb R\mathbb H$ of the companion articles. The Dirac–Hestenes spinor $\psi$ is an even multivector; it *is* a biquaternion, with the same eight real components as the framework's field. The source's letters are kept, and their values are fixed once and used throughout: the source's imaginary unit, the spin plane that multiplies the spinor, is $\omega=-\vec e_z$ with $\omega^2=-e_t$, an even element of $\mathbb B$, and the fixed timelike vector is $v_0$, with $v_0^2=+1$, an odd element of the spacetime algebra that $\mathbb B$ does not contain. The source's $\omega$ is not the corpus's central $i$. The central $i$ stays free in this article; $\omega$ anticommutes with $\vec e_x$ and $\vec e_y$, commutes with $\vec e_z$ and $e_t$, and acts on the two chiral halves as $\mp i$. The Dirac–Hestenes equation and the framework's equation are therefore two interpretations of the same algebra, and this article identifies where they agree and where they do not.

The article keeps three equations apart, because the corpus now carries more than one and they must not be read as one. The corpus's own equation is the **one-sided chiral pair**, in which the gradient acts on the left and the chirality is the central sign $\chi=i\tilde\Xi_{\mathrm{ad}}$, which splits the field into two halves. Kravchenko's equation is **two-sided**, with the derivative on the left, the mass on the right through a fixed direction, and a conjugation in the mass term. The Dirac–Hestenes equation is a third form: its derivative acts on the left, but its spin plane and its mass act on the right. It is the spacetime-algebra face of the chiral formulation, not a rewriting of Kravchenko's equation. The two-sided structure is the subject of the section *The Two Equations of the Corpus*.

What this buys the framework is a sharper statement of one of its open questions. The Dirac–Hestenes equation is not written with a left multiplication alone: the terms $\psi\omega$ and $m\psi v_0$ multiply the spinor on the **right**, by the fixed volume element and by the fixed **odd** vector $v_0$. The companion article on minimal coupling records, as an unresolved choice, whether the framework's matter field sits with the gradient on the left or on the right, and records that the conserved current needs an odd element. The Dirac–Hestenes equation is the standard formulation in which exactly that structure is explicit. This article does not resolve the framework's choice; it exhibits the formulation in which the choice is forced.

The article is organised as follows. The next section introduces the spacetime algebra. The third states the Dirac–Hestenes equation, reduces it to the matrix equation, and writes its current and its spin. The fourth sets it beside the corpus's one-sided and two-sided equations. The fifth treats the symmetries and the zitterbewegung reading. The sixth works out the relation to the biquaternion framework in detail. The closing sections are the open questions, the summary, the notation table and the literature.

## Spacetime Algebra

### The algebra and its grades

The spacetime algebra is the real Clifford algebra generated by four vectors $v_\mu$ with

$$
v_\mu v_\nu+v_\nu v_\mu=2\varepsilon_\mu\delta_{\mu\nu},
$$

with $\varepsilon=(1,-1,-1,-1)$, so that $v_0^2=+1$ and $v_k^2=-1$ for $k=1,2,3$. It is $\mathrm{Cl}_{1,3}(\mathbb R)$; a matrix representation is a convenience, not part of the structure, and this article uses none. A general element is a **multivector** with components of grades zero to four:

| Grade | Elements | Count |
|---|---|---|
| $0$ | scalar | $1$ |
| $1$ | vectors $v_\mu$ | $4$ |
| $2$ | bivectors $v_\mu v_\nu$ | $6$ |
| $3$ | trivectors, the products $v_0v_1v_2v_3\,v_\mu$ | $4$ |
| $4$ | pseudoscalar $v_0v_1v_2v_3$ | $1$ |

The pseudoscalar $v_0v_1v_2v_3$ squares to $-1$. It **commutes with every even-grade element** and **anticommutes with every odd-grade element**. That single fact is what makes the even part a complex algebra in its own right: on it, $v_0v_1v_2v_3$ is a commuting element of square $-1$.

### The even subalgebra and the spinor

The even-graded elements — scalars, bivectors and the pseudoscalar — form a subalgebra isomorphic to $\mathrm{Cl}_{3,0}(\mathbb R)$, the Pauli algebra. As a real algebra, $\mathrm{Cl}_{3,0}(\mathbb R)$ is $\mathbb C\otimes_\mathbb R\mathbb H$, which is the **biquaternion algebra of the framework**. A **spinor** in STA is an even multivector,

$$
\psi=\psi_0+\sum_{0\le\mu<\nu\le3}\psi_{\mu\nu}v_\mu v_\nu+\psi_4\,v_0v_1v_2v_3 ,
$$

with eight real components. The fixed bivectors $\sigma_k=v_kv_0$, for $k=1,2,3$, are the STA representatives of the Pauli vectors, and they square to $+1$.

**The imaginary unit.** Three objects square to $-1$ and are kept apart: the central scalar imaginary $i$ of $\mathbb B$, with $i^2=-1$; the pseudoscalar $v_0v_1v_2v_3$ of the spacetime algebra, with square $-1$, which is central on the even subalgebra; and the fixed spin plane $i\sigma_3$, with square $-1$, which is not central and is the phase generator of the equation. The source writes the pseudoscalar as $i$, and the equation never uses it alone: it appears only multiplied by $\sigma_3$, so what meets the spinor is the product $i\sigma_3$, the spin plane.

**The source's letter.** This article writes $\omega$ for that product, the imaginary unit of the equation, and fixes its value in the biquaternion algebra once:

$$
\omega=-\vec e_z,\qquad \omega^2=-e_t .
$$

It is the source's imaginary unit and not the corpus's central $i$; the central $i$ stays free in this article. $\omega$ anticommutes with $\vec e_x$ and $\vec e_y$, commutes with $\vec e_z$ and $e_t$, and acts on the two chiral halves as $\mp i$, so it is the central imaginary up to the sign that the chirality fixes. Two factors of $\omega$ give $-e_t$, so a double $\omega$ in any display below is a sign.

**The spinor decomposition.** Hestenes decomposes a general Dirac spinor as

$$
\boxed{\;\psi=\bigl(\rho\,e^{\beta\,v_0v_1v_2v_3}\bigr)^{1/2}R=\sqrt{\rho}\,e^{\beta\,v_0v_1v_2v_3/2}R\;},
$$

where $R$ is a unimodular even multivector — a **rotor**, that is, a Lorentz transformation, with $R\tilde R=1$ — $\rho\ge0$ is a scalar **density**, and $\beta$ is a scalar angle, the Yvon–Takabayasi angle, zero for a pure electron state. The density factor $(\rho e^{\beta v_0v_1v_2v_3})^{1/2}$ is central on the even subalgebra, so it commutes with $R$ and the order of the two factors is immaterial. The counting is exact: $R$ has the six parameters of a Lorentz transformation, $\rho$ and $\beta$ add two, and the total is the eight real components of a Dirac spinor. The **physical interpretation** is that the electron's spin and its kinematic frame are rotations in spacetime, and the density is a probability density.

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

These values are fixed once and used throughout. The source writes the derivative term with the spin plane on the right of the spinor, $i\sigma_3$, and in the biquaternion alphabet that factor is $\omega$, which multiplies the spinor on the right, $\psi\mapsto-\psi\vec e_z$. The mass multiplies the spinor on the right by $v_0$, and that right multiplication is the one ingredient of the equation the even algebra cannot hold: $v_0$ is odd and every element of $\mathbb B$ is even, so no element of the biquaternion algebra multiplies by it. Each term of the source's equation is odd-graded, as it must be: the vector derivative, the potential and $v_0$ are vectors, while $\psi$ and the spin plane are even. In the biquaternion alphabet every element is even in the spacetime grading, and the mass is the only term whose right factor is odd. The equation is written in the algebra rather than in a matrix representation, and it is covariant under a change of Lorentz frame

$$
\psi\mapsto R\psi,\qquad
A\mapsto R A\tilde R,\qquad
v_\mu\mapsto Rv_\mu\tilde R,\qquad
R\tilde R=1,
$$

with $\tilde R$ the reverse of the rotor. The frame is rotated with the field, so that the gradient transforms as $\tilde\nabla\mapsto R\tilde\nabla\tilde R$ and the derivative term of the transformed equation is the rotor times the original one.

### Reduction to the matrix equation

The matrix Dirac equation is recovered by replacing each frame vector by its Clifford image, a $4\times4$ matrix $V_\mu$, and reading $\psi$ in the column representation,

$$
\sum_{\mu=0}^{3}V_\mu\left(i\frac{\partial}{\partial x_\mu}-eA_\mu\right)|\psi\rangle=m|\psi\rangle .
$$

The column equation carries the matrix $iI_4$; its counterpart in the algebra, on the spinor module, is the right multiplication by $\omega$. The source's pseudoscalar becomes the chirality matrix, up to the factor of $i$; the fixed vector $v_0$ becomes $V_0$; and the right multiplications by $\omega$ and by $v_0$ become fixed matrix factors. The passage uses a fixed spinor $u$ with $V_0u=u$, which is why the mass term of the column equation carries no visible matrix. The two formulations are equivalent, and the STA version has the advantage that every object in it — the spin density, the current, the rotation — has a geometric meaning.

### The spinor and its observables

The spinor is the one of the previous section, a rotor times a density and an angle, and its bilinear covariants are geometric multivectors. The Dirac current is the geometric vector

$$
\boxed{\;J=\psi v_0\tilde\psi\;},
\qquad
J_\mu=J\cdot v_\mu,
\qquad
J=\sum_{\mu=0}^{3}J_\mu v^\mu ,
$$

with $J_\mu$ the covariant components and $\tilde\psi$ the reverse of the spinor, which is $\psi^{\natural}$ on the even part. It is a pure vector, future-pointing and timelike, with $J^2=\rho^2>0$, and its time component is the probability density. The spin density is the bivector

$$
S=\psi\,\omega\tilde\psi ,
\qquad
J\cdot S=0 \quad(\beta=0),
$$

built with the same fixed plane that multiplies the derivative term of the equation, and orthogonal to the current for a pure electron state. The density bilinear is

$$
\psi\tilde\psi=\rho\,e^{\beta\,v_0v_1v_2v_3}=\rho\cos\beta+\rho\sin\beta\,v_0v_1v_2v_3,
$$

whose scalar part is $\rho\cos\beta$ and whose pseudoscalar part is $\rho\sin\beta$; the density is the modulus $\rho$, and $\beta$ is the Yvon–Takabayasi angle. The framework's current is the four-vector $\tilde J=ic\rho\,e_t+\vec J\in\mathbb M_-$ of the Maxwell article, and the minimal-coupling article records that it is a spinor-module object rather than a product in $\mathbb B$, since it needs a Clifford-odd factor, the right multiplication by $i\vec e_x$. The Dirac–Hestenes current $J=\psi v_0\tilde\psi$ is the same current written in the full algebra, where the odd fixed vector $v_0$ supplies exactly the ingredient the even algebra cannot hold.

## The Two Equations of the Corpus

The corpus carries two Dirac equations, and the Dirac–Hestenes equation must be placed against both. They are distinguished by which side the operator acts on and by what carries the chirality.

### The one-sided equation

The corpus's own equation is the **chiral pair**

$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,
\qquad
\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R,
$$

in which the gradient multiplies each chiral half on the left, and the mass is the off-diagonal pairing of the two halves. The field is $\tilde\Psi=\tilde\Psi_L+\tilde\Psi_R\in\Delta=S\oplus S^{\mathrm c}$. Chirality is the right multiplication by $i\omega=-i\vec e_z$, a root of $+1$; on the module it splits the field into the two halves, and the value of the mass is what mixes them. Its central form is the sign $\chi=i\tilde\Xi_{\mathrm{ad}}$ of the complexified algebra. The sign is $+1$ on one half and $-1$ on the other, so it is not itself a multiplier: the multiplication that realizes it on the module is the right multiplication by $i\omega$, and the two writings are a right action and a sign. The operator is one-sided, and the two lines are the two chiralities.

### The two-sided equation

Kravchenko's equation is a single equation on $\mathbb B$, written $\mathcal NF=0$. Split into its two sides, it reads

$$
\Bigl(i\frac{\partial}{\partial t'}+\sum_{k=1}^{3}\vec e_k\frac{\partial}{\partial Q_k}\Bigr)F=mi\,\overline F\,\vec e_z ,
$$

and the operator that collects the two sides is

$$
\mathcal NF=\Bigl(i\frac{\partial}{\partial t'}+\sum_{k=1}^{3}\vec e_k\frac{\partial}{\partial Q_k}\Bigr)F-mi\,\overline F\,\vec e_z .
$$

Here $t'$ is the physical time, related to the corpus's coordinate by $Q_t=ict'$ on the material sector. The derivative is not a second letter for the gradient: at $c=1$ the corpus gradient is $\tilde\nabla=-ie_t\partial/\partial t'+\sum_k\vec e_k\partial/\partial Q_k$, so Kravchenko's $+i\partial/\partial t'$ is $\tilde\nabla$ with the $Q_t$ derivative taken with the opposite sign, and his spatial part is the $\vec e_k$ part of $\tilde\nabla$ unchanged. The sign is his convention for the time direction, and it is the only respect in which the two derivatives differ.

The left side is one-sided: the derivative acts from the left. The right side is the mass: the componentwise conjugation $\overline{\cdot}$ supplies the antilinear part, and the fixed direction $\vec e_z$ multiplies on the right. **The letter $\mathcal N$ is the whole two-sided operator and not a factor of it**: it is neither an element of the algebra nor a left or a right multiplication, since its action is a left derivative on one side and a conjugation followed by a right multiplier on the other. This is the **two-sided** equation of the corpus: two sides, one field, no chiral split. Its chirality is carried by the same unit $\vec e_z$, a right multiplication, not a splitting of the field.

### Where the Dirac–Hestenes equation sits

The Dirac–Hestenes equation is also two-sided, but its right factors are the fixed spin plane $\omega$ in the derivative term and the fixed timelike vector $v_0$ in the mass term. The spin plane is $\omega=-\vec e_z$ in the framework's units, so the two equations multiply by the same spatial unit and only the slot differs: Kravchenko puts $\vec e_z$ in the mass term, where a conjugation accompanies it, and the Dirac–Hestenes equation puts it in the derivative term, where it plays the part of the imaginary unit of the matrix theory. The spin plane is the phase generator and not the chirality. The chirality is the volume element read with the central $i$, that is $i\omega=-i\vec e_z$, the grading of the even part. The spin plane commutes with $v_0$ and the chirality anticommutes with it, because the pseudoscalar that separates the two anticommutes with every vector; and that is why the mass mixes the two graded halves. What differs between the two equations is the company the unit keeps: Kravchenko's factor carries a conjugation and this one generates the phase. The mass itself is a right multiplication by an odd vector, not a conjugation together with a spatial direction. It is therefore the spacetime-algebra face of the **chiral** equation, not a rewriting of Kravchenko's. The word "two-sided" does not identify the two: it says only that a right action is present.

| | One-sided chiral pair | Dirac–Hestenes | Kravchenko two-sided |
|---|---|---|---|
| Equation | $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$, $\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R$ | $\tilde\nabla\psi\,\omega-eA\psi=m\psi v_0$ | $\mathcal NF=0$, with $\mathcal N$ as displayed |
| Field | $\tilde\Psi\in\Delta=S\oplus S^{\mathrm c}$ | $\psi$ even, eight real components | $F\in\mathbb B$ |
| Derivative | left, by $\tilde\nabla$ and $\tilde\nabla^{\natural}$ | left, by $\tilde\nabla$ | left, by $\tilde\nabla$ with the $Q_t$ derivative reversed |
| Right factors | none | $\omega\,(=-\vec e_z)$ in the derivative, $v_0$ (odd, outside $\mathbb B$) in the mass | $\vec e_z$, on the right of the conjugated field |
| Mass | off-diagonal pairing of the two halves | right multiplication by the odd $v_0$ | $-mi\,\overline F\,\vec e_z$: a conjugation, then a right factor |
| Chirality | the sign $\chi=i\tilde\Xi_{\mathrm{ad}}$, realized on the module as the right multiplication by $i\omega$, splitting $S\oplus S^{\mathrm c}$ | the same right multiplier $i\omega=-i\vec e_z$, a grading on the even part | the same unit $\vec e_z$ as a right multiplier, not a grading |
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

a **right** multiplication by the phase rotor, accompanied by the gauge transformation of the potential, with $e$ the charge coupling constant of the equation. The side is forced by the equation: the phase must reach the derivative on the same side as the spin plane. The derivative term produces

$$
\tilde\nabla(\psi E)\,\omega
=(\tilde\nabla\psi)\,\omega E-e(\tilde\nabla\alpha)\,\psi E ,
$$

because $\partial E/\partial Q_\mu=e(\partial \alpha/\partial Q_\mu)\,\omega E$, because $E$ commutes with $\omega$, and because $\omega^2=-e_t$ turns the two factors of the spin plane into $-1$. The shifted potential produces $+e(\tilde\nabla\alpha)\psi E$, and the two cancel. The mass term is invariant as well, and this the source states in the spacetime algebra, where the phase generator is the spin plane $-v_1v_2$ and commutes with the vector $v_0$. A **left** multiplication by the phase does not work: it puts $\tilde\nabla\alpha$ between $\omega$ and $\psi$, where no sign removes it, and a direct computation leaves a residual of order one. This is the left-versus-right matter-representation question that the minimal-coupling article records, and the STA equation answers it on the other side from the corpus's one-sided pair: the derivative acts on the left, and the phase, the spin plane and the mass all act on the right.

### The discrete symmetries

The discrete operations are not all of one kind, and they are not the right multiplications of the equation. The corpus's operations on the spinor module are

$$
P[\psi]=\psi(t',-\vec x)\,i\vec e_x,
\qquad
C[\psi]=-\vec e_y\,\psi^{*}\,\vec e_y,
\qquad
T[\psi]=-\vec e_y\,\psi^{*}(-t',\vec x),
$$

with $\vec x=x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ and $\psi^{*}$ the module conjugation, the antilinear map that carries one chiral half onto the other. **The three are not three of one kind, and none of them is a plain multiplication by a single element on one side.** Parity is a right multiplication by the fixed element $i\vec e_x$, whose Clifford image is odd. Charge conjugation multiplies on **both** sides, by $-\vec e_y$ on the left and by $\vec e_y$ on the right — the conjugation by $\vec e_y$ up to sign — and it is composed with $\psi^{*}$. Time reversal multiplies on the left by $-\vec e_y$ and is composed with the same $\psi^{*}$. Their characters and the side of each factor are collected in the table.

| Operation | Character | Action | Side of the factor | Chirality |
|---|---|---|---|---|
| Parity $P$ | linear | $\psi(t',-\vec x)\,i\vec e_x$ | right multiplication | flips |
| Charge conjugation $C$ | antilinear | $-\vec e_y\,\psi^{*}\,\vec e_y$ | both sides | flips |
| Time reversal $T$ | antilinear | $-\vec e_y\,\psi^{*}(-t',\vec x)$ | left multiplication | preserves |

Parity is linear and is a one-sided Clifford multiplication. Charge conjugation and time reversal are **antilinear**, and each is a fixed Clifford factor composed with the module conjugation; charge conjugation is the one operation of the three that acts on both sides. This is why the right factors of the Dirac–Hestenes equation — the linear right multiplications by $\omega$ and by $v_0$ — are not the discrete operations: none of the three is that. The conventions, the signs and the composition $CPT$ are fixed in *The CPT Theorem in Biquaternionic Form* and *Parra's Four Options of the Dirac Equation and the Discrete Symmetries*.

### Zitterbewegung

Hestenes' interpretation reads the spinor's rotation as a physical rotation of a local frame, and the rapid oscillatory motion of a relativistic wave packet — zitterbewegung — as the rotation of the electron's frame along its world line. The framework's own companion article *Zitterbewegung in Biquaternionic Form* treats the same effect algebraically, through the structure of the velocity operator. The STA interpretation is the geometric counterpart, and the two share the observation that the oscillating quantity is a rotation.

## Relation to the Biquaternion Framework

### The eight-component match

The correspondence begins with a dimension count that is exact, not approximate. An even multivector of $\mathrm{Cl}_{1,3}$ has **eight real components**, and $\mathrm{Cl}_{1,3}^{+}\cong\mathbb C\otimes_\mathbb R\mathbb H$. The biquaternion field of the framework also has **eight real components**. The Dirac–Hestenes spinor $\psi$ is therefore an element of the biquaternion algebra, and the framework's field is the same object. This is the strongest correspondence in the series: not a transcription of coefficients, but an identity of the underlying real algebra.

### The two imaginaries

The framework carries a **central** imaginary unit $i$, commuting with everything; its basis is $e_t=1,\vec e_x,\vec e_y,\vec e_z$ over the complex numbers. The source carries an imaginary unit of its own, the volume element of the display, which multiplies the spinor on the right; this article writes it $\omega=-\vec e_z$, with $\omega^2=-e_t$.

The two are **not** one object, and the difference is the whole of the translation. The source's $\omega$ is not central: it anticommutes with $\vec e_x$ and $\vec e_y$, commutes with $\vec e_z$ and $e_t$, and acts on the two chiral halves as $\mp i$. It is the central imaginary up to the sign that the chirality fixes, and the central $i$ of the framework stays free. What the comparison gives is therefore narrower and sharper than an identification: the equation's imaginary unit is the corpus's **volume element**, a geometric object whose action is $\mp i$ on the two halves, and not a scalar. This is why the framework's complexification is natural rather than an extraneous addition: the source's imaginary unit was always geometric, and the corpus's central $i$ is what remains when the chirality sign is forgotten. The chirality itself is that same element read with the central $i$, $i\omega=-i\vec e_z$, a root of $+1$.

### The odd vector $v_0$ and the right action

The two places where the Dirac–Hestenes equation differs in shape from the framework's one-sided equation are the two places the companion articles flag as subtle.

First, the equation is **not** a pure left-action equation. The terms $\psi\omega$ and $m\psi v_0$ multiply the spinor on the right by fixed algebra elements. The corpus's one-sided equation is written in terms of the gradient acting on the left, and the minimal-coupling article records the left-action and right-action constructions as two consistent covariant options whose choice is an unresolved matter representation. The Dirac–Hestenes equation is a standard formulation in which the right action is essential, and the fixed element in the mass term is $v_0$, which selects a rest frame. The gauge phase of the section above acts on the same side.

Second, the mass term uses an **odd** vector. The framework's mass is the linear chirality-off-diagonal pair of terms derived from the gradient and the conjugate gradient, and the minimal-coupling article notes that the conserved current requires an odd element that a product of two even factors does not supply. In the STA form the odd element is explicit and unavoidable: $m\psi v_0$ is odd because $v_0$ is odd, and the current $J=\psi v_0\tilde\psi$ carries the same $v_0$. That vector has no image in $\mathbb B$, which holds only even elements; what the alphabet records of it is the Clifford-odd factor that the Dirac adjoint of the minimal-coupling article carries, the right multiplication by $i\vec e_x$, whose gamma image is a gamma matrix. The framework's observation and the STA structure are the same statement in two languages: the current needs one Clifford-odd factor, and the mass term here is built on one.

The distinction from Kravchenko's equation is the direction of the mass and the slot of the direction. In the Dirac–Hestenes equation the mass multiplies by the timelike $v_0$, and the spatial $\vec e_z$ sits in the derivative term as the spin plane; in Kravchenko's the mass multiplies by that same $\vec e_z$ and carries a conjugation. The two are different representations of the same mass term, and the table of the preceding section separates them.

### What the framework does not gain

The Dirac–Hestenes equation is an **equivalent rewriting** of the Dirac equation. It is real, matrix-free and geometric, and those are real advantages of exposition and interpretation; they are not new physics. In particular it neither resolves the framework's left-versus-right representation question nor supplies an empirical prediction. It does, however, tell the framework what a resolution of that question looks like in the standard formulation, and it identifies the source's imaginary unit with the corpus's volume element, whose action is $\mp i$ on the two chiral halves — a clarifying rather than a predictive result.

### The algebra of physical space and the spacetime algebra

The biquaternion framework is one of two interpretations of the same even algebra, and the other interpretation — the **algebra of physical space** of Baylis (*Relativity in Introductory Physics*, §VI; *Paravectors and the Geometry of Spacetime*) — is worth setting beside the spacetime algebra here, because the comparison is the reason the series prefers the smaller algebra.

Both are $\mathrm{Cl}_{3,0}$, the even subalgebra of $\mathrm{Cl}_{1,3}$, and both therefore have **eight** real independent elements against the **sixteen** of the full spacetime algebra. The generator identifications are

$$
\boldsymbol\sigma_k\;\longleftrightarrow\;v_kv_0\quad(\text{bivectors of STA}),
\qquad
i=\boldsymbol\sigma_1\boldsymbol\sigma_2\boldsymbol\sigma_3\;\longleftrightarrow\;v_0v_1v_2v_3 ,
$$

with $\boldsymbol\sigma_k$ the vectors of the algebra of physical space, which square to $+1$. The second identification is exact in the ordering shown, since $\sigma_1\sigma_2\sigma_3=v_0v_1v_2v_3$ in the spacetime algebra. Thus the three **vectors** of the algebra of physical space are the three timelike–spacelike planes of the spacetime algebra, and the two pseudoscalars are one element. This is the algebraic content of the corpus's statement that the biquaternion algebra is the even subalgebra of $\mathrm{Cl}_{1,3}$.

**Two structural differences follow.** First, the volume element. In the algebra of physical space $i$ is the **pseudoscalar**, and because the underlying dimension is odd it is **central**: it commutes with the vectors $\boldsymbol\sigma_k$ as well as with the bivectors, so it can be treated as the scalar imaginary of a complexification and the algebra is literally $\mathbb C\otimes_\mathbb R\mathbb H$. In the spacetime algebra the pseudoscalar $v_0v_1v_2v_3$ commutes with the even elements but **anticommutes with the four vectors** $v_\mu$. On the spinor, even, subalgebra it too is a central element of square $-1$, but on the full algebra it is an oriented volume element rather than a scalar imaginary, and this is why the spacetime algebra is normally presented as a real algebra where the complex structure appears only on restriction. Second, the presentation. The spacetime algebra is usually developed through the outer product and the grade decomposition of its sixteen dimensions; the algebra of physical space works with the geometric product alone, the outer product being the bivector part of a product and the duality being multiplication by $i$, so that no separate exterior calculus has to be carried.

**The compensating cost and gain.** The algebra of physical space needs the extra **Clifford conjugate** $p\mapsto\bar p$ to express the Minkowski form of a paravector, which the spacetime algebra gets from its indefinite signature directly. In exchange it gives the paravector identity $p\bar p=p_0^2-\vec p^2$ *inside* a definite algebra, and with it a metric relation that the spacetime algebra cannot state in the same way: the **measured** (Euclidean) length of a displacement on a spacetime diagram is the modulus of the paravector, while the **Minkowski** length is the same modulus combined with a hyperbolic angle read off from the diagram — the source's §III.C result. The series uses the biquaternion algebra, which is the algebra of physical space with the generators chosen to square to $-1$; the comparison above is the whole of the difference between them.

### The space Clifford formulation and the equivalence of the three

The STA formulation is one of three equivalent real rewritings of Dirac theory that the series records; the other two are the corpus's biquaternion chiral pair and the **space Clifford formulation** of Daviau. Daviau writes the equation for a general element $\varphi$ of the Pauli algebra $\mathcal P\cong M_2(\mathbb C)$ as

$$
\tilde\nabla\varphi\,i\sigma_1=m\varphi^{*}+qA\varphi ,
$$

with the gradient cyclically permuted over the space directions, the star $\varphi^{*}=\sigma_2\bar\varphi\sigma_2$, which multiplies by $\sigma_2$ on both sides, composed with the coefficient conjugation $\bar{\cdot}$, the charge written $q$ as in that article, and the algebra acting on the spinor from both sides. The charge $q$ is $-e$ in the sign convention of the equation above, and the mass enters with the opposite sign. The three formulations are related by the sign of the mass, a cyclic relabelling of the space directions, and the star; and the star is the corpus's **complex conjugation** $\bar{\cdot}$ under the identification of the Pauli algebra with $\mathbb B$, dressed with a two-sided pair of units. In particular the Dirac–Hestenes equation is Parra's option $\{2\}$ and the Daviau equation is Parra's option $\{1\}$, two of the four inequivalent sign conventions of one equation, permuted by the discrete group $\Gamma_{1,3}/\Gamma^+_{1,3}$. The details, the dictionary and the equivalence are in the two companion articles.

## Open Questions

1. **Which ideal?** The framework's two Peirce carriers are its left and right Weyl spinors, the minimal left ideals of this reading. In STA a minimal ideal is selected by an idempotent built from a fixed null or timelike vector, and the Dirac–Hestenes equation uses $v_0$ explicitly. Does the framework's choice of ideal correspond to the standard choice of $v_0$, or to a different fixed vector?

2. **The right action.** If the physical Dirac field is the STA spinor, then the framework's equation must be rewritten to act on the right for the spin plane, the mass and the gauge phase. What, algebraically, distinguishes the left from the right action here, and does the framework's sector split select one? The two-sided form of Kravchenko's equation is the other side of the same question.

3. **The rotor decomposition.** Hestenes' $\psi=(\rho e^{\beta v_0v_1v_2v_3})^{1/2}R$ singles out a rotor and a density as the physical content. Does the framework's field admit the same decomposition, and does its norm $\langle\tilde Q\rangle_{\natural}$ play the role of the density $\rho$?

4. **Charge conjugation.** Charge conjugation is antilinear, and its factor is the one operation of the three that multiplies on both sides, $-\vec e_y(\cdot)\vec e_y$; the parity's factor is the one-sided right multiplication by $i\vec e_x$. The framework's conjugation articles build charge conjugation from the real structure $\flat$. Are the two the same operation in different normalisations?

5. **Zitterbewegung.** The two interpretations — the algebraic one of the framework's zitterbewegung article and the geometric rotor one of STA — should be compared directly; the corpus does not yet contain the comparison.

6. **Empirical contact.** As everywhere, an equivalent rewriting carries no prediction. The question is whether the identification of the source's imaginary unit with the corpus's volume element lets the framework import any of STA's structural results, and if so whether any of them is testable.

## Summary

Spacetime algebra is the real Clifford algebra $\mathrm{Cl}_{1,3}(\mathbb R)$ of Minkowski space, and the Dirac–Hestenes equation

$$
\tilde\nabla\psi\,\omega-eA\psi=m\psi v_0
$$

is the Dirac equation rewritten in it as one real equation for an even multivector spinor. The spinor has eight real components; it decomposes as $\psi=(\rho e^{\beta v_0v_1v_2v_3})^{1/2}R$ into a Lorentz rotor, a density and an angle; and the current is the geometric vector $J=\psi v_0\tilde\psi$. The matrix theory is recovered by representing the frame vectors with matrices, the source's imaginary unit with $iI_4$, and the pseudoscalar with the chirality matrix up to the factor of $i$.

The corpus carries two Dirac equations, and the Dirac–Hestenes equation is a third form placed against both. The **one-sided chiral pair** $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$, $\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R$ carries chirality as the splitting of the field into two halves. **Kravchenko's two-sided equation** $\mathcal NF=0$ carries the derivative on the left, the mass on the right through $\vec e_z$, and a conjugation in the mass term. The Dirac–Hestenes equation carries the derivative on the left and the spin plane and the mass on the right, and it is the STA face of the chiral equation, not a rewriting of Kravchenko's.

The correspondence with the biquaternion framework is the closest in this series and is exact at the level of the algebra: the even subalgebra of $\mathrm{Cl}_{1,3}$ is the biquaternion algebra $\mathbb C\otimes_\mathbb R\mathbb H$, so the Dirac–Hestenes spinor *is* a biquaternion with the framework's eight real components. The equation's imaginary unit is not the corpus's central $i$: it is the volume element $\omega=-\vec e_z$, of square $-e_t$, which anticommutes with $\vec e_x$ and $\vec e_y$ and acts as $\mp i$ on the two chiral halves, so the central $i$ stays free and the chirality is $i\omega$. The equation's two characteristic features — the **right** action of the spin plane and of the mass, and the **odd** $v_0$ that carries the mass and the current, an element the even algebra does not contain — are exactly the structures the framework's companion articles flag as subtle, the left-versus-right matter representation and the odd element the current requires. The equation's gauge phase acts on the right, with the spin plane, while the derivative acts on the left; that is the answer the standard formulation gives to the representation question. The Dirac–Hestenes equation is an equivalent rewriting and carries no new prediction, but it is the standard formulation in which the structures behind the framework's open questions are explicit in the language of the full spacetime algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Cl}_{1,3}(\mathbb R)$ | Spacetime algebra, $v_0^2=+1$, $v_k^2=-1$ |
| $v_0v_1v_2v_3$ | Pseudoscalar of the spacetime algebra; square $-1$, central on the even part |
| $\sigma_k=v_kv_0$ | STA Pauli bivectors, $\sigma_k^2=+1$ |
| $\tilde\nabla$, $\tilde\nabla^{\natural}$, $\Box$ | Corpus gradient, its conjugate, and $\Box=\tilde\nabla\tilde\nabla^{\natural}$ |
| $\omega=-\vec e_z$ | The source's imaginary unit, the spin plane; $\omega^2=-e_t$, right multiplication, even |
| $i\omega=-i\vec e_z$ | The chirality, the right multiplication by $i\omega$; square $+e_t$, $+1$ on one half and $-1$ on the other |
| $\chi=i\tilde\Xi_{\mathrm{ad}}$ | The same chirality as a sign on the complexified algebra; not a multiplier |
| $\psi$ | Dirac–Hestenes spinor, an even multivector |
| $\psi=(\rho e^{\beta v_0v_1v_2v_3})^{1/2}R$ | Rotor, density and angle decomposition |
| $v_0$ | Fixed timelike vector, $v_0^2=+1$; odd, so not an element of $\mathbb B$; mass and current, right multiplication |
| $J=\psi v_0\tilde\psi$ | Dirac current, a vector with $J^2=\rho^2$ |
| $S=\psi\,\omega\tilde\psi$ | Spin density, a bivector with $J\cdot S=0$ at $\beta=0$ |
| $\mathbb B=\mathbb C\otimes_\mathbb R\mathbb H$ | Biquaternion algebra $=$ even subalgebra of $\mathrm{Cl}_{1,3}$ |
| $i$ | Framework's central imaginary unit, kept free; the source's unit is $\omega$ |

## Further Reading

- D. Hestenes, *Space–Time Algebra* (Gordon and Breach, 1966; reprinted Birkhäuser, 2015), for the original formulation.
- D. Hestenes, "Real spinor fields," *Journal of Mathematical Physics* **8** (1967) 798–808, for the spinor and its observables.
- C. Doran and A. Lasenby, *Geometric Algebra for Physicists* (Cambridge University Press, 2003), chapters 8 and 9, for the Dirac equation in STA and the spinor.
- C. Doran, A. Lasenby, S. Gull and S. Somaroo, "Spacetime algebra and electron physics," *Advances in Imaging and Electron Physics* **95** (1996) 271–386, for the systematic treatment.
- S. Gull, A. Lasenby and C. Doran, "Imaginary numbers are not real — the geometric algebra of spacetime," *Foundations of Physics* **23** (1993) 1175–1201, for the pedagogic account of the pseudoscalar and the imaginary unit.
- D. Hestenes, "Zitterbewegung in quantum mechanics," *Foundations of Physics* **40** (2010) 1–54, for the rotor interpretation of the oscillatory motion.
- W. E. Baylis (ed.), *Clifford (Geometric) Algebras with Applications in Physics, Mathematics and Engineering* (Birkhäuser, 1996), for the broader context.
- B. Fauser, "On the equivalence of Daviau's space Clifford algebraic, Hestenes' and Parra's formulations of (real) Dirac theory," arXiv:hep-th/9908200, 1999, for the equivalence of this formulation with the space Clifford and Parra formulations used in the subsection above.
- The companion articles of this series: [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), [The Daviau Map and the Space Clifford Formulation of the Dirac Equation](the-daviau-map-and-the-space-clifford-formulation-of-the-dirac-equation.html), [Parra's Four Options of the Dirac Equation and the Discrete Symmetries](parras-four-options-of-the-dirac-equation-and-the-discrete-symmetries.html), [Zitterbewegung in Biquaternionic Form](zitterbewegung-in-biquaternionic-form.html), [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html), [The CPT Theorem in Biquaternionic Form](the-cpt-theorem-in-biquaternionic-form.html), and [The Dirac–Kähler Equation](../articles_maths/the-dirac-kahler-equation.html).
