# __The Dirac Equation in Biquaternionic Form__

## Introduction

The Dirac equation is the relativistic wave equation for spin-$\frac{1}{2}$ particles. It was discovered by Paul Dirac in 1928 as an attempt to reconcile quantum physics with special relativity, and it predicted the existence of antimatter. It is one of the foundational equations of quantum field theory, and it is the equation that governs electrons, quarks, and all fermions.

The Dirac equation is usually written with matrices. In the biquaternion algebra it needs none. The field is an element of $\mathbb{B}$, the operator is an element multiplying it, and the mass is the one coefficient that ties its two components together. The dynamics is the chiral pair

$$
\tilde\nabla_\Phi\tilde\Xi_{R} = k_m\,\tilde\Xi_{L},
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_{L} = k_m\,\tilde\Xi_{R} ,
$$

which is the pair of *Operator and Calculus Conventions*. Every derivative in $\tilde\nabla_\Phi$ carries an inverse length, so the coefficient on the right must carry one too, and it is written as the reciprocal of a length:

$$
k_m=\dfrac{mc}{\hbar}.
$$

That wave number is the reciprocal of the reduced Compton wavelength of the field, and it is the only one the article needs. It is defined in *The Three Wavenumbers of a Particle*, where it is written $k_m=mc/\hbar$. Below, the mass coefficient is always written $k_m$ and the mass-squared term always $k_m^{2}$. Since $mc=\hbar\,k_m$, the rest energy is $m\,c^{2}$ and the mass shell is $\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural}=-m^{2}\,c^{2}$, so every mass statement is read in this one length. At $m=0$ the pair decouples into the two one-sided equations $\tilde\nabla_\Phi\tilde\Xi_{R}=0$ and $(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_{L}=0$, one for each value. No matrix, no column and no array enters either line. A frame is declared once, because the value of a part is read by the frame's third direction, and no further choice is made.

This article develops the biquaternionic formulation of the Dirac equation. The gradient $\tilde\nabla_\Phi$ is the Dirac operator of the algebra: it is first order, it acts by left multiplication, and it squares to the scalar d'Alembertian through its conjugate. The equation is the chiral pair on the two letters of the pair, and each half obeys the Klein–Gordon equation. A second, **two-sided** form of the same equation — Kravchenko's dictionary, in which the spatial derivative acts from the left and the mass term from the right — is developed in *An Explicit Dictionary with Conjugation in the Mass Term*; the two forms are compared in *The One-Sided and the Two-Sided Equation*.

The article is organized as follows. First the gradient and the equation are stated, then the algebra and the two components of the pair, the value being read as a rule on elements and not as a space. The **value** is not the operator chirality of *Operator Chirality on the Biquaternion Algebra*: that label is a side of an operator and needs neither an element nor a frame, while the value is read from an element and one declared direction. The solutions of the equation and its relation to the Maxwell equation each have their own article, *Explicit Solutions of the Biquaternionic Dirac Equation* and *The Dirac–Maxwell Correspondence in Biquaternionic Form*, and neither is repeated here. The two-sided form, the potentials and the algebra discussion follow, and a closing section states which constructions the literature carries beside a Dirac equation and which of them the equation does not need. *The Legacy Pauli Gamma Formulation* prints the older display for the reader who has to compare with it.

The conventions are those of the companion articles: the algebra and its units are those of *Algebra and Element Conventions*, the coordinates, the metric and the frame those of *Frame and Metric Conventions*, and the units and the two writings of the temporal slot those of *Physics Units and Common Elements Conventions*. No formula of theirs is repeated here. Two points are this article's own. The symbol $c$ is the speed of light **in the medium** and $c_0$ the vacuum speed, so that $c=c_0$ only in vacuum and a result quoted with $c$ is a result in the medium. A squared three-vector such as $\vec v^2$ or $\vec p^2$ is the Euclidean square, not the quaternion square, which is its negative; the symbol $v$ is kept for particle and frame velocities.

## The Gradient and the Equation

### The Units and the Gradient

The units are the coefficient basis of *Algebra and Element Conventions* and the gradient is the operator of *Operator and Calculus Conventions*, §*The Gradient*, written $\tilde\nabla_\Phi$, with the quaternion conjugate $(\tilde\nabla_\Phi)^{\natural}$ and the central scalar $\Box$ of the same file. This article repeats none of the three and derives nothing about them. What it uses is one consequence: the product of the operator and its conjugate is second order and scalar, so the equation below is first order in the field and second order in the wave, and no matrix square is needed anywhere in it.

### The Equation in the Algebra

The dynamics of this article is the **chiral pair**

$$
\boxed{\;
\begin{aligned}
\tilde\nabla_\Phi\tilde\Xi_{R} &= k_m\,\tilde\Xi_{L},\\[4pt]
(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_{L} &= k_m\,\tilde\Xi_{R},
\end{aligned}
\;}
$$

for a field of mass $m$. The gradient differentiates with respect to the coordinates $R_\mu$ and carries the unit of an inverse length, so the term it is equated to carries that unit as well: $m$ alone carries a mass, and $k_m$ carries the inverse length. The length $1/k_m=\hbar/(m\,c)$ is the Compton length of the mass. The parameter $\alpha$ of the harmonic amplitude equation is an inverse length in both entries, and it writes them as $k_{t}^{\prime}$ and $k_m$. Here $k_{t}^{\prime}=E/(\hbar\,c)$ is the energy length.

The field is one element $\tilde\Xi=\tilde\Xi_{L}+\tilde\Xi_{R}$ of $\mathbb{B}$, and its two parts are the two components that the subscript names. Each line applies the gradient to one component and equates the result to a multiple of the other: the gradient is off-diagonal in the pair, and $k_m$ is the coefficient that relates the two. The mass multiplies on the left and is central, so it keeps the value: it relates the two components without moving anything across.

At $m=0$, that is $k_m=0$, the pair decouples into two one-sided equations, one for each letter of the pair:

$$
\tilde\nabla_\Phi\tilde\Xi_{R} = 0,
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_{L} = 0 .
$$

A field with a single value obeys one of them. The member written $R$, $\tilde\nabla_\Phi\tilde\Xi_{R}=0$, is the one written $\tilde\nabla_\Phi\tilde\Xi=0$ in the massless sections below, and the member written $L$ is its quaternion conjugate. Each member is first order, both are linear in the field, and the mass couples the two parts. Applying $(\tilde\nabla_\Phi)^{\natural}$ to the first member and using the second gives

$$
(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi\tilde\Xi_{R} = \Box_\Phi\tilde\Xi_{R} = k_m\,(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_{L} = \tilde\Xi_{R}\,k_m^{2},
\qquad\text{that is}\qquad
\left(\Box_\Phi - k_m^{2}\right)\tilde\Xi_{R} = 0
$$

the Klein–Gordon operator in this normalization. The same holds for $\tilde\Xi_{L}$. So each part obeys the Klein–Gordon equation. The factorization is the one the algebra supplies; no matrix square is used and no second metric enters.

### The Subscript and the Two Parts

The subscript that names the part, and the two letters $L$ and $R$, are fixed in *Matrix Representations Conventions*, §*The Legacy Pauli Gamma Formulation*; the side that reads it is *Operator Chirality on the Biquaternion Algebra*, §*What Operator Chirality Is Not*. The field of this article is one element that carries both parts, and nothing is introduced to hold them.

A single element of $\mathbb{B}$ carries four complex numbers, which is the count the four-component column of the matrix formulation carries. The difference is not the count but the object: there the four numbers are entries of a column that a matrix multiplies, and here they are the coefficients of one element that the algebra multiplies. No index, no column and no basis enters the statement.

### Chirality

**The notion is a side, and one basis operator realises it.** The derivative of this article multiplies the field on the left; a right multiplier supplies the other side, and the basis operator $-iR_{\vec e_z}$ is one such operator. That basis operator is an example of the right slot and not the definition of the label (*Operator Chirality on the Biquaternion Algebra*, §*What Operator Chirality Is Not*). The basis operator is named here and not computed, and its arrays are printed in *The Legacy Pauli Gamma Formulation*, where the older display is compared. No other object is introduced to say which part is which.

**The rules of the value.** A product takes the value of its right factor, and left multiplication keeps it. The derivative therefore carries each part into a part of the same value, and nothing that multiplies on the left acts on the value at all.

**The physical interpretation, and the frame it needs.** The two parts are the two components of the fermion field, and at $m=0$ each carries one helicity in the frame whose third direction is the momentum's. The coincidence of value with helicity is derived here and not assumed, because the value test uses the frame's $\vec e_z$ while helicity uses the direction of $\vec k_\Phi$, and the two agree only when those directions agree.

**The derivation is two lines.** At $m=0$ the pair decouples, and a plane wave of the $R$ member satisfies $\tilde\nabla_\Phi\tilde\Xi_R=i\tilde K_\Phi\tilde\Xi_R=0$. On the light cone with $\vec k_\Phi\parallel\vec e_z$ and $k'_t>0$ the wave vector is proportional to a frame idempotent,

$$
\tilde K_\Phi=ik'_t\,e_t+k'_t\,\vec e_z=2ik'_t\,\tilde\Pi_-,
\qquad
\tilde\Pi_-=\tfrac12\bigl(e_t-i\vec e_z\bigr),
$$

so the wave equation is $\tilde\Pi_-\tilde\Xi_R=0$. The annihilator of left multiplication by $\tilde\Pi_-$ is the right ideal $\mathbb{B}\tilde\Pi_+$, and right multiplication by $\tilde\Pi_+$ returns the part of value $L$, $\tilde X\tilde\Pi_+=\tilde X_L$. The kernel of the massless member written $R$ is therefore the value-$L$ subspace. The same computation for the other member, whose symbol on the light cone is $\tilde K_\Phi^{\natural}=k'_t-i\vec k_\Phi\cdot\vec e=2k'_t\tilde\Pi_+$, gives $\tilde\Pi_+\tilde\Xi_L=0$, hence the right ideal $\mathbb{B}\tilde\Pi_-$ and the value-$R$ subspace.

**The two vocabularies are opposite in this frame, and that is the point.** In the aligned frame the two parts are exactly the two eigenspaces of the value test — that is the whole content of "each carries one helicity" — and the letter of the pair is the other value: the member written $R$ carries value $L$. The letters of the pair name components and were fixed before any frame was chosen; the values are read in a frame. The coincidence is a division of the field into two helicity states and not an identification of the two names.

**What the coincidence does not say.** A superposition carries modes of different momenta, so no single $\vec e_z$ is aligned with all of them and the two parts of a general massless field have no definite value. The identification is a statement about one plane wave in one frame. It is used in that form in §*The Harmonic Field: Two Projections, and the Helicity Reading* below and in *Explicit Solutions of the Biquaternionic Dirac Equation*; in any other frame the value and the helicity are two readings of the one field, and neither defines the other.

**A limit, stated once.** Left multiplication cannot tell the two components apart. A left multiplier keeps every value, so it acts on the two components in the same way, and the two components are two copies of one object. The inequivalence of a left-handed field and its conjugate is a fact about a larger object and not about this algebra, and nothing in this article asserts it.

**The letters of the pair, and the values the basis operator returns.** The two subscripts of the chiral pair name two components. They are not the two values that the basis operator returns, and the difference is not cosmetic. The basis operator multiplies on the right and the gradient on the left, and a left multiplier and a right multiplier commute, $\tilde a(\tilde X\tilde b)=(\tilde a\tilde X)\tilde b$ by associativity, so left multiplication keeps the value: $\tilde\nabla_\Phi\tilde X$ carries the value of $\tilde X$ for every element $\tilde X$. A pair whose two lines equated a value-$L$ part with a value-$R$ part would therefore have only the zero solution. What the pair does is relate two components by a coefficient, and the coefficient is central.

### The Value Is a Rule

**The reading.** The value of an element is fixed by one multiplication, applied to the element itself:
$$
\tilde X\vec e_z=-i\tilde X\ \Longrightarrow\ \tilde X\text{ carries the value }L,
\qquad
\tilde X\vec e_z=+i\tilde X\ \Longrightarrow\ \tilde X\text{ carries the value }R .
$$
The test is made on the coefficients of the element and returns a letter. Two values, and an element that is neither is the sum of one part of each. Nothing is chosen in order to make the test: the frame supplies $\vec e_z$, and the element supplies the answer.

**The calculus.** Three rules follow from that line, and they are the whole of the arithmetic the equation needs. A product takes the value of its right factor, since $(\tilde X\tilde Y)\vec e_z=\tilde X(\tilde Y\vec e_z)$. Left multiplication keeps the value, because it acts before the test is applied. Right multiplication keeps the value for $e_t$, for $\vec e_z$ and for a central scalar, reverses it for $\vec e_x$ and for $\vec e_y$, and returns no value at all for a general element, in which the keeping and the reversing parts arrive together. Each case is one line of multiplication of units, and none of them expands the element.

**The equation read with them.** The gradient is an element and multiplies on the left, so it keeps the value of whatever it meets; a central scalar is a left multiplier as well and keeps the value too; no term of the chiral pair of §*The Biquaternionic Dirac Equation* moves a value across. The pair's two letters therefore name two components and not two values: two components of definite value, one of each, would satisfy both lines only by vanishing. What the pair does is exchange its components, each line applying the gradient to one and equating the result to a multiple of the other, and $k_m$ is the coefficient of that exchange. Two operations do reverse a value, and only two. The first is a right multiplication by an element of the plane of $\vec e_x$ and $\vec e_y$, which reverses the value. The second is the coefficient conjugation, which reverses it because it sends the central $i$ to $-i$ and leaves the units alone. The dictionary of §*An Explicit Dictionary with Conjugation in the Mass Term* uses both at once, the conjugation for the reversal and the right multiplication by $\vec e_z$ to carry a direction. No left multiplication and no central scalar can cross, so in the pair of the Introduction the mass is the coefficient that relates the two components and not a crossing operation; where a letter is carried across, the term that does it is the two-sided mass term, with its bar and its right multiplier.

**What the reading does not use.** No column, no basis, no frame beyond the one already declared, no ideal, no idempotent, no projector and no state space. The field is the element that is tested, the value is the letter returned, and the three rules are read from the multiplication of the algebra.

## The Algebra and the Gradient

### The Gradient Is an Element

The gradient is an element of $\mathbb{B}$, and an element acts on the algebra by multiplication. Nothing about that action needs a basis: the equation says what the gradient does to the field, and the answer is another element. A basis enters only when numbers are wanted, and then the choice of basis is a coordinate choice that changes nothing in the operator — two bases give two lists of numbers for one action. The equation of this article is written in neither.

The place where a basis does make a difference is the diagonal. An operator is diagonal in a basis when each basis element is carried into a multiple of itself. Of the sixteen basis operators $L_{e_\mu}R_{e_\nu}$ of the coefficient basis exactly four are diagonal, the four with $\mu=\nu$. The three spatial basis operators $L_{e_\eta}R_{e_\eta}$ send each basis element to a multiple of itself, $e_\nu\mapsto\pm e_\nu$, with the sign $-1$ where $e_\nu$ commutes with $e_\eta$ and $+1$ where it anticommutes; that is the eigenvalue $-1$ on $e_t$ and on the basis operator's own unit, and $+1$ on the other two. The fourth, $L_{e_t}R_{e_t}$, is the identity. No other basis operator carries all four basis elements into multiples of themselves. The set is $\{L_{e_\eta}R_{e_\eta}\}$, so a permutation of the three spatial units permutes the last three members of the set and leaves the set unchanged.

The set therefore names no direction. An axis is not a property of the algebra; it is a property of the frame that is declared, and the frame and its metric are fixed in *Frame and Metric Conventions*. This article states the point once, here, and does not use it again: the equation names no unit and no axis, and the five basis operators printed in *The Legacy Pauli Gamma Formulation* are printed there for comparison with the older display.

### An Explicit Dictionary with Conjugation in the Mass Term

The route used so far is the algebra's own: one element, two values, the mass between them. There is a second route, due to V. V. Kravchenko (1995), which is a **change of variable** rather than a decomposition. It writes the whole Dirac equation as a single equation on $\mathbb{B}$ in which the derivatives act from the left and the mass from the right, and its interest for this article is that its mass term carries complex conjugation.

**The equation.** In the source's normalization the spatial derivative is the element

$$
\vec\nabla := \sum_{\eta=x,y,z}\vec e_\eta\,\frac{\partial}{\partial R_\eta},
\qquad
\vec\nabla^2 = -\Delta ,
\qquad
\lvert\vec\nabla\rvert^2 = \Delta ,
$$

the spatial gradient of *Operator and Calculus Conventions*, §*The Gradient*, which is the vector part of $\tilde\nabla_\Phi$ and is therefore pure and arrowed, with real quaternion coefficients on the material sector. The equation is

$$
\mathcal{N}F := \Bigl(i\frac{\partial}{\partial r'_t} + \vec\nabla\Bigr)F - i\,\overline{F}\,\vec e_z\,k_m = 0,
$$

where $\overline{\cdot}$ is the coefficient conjugation of *Algebra and Element Conventions*, the corpus's glyph for the map the source writes $C$, applied to the coefficients of the field, and the unit $\vec e_z$ multiplies the result from the right. The corpus's spatial operator of *Biquaternion Regular Functions* is $D=i\vec\nabla$, with $D^2=\Delta$; the two differ by the fixed central imaginary, and this section keeps $\vec\nabla$, because that is the normalization in which the mass term of the equation above is real. A reader who changes normalization in the middle of a computation changes the operator.

**Three kinds of action in one operator.** The display mixes a left action, an antilinear map and a right action, and the mixture is the dictionary's content rather than a slip of notation. The time derivative and $\vec\nabla$ act from the left; the bar acts on the coefficients, has no side, and is the antilinear entry; the multiplication by $\vec e_z$ acts from the right. How such a combination is printed is fixed by the conventions (*Product and Form Conventions*, both copies): the side is carried by position and never by a mark. The mass term is therefore $\overline{F}\,\vec e_z$ and not a product of two operator letters: the bar is applied to the field and the unit multiplies what comes out. Because $\vec e_z$ has real coefficients, the bar commutes with that multiplication, $\overline{F\vec e_z}=\overline{F}\,\vec e_z$, so the source's order and the corpus's are one operator.

**Why the $1/c$.** The operator adds an inverse time to an inverse length, and only $i\partial/\partial r'_t$ is an inverse length like $\vec\nabla$, and the mass term carries that same unit by the identification made at the box. The source prints the equation at $c=1$, where the first factor is $i\partial/\partial r'_t$.

**One sector, two coordinates.** The operator is read on the material sector $\mathbb{B}_{\Phi}$, where $Q_t=i q'_t$ and $Q_\eta=q_\eta$. There $R_t=i r'_t$ is the complex time coordinate, so $\partial/\partial r'_t$ differentiates with respect to the physical time and $\partial/\partial R_\eta$ is the physical spatial derivative: the two symbols name the two coordinates of one sector and do not mix two conventions. Since $\partial/\partial R_t=-i\partial/\partial r'_t$,

$$
i\frac{\partial}{\partial r'_t} = -\frac{\partial}{\partial R_t},
\qquad\text{so that}\qquad
i\frac{\partial}{\partial r'_t} + \vec\nabla = -(\tilde\nabla_\Phi)^{\natural},
$$

the time term of the gradient carrying $e_t$, the identity of the algebra, so that the three symbols are one operator.

The free part of $\mathcal{N}$ is therefore the **conjugate** gradient and not the gradient: the free equation is the member written $L$, $(\tilde\nabla_\Phi)^{\natural}F=0$, written on the whole algebra, and the other member is its conjugate. With the mass term moved to the right the equation reads

$$
(\tilde\nabla_\Phi)^{\natural}F = -i\,\overline{F}\,\vec e_z\,k_m,
$$

which has the shape of the corpus's $(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_{L}=k_m\,\tilde\Xi_{R}$ with the second field read as $-i\,\overline{F}\,\vec e_z$: a conjugation and a fixed direction, and nothing else. That is the operator-theoretic content of the two-sidedness — the dictionary reaches the member written $L$, and the second field of that member is the conjugate of the first. The normalization with the imaginary-time derivative is not used for the operator itself, and the reason is the reality of the operator $R$ below: the factor $-i$ that carries $\partial/\partial r'_t$ into $\partial/\partial R_t$ would put the central imaginary into every coefficient of $R$ and take away the property that makes $R$ real.

Following the source, $i_1,i_2,i_3$ denote the quaternion units; this article writes them $\vec e_x,\vec e_y,\vec e_z$ and keeps the source's $i_k$ only where it quotes the source. The product $i\,i_k$ is the scalar imaginary times a quaternion unit, not a square: $i^2=-1$, while $(i\,i_k)^2=i^2i_k^2=+1$.

**Which conjugation.** The bar of the equation is the algebra's **coefficient conjugation** $\bar{\cdot}$, not the algebra's real structure $\flat$. They are different maps with different fixed spaces, and the corpus keeps them apart (*Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*, and the convention remark of *The Massive Case* above). The distinction has teeth here, because the dictionary's mass term is antilinear and the framework has already found that not every antilinear mass term is admissible. The retired single-field equation $\tilde\nabla_\Phi\tilde\Xi = k_m\,\tilde\Xi^{\flat}$ fails on the dispersion, whereas the Lanczos form $\tilde\nabla_\Phi D = D^{*}i\vec{\nu}\,k_m$ of *The Lanczos Route: Maxwell with Feedback* is exact. Kravchenko's mass term is of the second kind: its conjugation is $\bar{\cdot}$, and it is accompanied by a right multiplication by a spatial direction, its $\vec e_z$ standing where the Lanczos unit vector $\vec{\nu}$ stands.
 The corpus reads the two as one structure — a conjugation together with a direction, rather than the algebra's real structure — and the dictionary is the second explicit instance of it.

**The price, and its refund.** Because the bar is antilinear, $\mathcal{N}$ is not left multiplication by an element of the algebra, so the Cauchy kernel, the Teodorescu transform and the boundary-value theory do not apply to it as it stands. The conjugation is removed by factoring $\mathcal{N}$ into two complex-linear equations and changing variable; the time-harmonic amplitude then obeys a **shifted** equation with a biquaternionic parameter, $\vec\nabla f+f\alpha=0$ at a constant $\alpha$ — the corpus's $D_\alpha=D+M_\alpha$ of *Biquaternion Regular Functions*, written with $D=i\vec\nabla$ and read as the action $f\mapsto Df+f\alpha$ — used in *Confinement and the Loss of Partonic Information in Biquaternionic Form*. The conjugation is thus the cost of shrinking the equation to a single biquaternion, and it is refunded whenever the boundary-value theory is what is wanted.

### The Conjugation-Free Operator and Its Reality

The same source takes the conjugation off the operator and puts it into the change of variable. With the two complementary projections built from the first spatial unit,

$$
e_{+} := \tfrac12\bigl(e_t + i\,\vec e_x\bigr),
\qquad
e_{-} := \tfrac12\bigl(e_t - i\,\vec e_x\bigr),
\qquad
e_{+}+e_{-}=e_t,
\qquad
e_{+}e_{-}=0 ,
$$

the operator

$$
R[F] := \Bigl(i\partial/\partial r'_t + \vec\nabla\Bigr)F\;e_{+} + \Bigl(-i\partial/\partial r'_t + \vec\nabla\Bigr)F\;e_{-} - F\,\vec e_y\,k_m
$$

is related to $\mathcal{N}$ by a change of variable on each side. The conjugation has not been removed, only moved: it sits in the two factors that surround the operator, and the operator itself is free of it.

**The reality of $R$, recomputed.** The two projections collapse, because $e_{+}+e_{-}=e_t$ and $e_{+}-e_{-}=i\,\vec e_x$. Writing $A=i\,\partial F/\partial r'_t$ and $B=\vec\nabla F$, the first two terms give

$$
(A+B)e_{+} + (-A+B)e_{-} = B\,(e_{+}+e_{-}) + A\,(e_{+}-e_{-}) = B + A\,i\vec e_x ,
$$

and the step $i\cdot i=-1$ turns the second into the right multiplication by $-\vec e_x$. The operator is therefore

$$
R[F] = \vec\nabla F - \frac{\partial F}{\partial r'_t}\,\vec e_x - F\,\vec e_y\,k_m ,
$$

and its coefficients are the three spatial units of $\vec\nabla$ and the two right multiplications by $\vec e_x$ and $\vec e_y$. All of them are real quaternions, and no central imaginary appears. That is the property the source names when it calls the quaternionic Dirac operator **real**.

**Real and imaginary parts are separately solutions.** Since no coefficient of $R$ carries the central imaginary, the bar passes through it,

$$
R\bigl[\overline{F}\bigr] = \overline{R[F]} ,
$$

the bar being coefficientwise. Writing $F = \mathrm{Re}\,F + i\,\mathrm{Im}\,F$ and using that commutation, a solution of $R[F] = 0$ splits into two solutions:

$$
R\bigl[\mathrm{Re}\,F\bigr] = 0, \qquad R\bigl[\mathrm{Im}\,F\bigr] = 0 .
$$

One quaternionic solution therefore carries two Dirac solutions. This doubling is the source's stated purpose: the real operator is offered as a contribution to a *real* Dirac theory, and it is obtained without a conjugation operator in the operator, in the real quaternion algebra rather than in the complexified one.

**The current, and the modulus.** For a real $F$ the quaternionic conjugate of the equation is the equation of the conjugate field, and from the pair the source derives the conservation law

$$
\partial/\partial r'_t|F|^2 = -\hbar\bigl[(\vec\nabla F^{\natural})F + \bar{F}\,(\vec\nabla F)\bigr],
\qquad |F|^2 := \langle  F\rangle_{*}  = \sum_{\mu=0}^{3}|F_\mu|^2,
$$

printed there in its own normalization, with $\hbar$ restored, and with the source's $\dagger$ read as the quaternionic conjugate $\natural$ and its $*$ as the coefficient bar. The equation of this section carries no $\hbar$, and the same pair gives the law in the units of this section,

$$
\frac{\partial}{\partial r'_t}\bigl(FF^{\natural}\bigr)
= F\,\vec e_x\,(\vec\nabla F)^{\natural} - (\vec\nabla F)\,\vec e_x\,F^{\natural},
$$

which is the quaternionic form of the current-conservation equation of the Dirac field: the time derivative of the density on the left, and on the right the two terms that carry the spatial derivative, with the direction $\vec e_x$ of the operator in the place the source's $M_{i_1}$ occupies. Writing $A=F\,\vec e_x\,(\vec\nabla F)^{\natural}$, the second term is $A^{\natural}$, so the right side is $A+A^{\natural}$ and is scalar. The mass cancels between the two terms: the operator gives the time derivative the mass part $-k_mF\vec e_z$, and $\vec e_z^{\natural}=-\vec e_z$ transmits it to $-k_mF\vec e_zF^{\natural}+k_mF\vec e_zF^{\natural}=0$. The law is therefore the same at $m=0$, and it was checked at residual $1.1\times10^{-15}$ over $100$ random real fields and again symbolically on a polynomial field. The density is the modulus $FF^{\natural}$. On the real representative it coincides with the Hermitian norm, $FF^{\natural}=\langle F\rangle_{*}=\sum_\mu F_\mu^2$, and that shared value is indefinite: what the pair conserves is a density, not a probability density. The definite Hermitian norm carries the probability reading only on the complex field, where the two norms differ.

### The One-Sided and the Two-Sided Equation

The article now carries two equations, and they must not be read as one. The corpus's own equation is **one-sided**: it is the chiral pair in which the gradient acts by left multiplication and the mass is the central coefficient that relates the two components. Kravchenko's equation is **two-sided**: it is a single equation on $\mathbb{B}$ in which the derivative acts from the left, the mass term acts from the right through $\vec e_z$, and the coefficient conjugation supplies the antilinear part. The two are related by a change of variable, but they are not the same operator, and the table separates them.

| | One-sided equation | Two-sided equation |
|---|---|---|
| the equation | $\tilde\nabla_\Phi\tilde\Xi_{R}=k_m\,\tilde\Xi_{L}$, $(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_{L}=k_m\,\tilde\Xi_{R}$ | $\bigl(i\partial/\partial r'_t+\vec\nabla\bigr)F-i\,\overline{F}\,\vec e_z\,k_m=0$, that is $-(\tilde\nabla_\Phi)^{\natural}F-i\,\overline{F}\,\vec e_z\,k_m=0$ |
| the action | left, by $\tilde\nabla_\Phi$ and $(\tilde\nabla_\Phi)^{\natural}$ | left by the derivative, right by $\vec e_z$ in the mass term, and the coefficient bar |
| the field | one element $\tilde\Xi=\tilde\Xi_{L}+\tilde\Xi_{R}$ of $\mathbb{B}$ | one element $F$ of $\mathbb{B}$ |
| the mass | the coefficient relating the two parts; central, so it keeps the value | $-i\,\overline{F}\,\vec e_z\,k_m$: a conjugation together with a direction |
| the subscript | two components, $L$ and $R$ | no subscript, the direction $\vec e_z$ standing in its place |
| the use | the corpus's formulation and its kinematics | the dictionary, the Cauchy theory and the integral representation |

The dictionary is therefore not a second definition of the same equation. It is a change of variable that makes the equation two-sided, and the price of the change is the conjugation in the mass term. The one-sided pair is the definition; the two-sided equation is the form in which the analytic machinery acts.

The comparison has an algebraic reading. The two operators of the one-sided pair are the gradient and its quaternion conjugate, both pure left multipliers, so their operator chirality is the left slot. The mass coefficient multiplies on the left as well; it is central, so its own label is *both slots*, and the pair is written with no right multiplier anywhere. The two-sided operator is different in kind: its derivative is a left multiplier and its mass term is a right multiplier, so one end of the multiplication carries the derivative and the other end carries the mass. That sum is not labelled *both slots*: the label of *Operator Chirality on the Biquaternion Algebra* reserves that case for the central scalars, and a sum of two one-sided multipliers with non-central parameters is *no single side*. The coefficient conjugation makes the map not complex-linear, so the label, which classifies operators of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, does not apply to the two-sided equation as it stands. The two-sidedness of the name is the use of the two ends, one for the derivative and one for the mass, and it is what the one-sided pair does not do. What the comparison adds is that the two forms differ in the ends their terms use, and that this is a property of the operator and not of the field.

### The Harmonic Field: Two Projections, and the Helicity Reading

The same source carries the dictionary one step further, to the field that oscillates in time, and that is where the algebra is read physically. For a time-harmonic field of frequency $\omega\in\mathbb{R}$ the general solution is a **sum of two exponentials with opposite signs**,

$$
F = \tfrac12\,f\,\bigl(e_t+\alpha/\sqrt{\alpha^2}\bigr)\exp(i\theta_{\mathrm{pwt}}) + \tfrac12\,f\,\bigl(e_t-\alpha/\sqrt{\alpha^2}\bigr)\exp(-i\theta_{\mathrm{pwt}}),
$$

Throughout, $\theta_{\mathrm{pwt}}:=\omega r'_t/c$ is the plane-wave time angle: $\omega$ is real for a monochromatic wave, so the factor $\exp(-i\theta_{\mathrm{pwt}})$ is a phase of modulus one and it is the time part of the plane-wave angle of the full wave form.

where the two factors $\tfrac12(e_t\pm\alpha/\sqrt{\alpha^2})$ are complementary projections built from the unit in the direction of the parameter, and they multiply the field on the right; and $f$ is a solution of the shifted amplitude equation $\vec\nabla f+f\alpha=0$. The pair of signs of the frequency and the pair of right multiplications are one pairing: each half of the field is a projected shifted equation.

**The interpretation the source attaches to it.** The source states that its two projections are *closely related to particle helicity*, and on that interpretation the two halves of the harmonic field are the two helicity components, the half with the plus sign of the frequency being the **neutrino** and the other the **antineutrino**. In the massless case the equation they come from is

$$
i\,\partial F/\partial r'_t + \vec\nabla F = 0,
$$

which for a field equal to its own conjugate is a known reformulation of the vacuum Maxwell equations, attributed by the source to Imaeda's vacuum equation, whose entry is in the Further Reading of *The Dirac–Maxwell Correspondence in Biquaternionic Form*. The algebra thus supplies the two helicities in one object: the two complementary projections of the parameter, one for each sign of the frequency, with the parameter's direction in place of a vacuum direction.

**Which pair.** The two projections above are **not** the two values. The value is a property of the element, $L$ or $R$, and no parameter enters it; the two projections above are built from the parameter $\alpha$, so they carry the frequency and the mass of the field. The value is read from the frame's third direction and the projection from the parameter's, so the two agree only in the frame whose third direction is the parameter's; in the frame of this article the parameter lies along $\vec e_x$ at $m=0$ and in the plane of $\vec e_x$ and $\vec e_y$ at $m\neq0$. The value basis operator exchanges the two projections, $-i\,(P_\pm\tilde X)\vec e_z=P_\mp(-i\tilde X\vec e_z)$, so in this frame no element carries a projection and a value at once. What the mass changes is not that agreement but the existence of the states: at $m=0$ the kernel of the wave biquaternion splits into one state of each value, and at $m\neq0$ the mass couples the two components, so a plane wave of definite value is the zero wave. The neutrino or antineutrino identification is a statement about the helicity pair and not about the values. The corpus records the identification as the source's interpretation rather than as a derivation: what the algebra contributes to it is the shape — two complementary projections, one for each sign of the frequency — and the name *neutrino* is the source's, not the algebra's.

### The Integral Representation of the Harmonic Field

Removing the conjugation is what buys the analytic theory back, and for the harmonic field the source's announcement states what is bought. The time-harmonic amplitude obeys the first-order equation

$$
\vec\nabla f + f\alpha = 0,\qquad \alpha=-i\omega\,\vec e_x ,
$$

which is the shifted equation in the source's normalization, the frequency entering as the inverse length $\omega/c$. The parameter is an inverse length, as $\vec\nabla$ is, so the frequency enters it as $\omega/c$: the general-units form of this $\alpha$ is $-i\frac{\omega}{c}\vec e_x$, the inverse length that *The Dirac–Maxwell Correspondence in Biquaternionic Form*, §*The Mass Shell as the Condition on the Dirac–Maxwell Correspondence* prints as $k_{t}^{\prime}$. The corpus's *Biquaternion Regular Functions* writes it with $D=i\vec\nabla$, where the same equation reads $Df+f(i\alpha)=0$. The source writes the same amplitude equation in its matrix form, with an operator it calls $D_\omega$; that operator and $\vec\nabla+\cdot\,\alpha$ carry the same kernel, so the analysis is the same. The source derives its results in this massless case — the case it calls the neutrino — while the massive parameter $\alpha = -\bigl(i(\omega/c) \vec e_x + k_m \vec e_y\bigr)$, the same inverse length, is the one carried by the boundary-value treatment of the bag in *Confinement and the Loss of Partonic Information in Biquaternionic Form*.

With that one remark the three theorems of the hyperholomorphic theory hold for the harmonic field in the same shape as for the electromagnetic field of the companion *The Time-Harmonic Maxwell Operator and the Quaternionic Cauchy Integral*: a **Cauchy integral formula**, with the Cauchy-type operator $\mathcal{C}_{\mathrm{cau},\omega}$ of the amplitude equation acting as the identity on a field of the kernel that is continuous up to the boundary; the **Plemelj–Sokhotski formulas**, which express the one-sided boundary limits of $\mathcal{C}_{\mathrm{cau},\omega} f$ for Hölder data through the principal-value integral; and a **boundary-value criterion**, that a Hölder function on the boundary is the boundary value of a solution of the amplitude equation if and only if it is its own $\mathcal{C}_{\mathrm{cau},\omega}$ image. This is the refund of the price recorded in *An Explicit Dictionary with Conjugation in the Mass Term*: the conjugation obstructs the Cauchy kernel on the two-sided image, and changing the variable back hands the kernel over. It is also the whole content of the second half of the source's title, and it is the Dirac half of the source's thesis — the same parametric equation, at one value of its parameter, is the time-harmonic Maxwell system and, at another, the time-harmonic Dirac system, so that one Cauchy theory serves both. The Dirac case is an instance of the general boundary-value criterion $P_\alpha f = f$ of *Biquaternion Regular Functions*; what the physics register adds to the general statement is the identification of the parameter and the fields.

## Relativistic Kinematics in Biquaternionic Form

Before the solutions are written, it is useful to collect the basic relativistic kinematic quantities in biquaternion form. These are the objects that appear in the Dirac equation and its solutions, and they are established physics rewritten in biquaternion notation.

### The Four-Position

The **four-position biquaternion** is

$$
\tilde R_\Phi = i r'_t\, e_t + r_x\, \vec e_x + r_y\, \vec e_y + r_z\, \vec e_z,
$$

with $Q_t=i q'_t$. The scalar part is the complex time coordinate, and the vector part is the ordinary spatial position.

### The Invariant Interval

The invariant interval is the square of the biquaternion displacement:

$$
ds^2 = \langle d\tilde R_\Phi\rangle_{\natural} = d\tilde R_\Phi\,d\tilde{R}_\Phi^{\natural} = (i\,dr'_t)^2 + dr_x^2 + dr_y^2 + dr_z^2 = -d{r'_{t}}^2 +dr_x^2+dr_y^2+dr_z^2.
$$

This is the biquaternion form of the Minkowski interval. The Lorentzian signature emerges algebraically from $i^2 = -1$, as discussed in the companion article on the $i r'_t$ convention.

### The Four-Velocity

The **four-velocity biquaternion** is

$$
\tilde{V}_{\Phi} = \gamma(ic\, e_t + \vec v),
$$

where $\vec v$ is the ordinary three-velocity of the particle and

$$
\gamma = \frac{1}{\sqrt{1 - \vec v^2/c^2}}
$$

is the Lorentz factor. The four-velocity satisfies the **normalization condition**

$$
\tilde{V}_{\Phi}\tilde{V}_{\Phi}^{\natural} = \gamma^2\big(-c^2 + \vec v^2\big) = -c^2.
$$

This is the biquaternion form of the standard relativistic normalization $\sum_\mu\varepsilon_\mu v_\mu v_\mu = -c^2$.

### The Four-Momentum

The **four-momentum biquaternion** is

$$
\tilde{P}_{\Phi} =m\,\tilde{V}_{\Phi} =m\,c\,\gamma\left(i\,e_t + \frac{\vec v}{c}\right) = i\,\frac{E}{c}\, e_t + \vec p,
$$

which is $m\tilde{V}_{\Phi}$; here $E =m\,c^{2}\,\gamma$ is the relativistic energy and $\vec p =m\,\gamma\,\vec v$ is the relativistic three-momentum. The scalar part of $\tilde{P}_{\Phi}$ is $iE/c$, and the vector part is $\vec p$.

The four-momentum satisfies the **mass-shell relation**

$$
\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural} =m^{2}\,\tilde{V}_{\Phi}\,\tilde{V}_{\Phi}^{\natural} = -m^{2}\,c^{2}.
$$

This is the biquaternion form of the standard relativistic energy-momentum relation

$$
E^2 = \vec p^2 c^2 +m^{2}\,c^{4},
$$

which is obtained by expanding $-m^{2}\,c^{2}= -(E/c)^2 + \vec p^2$.

### The Four-Acceleration and Four-Force

The **four-acceleration biquaternion** is $\tilde{A}_{\Phi} = d\tilde{V}_{\Phi}/d\tau$, where $\tau$ is the proper time. The **four-force biquaternion** is $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = d\tilde{P}_{\Phi}/d\tau =m\,\tilde{A}_{\Phi}$. The four-acceleration satisfies $\tilde{A}_{\Phi}\tilde{V}_{\Phi}^{\natural} + \tilde{V}_{\Phi}\tilde{A}_{\Phi}^{\natural} = 0$, which is the biquaternion form of the orthogonality condition $\sum_\mu\varepsilon_\mu a_\mu v_\mu = 0$.

### Summary of Relativistic Kinematics

| Quantity | Biquaternion | Constraint |
|---|---|---|
| Four-position | $\tilde R_\Phi = i r'_t\, e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ | — |
| Interval | $ds^2 = \langle d\tilde R_\Phi\rangle_{\natural} = d\tilde R_\Phi\,d\tilde{R}_\Phi^{\natural}$ | $= -d{r'_{t}}^2 +dr_x^2+dr_y^2+dr_z^2$ |
| Four-velocity | $\tilde{V}_{\Phi} = \gamma(ic\, e_t + \vec v)$ | $\tilde{V}_{\Phi}\tilde{V}_{\Phi}^{\natural} = -c^2$ |
| Four-momentum | $\tilde{P}_{\Phi} =m\,\tilde{V}_{\Phi}$ | $\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural} = -m^{2}\,c^{2}$ |
| Four-force | $\tilde{\mathcal F}_{\Phi,\mathrm{frc}} = d\tilde{P}_{\Phi}/d\tau$ | — |

These kinematic relations are the biquaternion form of standard relativistic mechanics, and they are the natural setting for the biquaternionic Dirac equation.

## The Biquaternionic Dirac Equation

### Statement

The equation is the chiral pair of *The Equation in the Algebra*. Let $\tilde\Xi$ be a field with values in $\mathbb{B}$, written as a pair of parts $\tilde\Xi=\tilde\Xi_{L}+\tilde\Xi_{R}$, one for each letter of the pair. For a field of mass $m$ the **biquaternionic Dirac equation** is

$$
\boxed{\;
\begin{aligned}
\tilde\nabla_\Phi\tilde\Xi_{R} &= k_m\,\tilde\Xi_{L},\\[4pt]
(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_{L} &= k_m\,\tilde\Xi_{R}.
\end{aligned}
\;}
$$

It is **linear** in $\tilde\Xi$, **off-diagonal in the part** and **diagonal in the value**: each line applies a left multiplication to one part and equates the result to a multiple of the other, and a left multiplication keeps the value it meets, so the two sides of one line carry one value. The two letters of this display therefore name the two factors of the factorisation and not two values; where they are to name the values, the mass is the term that carries the field across, and §*The Massive Case* writes the pair in that form. At $m=0$ it decouples into two one-sided equations,

$$
\tilde\nabla_\Phi\tilde\Xi_{R}=0,
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_{L}=0,
$$

one for each letter of the pair; a field of a single value obeys one of them. The two lines equate parts of different letters because the gradient is off-diagonal in the pair: each line applies it to one part and equates the result to a multiple of the other, and $k_m$ is the coefficient of that relation. The mass multiplies on the left, so it keeps the value, and the two lines are equalities of elements, not of matrices. The Klein–Gordon consequence for each part is derived in *The Equation in the Algebra*.

A **single-string form** of the same pair is recorded in *The Chiral Algebra of Biquaternions and the Cyclic Representation of the Dirac Equation*. Writing the wave function in the light-cone coordinates and using that article's outer and inner products, the chiral pair becomes one expression, $F^- \odot \bar D + D \otimes F^+ = im\overset{\curvearrowleft}{F}$, in which the two products carry the two values and the cyclic conjugation $\overset{\curvearrowleft}{\phantom{x}}$ carries the mass term. The equivalence of that expression with the chiral pair is verified row by row there. The pair above remains the definitional home of the biquaternionic Dirac equation; the single-string form is a repackaging in a different product, not a different equation.

### The Massless Case

For a single value the massless equation is one-sided. The member written $R$, $\tilde\nabla_\Phi\tilde\Xi_{R}=0$, is identical in form to the **homogeneous biquaternion Maxwell equation** for the field-strength biquaternion $\tilde{F}$:

$$
\tilde\nabla_\Phi\tilde\Xi_{R} = 0 \quad \text{(the member written }R\text{)}, \qquad \tilde\nabla_\Phi\tilde{F} = 0 \quad \text{(source-free Maxwell)}.
$$

The member written $L$ is the quaternion conjugate, $(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_{L}=0$; it has the same form with $(\tilde\nabla_\Phi)^{\natural}$ in place of $\tilde\nabla_\Phi$. The full massless Dirac field is the pair of the two, not the single equation. The solutions are also the same in form: the kernel of the biquaternionic gradient consists of plane waves, spherical waves, and cylindrical waves (as in the companion article on Maxwell). The **physical interpretation** differs: $\tilde\Xi$ is a fermion field (spin-$\frac{1}{2}$), and $\tilde{F}$ is a boson field (spin-1).

The structural identity of the two equations is the algebraic content of the statement that both fields are read in the same algebra. The difference is not in the operator but in the object it acts on and in the value of the field: the Maxwell field-strength biquaternion lives in the vector part of the algebra, and the Dirac field is a general element carrying a letter of the pair.

### The Massive Case

The massive equation is the chiral pair boxed in *Statement*. The mass term is **linear** in the field and acts between the two parts: it is the biquaternion transcription of the mass term of the matrix Dirac equation, and it is what relates the two components.

The coupling does not come from the left. Left multiplication by any element preserves the value of the field: a product takes the letter of its right factor, and the left multiplier does not touch it (*Matrix Representations Conventions*, §*The Bridge to the $4\times4$ Displays*). So no left multiplication carries one value into the other. Read with its letters as the two values, the pair as printed has **no nonzero solution at all**: the first line would equate a value-$R$ element to a value-$L$ one, and the two halves meet only at zero. Read as a factorisation it is exact — in momentum space the second part is the first multiplied on the left, $\tilde\Xi_{L}=\frac{i}{k_m}\tilde{K}_{\Phi}\tilde\Xi_{R}$, and $(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi=\Box_\Phi$ carries the second-order equation — and in that reading the two letters name the two **factors** and not the two values, which is how the mathematical article that supplies the factorisation uses them (*The First Order Root of the Biquaternion d'Alembertian*). What does exchange the two values is a right multiplication by a unit $i\vec v$ with $\vec v$ perpendicular to the axis, or the coefficient conjugation, and the side on which it acts is the side of the **mass** and never of the derivative: a left multiplier keeps every value, so a derivative term can carry the field out of its part only by ceasing to be a multiplication by an element (*Operator Chirality on the Biquaternion Algebra*, §*What Operator Chirality Is Not*; *Spinors and Dirac Spinors in the Biquaternion Algebra*, §*What Carries One Part to the Other*). A right multiplication by a unit that commutes with the axis — the time unit or the axis unit itself — is a different object again: it acts inside one value, leaves the letter alone, and carries a direction. That is why the two-sided form of *An Explicit Dictionary with Conjugation in the Mass Term* needs the coefficient bar beside the direction, and neither of the two alone.

**The two letters, in the two readings.** Written with the exchange on the right, the pair reads
$$
\tilde\nabla_\Phi\tilde\Xi_{R}=k_m\,\tilde\Xi_{L}\,i\vec v,
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde\Xi_{L}=k_m\,\tilde\Xi_{R}\,i\vec v,
$$
with $\vec v$ a unit real vector perpendicular to the declared axis. Each line then lands inside one value on both sides, the mass carries the exchange, and the square is unchanged because $(i\vec v)^{2}=+1$: applying $(\tilde\nabla_\Phi)^{\natural}$ to the first line returns $\Box\tilde\Xi_{R}=k_m^{2}\tilde\Xi_{R}$. This is the display in which the letters name the two values, and it is the display the two mathematical articles describe; the pair boxed in §*Statement* is the same equation with the right factor left implicit, and a reader who takes its letters for values finds the two halves meeting at zero.

**A remark on the anti-Hermitian conjugation $\flat$.** The algebra carries, besides the quaternion conjugate and the Hermitian conjugation ${}^{*}$, a further antilinear involution:

$$
\tilde\Xi^{\flat} = -\tilde\Xi^* = -\overline{\tilde\Xi^{\natural}},
$$

the **anti-Hermitian conjugate** $\flat = -{}^{*}$. It is a $\mathbb{C}$-**antilinear** involution, and it is order-reversing with a twist,

$$
\left(\tilde{Q}_2\tilde{Q}_1\right)^\flat = -\,\tilde{Q}_1^\flat\tilde{Q}_2^\flat ,
$$

the sign being the only difference from an ordinary anti-automorphism, and it acts by a sign on the two Hermitian sectors,

$$
\tilde\Xi^{\flat} = +\tilde\Xi\ \ (\tilde\Xi\in\mathbb{B}_{\Phi}), \qquad \tilde\Xi^{\flat} = -\tilde\Xi\ \ (\tilde\Xi\in\mathbb{B}_{\Psi}),
$$

so that the **fixed space of $\flat$ is the anti-Hermitian sector $\mathbb{B}_{\Phi}$**.

The convention is worth a remark, because the more familiar one takes the *Hermitian* part as the real one, and here the *anti*-Hermitian part plays that role. The two differ only by the central factor $i$: anti-Hermitian elements are $i$ times Hermitian ones, and anti-Hermitian generators are the standard choice for the Lie algebra of a $*$-unitary group (in the companion quantum article the Lie algebra of the $*$-unitary group is $\mathbb{B}_{\Phi}$). What is unusual here is not the sign convention as such, but that it is applied to the *field* rather than to the generators: it is $\mathbb{B}_{\Phi}$ that is fixed, and that is what makes $\mathbb{B}_{\Phi}$ the framework's "material" sector (the companion article *The Material Sector: Four-Vectors, Interval and Lorentz Action* takes $\mathbb{B}_{\Phi}$ as the fixed space of $\flat$).

The map $\flat$ is the algebra's **real structure**, and its shape is that of a charge-conjugation (Majorana) pairing: it relates the field to its own conjugate. It is *not* the mass term. A coupling built on $\flat$ pairs $\tilde\Xi$ with $\tilde\Xi^{\flat}$ rather than relating two independent chiralities, and because $\flat$ is antilinear such a coupling is not invariant under the continuous central phase — precisely the two differences between a Majorana-type pairing and an ordinary Dirac mass. The single-field equation $\tilde\nabla_\Phi\tilde\Xi = k_m\,\tilde\Xi^{\flat}$ is a real-linear equation of that type; it is a different equation from the one studied here, and its central-phase plane waves sit on the *spacelike* locus, not on the physical mass shell. The map $\flat$ is retained in the framework for what it is genuinely for — conjugation, the $\mathbb{B}_{\Psi}/\mathbb{B}_{\Phi}$ split, the trace and bilinear pairings, and the real-form question of Dirac versus Majorana fermions, which the companion articles on chirality, the neutrino, and the CPT theorem develop. In the present article $\flat$ is used only for conjugation, never as the mass.

**The associated Klein–Gordon equation.** Applying $(\tilde\nabla_\Phi)^{\natural}$ to the first member of the pair and substituting the second gives $\Box\tilde\Xi_{R}=\tilde\Xi_{R}\,k_m^{2}$, and likewise for $\tilde\Xi_{L}$. With $\hbar$ and $c$ restored, each chiral component satisfies

$$
\left(\Box - k_m^{2}\right)\tilde\Xi_{L,R} = 0 ,
$$

in agreement with the companion article on the Klein–Gordon equation. This is the biquaternion form of the statement that the square of the first-order operator is the Klein–Gordon operator.

## The Solutions and the Correspondence Elsewhere

**The solutions.** The plane waves, the massless and the massive kernel conditions, the spherical and cylindrical solutions, and the field read as the gradient of a scalar potential are developed in *Explicit Solutions of the Biquaternionic Dirac Equation*, together with the shifted gradient, the completion, the nullness of the elementary field and the constrained gauge freedom of the potential.

**The correspondence.** The Maxwell correspondence, the static-medium dictionary, the mass-shell condition and the Lanczos feedback reading are developed in *The Dirac–Maxwell Correspondence in Biquaternionic Form*.

## The Dirac Operator with Potentials in Quaternionic Form

The Dirac equations of this article so far are free. The standard Dirac potentials — the **electric** (the time component of a four-vector), the **magnetic** (its spatial part), the **scalar**, and the **pseudoscalar** — are usually attached one at a time in the matrix formalism, each changing the operator differently. Kravchenko's monograph attaches all four in one place, and the result is a statement about the algebra rather than about the potentials. The free quaternionic operator and the free classical Dirac operator are related by **one constant linear transformation** — a change of basis; the monograph's Lemma 3 — and the *same* transformation, together with one permutation of the index labels, carries each of the four potentials into the corresponding quaternionic operator. The four potentials therefore do not enlarge the formalism. Each is an explicit coefficient function multiplying one of the algebra's basis directions, and the quaternionic Dirac equation with any one of them is the same first-order equation with a different coefficient.

The four directions are the four the algebra distinguishes. The scalar potential multiplies the identity $e_t$; the pseudoscalar potential multiplies the scalar imaginary $i$, the algebra's central pseudoscalar; the electric potential multiplies the timelike direction; and the magnetic potential enters through the spatial vector $\sum_\mu A_\mu \vec e_\mu$. This is the same fourfold list that Gürsey reads as the degenerate cases of the Lanczos system, and here it is the list of the algebra's carrier directions for a *coupling* rather than for a field.

**The pseudoscalar potential.** Of the four, the pseudoscalar case is the one that reaches machinery the corpus already has. It is the coupling of the field to the central imaginary $i$ — a coupling that changes the value of the field, not the minimal coupling of the companion article, which multiplies by a four-vector direction. Write $\vec r:=r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ for the position vector. For a time-harmonic field the pseudoscalar-potential equation reduces to

$$
\bigl(D + \xi_{\mathrm{scl}}(\vec r)I + M\bigr)f(\vec r) = 0,
$$

where $\xi_{\mathrm{scl}}$ is the potential, $I$ the identity of the algebra, and $M$ the constant frequency–mass shift; the only position dependence in the whole operator is the scalar coefficient $\xi_{\mathrm{scl}}(\vec r)$. That is exactly the corpus's shifted operator $D_\alpha = D + M_\alpha$ of *Biquaternion Regular Functions*, with the parameter no longer a constant but a function of position. The pseudoscalar-potential Dirac equation is therefore a shifted-operator equation, and the shift is the potential.

**The splitting.** The reduction is the monograph's Theorem 15. Let the constant biquaternion $\omega$ carry the frequency and the mass, so that $\omega^2 = \beta^2$, and suppose $\omega^2$ is not a zero divisor. Then the pseudoscalar equation is equivalent to a **pair** of scalar-coefficient equations,

$$
\bigl(D + (\xi_{\mathrm{scl}}(\vec r) + \beta)I\bigr)f_+ = 0,
\qquad
\bigl(D + (\xi_{\mathrm{scl}}(\vec r) - \beta)I\bigr)f_- = 0,
$$

the two parts $f_\pm$ being the images of $f$ under the two complementary projections that the shifted-operator theory supplies, multiplying on the right. Each of the two is an equation of the form $(D + \alpha(\vec r))u = 0$ with a **scalar** coefficient. That equation is the subject of the monograph's §4.1.5, and the corpus already carries its solution: the **zero-divisor device** recorded in *Maxwell's Equations in Chiral Media*, in which a solution of the eikonal equation $(\nabla\xi)^2 = \alpha^2$ conjugates $D + \alpha$ into $D + \mathcal{Q}_+$ with $\mathcal{Q}_+ = \nabla\xi$ a zero divisor, and the solutions are built from the exponentials $\exp(\pm i\theta_{\mathrm{phs}})$ of the accumulated phase and analytic transverse functions. The chain therefore closes inside the corpus: pseudoscalar-potential Dirac equation $\to$ shifted operator with a scalar coefficient $\to$ eikonal conjugation by a zero divisor $\to$ explicit solutions. The exceptional case, $\omega^2$ a zero divisor (an isotropic $\omega$), is separate; the monograph handles it with a one-variable ansatz, because the two projections degenerate there.

**What this does and does not add.** It adds the observation that the pseudoscalar Dirac coupling is not new machinery: it is the shifted operator the corpus already possesses, read at a position-dependent parameter, and the corpus's zero-divisor device solves it. It does not supply solutions for the electric potential — the monograph reaches that case by the same conjugation, but the corpus treats electromagnetic coupling separately in *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism* — and it claims no new physics: the coupling list is standard, and it is surveyed in the encyclopaedic compendium the monograph cites for the classification of exact Dirac solutions up to the late 1980s, now recorded in the Further Reading below.

## The Dirac Equation and the Biquaternion Algebra

### Why the Algebra and Not an Array

The Dirac equation is usually carried by four arrays that anticommute in pairs and act on a column. The same anticommutation holds inside $\mathbb{B}$, and over the reals the biquaternion algebra is the even part of the Clifford algebra those four real arrays generate,

$$
\mathrm{Cl}_{1,3}(\mathbb{R})^{\mathrm{even}}\cong\mathrm{Cl}_{3,0}(\mathbb{R})\cong M_2(\mathbb{C})\cong\mathbb{B},
$$

all four of real dimension eight, so the equation can be carried by $\mathbb{B}$ directly.

**The identity is a statement about the real form and not about the complexification.** Complexifying the generators gives $\mathrm{Cl}_{1,3}(\mathbb{C})\cong M_4(\mathbb{C})$, whose even part is $M_2(\mathbb{C})\oplus M_2(\mathbb{C})$, of complex dimension eight. That is the complexification of $\mathbb{B}$ and not $\mathbb{B}$ itself: $\mathbb{B}$ is a real form of it, the subalgebra fixed by a conjugation that exchanges the two summands — which is why "the even part" is the right description in one frame and the wrong one in the other. The doubling is where the two chiral summands appear, and it is a property of the complex display; the carrier of this article is one of them.

The advantage is that the algebra is the object and the array is a display of it. A biquaternion has four complex coefficients and the equation is one element acting on one element; the array needs a frame, a labelling of rows by the values and of columns by the letters of the units, and every identity is then a statement about one display. The corpus writes the element and prints the array only where a comparison wants it.

The price is a boundary case. A biquaternion acts on itself by left multiplication, so the field is a general element rather than a column, and the mass is a pairing of the two parts rather than an entry of a matrix; both are available in the algebra, and neither needs an extra object to hold the four numbers. What the array does better is bookkeeping: four rows make the four coefficients visible one by one, and a reader who is counting degrees of freedom will reach for it. That is why *The Legacy Pauli Gamma Formulation* keeps the arrays, from the article *Why AXF Matrices instead of Pauli and Gamma Matrices* onward, as a check on the algebra and not as its definition.

### What the Biquaternion Formulation Adds

The biquaternion formulation adds three things:

**1. A unified algebraic framework for Maxwell and Dirac.** The two equations are one operator acting in one algebra, and the two fields are two objects of that algebra. Nothing has to be added to pass from one to the other.

**2. A compact notation for the value.** The value is a letter, $L$ or $R$. No index is written: the field is one element, its two parts are named by the letter of their component, and the mass is the coefficient that relates them.

**3. A natural language for relativistic kinematics.** The four-velocity $\tilde{V}_{\Phi}$, the four-momentum $\tilde{P}_{\Phi}$, and the mass-shell relation $\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural} = -m^{2}\,c^{2}$ are all natural objects in the biquaternion algebra. The Dirac equation is naturally stated in terms of these objects, and the plane-wave solutions are naturally written in terms of the wave biquaternion $\tilde{K}_{\Phi}=\tilde{P}_{\Phi}/\hbar$ and the four-position $\tilde R_\Phi$.

### The Mass as a Non-Integrable Phase

A change of variable on the same field makes the mass look like a *phase*. Liu Yu-Fen's observation is that the mass term of the massive Dirac equation can be written as a coupling to a four-vector built from the field itself, so that the massive equation is the massless equation with the ordinary derivative replaced by a derivative along that four-vector and the mass becomes a phase rather than a scalar. The source states the identity in its array form,

$$
k_m\,\tilde\Xi^{\dagger}iR_{\mathrm{axf},\vec e_x}\tilde\Xi = \tilde\Xi^{\dagger}iR_{\mathrm{axf},\vec e_x}\bigl(iK_t\,e_t\tilde\Xi \vec e_x + i\sum_\eta B_{\mathrm{boost},\eta}\,\vec e_\eta\tilde\Xi \vec e_y\bigr),
$$

with $\tilde\Xi^{\dagger}iR_{\mathrm{axf},\vec e_x}$ the Dirac adjoint, written in the frame basis operator $iR_{\mathrm{axf},\vec e_x}$, and $U_{\mathrm{vec},\mu}$ a unit complex four-vector. The corpus records the display as the source's and does not restate it in basis operators: what the display carries is the shape, a four-vector built from the field and multiplying it from the right, and the shape survives the transcription while the array does not. The phase is **non-integrable**: if $U_{\mathrm{vec},\mu} = \partial/\partial R_\mu\,\theta_{\mathrm{cen}}$ were a gradient, the change of variable $\tilde\Xi \mapsto \exp(i\theta_{\mathrm{cen}})\tilde\Xi$ would remove it and the field would be massless; the mass is exactly the statement that $K$ is not a gradient, and the obstruction is the field strength $\partial U_{\mathrm{vec},\mu}/\partial R_\nu - \partial U_{\mathrm{vec},\nu}/\partial R_\mu$.

Here $\theta_{\mathrm{cen}}$ is the central phase: it is the argument of a unit complex number, so it is real.

The on-shell content of the interpretation is verified and simple: for a plane wave of momentum $p_\mu$ satisfying the mass shell $p^2 = m^2$, the vector

$$
U_{\mathrm{vec},\mu} = \frac{p_\mu}{m}
$$

satisfies $\sum_\mu\varepsilon_\mu U_{\mathrm{vec},\mu} U_{\mathrm{vec},\mu} = 1$. The momentum per unit mass is a unit vector, and the source reads it as the unit vector that carries the mass term. The condition is this article's own mass shell and not a new one: dividing $\langle\tilde K_\Phi\rangle_{\natural}=-k_m^{2}$ by $k_m^{2}$ gives $-(k'_t/k_m)^{2}+|\vec k_\Phi/k_m|^{2}=1$, and the two brackets are $U_{\mathrm{vec},t}=E/(mc^{2})$ and $U_{\mathrm{vec},\eta}=p_\eta/(mc)$, the slots of $\tilde V_\Phi/c$ for a plane wave. What the source adds is the reading of that unit vector as the carrier of the mass term, and the reading is a statement about the equation of §*The Biquaternionic Dirac Equation* and not about a different one.

This interpretation is the origin of the *triality construction* recorded in the companion articles. The two parts of the field, the vector they combine into, and the unit vector $K$ are the three objects that the order-three map permutes; the mass term is the coupling that the order-three (cubic) form expresses. The reader who wants the construction itself is referred to *The s-Vector Representation of the Dirac Spinor in Biquaternionic Form*, *Triality and the Ding Construction for the Dirac Spinor in Biquaternionic Form*, and *Dual Equivalence of the Dirac and Topologically Massive Gauge Fields*. The present article records only the origin: the mass is a unit vector, a non-integrable phase, and it is the object the triality construction is built on.

## The Letters Are Not Defined by Idempotents

**The claim to be refuted.** A recurring reading says the letters $L$ and $R$ are defined by choosing an idempotent $\tilde\Pi$, a square root of $e_t$, or another element of the algebra. The claim is false, and it fails twice over. The letters have two uses, the side of an operator and the value of an element, and neither is an idempotent construction. An idempotent exists in the second case, and there it is derived.

**The side is a membership, and nothing is chosen.** Multiplication defines two maps,
$$
L\colon\mathbb{B}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\quad L(a)(\tilde X)=a\tilde X,
\qquad
R\colon\mathbb{B}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\quad R(b)(\tilde X)=\tilde Xb,
$$
and nothing else enters their definition: no basis, no frame, no root, no idempotent, no unit. Both are complex-linear, unital and injective. The label of an operator is its membership in the two images,
$$
A\in L(\mathbb{B})\ \text{(left slot)},\quad
A\in R(\mathbb{B})\ \text{(right slot)},\quad
A\in L(\mathbb{B})\cap R(\mathbb{B})\ \text{(both)},\quad
A\notin L(\mathbb{B})\cup R(\mathbb{B})\ \text{(no single side)} .
$$
This is the operator chirality of *Operator Chirality on the Biquaternion Algebra*, and it takes four values, of which the last is not a subspace at all.

**The two images are four-dimensional and meet in the scalars.** If $L(a)=R(b)$ then $a\tilde X=\tilde Xb$ for every element $\tilde X$; at $\tilde X=e_t$ this gives $a=b$, and the common element then commutes with everything, so it is central. The intersection is therefore the line $\mathbb{C}\,\mathrm I$ and their sum is seven-dimensional, so nine of the sixteen dimensions of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ carry no side.

**The swap.** The structure isomorphism $a\otimes b\mapsto L_aR_b$ carries the flip of the two tensor factors to $\sigma$, with $\sigma(L_aR_b)=L_bR_a$ and so $\sigma(L_a)=R_a$ for every $a$. The swap is an involution, an anti-automorphism, intrinsic and not inner, and it names no element: it is the map that belongs to the definition of the two sides.

**The second exchanger.** The quaternion conjugation exchanges the sides as well, but it moves the parameters,
$$
\natural\,L(a)\,\natural=R\bigl(a^{\natural}\bigr).
$$
Away from the scalars the two maps differ, and that difference is where the phases the corpus computes from a change of side come from. Neither map replaces the other.

**The value uses a unit.** The second use of the letters is the split $\tilde X=\tilde X_L+\tilde X_R$, and it does use a chosen element. The element is the frame's third unit $\vec e_z$, a traceless unit with $\vec e_z^2=-e_t$, and the letters name the two eigenspaces of the right multiplier,
$$
R_{\vec e_z}\tilde X_L=-i\tilde X_L,\qquad R_{\vec e_z}\tilde X_R=+i\tilde X_R ,
$$
which is the test of §*The Value Is a Rule* written as an eigenvalue problem. No idempotent is chosen here either, and the halves belong to the unit: a different third direction splits the same element differently. What the value costs is the frame, declared once for the whole article; what it does not cost is an idempotent.

**The idempotent is derived, and the direction of the derivation is the point.** With $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ one has $\tilde\Pi_\pm^2=\tilde\Pi_\pm$, $\tilde\Pi_+\tilde\Pi_-=0$ and $\tilde\Pi_++\tilde\Pi_-=e_t$, and right multiplication by $\tilde\Pi_\pm$ returns the two parts, $\tilde X\tilde\Pi_+=\tilde X_L$ and $\tilde X\tilde\Pi_-=\tilde X_R$. The idempotent reproduces the split exactly, and it is a polynomial in the unit: the unit is the datum, the idempotent is derived from it. Read as a definition, "the split is made by an idempotent" inverts that order.

**The category error.** Operator chirality is a membership in a subspace of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, of complex dimension sixteen. An idempotent is an element of $\mathbb{B}$, of complex dimension four. A membership in a subspace of operators cannot be read off a chosen element, and the four cases are fixed before any element is named. The confusion merges the third row of the table below with the first two.

**The instructive case.** The basis operator $-iR_{\vec e_z}$ is a right multiplier, so its label is the right slot; it squares to $\mathrm I$, has trace zero and, its multiplier being traceless, the spectrum $\{+1,+1,-1,-1\}$. It behaves like a chirality element because it is an example of a side, and an example is not a definition: an object that has a chirality cannot be what chirality means.

**What the letters are not.**

| Object | Why it is not the label |
| --- | --- |
| a square root of $e_t$ | the label uses no element |
| an idempotent $\tilde\Pi$ | a condition on an element, not on an operator |
| a Peirce decomposition | four lines of $\mathbb{B}$, not four cases on the operator space |
| a Peirce basis | a display; the images exist before one is declared |
| a spectrum $\{+1,+1,-1,-1\}$ | a consequence of a basis operator that was chosen |
| a spinor, an element of a minimal left ideal | a subspace of $\mathbb{B}$ of dimension two; the label lives in the sixteen-dimensional endomorphism algebra |
| a Clifford algebra | it fixes a dimension and a signature; the images do not |
| a matrix unit of $M_4(\mathbb{C})$ | a display; a basis operator is a sum of four of them |
| $-iR_{\vec e_z}$ | an example of the right slot |

**One display.**

| Notion | Carrier | Chosen element | Idempotent |
| --- | --- | --- | --- |
| the side: $L(\mathbb{B})$, $R(\mathbb{B})$, both, neither | $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, $16$ | no | no |
| the swap $\sigma$ | $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, $16$ | no | no |
| the value, $\tilde X=\tilde X_L+\tilde X_R$ | $\mathbb{B}$, $4$ | yes, the frame's $\vec e_z$ | no; $\tilde\Pi_\pm$ is derived |

**The statement.** As sides, $L$ and $R$ are the two images of the regular representation, fixed by the multiplication. As values, they are the two eigenspaces of the right multiplier by the frame's third unit. Neither is fixed by an idempotent, and the second is not fixed by one even though an idempotent exists that reproduces it. A text that grounds the letters in an idempotent has merged a membership in $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ with a choice of element in $\mathbb{B}$.

**The dimensions are the whole check, and they are exact.** Both images are four-dimensional, because $L$ and $R$ are faithful representations of a four-dimensional algebra; their intersection is the line $\mathbb{C}\,\mathrm I$ of central elements, so the sum has dimension $4+4-1=7$ and the operators outside both images form a line. That line is why a general $L_a+R_b$ is in neither image, and it is the reason the two-sided display needs a conjugation as well as a right multiplication. The spectrum $\{+1,+1,-1,-1\}$ of $-iR_{\vec e_z}$ follows from the trace: it is an involution, so its eigenvalues are $\pm1$, and its trace is zero, so the multiplicities are equal.

## The Approaches the Equation Does Not Need

**The position.** The equation of this article is one element acting on one element by left multiplication, no term of it moving a value across; the crossing belongs to the two-sided dictionary, where the conjugation and the right multiplication supply it. Every other object that the literature carries beside a Dirac equation is either a display of that action or a construction that pays a choice the equation does not make. The section states the list once, because the cost of each is not a matter of taste: a construction that adjoins an object also adjoins the choice that selects the object, and the choice is then mistaken for physics.

| Object | What it would supply | Why the equation does not need it |
| --- | --- | --- |
| a column of four numbers | the field as a list | the field is the element itself; a column is the element read in a basis and multiplied from outside |
| four anticommuting arrays | the factors of the operator | the anticommutation is a product of the units of the algebra |
| a separate state space | somewhere for the field to live | the algebra acts on itself by left multiplication, and the field is an element of it |
| a minimal left ideal | a two-component object called a spinor | an ideal is chosen by an idempotent, that is by a point of a projective line, and the field is in no chosen subspace |
| a Peirce decomposition | the two parts of the field | the value is a letter returned by a test on the element |
| a chiral projector | one of the two parts | the test returns the value; a projector is derived from the basis operator when one is wanted |
| a Clifford algebra | the sign the mass needs | the sign is the side on which an operator multiplies |
| a second-order equation | the dynamics | it follows from the gradient being an element, with no matrix square |

**No column.** A column needs a basis in order to be written and a matrix in order to be multiplied, and both are displays. The equation says what an element does to an element and the answer is another element; four coefficients appear when numbers are wanted, and they appear as coefficients of the element and not as entries of a column. The arrays printed in §*The Legacy Pauli Gamma Formulation* are printed there for comparison and are not the equation.

**No anticommuting arrays.** The four arrays of the traditional display anticommute in pairs and multiply a column. In the algebra the same anticommutators are products of units, computed from the multiplication of the frame rather than imposed as relations. The algebra is then free of the two quantities that the arrays carry in from outside, a dimension and a signature.

**No separate state space, and no space of spinors.** The phrase "the Dirac equation acts on a spinor" survives because a bispinor is a spinor in the older vocabulary, and the field of this article is a bispinor in that sense. What does not survive is the inference drawn from the phrase, that the equation needs a space of spinors to act on. The operator is an element of the algebra, the field is an element of the algebra, and the multiplication is the algebra's own: nothing is adjoined, and nothing has to be.

**No minimal left ideal.** A minimal left ideal is a subspace chosen by an idempotent, and the idempotent is a point of a projective line. To place the field in one is to choose that point, and a choice the equation does not make has to be justified by something outside the equation. Here the field is the whole element, and the two values are read from the element and not selected from it.

**No Peirce decomposition and no chiral projector.** A Peirce decomposition returns four corners of two idempotents, and a projector onto one part returns a part. Neither is used: the test returns the letter, the letter is the whole of what §*Chirality* needs, and the mass reverses the letter rather than exchanging two subspaces. A projector can be built from the basis operator whenever a projection is wanted, since the basis operator is an involution, and it is then a derived object.

**No Clifford algebra.** Two algebras must be kept apart before the phrase is used. The carrier is $\mathbb{B}$, of complex dimension four. The operators on it are $\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C})$, of complex dimension sixteen, and the four generators of §*The Legacy Pauli Gamma Formulation* live in that second algebra: each is a product $L_aR_b$, one left multiplication and one right. The Dirac algebra of the literature is the operator algebra and $\mathbb{B}$ is what it acts on; running the two together is what makes the construction look as though a Clifford algebra were needed for the field to exist. A Clifford algebra is generated by vectors with a stated anticommutator, and it fixes a dimension and a signature. The frame here is four declared units whose products are computed, and the anticommutation of the three spatial ones is a fact about them and not an axiom. Nothing in the equation is derived from a Clifford relation that the multiplication of the algebra does not already give.

**No second-order equation.** The product of the operator with its quaternion conjugate is the wave operator, $(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi=\Box_\Phi$, so each part of the field obeys $\Box\tilde\Xi=k_m^{2}\tilde\Xi$. That is a consequence, used in §*The Biquaternionic Dirac Equation* to check the pair, and not a starting point: nothing is squared in order to reach the first-order equation, and no matrix square is taken.

**The criterion.** One test separates the two families of approach. If a construction needs an object chosen that the equation does not otherwise use — a basis for a column, an idempotent for an ideal, a frame for an array, a signature for a Clifford algebra — then the object belongs to the display and not to the equation, and whatever physics is attached to it is attached to the choice. The equation of this article needs the algebra, the field, and the frame that supplies $\vec e_z$ in the test. It needs nothing else.

## Open Questions

1. **The real structure $\flat$ and the electroweak interaction.** The conjugation $\flat = -{}^{*}$, whose fixed space is the anti-Hermitian sector $\mathbb{B}_{\Phi}$ and which is the algebra's real structure, has the shape of a Majorana-type pairing. Does that real structure have a natural interpretation in terms of the electroweak interaction — in particular, does it supply the real form in which the neutrino is distinguished from the charged fermions?

2. **The relation to the Standard Model.** The Standard Model describes fermions in the spinor representation of the Lorentz group. How does the biquaternion framework extend to the full Standard Model, including the gauge fields?

3. **The non-abelian generalization.** The biquaternionic Dirac equation is abelian (the field is a single biquaternion). How does the framework extend to non-abelian gauge theories, where the fermion field is a vector in a representation of the gauge group?

4. **The relation to the twistor program.** Twistor theory works in the complex four-dimensional space $\mathbb{C}^4$, which is the coefficient space of $\mathbb{B}$. How do the biquaternion Dirac equation and the twistor equation relate?

5. **The quantization.** The Dirac equation is the classical equation of motion for a fermion field. How does the biquaternion framework extend to the quantized theory (quantum field theory), and what is the role of the biquaternion structure in the quantized case?

These questions are open.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, $\gamma_0^2=I_4$ and $\gamma_\eta^2=-I_4$. The frame belongs to the coordinate, not to the array.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

$$
\begin{aligned}
\gamma_0 &= iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x}, &\gamma_1 &= iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\\[2pt]
\gamma_2 &= iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y}, &\gamma_3 &= iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\\[2pt]
\gamma_5 &= -iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z}.
\end{aligned}
$$

The same in the axis-free display:

$$
\begin{aligned}
\gamma_0 &= iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x}, &\gamma_1 &= iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\\[2pt]
\gamma_2 &= iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}, &\gamma_3 &= iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\\[2pt]
\gamma_5 &= -iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z}.
\end{aligned}
$$

A single product is a pure tensor; the products form the seven-dimensional cone of rank at most one, and a general element is a sum of at most four.

$\gamma_5$ is the fifth basis operator of the frame, one operator that realises the split (*Operator Chirality on the Biquaternion Algebra*): the right multiplication $-iR_{\vec e_z}$, written $-iL_{e_t}R_{\vec e_z}$ because $L_{e_t}=\mathrm I$. The two arrays above are its arrays in the two displays. The operator is neither array. The side is what this basis operator shows and what the four generators do not: the four multiply on the left, and the basis operator multiplies on the right. Its being a chirality is that side, and the side is fixed without it.

The dictionary of basis operators is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the basis operators span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{\mathrm{axf},e_\mu}=C_{\Pi}L_{\mathrm{pau},e_\mu}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a basis operator named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The Dirac equation in biquaternionic form is the chiral pair

$$
\tilde\nabla_\Phi\tilde\Xi_{R} = k_m\,\tilde\Xi_{L}, \qquad (\tilde\nabla_\Phi)^{\natural}\tilde\Xi_{L} = k_m\,\tilde\Xi_{R}
$$

for a field of mass $m$, where $\tilde\nabla_\Phi$ is the biquaternionic gradient, $\tilde\Xi = \tilde\Xi_{L} + \tilde\Xi_{R}$ is one element of $\mathbb{B}$ whose parts are the two components that the subscript names, the coefficient of the mass term is $k_m$, the inverse reduced Compton wavelength, and the mass is the central coefficient that relates the two components. At $m=0$ the pair decouples into the two one-sided equations

$$
\tilde\nabla_\Phi\tilde\Xi_{R}=0, \qquad (\tilde\nabla_\Phi)^{\natural}\tilde\Xi_{L}=0,
$$

one for each letter of the pair; the single equation $\tilde\nabla_\Phi\tilde\Xi=0$ is the member written $R$. The letters $L$ and $R$ name the two components of the pair; the value is a separate property of an element, read by the basis operator, the value of a product is the value of its right factor, and left multiplication keeps it. The mass multiplies on the left and is central, so it relates the two components and moves no value across. The value is read by one test on the element, $\tilde X\vec e_z=-i\tilde X$ for $L$ and $\tilde X\vec e_z=+i\tilde X$ for $R$, so no column, no basis, no ideal, no idempotent, no projector and no space of spinors is needed anywhere; §*The Letters Are Not Defined by Idempotents* states why the letters are fixed without one, and §*The Approaches the Equation Does Not Need* states for each of them what it would supply and why the equation does without it. In the massless limit, in the frame whose third direction is the momentum's, each part carries one helicity, the two parts being the two eigenspaces of the value test there and the letter of the pair being the other value (§*Chirality*). The member written $R$ has the same form as the source-free biquaternion Maxwell equation, and the member written $L$ is its conjugate. The structural identity is the statement that both fields are read in the same algebra — no matrix, no column and no separate space. Each part satisfies the Klein–Gordon equation $(\Box - k_m^{2})\tilde\Xi_{L,R} = 0$.

The relativistic kinematic relations are expressed in the same language: the four-velocity $\tilde{V}_{\Phi} = \gamma(ic\, e_t + \vec v)$ satisfies $\tilde{V}_{\Phi}\tilde{V}_{\Phi}^{\natural} = -c^2$, the four-momentum $\tilde{P}_{\Phi} =m\,\tilde{V}_{\Phi}$ satisfies the mass-shell relation $\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural} = -m^{2}\,c^{2}$, and the four-position $\tilde R_\Phi = i r'_t\, e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ gives the invariant interval $ds^2 = \langle d\tilde R_\Phi\rangle_{\natural} = d\tilde R_\Phi\,d\tilde{R}_\Phi^{\natural}$.

**The solutions** are in *Explicit Solutions of the Biquaternionic Dirac Equation*: the massless plane wave with $\tilde{K}_{\Phi}\tilde\Xi_{0} = 0$ and its two-state kernel on the light cone, the massive plane waves with the mass shell $\tilde{K}_{\Phi}\tilde{K}_{\Phi}^{\natural}=-k_m^{2}$, whose two frequency branches and two spin states give the four solutions the field carries, and the completed spherical and cylindrical harmonics.

A second form of the same equation is Kravchenko's, and it is two-sided: $\bigl(i\partial/\partial r'_t+\vec\nabla\bigr)F-i\,\overline{F}\,\vec e_z\,k_m=0$, whose free part is $-(\tilde\nabla_\Phi)^{\natural}$ and whose mass term is a coefficient conjugation together with the right multiplication by the direction $\vec e_z$. The conjugation obstructs the analytic theory, so it is moved into the change of variable, and the conjugation-free operator

$$
R[F] = \vec\nabla F - \frac{\partial F}{\partial r'_t}\,\vec e_x - F\,\vec e_y\,k_m
$$

has coefficients in the real quaternions. The real and imaginary parts of a solution of $R[F]=0$ are therefore separately solutions, so one quaternionic solution carries two Dirac solutions. With the conjugation removed, the time-harmonic amplitude obeys a shifted equation with a biquaternionic parameter, and the Cauchy integral formula, the Plemelj–Sokhotski formulas and the boundary-value criterion hold for it in the same shape as for the time-harmonic Maxwell field.

The dictionary between the massive equation and the static Maxwell medium, the mass shell read as the condition on that correspondence, and the Lanczos feedback reading of the two equations are in *The Dirac–Maxwell Correspondence in Biquaternionic Form*. The four potentials — scalar, pseudoscalar, electric and magnetic — are coefficients on four distinguished directions of the algebra, and the pseudoscalar one is the shifted operator that the corpus already solves.

The mass can be written as a non-integrable phase: $U_{\mathrm{vec},\mu} = p_\mu/m$ is a unit four-vector on shell, and the mass term is the statement that $K$ is not a gradient. That observation is the origin of the triality construction of the companion articles.

The biquaternion framework provides a compact and unified language for the Maxwell and Dirac equations, but it does not by itself derive the mass term or the electroweak structure. Those require additional physics beyond the algebraic framework.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\tilde{Q}_L$, $\tilde{Q}_R$ | A part of the pair, named by the letter of its component; the value is read from the element by the chirality test, and only the zero element carries both values |
| $L_a$, $R_b$ | The left and right multipliers, $L_a(\tilde X)=a\tilde X$ and $R_b(\tilde X)=\tilde Xb$; the images $L(\mathbb{B})$ and $R(\mathbb{B})$ are what an operator's side is a membership in |
| $\sigma$ | The swap, $\sigma(L_aR_b)=L_bR_a$ and $\sigma(L_a)=R_a$; the flip of the two tensor factors of $a\otimes b\mapsto L_aR_b$, intrinsic, an anti-automorphism, not inner |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ | The idempotents derived from the frame's third unit; right multiplication by them returns the two parts, and they are not what defines the letters |
| $\gamma_5$ | The fifth basis operator of the frame, the chirality basis operator; its array is printed in *The Legacy Pauli Gamma Formulation* |
| $i_1,i_2,i_3$ | The source's symbols for the quaternion units $\vec e_x,\vec e_y,\vec e_z$; the scalar imaginary is its $i$ as here |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum |
| $\vec v$ | Particle three-velocity |
| $\gamma = 1/\sqrt{1 - \vec v^2/c^2}$ | Lorentz factor |
| $\tilde R_\Phi = i r'_t\,e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ | Four-position biquaternion |
| $\tilde{V}_{\Phi} = \gamma(ic\,e_t + \vec v)$ | Four-velocity biquaternion |
| $\tilde{P}_{\Phi} =m\,\tilde{V}_{\Phi}$ | Four-momentum biquaternion, since $m\,c=mc$; the shell is $\tilde{P}_{\Phi}\tilde{P}_{\Phi}^{\natural}=-m^{2}\,c^{2}$ |
| $k_m=\dfrac{mc}{\hbar}$ | The mass wave number of the field, the one wave number of the article; $\mathsf{L}^{-1}$, the coefficient of the mass term, and $k_m^{2}$ the coefficient of the Klein–Gordon mass term. Its inverse $1/k_m=\hbar/(mc)$ is the reduced Compton wavelength. Defined in *The Three Wavenumbers of a Particle* |
| $\tilde\nabla_\Phi$ | Biquaternionic gradient (Dirac operator), the first-order element of *Operator and Calculus Conventions* |
| $(\tilde\nabla_\Phi)^{\natural}$ | Its quaternion conjugate |
| $\Box_\Phi = \tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}$ | d'Alembertian, central scalar |
| $\tilde\Xi = \tilde\Xi_{L} + \tilde\Xi_{R}$ | The field: one element of $\mathbb{B}$, one part per letter of the pair |
| $\tilde\Xi^{\flat} = -\tilde\Xi^*$ | Anti-Hermitian conjugate (the algebra's real structure; not the mass term) |
| $\bar{\cdot}$, written $C$ by the source | Componentwise complex conjugation, $Q_\mu\mapsto\bar Q_\mu$ on the coefficients: an automorphism, $\mathbb{C}$-antilinear and not an anti-automorphism |
| $\vec\nabla = \sum_{\eta=1}^{3}\vec e_\eta\,\partial/\partial R_\eta$ | The spatial gradient, pure, $\vec\nabla^2=-\Delta$ and $\lvert\vec\nabla\rvert^2=\Delta$, with real quaternion coefficients on the material sector; the source writes it $D$ |
| $D = i\vec\nabla$ | The corpus's spatial operator of *Biquaternion Regular Functions*, $D^2=\Delta$ |
| $\mathcal{N} = i\partial/\partial r'_t + \vec\nabla - i\,\overline{\cdot}\,\vec e_z\,k_m$ | The two-sided Dirac operator with the conjugation in the mass term; its free part is $-(\tilde\nabla_\Phi)^{\natural}$ |
| $R[F] = \vec\nabla F-\partial F/\partial r'_t\,\vec e_x-F\vec e_y\,k_m$ | The conjugation-free operator of the same source; real, with coefficients in $\mathbb{H}$, so $R[\mathrm{Re}\,F]=R[\mathrm{Im}\,F]=0$ |
| $\vec\nabla+\cdot\,\alpha$ | The shifted operator for the time-harmonic amplitude, $\vec\nabla f+f\alpha=0$ at a constant $\alpha$ |
| $\xi_{\mathrm{scl}}$ | Scalar (pseudoscalar-potential) coefficient of the shifted Dirac operator |
| $\tfrac12(e_t\pm\alpha/\sqrt{\alpha^2})$ | The two complementary projections of the harmonic field, multiplying on the right; they split it into the two signs of the frequency, and in the source's reading the two helicities |
| $\mathcal{C}_{\mathrm{cau},\omega}$ | The Cauchy-type operator of the amplitude equation; the Cauchy integral formula, the Plemelj–Sokhotski formulas and the boundary-value criterion $\tilde\Xi = \mathcal{C}_{\mathrm{cau},\omega}\tilde\Xi$ on $\Gamma$ hold for it |
| $\tilde{K}_{\Phi}=\frac{\tilde{P}_{\Phi}}{\hbar}=i k_{t}^{\prime}e_t+\vec k_\Phi$ | Wave biquaternion; $k_{t}^{\prime}=\omega/c$ |
| $U_{\mathrm{vec},\mu}$ | Unit complex four-vector carrying the mass term, $k_m\tilde\Xi^{\dagger}iR_{\mathrm{axf},\vec e_x}\tilde\Xi=\tilde\Xi^{\dagger}iR_{\mathrm{axf},\vec e_x}(iK_t\,e_t\tilde\Xi \vec e_x+i\sum_\eta B_{\mathrm{boost},\eta}\,\vec e_\eta\tilde\Xi \vec e_y)$; $U_{\mathrm{vec},\mu}=\frac{p_{\mu}}{m}$ on shell, $\sum_\mu\varepsilon_\mu U_{\mathrm{vec},\mu} U_{\mathrm{vec},\mu}=1$ |
| $iR_{\mathrm{axf},\vec e_x}$ | The timelike basis operator, the Dirac adjoint in the bilinear covariants |
| $\lvert F\rvert^2 = \langle F\rangle_{*} = \sum_\mu\lvert F_\mu\rvert^2$ | Hermitian norm of the biquaternion field, the definite one; the probability density of a complex field |
| $m$ | Fermion mass; in the equations of this article it enters only through the length, so a display writes $k_m$ and never $m$ |

## Further Reading

- [Explicit Solutions of the Biquaternionic Dirac Equation](explicit-solutions-of-the-biquaternionic-dirac-equation.html), for the plane waves, the massless and massive kernel conditions, the completed spherical and cylindrical solutions and the field as the gradient of a scalar potential.
- [The Dirac–Maxwell Correspondence in Biquaternionic Form](the-dirac-maxwell-correspondence-in-biquaternionic-form.html), for the identity of form with the Maxwell equation, the mass term, the static-medium dictionary, the mass shell as a condition and the Lanczos feedback reading.
- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- [The Three Wavenumbers of a Particle](the-three-wavenumbers-of-a-particle.html), for the definition of the wave number $k_m=mc/\hbar$ and of the two state wave numbers $k_{\Phi}$ and $k_{t}^{\prime}$, their values for the electron, the proton and the other particles, and the unit argument that fixes the coefficient of the mass term.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original Dirac equation.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the foundational treatment of the Dirac equation.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the standard physics treatment.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the historical background on Clifford algebras and the objects the literature calls spinors.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric algebra approach to the Dirac equation.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original formulation of the Dirac equation in geometric algebra.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the spinor formulation of the Dirac equation.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the regular functions of that tradition and its analysis of the Dirac operator.
- L. A. Alexeyeva, "Differential algebra of biquaternions. Dirac equation and its generalized solutions," *Progress in Analysis, Proceedings of the 8th Congress of the ISAAC* (Moscow, 2013), pp. 153–161, for the biquaternion formulation of the Dirac equation.
- V. V. Kravchenko, "On a Biquaternionic Bag Model," *Zeitschrift für Analysis und ihre Anwendungen* **14** (1995), no. 1, 3–14, DOI 10.4171/ZAA/658, for the explicit real-linear dictionary from the four-component bispinors onto the biquaternions, with the timelike generator realized by complex conjugation — the images of the spatial generators, not readable from this source alone, are stated in the Doklady note of the next entry; for the biquaternionic Dirac operator $i\partial/\partial r'_t + D - miCM_{i_3}$, printed there at $c=1$ — the source's real time, the $r'_t$ of the material sector — the source's $D$ being the spatial gradient $\vec\nabla$ of this article, whose mass term carries the conjugation; for the removal of the conjugation by a change of variable, realised as the factorisation $\mathcal{N}=u^{+}Ru^{-}$ with the conjugation-free operator $R=P_1^{+}(i\partial/\partial r'_t+D)+P_1^{-}(-i\partial/\partial r'_t+D)-mM_{i_2}=D-\partial/\partial r'_tM_{i_1}-mM_{i_2}$; and for the two projections $\tfrac12(e_t\pm i\vec e_\eta)$ of that factorisation, which the source writes $P_\eta^{\pm}=\tfrac12 M_{(1\pm i i_k)}$.
- V. V. Kravchenko, "Quaternion-Valued Integral Representations of the Harmonic Electromagnetic and Spinor Fields," *Doklady Mathematics* **51** (1995), no. 2, 287–289 (translated from *Doklady Akademii Nauk* **341** (1995), no. 5, 603–605), for the dictionary of the preceding entry as a real-linear bijection with the mass term carrying complex conjugation, and for that dictionary in full — the components of $A$, and the images of the three timelike bivectors, $A(L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_z}\Xi)=-i\,i_1A(\Xi)$, $A(L_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_z}\Xi)=-i\,i_2A(\Xi)$, $A(L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_z}\Xi)=+i\,i_3A(\Xi)$, with the volume element carried by a right multiplication through $i_3$; for the bijection between the solutions of the Dirac equation and the solutions of the quaternionic equation $i\partial/\partial r'_tF+DF-\mathrm{Im}(F)\,i=0$; for the time-harmonic field $F = P_+f(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\exp(i\theta_{\mathrm{pwt}})+P_-f(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\exp(-i\theta_{\mathrm{pwt}})$ with the two complementary projections and the helicity interpretation of the two parts; for the massless case $i\partial/\partial r'_tF+DF=0$, attributed there to Imaeda; and for the spinor-side integral representation recorded in the section *The Integral Representation of the Harmonic Field* — the amplitude operator $D_\omega\tilde\Xi = -\omega\,e_t\tilde\Xi \vec e_x+i\sum_{\eta=1}^{3}\vec e_\eta\,(\partial\tilde\Xi/\partial R_\eta)\,\vec e_y$, the Cauchy-type operator $\mathcal{C}_{\mathrm{cau},\omega} = A^{-1}KA$, and the three results that follow for it: the Cauchy integral formula, the Plemelj–Sokhotski formulas, and the boundary-value criterion $\tilde\Xi = \mathcal{C}_{\mathrm{cau},\omega}\tilde\Xi$ on $\Gamma$. The same note is the source of the unifying statement that one parametric system, at different values of its parameter, is the time-harmonic Maxwell system and the time-harmonic Dirac system; that statement is recorded in the companion *The Time-Harmonic Maxwell Operator and the Quaternionic Cauchy Integral*.
- V. V. Kravchenko and M. V. Shapiro, *Integral Representations for Spatial Models of Mathematical Physics* (Pitman Research Notes in Mathematics 351, Addison-Wesley Longman, 1996), for the shifted operator $D_\alpha$ and its boundary-value theory, which is where the conjugated equation is taken once the conjugation has been removed.
- V. V. Kravchenko, *Applied Quaternionic Analysis* (Research and Exposition in Mathematics 28, Heldermann, 2003), §§4.2.1–4.2.2.1, for the four standard Dirac potentials — electric, scalar, pseudoscalar, magnetic — in quaternionic form, for the single constant transformation that relates the classical and quaternionic Dirac operators with potentials, and for the reduction of the pseudoscalar-potential equation to a pair of scalar-coefficient equations.
- V. V. Kravchenko and M. P. Ramirez Tachiquin, "On a quaternionic reformulation of the Dirac equation and its relationship with Maxwell's system," *Bulletin de la Société des Sciences et des Lettres de Łódź* **53** (2003) 101–114, for the **reality** of the conjugation-free quaternionic Dirac operator — $R = D-\partial/\partial r'_tM_{i_1}-mM_{i_2}$, the source's $D$ being the spatial gradient $\vec\nabla$ of this article, with coefficients in the real quaternion algebra, hence $R[\mathrm{Re}\,F]=R[\mathrm{Im}\,F]=0$ — and for the **involutive symmetry** $\Xi_{\mathrm{inv}}=iZ_c\Xi$ that follows, the symmetry itself attributed there to J. Niederle and A. G. Nikitin, "Involutive symmetries, supersymmetries and reductions of the Dirac equation," *J. Phys. A: Math. Gen.* **30** (1997) 999–1010; and for the quaternionic current-conservation equation $\partial/\partial r'_t|F|^2 = -\hbar[(DF^{\dagger})F+F^{*}(DF)]$ with the identity $|F|^2=|\Xi|^2$ of the biquaternion modulus and the Dirac density. The paper's correspondence with the static Maxwell system of an inhomogeneous medium and its condition $k_\Phi^2=\alpha^2$ are described in *The Dirac–Maxwell Correspondence in Biquaternionic Form*. The paper's factors $u^{\pm}$ of the factorisation $\mathcal{N}=u^{+}Ru^{-}$ and its explicit action of $A^{-1}$ on $\mathrm{Re}\,F$ are quoted, not reproduced: the available copy is a scan without a text layer.
- Liu Yu-Fen, "Triality, Biquaternion and Vector Representation of the Dirac Equation," arXiv:math-ph/0109008 (2001), for the interpretation of the mass term as a coupling $\tilde\Xi^{\dagger}iR_{\mathrm{axf},\vec e_x}(iK_t\,e_t\tilde\Xi \vec e_x+i\sum_\eta B_{\mathrm{boost},\eta}\,\vec e_\eta\tilde\Xi \vec e_y)$ to a unit vector, hence as a non-integrable phase; and for the vector representation of the spinor built on it, recorded in the companion *The s-Vector Representation of the Dirac Spinor in Biquaternionic Form*.
- Liu Yu-Fen, "Triality and Dual Equivalence Between Dirac Field and Topologically Massive Gauge Field," arXiv:hep-th/0602275 (2006), for the same interpretation in the order-$\ell$ ding language, and for the parent-action duality recorded in *Dual Equivalence of the Dirac and Topologically Massive Gauge Fields*.
