# __The Dirac Equation in Biquaternionic Form__

## Introduction

The Dirac equation is the relativistic wave equation for spin-$\frac{1}{2}$ particles. It was discovered by Paul Dirac in 1928 as an attempt to reconcile quantum physics with special relativity, and it predicted the existence of antimatter. It is one of the foundational equations of quantum field theory, and it is the equation that governs electrons, quarks, and all fermions.

The Dirac equation is usually written with matrices. In the biquaternion algebra it needs none. The field is an element of $\mathbb{B}$, the operator is an element multiplying it, and the mass is the one term that carries the field from one value of the subscript to the other. The dynamics is the chiral pair

$$
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = k_m\,\tilde{Ξ}_{\mathrm{sp},L},
\qquad
\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\,\tilde{Ξ}_{\mathrm{sp},R} ,
$$

which is the pair of *Operator and Calculus Conventions*. Every derivative in $\tilde\nabla$ carries an inverse length, so the coefficient on the right must carry one too, and it is written as the reciprocal of a length:

$$
k_m=\dfrac{mc}{\hbar}.
$$

That wave number is the reciprocal of the reduced Compton wavelength of the field, and it is the only one the article needs. It is defined in *The Three Wavenumbers of a Particle*, where it is written $k_m=mc/\hbar$. Below, the mass coefficient is always written $k_m$ and the mass-squared term always $k_m^{2}$. Since $mc=\hbar\,k_m$, the rest energy is $m\,c^{2}$ and the mass shell is $\tilde{P}\tilde{P}^{\natural}=-m^{2}\,c^{2}$, so every mass statement is read in this one length. At $m=0$ the pair decouples into the two one-sided equations $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R}=0$ and $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=0$, one for each value. No matrix, no column and no array enters either line. A frame is declared once, because the value of a part is read by the frame's third direction, and no further choice is made.

This article develops the biquaternionic formulation of the Dirac equation. The gradient $\tilde{\nabla}$ is the Dirac operator of the algebra: it is first order, it acts by left multiplication, and it squares to the scalar d'Alembertian through its conjugate. The equation is the chiral pair on the two values of the subscript, and each half obeys the Klein–Gordon equation. A second, **two-sided** form of the same equation — Kravchenko's dictionary, in which the spatial derivative acts from the left and the mass term from the right — is developed in *An Explicit Dictionary with Conjugation in the Mass Term*; the two forms are compared in *The One-Sided and the Two-Sided Equation*.

The article is organized as follows. First the gradient and the equation are stated, then the algebra and the two values of the subscript. The equation is solved, first for plane waves and then in spherical and cylindrical coordinates, and the relation to the Maxwell equation follows. The two-sided form, the potentials and the algebra discussion close the body, and *The Legacy Pauli Gamma Formulation* prints the older display for the reader who has to compare with it.

The conventions are those of the companion articles: the algebra and its units are those of *Algebra and Element Conventions*, the coordinates, the metric and the frame those of *Frame and Metric Conventions*, and the units and the two writings of the temporal slot those of *Physics Units and Common Elements Conventions*. No formula of theirs is repeated here. Two points are this article's own. The symbol $c$ is the speed of light **in the medium** and $c_0$ the vacuum speed, so that $c=c_0$ only in vacuum and a result quoted with $c$ is a result in the medium. A squared three-vector such as $\vec v^2$ or $\vec p^2$ is the Euclidean square, not the quaternion square, which is its negative; the symbol $v$ is kept for particle and frame velocities.

## The Gradient and the Equation

### The Units and the Gradient

The units are the coefficient basis of *Algebra and Element Conventions* and the gradient is the operator of *Operator and Calculus Conventions*, §*The Gradient*, written $\tilde{\nabla}$, with the quaternion conjugate $\tilde{\nabla}^{\natural}$ and the central scalar $\Box$ of the same file. This article repeats none of the three and derives nothing about them. What it uses is one consequence: the product of the operator and its conjugate is second order and scalar, so the equation below is first order in the field and second order in the wave, and no matrix square is needed anywhere in it.

### The Equation in the Algebra

The dynamics of this article is the **chiral pair**

$$
\boxed{\;
\begin{aligned}
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} &= k_m\,\tilde{Ξ}_{\mathrm{sp},L},\\[4pt]
\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} &= k_m\,\tilde{Ξ}_{\mathrm{sp},R},
\end{aligned}
\;}
$$

for a field of mass $m$. The gradient differentiates with respect to the coordinates $R_\mu$ and carries the unit of an inverse length, so the term it is equated to carries that unit as well: $m$ alone carries a mass, and $k_m$ carries the inverse length. In the units $\hbar=c=1$ used below, $1/k_m$ is the inverse mass. The parameter $\alpha$ of the harmonic amplitude equation is an inverse length in both entries, and it writes them as $k_E$ and $k_m$. Here $k_E=E/(\frac{m\,c^{2}}{k_m})$ is the energy length.

The field is one element $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$ of $\mathbb{B}$, and its two parts carry the two values of the subscript. Each line multiplies the part with one value by the gradient and pairs it with the part with the other value; the mass is the term that carries the value across, and it is the only such term in the equation.

At $m=0$, that is $k_m=0$, the pair decouples into two one-sided equations, one for each value:

$$
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = 0,
\qquad
\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = 0 .
$$

A field with a single value obeys one of them. The equation with the plus value, $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R}=0$, is the one written $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp}}=0$ in the massless sections below, and the equation with the minus value is its quaternion conjugate. Each member is first order, both are linear in the field, and the mass couples the two parts. Applying $\tilde{\nabla}^{\natural}$ to the first member and using the second gives

$$
\tilde{\nabla}^{\natural}\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = \Box\tilde{Ξ}_{\mathrm{sp},R} = k_m\,\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = \tilde{Ξ}_{\mathrm{sp},R}\,k_m^{2},
\qquad\text{that is}\qquad
\left(\Box - k_m^{2}\right)\tilde{Ξ}_{\mathrm{sp},R} = 0
$$

the Klein–Gordon operator in this normalization. The same holds for $\tilde{Ξ}_{\mathrm{sp},L}$. So each part obeys the Klein–Gordon equation. The factorization is the one the algebra supplies; no matrix square is used and no second metric enters.

### The Two Values of the Subscript

The subscript that names the part, and the two letters $L$ and $R$, are fixed in *Matrix Representations Conventions*, §*The Legacy Pauli Gamma Formulation*; the side that reads it is *Operator Chirality on the Biquaternion Algebra*, §*The Subscript on an Element*. The field of this article is one element that carries both parts, and nothing is introduced to hold them.

A single element of $\mathbb{B}$ carries four complex numbers, which is the count the four-component column of the matrix formulation carries. The difference is not the count but the object: there the four numbers are entries of a column that a matrix multiplies, and here they are the coefficients of one element that the algebra multiplies. No index, no column and no basis enters the statement.

### Chirality

**The notion is a side, and the frame supplies it.** The derivative of this article multiplies the field on the left; the frame has a fifth cell that multiplies on the right, its volume cell, and that cell is what the corpus calls the operator chirality of the frame (*Operator Chirality on the Biquaternion Algebra*, §*The Chirality Operator of the Frame*). The cell is named here and not computed, and its arrays are printed in *The Legacy Pauli Gamma Formulation*, where the older display is compared. No other object is introduced to say which part is which.

**The rules of the value.** A product takes the value of its right factor, and left multiplication keeps it. The derivative therefore carries each part into a part of the same value, and nothing that multiplies on the left acts on the value at all.

**The physical interpretation.** The two parts are the left-handed and the right-handed parts of the fermion field. At $m=0$ each part carries one helicity: a plane wave of one value has one helicity, a plane wave of the other has the other, and the mass is the term that couples the two. That interpretation is used in §*Plane-Wave Solutions* and again in §*The Harmonic Field: Two Projections, and the Helicity Reading*, both below.

**A limit, stated once.** Left multiplication cannot tell the two parts apart. For any element $\tilde a$ the product $\tilde a\tilde{Ξ}_{\mathrm{sp},L}$ carries the value $L$ and $\tilde a\tilde{Ξ}_{\mathrm{sp},R}$ carries the value $R$, so a gauge action by left multiplication acts on the two parts in the same way, and the two parts are two copies of one object. The inequivalence of a left-handed field and its conjugate is a fact about a larger object and not about this algebra, and nothing in this article asserts it.

## The Algebra and the Gradient

### The Gradient Is an Element

The gradient is an element of $\mathbb{B}$, and an element acts on the algebra by multiplication. Nothing about that action needs a basis: the equation says what the gradient does to the field, and the answer is another element. A basis enters only when numbers are wanted, and then the choice of basis is a coordinate choice that changes nothing in the operator — two bases give two lists of numbers for one action. The equation of this article is written in neither.

The place where a basis does make a difference is the diagonal. An operator is diagonal in a basis when each basis element is carried into a multiple of itself. Of the sixteen cells of the coefficient basis exactly four are diagonal, the four squares $e_te_t$, $\vec e_x\vec e_x$, $\vec e_y\vec e_y$, $\vec e_z\vec e_z$: the square of a unit is a scalar, so it multiplies every basis element by that scalar, and no other cell carries all four basis elements into multiples of themselves. Each spatial unit is diagonal in exactly one cell, its own square, so a permutation of the three spatial units permutes the last three members of the set and leaves the set unchanged.

The set therefore names no direction. An axis is not a property of the algebra; it is a property of the frame that is declared, and the frame and its metric are fixed in *Frame and Metric Conventions*. This article states the point once, here, and does not use it again: the equation names no unit and no axis, and the five cells printed in *The Legacy Pauli Gamma Formulation* are printed there for comparison with the older display.

### An Explicit Dictionary with Conjugation in the Mass Term

The route used so far is the algebra's own: one element, two values, the mass between them. There is a second route, due to V. V. Kravchenko (1995), which is a **change of variable** rather than a decomposition. It writes the whole Dirac equation as a single equation on $\mathbb{B}$ in which the derivatives act from the left and the mass from the right, and its interest for this article is that its mass term carries complex conjugation.

**The equation.** In the source's normalization the spatial derivative is the element

$$
\vec\nabla := \sum_{k=x,y,z}\vec e_k\,\frac{\partial}{\partial R_k},
\qquad
\vec\nabla^2 = -\Delta ,
\qquad
\lvert\vec\nabla\rvert^2 = \Delta ,
$$

the spatial gradient of *Operator and Calculus Conventions*, §*The Gradient*, which is the vector part of $\tilde\nabla$ and is therefore pure and arrowed, with real quaternion coefficients on the material sector. The equation is

$$
\mathcal{N}F := \Bigl(\frac{i}{c}\frac{\partial}{\partial r'_t} + \vec\nabla\Bigr)F - i\,\overline{F}\,\vec e_z\,k_m = 0,
$$

where $\overline{\cdot}$ is the coefficient conjugation of *Algebra and Element Conventions*, the corpus's glyph for the map the source writes $C$, applied to the coefficients of the field, and the unit $\vec e_z$ multiplies the result from the right. The corpus's spatial operator of *Biquaternion Regular Functions* is $D=i\vec\nabla$, with $D^2=\Delta$; the two differ by the fixed central imaginary, and this section keeps $\vec\nabla$, because that is the normalization in which the mass term of the equation above is real. A reader who changes normalization in the middle of a computation changes the operator.

**Three kinds of action in one operator.** The display mixes a left action, an antilinear map and a right action, and the mixture is the dictionary's content rather than a slip of notation. The time derivative and $\vec\nabla$ act from the left; the bar acts on the coefficients, has no side, and is the antilinear entry; the multiplication by $\vec e_z$ acts from the right. How such a combination is printed is fixed by the conventions (*Product and Form Conventions*, both copies): the side is carried by position and never by a mark. The mass term is therefore $\overline{F}\,\vec e_z$ and not a product of two operator letters: the bar is applied to the field and the unit multiplies what comes out. Because $\vec e_z$ has real coefficients, the bar commutes with that multiplication, $\overline{F\vec e_z}=\overline{F}\,\vec e_z$, so the source's order and the corpus's are one operator.

**Why the $1/c$.** The operator adds an inverse time to an inverse length, and only $\frac{i}{c}\partial/\partial r'_t$ is an inverse length like $\vec\nabla$, and the mass term carries that same unit by the identification made at the box. The source prints the equation at $c=1$, where the first factor is $i\partial/\partial r'_t$.

**One sector, two coordinates.** The operator is read on the material sector $\mathbb{B}_{\Phi}$, where $Q_t=i c r'_t$ and $Q_k=q_k$. There $R_t=i c r'_t$ is the complex time coordinate, so $\partial/\partial r'_t$ differentiates with respect to the physical time and $\partial/\partial R_k$ is the physical spatial derivative: the two symbols name the two coordinates of one sector and do not mix two conventions. Since $\partial/\partial R_t=-\frac{i}{c}\,\partial/\partial r'_t$,

$$
\frac{i}{c}\frac{\partial}{\partial r'_t} = -\frac{\partial}{\partial R_t},
\qquad\text{so that}\qquad
\frac{i}{c}\frac{\partial}{\partial r'_t} + \vec\nabla = -\tilde{\nabla}^{\natural},
$$

the time term of the gradient carrying $e_t$, the identity of the algebra, so that the three symbols are one operator.

The free part of $\mathcal{N}$ is therefore the **conjugate** gradient and not the gradient: the free equation is the member with the minus value, $\tilde{\nabla}^{\natural}F=0$, written on the whole algebra, and the other member is its conjugate. With the mass term moved to the right the equation reads

$$
\tilde{\nabla}^{\natural}F = -i\,\overline{F}\,\vec e_z\,k_m,
$$

which has the shape of the corpus's $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\,\tilde{Ξ}_{\mathrm{sp},R}$ with the second field read as $-i\,\overline{F}\,\vec e_z$: a conjugation and a fixed direction, and nothing else. That is the operator-theoretic content of the two-sidedness — the dictionary reaches the member with the minus value, and the second field of that member is the conjugate of the first. The normalization with the imaginary-time derivative is not used for the operator itself, and the reason is the reality of the operator $R$ below: the factor $-\frac{i}{c}$ that carries $\partial/\partial r'_t$ into $\partial/\partial R_t$ would put the central imaginary into every coefficient of $R$ and take away the property that makes $R$ real.

Following the source, $i_1,i_2,i_3$ denote the quaternion units; this article writes them $\vec e_x,\vec e_y,\vec e_z$ and keeps the source's $i_k$ only where it quotes the source. The product $i\,i_k$ is the scalar imaginary times a quaternion unit, not a square: $i^2=-1$, while $(i\,i_k)^2=i^2i_k^2=+1$.

**Which conjugation.** The bar of the equation is the algebra's **coefficient conjugation** $\bar{\cdot}$, not the algebra's real structure $\flat$. They are different maps with different fixed spaces, and the corpus keeps them apart (*Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*, and the convention remark of *The Massive Case* above). The distinction has teeth here, because the dictionary's mass term is antilinear and the framework has already found that not every antilinear mass term is admissible. The retired single-field equation $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp}} = k_m\,\tilde{Ξ}_{\mathrm{sp}}^{\flat}$ fails on the dispersion, whereas the Lanczos form $\tilde{\nabla}D = D^{*}i\vec{\nu}\,k_m$ of *The Lanczos Route: Maxwell with Feedback* is exact. Kravchenko's mass term is of the second kind: its conjugation is $\bar{\cdot}$, and it is accompanied by a right multiplication by a spatial direction, its $\vec e_z$ standing where the Lanczos unit vector $\vec{\nu}$ stands.
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
R[F] := \Bigl(\frac{i}{c}\partial/\partial r'_t + \vec\nabla\Bigr)F\;e_{+} + \Bigl(-\frac{i}{c}\partial/\partial r'_t + \vec\nabla\Bigr)F\;e_{-} - F\,\vec e_y\,k_m
$$

is related to $\mathcal{N}$ by a change of variable on each side. The conjugation has not been removed, only moved: it sits in the two factors that surround the operator, and the operator itself is free of it.

**The reality of $R$, recomputed.** The two projections collapse, because $e_{+}+e_{-}=e_t$ and $e_{+}-e_{-}=i\,\vec e_x$. Writing $A=\frac{i}{c}\,\partial F/\partial r'_t$ and $B=\vec\nabla F$, the first two terms give

$$
(A+B)e_{+} + (-A+B)e_{-} = B\,(e_{+}+e_{-}) + A\,(e_{+}-e_{-}) = B + A\,i\vec e_x ,
$$

and the step $i\cdot i=-1$ turns the second into the right multiplication by $-\vec e_x$. The operator is therefore

$$
R[F] = \vec\nabla F - \frac{1}{c}\frac{\partial F}{\partial r'_t}\,\vec e_x - F\,\vec e_y\,k_m ,
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
\partial/\partial r'_t|F|^2 = -\frac{m\,c}{k_m}\bigl[(\vec\nabla F^{\natural})F + \bar{F}\,(\vec\nabla F)\bigr],
\qquad |F|^2 := \langle  F\rangle_{*}  = \sum_{\mu=0}^{3}|F_\mu|^2,
$$

printed there in its own normalization, at $c=1$ and with $\frac{m\,c}{k_m}$ restored, and with the source's $\dagger$ read as the quaternionic conjugate $\natural$ and its $*$ as the coefficient bar. The equation of this section carries no $\frac{m\,c}{k_m}$, and the same pair gives the law in the units of this section,

$$
\frac{1}{c}\frac{\partial}{\partial r'_t}\bigl(FF^{\natural}\bigr)
= F\,\vec e_x\,(\vec\nabla F)^{\natural} - (\vec\nabla F)\,\vec e_x\,F^{\natural},
$$

which is the quaternionic form of the current-conservation equation of the Dirac field: the time derivative of the density on the left, and on the right the two terms that carry the spatial derivative, with the direction $\vec e_x$ of the operator in the place the source's $M_{i_1}$ occupies. Writing $A=F\,\vec e_x\,(\vec\nabla F)^{\natural}$, the second term is $A^{\natural}$, so the right side is $A+A^{\natural}$ and is scalar; the mass cancels between the two terms, so the law is the same at $m=0$, and it was checked at residual $1.1\times10^{-15}$ over $100$ random real fields and again symbolically on a polynomial field. The density is the modulus $FF^{\natural}$. On the real representative it coincides with the Hermitian norm, $FF^{\natural}=\langle F\rangle_{*}=\sum_\mu F_\mu^2$, and that shared value is indefinite: what the pair conserves is a density, not a probability density. The definite Hermitian norm carries the probability reading only on the complex field, where the two norms differ.

### The One-Sided and the Two-Sided Equation

The article now carries two equations, and they must not be read as one. The corpus's own equation is **one-sided**: it is the chiral pair in which the gradient acts by left multiplication and the mass carries the field from one value to the other. Kravchenko's equation is **two-sided**: it is a single equation on $\mathbb{B}$ in which the derivative acts from the left, the mass term acts from the right through $\vec e_z$, and the coefficient conjugation supplies the antilinear part. The two are related by a change of variable, but they are not the same operator, and the table separates them.

| | One-sided equation | Two-sided equation |
|---|---|---|
| the equation | $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R}=k_m\,\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{\nabla}^\natural\tilde{Ξ}_{\mathrm{sp},L}=k_m\,\tilde{Ξ}_{\mathrm{sp},R}$ | $\bigl(\frac{i}{c}\partial/\partial r'_t+\vec\nabla\bigr)F-i\,\overline{F}\,\vec e_z\,k_m=0$, that is $-\tilde{\nabla}^\natural F-i\,\overline{F}\,\vec e_z\,k_m=0$ |
| the action | left, by $\tilde{\nabla}$ and $\tilde{\nabla}^\natural$ | left by the derivative, right by $\vec e_z$ in the mass term, and the coefficient bar |
| the field | one element $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$ of $\mathbb{B}$ | one element $F$ of $\mathbb{B}$ |
| the mass | the term that carries the value across | $-i\,\overline{F}\,\vec e_z\,k_m$: a conjugation together with a direction |
| the subscript | two values, $L$ and $R$ | no subscript, the direction $\vec e_z$ standing in its place |
| the use | the corpus's formulation and its kinematics | the dictionary, the Cauchy theory and the integral representation |

The dictionary is therefore not a second definition of the same equation. It is a change of variable that makes the equation two-sided, and the price of the change is the conjugation in the mass term. The one-sided pair is the definition; the two-sided equation is the form in which the analytic machinery acts.

### The Harmonic Field: Two Projections, and the Helicity Reading

The same source carries the dictionary one step further, to the field that oscillates in time, and that is where the algebra is read physically. For a time-harmonic field of frequency $\omega\in\mathbb{R}$ the general solution is a **sum of two exponentials with opposite signs**,

$$
F = \tfrac12\,f\,\bigl(e_t+\alpha/\sqrt{\alpha^2}\bigr)\exp(i\omega r'_t) + \tfrac12\,f\,\bigl(e_t-\alpha/\sqrt{\alpha^2}\bigr)\exp(-i\omega r'_t),
$$

where the two factors $\tfrac12(e_t\pm\alpha/\sqrt{\alpha^2})$ are complementary projections built from the unit in the direction of the parameter, and they multiply the field on the right; and $f$ is a solution of the shifted amplitude equation $\vec\nabla f+f\alpha=0$. The pair of signs of the frequency and the pair of right multiplications are one pairing: each half of the field is a projected shifted equation.

**The interpretation the source attaches to it.** The source states that its two projections are *closely related to particle helicity*, and on that interpretation the two halves of the harmonic field are the two helicity components, the half with the plus sign of the frequency being the **neutrino** and the other the **antineutrino**. In the massless case the equation they come from is

$$
\frac{i}{c}\,\partial F/\partial r'_t + \vec\nabla F = 0,
$$

which for a field equal to its own conjugate is a known reformulation of the vacuum Maxwell equations, attributed by the source to Imaeda [1976]. The algebra thus supplies the two helicities in one object: the two complementary projections of the parameter, one for each sign of the frequency, with the parameter's direction in place of a vacuum direction.

**Which pair.** The two projections above are **not** the two values. The value is a property of the element, $L$ or $R$, and no parameter enters it; the two projections above are built from the parameter $\alpha$, so they carry the frequency and the mass of the field. Helicity and the value coincide only for a massless field; at $m\neq0$ the two readings of the one field are genuinely different, and the neutrino or antineutrino identification is a statement about the helicity pair and not about the values. The corpus records the identification as the source's interpretation rather than as a derivation: what the algebra contributes to it is the shape — two complementary projections, one for each sign of the frequency — and the name *neutrino* is the source's, not the algebra's.

### The Integral Representation of the Harmonic Field

Removing the conjugation is what buys the analytic theory back, and for the harmonic field the source's announcement states what is bought. The time-harmonic amplitude obeys the first-order equation

$$
\vec\nabla f + f\alpha = 0,\qquad \alpha=-i\omega\,\vec e_x ,
$$

which is the shifted equation in the source's normalization, at $c=1$. The parameter is an inverse length, as $\vec\nabla$ is, so the frequency enters it as $\omega/c$: the general-units form of this $\alpha$ is $-i\frac{\omega}{c}\vec e_x$, the inverse length that §*The Mass Shell as the Condition on the Dirac–Maxwell Correspondence* prints as $k_E$. The corpus's *Biquaternion Regular Functions* writes it with $D=i\vec\nabla$, where the same equation reads $Df+f(i\alpha)=0$. The source writes the same amplitude equation in its matrix form, with an operator it calls $D_\omega$; that operator and $\vec\nabla+\cdot\,\alpha$ carry the same kernel, so the analysis is the same. The source derives its results in this massless case — the case it calls the neutrino — while the massive parameter $\alpha = -\bigl(i\omega \vec e_x + k_m \vec e_y\bigr)$, in the same $c=1$ units, is the one carried by the boundary-value treatment of the bag in *Confinement and the Loss of Partonic Information in Biquaternionic Form*.

With that one remark the three theorems of the hyperholomorphic theory hold for the harmonic field in the same shape as for the electromagnetic field of the companion *The Time-Harmonic Maxwell Operator and the Quaternionic Cauchy Integral*: a **Cauchy integral formula**, with the Cauchy-type operator $K_\omega$ of the amplitude equation acting as the identity on a field of the kernel that is continuous up to the boundary; the **Plemelj–Sokhotski formulas**, which express the one-sided boundary limits of $K_\omega f$ for Hölder data through the principal-value integral; and a **boundary-value criterion**, that a Hölder function on the boundary is the boundary value of a solution of the amplitude equation if and only if it is its own $K_\omega$ image. This is the refund of the price recorded in *An Explicit Dictionary with Conjugation in the Mass Term*: the conjugation obstructs the Cauchy kernel on the two-sided image, and changing the variable back hands the kernel over. It is also the whole content of the second half of the source's title, and it is the Dirac half of the source's thesis — the same parametric equation, at one value of its parameter, is the time-harmonic Maxwell system and, at another, the time-harmonic Dirac system, so that one Cauchy theory serves both. The Dirac case is an instance of the general boundary-value criterion $P_\alpha f = f$ of *Biquaternion Regular Functions*; what the physics register adds to the general statement is the identification of the parameter and the fields.

## Relativistic Kinematics in Biquaternionic Form

Before the solutions are written, it is useful to collect the basic relativistic kinematic quantities in biquaternion form. These are the objects that appear in the Dirac equation and its solutions, and they are established physics rewritten in biquaternion notation.

### The Four-Position

The **four-position biquaternion** is

$$
\tilde R_\Phi = i c r'_t\, e_t + r_x\, \vec e_x + r_y\, \vec e_y + r_z\, \vec e_z,
$$

with $Q_t = i c r'_t$. The scalar part is the complex time coordinate, and the vector part is the ordinary spatial position.

### The Invariant Interval

The invariant interval is the square of the biquaternion displacement:

$$
ds^2 = \langle d\tilde R_\Phi\rangle_{\natural} = d\tilde R_\Phi\,d\tilde{R}_\Phi^{\natural} = (ic\,dr'_t)^2 + dr_x^2 + dr_y^2 + dr_z^2 = -c^2 d{r'_{t}}^2 +dr_x^2+dr_y^2+dr_z^2.
$$

This is the biquaternion form of the Minkowski interval. The Lorentzian signature emerges algebraically from $i^2 = -1$, as discussed in the companion article on the $i c r'_t$ convention.

### The Four-Velocity

The **four-velocity biquaternion** is

$$
\tilde{V} = \gamma(ic\, e_t + \vec v),
$$

where $\vec v$ is the ordinary three-velocity of the particle and

$$
\gamma = \frac{1}{\sqrt{1 - \vec v^2/c^2}}
$$

is the Lorentz factor. The four-velocity satisfies the **normalization condition**

$$
\tilde{V}\tilde{V}^{\natural} = \gamma^2\big(-c^2 + \vec v^2\big) = -c^2.
$$

This is the biquaternion form of the standard relativistic normalization $\sum_\mu\varepsilon_\mu v_\mu v_\mu = -c^2$.

### The Four-Momentum

The **four-momentum biquaternion** is

$$
\tilde{P} =m\,\tilde{V} =m\,c\,\gamma\left(i\,e_t + \frac{\vec v}{c}\right) = i\,\frac{E}{c}\, e_t + \vec p,
$$

which is $m\tilde{V}$, because $m\,c=mc$; here $E =m\,c^{2}\,\gamma$ is the relativistic energy and $\vec p =m\,\gamma\,\vec v$ is the relativistic three-momentum. The scalar part of $\tilde{P}$ is $iE/c$, and the vector part is $\vec p$.

The four-momentum satisfies the **mass-shell relation**

$$
\tilde{P}\tilde{P}^{\natural} =m^{2}\,\tilde{V}\,\tilde{V}^{\natural} = -m^{2}\,c^{2}.
$$

This is the biquaternion form of the standard relativistic energy-momentum relation

$$
E^2 = \vec p^2 c^2 +m^{2}\,c^{4},
$$

which is obtained by expanding $-m^{2}\,c^{2}= -(E/c)^2 + \vec p^2$.

### The Four-Acceleration and Four-Force

The **four-acceleration biquaternion** is $\tilde{A} = d\tilde{V}/d\tau$, where $\tau$ is the proper time. The **four-force biquaternion** is $\tilde{\mathcal F}_{\mathrm{frc}} = d\tilde{P}/d\tau =m\,\tilde{A}$. The four-acceleration satisfies $\tilde{A}\tilde{V}^{\natural} + \tilde{V}\tilde{A}^{\natural} = 0$, which is the biquaternion form of the orthogonality condition $\sum_\mu\varepsilon_\mu a_\mu v_\mu = 0$.

### Summary of Relativistic Kinematics

| Quantity | Biquaternion | Constraint |
|---|---|---|
| Four-position | $\tilde R_\Phi = i c r'_t\, e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ | — |
| Interval | $ds^2 = \langle d\tilde R_\Phi\rangle_{\natural} = d\tilde R_\Phi\,d\tilde{R}_\Phi^{\natural}$ | $= -c^2 d{r'_{t}}^2 +dr_x^2+dr_y^2+dr_z^2$ |
| Four-velocity | $\tilde{V} = \gamma(ic\, e_t + \vec v)$ | $\tilde{V}\tilde{V}^{\natural} = -c^2$ |
| Four-momentum | $\tilde{P} =m\,\tilde{V}$ | $\tilde{P}\tilde{P}^{\natural} = -m^{2}\,c^{2}$ |
| Four-force | $\tilde{\mathcal F}_{\mathrm{frc}} = d\tilde{P}/d\tau$ | — |

These kinematic relations are the biquaternion form of standard relativistic mechanics, and they are the natural setting for the biquaternionic Dirac equation.

## The Biquaternionic Dirac Equation

### Statement

The equation is the chiral pair of *The Equation in the Algebra*. Let $\tilde{Ξ}_{\mathrm{sp}}$ be a field with values in $\mathbb{B}$, written as a pair of parts $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$, one for each value of the subscript. For a field of mass $m$ the **biquaternionic Dirac equation** is

$$
\boxed{\;
\begin{aligned}
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} &= k_m\,\tilde{Ξ}_{\mathrm{sp},L},\\[4pt]
\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} &= k_m\,\tilde{Ξ}_{\mathrm{sp},R}.
\end{aligned}
\;}
$$

It is **linear** in $\tilde{Ξ}_{\mathrm{sp}}$ and **off-diagonal in the value**: each line holds the part with one value on the left and the part with the other value on the right. At $m=0$ it decouples into two one-sided equations,

$$
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R}=0,
\qquad
\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=0,
$$

one for each value; a field with a single value obeys one of them. The two lines equate parts of different values because the mass is a pairing of the two parts and not a multiplication: it is the only term of the equation that carries the value across, and the two lines are equalities of elements, not of matrices. The Klein–Gordon consequence for each part is derived in *The Equation in the Algebra*.

A **single-string form** of the same pair is recorded in *The Chiral Algebra of Biquaternions and the Cyclic Representation of the Dirac Equation*. Writing the wave function in the light-cone coordinates and using that article's outer and inner products, the chiral pair becomes one expression, $F^- \odot \bar D + D \otimes F^+ = im\overset{\curvearrowleft}{F}$, in which the two products carry the two values and the cyclic conjugation $\overset{\curvearrowleft}{\phantom{x}}$ carries the mass term. The equivalence of that expression with the chiral pair is verified row by row there. The pair above remains the definitional home of the biquaternionic Dirac equation; the single-string form is a repackaging in a different product, not a different equation.

### The Massless Case

For a single value the massless equation is one-sided. The equation with the plus value, $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R}=0$, is identical in form to the **homogeneous biquaternion Maxwell equation** for the field-strength biquaternion $\tilde{F}$:

$$
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = 0 \quad \text{(plus value)}, \qquad \tilde{\nabla}\tilde{F} = 0 \quad \text{(source-free Maxwell)}.
$$

The left-handed equation is the quaternion conjugate, $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=0$; it has the same form with $\tilde{\nabla}^{\natural}$ in place of $\tilde{\nabla}$. The full massless Dirac field is the pair of the two, not the single equation. The solutions are also the same in form: the kernel of the biquaternionic gradient consists of plane waves, spherical waves, and cylindrical waves (as in the companion article on Maxwell). The **physical interpretation** differs: $\tilde{Ξ}_{\mathrm{sp}}$ is a fermion field (spin-$\frac{1}{2}$), and $\tilde{F}$ is a boson field (spin-1).

The structural identity of the two equations is the algebraic content of the statement that both fields are read in the same algebra. The difference is not in the operator but in the object it acts on and in the value of the field: the Maxwell field-strength biquaternion lives in the vector part of the algebra, and the Dirac field is a general element carrying a value of the subscript.

### The Massive Case

The massive equation is the chiral pair boxed in *Statement*. The mass term is **linear** in the field and acts between the two parts: it is the biquaternion transcription of the mass term of the matrix Dirac equation, and it is what couples the two values.

The coupling has to change the value. Left multiplication by an element of $\mathbb{B}_{\mathbb{R}}$ preserves the value of the field: a product takes the letter of its right factor, and the left multiplier does not touch it (*Matrix Representations Conventions*, §*The Bridge to the $4\times4$ Displays*). So no left multiplication carries one part into the other. The mass is the term that does. It is a pairing of the two parts and not a multiplication, it is not $\mathbb{B}$-linear, and that is why it can couple them and why it is the only term of the equation that changes the value. A right multiplication by a unit that commutes with the axis — the time unit or the axis unit itself — is a different object again: it acts inside one part, leaves the value alone, and carries a direction; a right multiplication by either of the other two units exchanges the two values. That is why the two-sided form of *An Explicit Dictionary with Conjugation in the Mass Term* needs the coefficient bar beside the direction, and neither of the two alone.

**A remark on the anti-Hermitian conjugation $\flat$.** The algebra carries, besides the quaternion conjugate and the Hermitian conjugation ${}^{*}$, a further antilinear involution:

$$
\tilde{Ξ}_{\mathrm{sp}}^{\flat} = -\tilde{Ξ}_{\mathrm{sp}}^* = -\overline{\tilde{Ξ}_{\mathrm{sp}}^{\natural}},
$$

the **anti-Hermitian conjugate** $\flat = -{}^{*}$. It is a $\mathbb{C}$-**antilinear** involution, and it is order-reversing with a twist,

$$
\left(\tilde{Q}_2\tilde{Q}_1\right)^\flat = -\,\tilde{Q}_1^\flat\tilde{Q}_2^\flat ,
$$

the sign being the only difference from an ordinary anti-automorphism, and it acts by a sign on the two Hermitian sectors,

$$
\tilde{Ξ}_{\mathrm{sp}}^{\flat} = +\tilde{Ξ}_{\mathrm{sp}}\ \ (\tilde{Ξ}_{\mathrm{sp}}\in\mathbb{B}_{\Phi}), \qquad \tilde{Ξ}_{\mathrm{sp}}^{\flat} = -\tilde{Ξ}_{\mathrm{sp}}\ \ (\tilde{Ξ}_{\mathrm{sp}}\in\mathbb{B}_{\Psi}),
$$

so that the **fixed space of $\flat$ is the anti-Hermitian sector $\mathbb{B}_{\Phi}$**.

The convention is worth a remark, because the more familiar one takes the *Hermitian* part as the real one, and here the *anti*-Hermitian part plays that role. The two differ only by the central factor $i$: anti-Hermitian elements are $i$ times Hermitian ones, and anti-Hermitian generators are the standard choice for the Lie algebra of a $*$-unitary group (in the companion quantum article the Lie algebra of the $*$-unitary group is $\mathbb{B}_{\Phi}$). What is unusual here is not the sign convention as such, but that it is applied to the *field* rather than to the generators: it is $\mathbb{B}_{\Phi}$ that is fixed, and that is what makes $\mathbb{B}_{\Phi}$ the framework's "material" sector (the companion article *The Material Sector: Four-Vectors, Interval and Lorentz Action* takes $\mathbb{B}_{\Phi}$ as the fixed space of $\flat$).

The map $\flat$ is the algebra's **real structure**, and its shape is that of a charge-conjugation (Majorana) pairing: it relates the field to its own conjugate. It is *not* the mass term. A coupling built on $\flat$ pairs $\tilde{Ξ}_{\mathrm{sp}}$ with $\tilde{Ξ}_{\mathrm{sp}}^{\flat}$ rather than relating two independent chiralities, and because $\flat$ is antilinear such a coupling is not invariant under the continuous central phase — precisely the two differences between a Majorana-type pairing and an ordinary Dirac mass. The single-field equation $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp}} = k_m\,\tilde{Ξ}_{\mathrm{sp}}^{\flat}$ is a real-linear equation of that type; it is a different equation from the one studied here, and its central-phase plane waves sit on the *spacelike* locus, not on the physical mass shell. The map $\flat$ is retained in the framework for what it is genuinely for — conjugation, the $\mathbb{B}_{\Psi}/\mathbb{B}_{\Phi}$ split, the trace and bilinear pairings, and the real-form question of Dirac versus Majorana fermions, which the companion articles on chirality, the neutrino, and the CPT theorem develop. In the present article $\flat$ is used only for conjugation, never as the mass.

**The associated Klein–Gordon equation.** Applying $\tilde{\nabla}^{\natural}$ to the first member of the pair and substituting the second gives $\Box\tilde{Ξ}_{\mathrm{sp},R}=\tilde{Ξ}_{\mathrm{sp},R}\,k_m^{2}$, and likewise for $\tilde{Ξ}_{\mathrm{sp},L}$. With $\frac{m\,c}{k_m}$ and $c$ restored, each chiral component satisfies

$$
\left(\Box - k_m^{2}\right)\tilde{Ξ}_{\mathrm{sp},L,R} = 0 ,
$$

in agreement with the companion article on the Klein–Gordon equation. This is the biquaternion form of the statement that the square of the first-order operator is the Klein–Gordon operator.

## Plane-Wave Solutions

### Massless Plane Waves

Plane-wave solutions of the right-handed massless equation are

$$
\boxed{\;\tilde{Ξ}_{\mathrm{sp}}(\tilde R_\Phi) = \tilde{Ξ}_{\mathrm{sp},0} \exp\!\left(i\,\mathrm{Sc}\!\left(\tilde{P}\tilde{R}_\Phi^{\natural}\right)\frac{k_m}{m\,c}\right)
= \tilde{Ξ}_{\mathrm{sp},0}\,\exp(\,i(\vec k\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)-\omega r'_t))\;},
$$

where $\tilde{Ξ}_{\mathrm{sp},0} \in \mathbb{B}$ is a constant biquaternion, $\frac{k_m\,\tilde{P}}{m\,c}= i k_0 e_t + \vec e_x k_1 + \vec e_y k_2 + \vec e_z k_3$ (with $k_0 = \omega/c$) is the wave biquaternion, and $\tilde R_\Phi = e_t (i c r'_t) + \vec e_x r_x + \vec e_y r_y + \vec e_z r_z$ is the four-position biquaternion. The scalar part $\mathrm{Sc}(\tilde{P}\tilde{R}_\Phi^{\natural})/\hbar = \vec k\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) - \omega r'_t$ is real, so the exponent $i\,\mathrm{Sc}\frac{k_m\,\tilde{P}\,\tilde{R}_{\Phi}^{\natural}}{m\,c}$ is a purely imaginary central element; the exponential therefore commutes with $\tilde{Ξ}_{\mathrm{sp},0}$ and differentiates to left multiplication by $\frac{k_m\,i\,\tilde{P}}{m\,c}$,

$$
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp}} =\frac{k_m\,i\,\tilde{P}\,\tilde{Ξ}_{\mathrm{sp}}}{m\,c},
$$

so the equation $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp}} = 0$ becomes

$$
\tilde{P}\tilde{Ξ}_{\mathrm{sp},0}/\hbar = 0,
$$

i.e., the polarization biquaternion $\tilde{Ξ}_{\mathrm{sp},0}$ is annihilated by the wave biquaternion $\frac{k_m\,\tilde{P}}{m\,c}$. This is the momentum-space massless equation in the algebra; its kernel has complex dimension two, the two spin states of the field with this value. The two values are the two helicities, so the full massless field is the pair of this equation and its conjugate.

Nonzero solutions of $\tilde{P}\tilde{Ξ}_{\mathrm{sp},0}/\hbar = 0$ exist only when $\frac{k_m\,\tilde{P}}{m\,c}$ is a zero divisor in $\mathbb{B}$, that is, when $\frac{k_m\,\tilde{P}}{m\,c}$ is null: $\frac{k_m^{2}\,\tilde{P}\,\tilde{P}^{\natural}}{m^{2}\,c^{2}}= 0$, equivalently $k_0^2 = \|\vec k\|^2$, the massless dispersion relation. In that case the kernel is a two-dimensional complex vector space, the two spin states; for non-null $\frac{k_m\,\tilde{P}}{m\,c}$ the kernel is trivial.

### Massive Plane Waves

For the massive equation a single central-phase plane wave,

$$
\tilde{Ξ}_{\mathrm{sp}}(\tilde R_\Phi) = \tilde{Ξ}_{\mathrm{sp},0} \exp\!\left(i\,\mathrm{Sc}\!\left(\tilde{P}\tilde{R}_\Phi^{\natural}\right)\frac{k_m}{m\,c}\right) = \tilde{Ξ}_{\mathrm{sp},0}\,\exp(i\theta), \qquad \theta = \vec k\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) - \omega r'_t,
$$

does solve the pair, with one polarization biquaternion per value, $\tilde{Ξ}_{\mathrm{sp},0} = \tilde{Ξ}_{\mathrm{sp},0}^L + \tilde{Ξ}_{\mathrm{sp},0}^R$. Differentiating as in the massless case, $\tilde{\nabla}$ acts on $\exp(i\theta)$ as left multiplication by $\frac{k_m\,i\,\tilde{P}}{m\,c}$ and $\tilde{\nabla}^{\natural}$ acts on it as left multiplication by $\frac{k_m\,i\,\tilde{P}^{\natural}}{m\,c}$, so the chiral pair becomes the momentum-space system

$$\frac{k_m\,i\,\tilde{P}\,\tilde{Ξ}_{\mathrm{sp},0}^{R}}{m\,c}= k_m\,\tilde{Ξ}_{\mathrm{sp},0}^L,\frac{k_m\,i\,\tilde{P}^{\natural}\,\tilde{Ξ}_{\mathrm{sp},0}^{L}}{m\,c}= k_m\,\tilde{Ξ}_{\mathrm{sp},0}^R .
$$

Eliminating $\tilde{Ξ}_{\mathrm{sp},0}^L$ gives

$$\frac{k_m^{2}\,\tilde{P}\,\tilde{P}^{\natural}}{m^{2}\,c^{2}}\,\tilde{Ξ}_{\mathrm{sp},0}^R = -k_m^{2}\,\tilde{Ξ}_{\mathrm{sp},0}^R ,
$$

so a nonzero solution requires the **mass-shell condition**

$$\frac{k_m^{2}\,\tilde{P}\,\tilde{P}^{\natural}}{m^{2}\,c^{2}}=-k_m^{2},
$$

i.e., $-k_0^2 + \|\vec k\|^2 = -k_m^{2}$, which is the standard mass-shell relation $k_0^2 = \|\vec k\|^2 + k_m^{2}$ (with $k_0 = c\,k_E c$). This is the biquaternion form of the standard relativistic energy-momentum relation $E^2 = \vec p^2 c^2 +m^{2}\,c^{4}$ (with $\vec p =\frac{m\,c\,\vec k}{k_m}$), the same shell as the four-momentum kinematics of the preceding section. The two signs of $k_0$ are the two frequency branches — the particle and the antiparticle — and with the two spin states they give the four solutions that the field carries.

### The Field as the Gradient of a Scalar Potential

The completion of the next section has a shifted form, and the shift is the operator of the companion *The Biquaternion D'Alembertian and Its Green's Functions*. With the **shifted gradient** $\tilde{\nabla}_\kappa = \tilde{\nabla} + \kappa$,
$$
\tilde{\nabla}_\kappa\tilde{\nabla}^{\natural}_\kappa = \Box + 2\kappa\,\partial/\partial R_t + \kappa^2 ,
$$
because the two spatial parts cancel in the sum of the operator and its conjugate, $\tilde{\nabla}+\tilde{\nabla}^{\natural}=2e_t\partial/\partial R_t$. A **scalar** solution of that operator therefore produces a field of the algebra,
$$
\left(\Box + 2\kappa\,\partial/\partial R_t + \kappa^2\right) u = 0
\quad\Longrightarrow\quad
\tilde{\nabla}_\kappa\left(\tilde{\nabla}^{\natural}_\kappa u\right) = 0 ,
$$
and the field is the shifted conjugate gradient of a potential: one element of $\mathbb{B}$ built from another by differentiation, with no column and no second carrier. At $\kappa = 0$ it is the completion $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp}}$ of the next section, and for $\kappa \neq 0$ it is its shifted form. The source calls the scalar generator a **C-field** and takes the field to be the convolution of $\tilde{\nabla}^{\natural}_\kappa\tilde{Ξ}_{\mathrm{sp},0}$ with it, which is how the same construction produces extended rather than only elementary solutions; the convolution is the one developed in the companion article on distributions.

**Why the elementary field is null.** For the elementary case the potential is a plane wave, $\xi_{\mathrm{scl}}=\exp(i(\vec k\cdot(r_x\vec e_x+r_y\vec e_y+r_z\vec e_z)-\omega r'_t))$, and the field is read off by differentiating it. In the coordinate $Q_t=i c r'_t$ the time derivative is $\partial\xi_{\mathrm{scl}}/\partial R_t=-\omega\xi_{\mathrm{scl}}$ and the three spatial ones are $\partial_k\xi_{\mathrm{scl}}=ik_k\xi_{\mathrm{scl}}$, so
$$
\tilde{\nabla}^{\natural}_\kappa\,\xi_{\mathrm{scl}} = \bigl((\kappa-\omega)\,e_t - i k_x\vec e_x - i k_y\vec e_y - i k_z\vec e_z\bigr)\xi_{\mathrm{scl}} ,
$$
and its quaternion norm is the shifted symbol of the operator,
$$
\left\langle\tilde{\nabla}^{\natural}_\kappa\,\xi_{\mathrm{scl}}\right\rangle_{\natural} = (\omega-\kappa)^2 - \|\vec k\|^2 .
$$
The two lines are one statement in two languages: the norm of the field vanishes exactly when the potential solves the shifted scalar equation, so the field is a zero divisor on the shifted cone, as the massless plane-wave fields of the preceding subsection are on the light cone. The zero-divisor cone of the algebra is the light cone, and the shifted cone is the norm-zero set of the shifted operator. The source normalises its representatives and records separate norm and pseudonorm values for them; the corpus keeps the invariant statement, that the element is null, and the dictionary between the source's mass $m$ and the corpus shift $\kappa$ — $\kappa = -i\,k_m$, so that the source's imaginary mass is a real shift — is the one recorded in the d'Alembertian companion.

**The completion is exhaustive, and the mass takes the place of the shift.** The construction above is not only a way to manufacture examples. In the massive chiral pair the second half is the completion of the first,

$$
\tilde{Ξ}_{\mathrm{sp},L}=1/k_m\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} ,
\qquad
\tilde{Ξ}_{\mathrm{sp},R}=1/k_m\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} ,
$$

so a free Dirac field carries nothing that one part does not already carry, and the consistency of the pair is the Klein–Gordon equation $\Box\tilde{Ξ}_{\mathrm{sp},R}=\tilde{Ξ}_{\mathrm{sp},R}\,k_m^{2}$ of *Klein–Gordon from the Dirac Square in Biquaternionic Form*. The source states the same identity in its own variables, the second half computed from the first by differentiation. One structural difference separates this from the shifted completion above: the shift contributes the first-order-in-time term $2\kappa\,\partial/\partial R_t$ and so moves the cone, whereas the mass contributes a constant and leaves the cone where it is. The mass is not a central shift of the operator — it is the off-diagonal pairing of *The Massive Case* — and what the two share is only the shape of the implication, one half of the field being a gradient of the other.

**The potential is defined only up to a constrained shift.** The map $u\mapsto\tilde{\nabla}^{\natural}_\kappa u$ is not injective. Any $u'$ with $\tilde{\nabla}^{\natural}_\kappa u'=0$ leaves the field unchanged, and such $u'$ are supplied by the scalars: every $\zeta$ solving the shifted scalar equation gives one, $u'=\tilde{\nabla}_\kappa\zeta$, because $\tilde{\nabla}^{\natural}_\kappa\tilde{\nabla}_\kappa=\Box+2\kappa\,\partial/\partial R_t+\kappa^2$. The potential is therefore fixed only up to

$$
u\longmapsto u+\tilde{\nabla}_\kappa\zeta ,
\qquad
\bigl(\Box+2\kappa\,\partial/\partial R_t+\kappa^2\bigr)\zeta=0 ,
$$

which was checked on both branches of the shifted cone. The gauge function is **constrained** by the scalar equation, and that is what separates this freedom from a local phase: no arbitrary function, no connection, no curvature, no gauge boson. What the freedom states is structural, and it is the electromagnetic analogy taken at its word: the field is the invariant object and the scalar is its potential, as the field strength is the invariant object of the Maxwell potential, so that the free Dirac field stands to its Klein–Gordon potential as a strength stands to a potential. The source states the same for the free massive field, whose Dirac field is invariant under a shift of its Klein–Gordon potentials by a solution of the conjugate Dirac equation; under the dictionary $\kappa=-i\,k_m$, that is $m=i\kappa$ at $\hbar=c=1$, that operator is $i\tilde{\nabla}^{\natural}_\kappa$, the shifted conjugate gradient up to the unit $i$, so the corpus records the structure once. The source adds that its alternative, potential-based transformation of the Dirac field is nonlinear on the field and free of two-valuedness under a full rotation. The boundary is worth keeping explicit: that alternative is a solution-generating map, and the linear representation on the algebra, whose two-valuedness *The Spin–Statistics Theorem in Biquaternionic Form* uses, is untouched by it.

## Spherical and Cylindrical Solutions

### Spherical Solutions

Spherical solutions of the biquaternionic Dirac equation can be constructed by the methods of the shifted operator, adapted to the biquaternion algebra. The standard technique is the **completion** of scalar harmonic functions: given a harmonic scalar function on the sphere, the completion produces a biquaternion-valued function that lies in the kernel of the Dirac operator.

The construction is more involved than the corresponding construction for the Maxwell equation, because $\tilde{\nabla}$ is not the operator whose square is the scalar wave operator. One has

$$
\tilde{\nabla}^2 = \frac{\partial^2}{\partial R_t^2} - \Delta + 2\,\frac{\partial}{\partial R_t}\,\vec\nabla ,
$$

a derived form, whose first-order cross term does not vanish, so $\tilde{\nabla}^2 \neq \Box$. It is the **conjugate** gradient that squares to the d'Alembertian, $\tilde{\nabla}\tilde{\nabla}^{\natural} = \Box$, so the completion operator is $\tilde{\nabla}^{\natural}$: for every harmonic scalar function $\tilde{Ξ}_{\mathrm{sp}}$ with $\Box\tilde{Ξ}_{\mathrm{sp}} = 0$, the function $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp}}$ satisfies

$$
\tilde{\nabla}\left(\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp}}\right) = \Box\tilde{Ξ}_{\mathrm{sp}} = 0
$$

and is a solution of the massless Dirac equation. This is the biquaternion form of the completion of the scalar harmonic functions, and it is the reason the spherical solutions are indexed by the scalar spherical harmonics.

For the massless case, the spherical solutions of the biquaternionic Dirac equation are the **completed spherical harmonics**, and they form a basis of the solution space. For the massive case, the construction is more involved: the solution is a combination of the completed spherical harmonics and their anti-Hermitian conjugates, with coefficients determined by the mass-shell condition.

The spherical solutions describe the **angular momentum states** of a relativistic fermion. The quantum numbers $(n, \ell, m)$ correspond to the radial, orbital, and magnetic quantum numbers of the standard hydrogen-like Dirac equation.

### Cylindrical Solutions

Cylindrical solutions are similarly constructed from cylindrical harmonics by the same completion technique. They describe **waveguide modes** of a fermion field in a cylindrical geometry, with the transverse-electric and transverse-magnetic modes corresponding to the two spin states.

## Relation to the Maxwell Equation

### Structural Identity

The massless biquaternionic Dirac equation with the plus value and the homogeneous biquaternion Maxwell equation have the same form:

$$
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = 0 .
$$

The equation with the minus value has the conjugate form, $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = 0$, which is the same equation for the conjugate field. The difference is the object:

- In the Maxwell case, the field is the field-strength biquaternion $\tilde{F}$, which lives in the vector part of the algebra and describes the electromagnetic field.
- In the Dirac case, the field is the fermion field $\tilde{Ξ}_{\mathrm{sp},R}$, which is a general element carrying the plus value of the subscript and describes the spin-$\frac{1}{2}$ particle.

The structural identity is the algebraic content of the statement that both fields are read in the same algebra. The two fields differ in **what they are**: the photon field is a vector of the algebra (spin-1), and the electron field is a general element with a value (spin-$\frac{1}{2}$).

### The Mass Term

The **mass term** is the term that distinguishes the massive Dirac equation from the massless case, and it does not appear in the Maxwell equation. In the biquaternion formulation it is the linear pairing of the pair $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = k_m\,\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\,\tilde{Ξ}_{\mathrm{sp},R}$ of the section *The Massive Case*: it is not a multiplication, it is not central, and it is the only term of the equation that carries the field from one value to the other. In the corpus's one-sided formulation the coupling is that pairing and not a right multiplication; the two-sided form of *An Explicit Dictionary with Conjugation in the Mass Term* carries the same pairing as a coefficient conjugation together with the right multiplication by $\vec e_z$, and the two are one mass term in two variables. In the Standard Model the mass term arises from the **Higgs mechanism**: the fermion couples to the Higgs field, and the coupling generates an effective mass term.

The biquaternion framework does not derive the Higgs mechanism; it simply provides a compact notation for the mass term once the mechanism is assumed. The conjugation $\flat$ is a separate object — the algebra's real structure, discussed in the section *The Massive Case* — and is not the mass term.

### The Static Maxwell Field of an Inhomogeneous Medium as a Dirac Potential

The dictionary gives one more interpretation of the massive equation, in which its potential *is* a Maxwell medium. The static sourceless Maxwell system of an isotropic inhomogeneous medium,

$$
\mathrm{rot}\,\vec H = 0, \qquad \mathrm{rot}\,\vec E = 0, \qquad \mathrm{div}(\epsilon\vec E) = 0, \qquad \mathrm{div}(\mu\vec H) = 0 ,
$$

carries its position dependence only through the two divergence equations, and on the normalised fields $\vec E_{\mathrm n} := \sqrt{\epsilon}\,\vec E$, $\vec H_{\mathrm n} := \sqrt{\mu}\,\vec H$ it becomes the pair of first-order equations with constant-free leading part,

$$
D\vec E_{\mathrm n} + \vec E_{\mathrm n}\vec{\nu} = 0, \qquad D\vec H_{\mathrm n} + \vec H_{\mathrm n}\vec{\nu}_2 = 0,
\qquad
\vec{\nu} := \frac{\mathrm{grad}\sqrt{\epsilon}}{\sqrt{\epsilon}}, \quad \vec{\nu}_2 := \frac{\mathrm{grad}\sqrt{\mu}}{\sqrt{\mu}} ,
$$

which is the **carrier identity** of *Electromagnetism in Media — The Local Complex Structure at Work*, read in the static case, where no time coordinate is present and the operator is the Moisil–Theodorescu operator $D$ alone, in the corpus's normalization $D=i\vec\nabla$. The Dirac side has the same shape: the massive equation with an electric potential, and separately with a scalar potential, becomes after the dictionary a first-order equation whose only position dependence is a coefficient multiplying one basis direction, as recorded in *The Dirac Operator with Potentials in Quaternionic Form* above. Matching the two shapes, the 2003 paper concludes that a solution of the Dirac equation with an electric or a scalar potential is a solution of the static Maxwell system of an isotropic inhomogeneous medium, the medium being the potential read as a parameter:

$$
\epsilon = \exp(\,2G(r_x)), \qquad G(r_x) = \int g(r_x)\,dr_x ,
$$

with $g$ the Dirac potential. The identification is a statement about **coefficients** and not about fields: the potential is the logarithmic derivative of the square root of the permittivity, $\vec{\nu} = \mathrm{grad}\,G$, which is checked at once from $\sqrt{\epsilon} = \exp(G)$. What the correspondence does not do is identify the Dirac field with the electromagnetic field — the Dirac biquaternion and the field-strength biquaternion are different objects, and the matching is at the level of the equations they solve, with the restriction $\mathrm{Sc} = 0$ on the Maxwell side. The corpus records it because both ends already exist here, the carrier function of the media article and the potential coupling of the Dirac article, and this is the statement that joins them.

**What is quoted.** The source's own forms of the two reduced operators, for the electric and for the scalar potential, are partly illegible in the scan. What is legible, and what is recorded above, is the shape of the reduction, the normalisation by $\sqrt{\epsilon}$, and the parameter $\epsilon = \exp(2G)$ with $\vec\nu = \mathrm{grad}\,G$; the identification of the potential with an inhomogeneity of that form is the source's statement, carried here as such.

### The Mass Shell as the Condition on the Dirac–Maxwell Correspondence

The time-harmonic comparison is the paper's last section, and its conclusion is a condition rather than an identity. Let the massive quaternionic equation be read on a time-harmonic field, as in the section *The Harmonic Field: Two Projections, and the Helicity Reading* above. There the frequency is the Dirac frequency; write it $\omega_D$, and write $E=\frac{m\,c\,\omega_{D}}{k_m}$ for the particle energy. The amplitude obeys the shifted equation $\vec\nabla f+f\alpha=0$ at the parameter

$$
\alpha = -\left(\frac{k_m\,i\,E}{m\,c^{2}}\,\vec e_x + \vec e_y\,k_m\right),
$$

and the massless case of the same equation is the vacuum Maxwell equation. The time-harmonic Maxwell field of a homogeneous isotropic medium is likewise a pair of Beltrami fields, with its own frequency $\omega$ and wave number $k=\omega\sqrt{\epsilon\mu}=\omega/c$, and the projection identity that relates the two pairs,

$$
\vec\nabla f+f\alpha = \tfrac12\bigl(\vec\nabla f+fk\bigr)\bigl(e_t+\alpha/k\bigr) + \tfrac12\bigl(\vec\nabla f-fk\bigr)\bigl(e_t-\alpha/k\bigr),
$$

holds in both directions, with the two terms genuine projections of the two Maxwell pairs, **if and only if** the Maxwell wave number and the Dirac parameter agree,

$$
k^2 = \alpha^2 .
$$

The parameter's square is central, because the two units anticommute:

$$
\alpha^2 =\frac{k_m^{2}\,E^{2}}{m^{2}\,c^{4}} - k_m^{2} .
$$

The condition is therefore

$$
\boxed{\;\frac{\omega^2}{c^2} =\frac{k_m^{2}\,E^{2}}{m^{2}\,c^{4}} - k_m^{2}
\quad\Longleftrightarrow\quad
E^2 =\frac{m^{2}\,c^{2}\,\omega^{2}}{k_m^{2}}+m^{2}\,c^{4}},
$$

which, with the de Broglie relation $\frac{m\,c\,\omega}{k_m}=pc$ for the Maxwell wave number, is the relativistic dispersion relation $E^2=p^2c^2+m^{2}\,c^{4}$. In the natural units $\hbar=c=1$ of this section it reads $E^2=\omega^2+k_m^{2}$, equivalently $k^2=E^2-k_m^{2}$ at $k=\omega=p$. The paper draws attention to the agreement — the condition on which its Dirac–Maxwell equivalence rests is the same relation that defines the particle's mass — and the corpus records it as what ties the parametric statements together: the parameter that makes the shifted equation solvable is the parameter that puts the field on shell.

The same interpretation is why the massless (neutrino) case of the section *The Harmonic Field: Two Projections, and the Helicity Reading* needs no condition at all: at $m=0$, that is $k_m=0$, the parameter is $\alpha=-(i\,k_E)\,\vec e_x$ with $\alpha^2=E^2/(\frac{m^{2}\,c^{4}}{k_m^{2}})$, and $k^2=\alpha^2$ becomes $\omega^2=\frac{k_m^{2}\,E^{2}}{m^{2}\,c^{2}}$, i.e., $\omega=\omega_D$ — the two frequencies coincide, the vacuum null-wave relation $\omega=k$, the case the source calls the neutrino, and the one the corpus records as Imaeda's vacuum Maxwell equation.

**What is quoted.** The source's intermediate equations, which restore $c$ and $\frac{m\,c}{k_m}$ at a different point of the reduction, are quoted as its own; the printed power of $c$ in them could not be read from the scan. The two statements used above — the condition $k^2=\alpha^2$ and the central value of $\alpha^2$ in terms of the energy and the mass — are legible, and the mass-shell interpretation follows from them.

### The Lanczos Route: Maxwell with Feedback

The identity of form is not an artifact of the notation, and Lanczos read it as a statement about matter. In his 1929 articles he derived Dirac's equation from the coupled biquaternion system

$$
\tilde{\nabla}\tilde{Q}_1 = \tilde{Q}_2\,k_m, \qquad \tilde{\nabla}\tilde{Q}_2 = \tilde{Q}_1\,k_m,
$$

comparing it with the biquaternion Maxwell equation $\tilde{\nabla}\tilde{F} = -4\pi\tilde{J}$ of the companion article. The first equation is then Maxwell's equation, and the second is a **feedback**: the field $\tilde{Q}_2$ acts back on the object that generates it, with the strength $k_m$. The feedback is the mass; the massless case $m=0$ breaks the coupling and leaves two independent field equations, of which the Maxwell equation is one. This is the source's interpretation, and it answers the question at the end of this article: what the Dirac and Maxwell equations share is the **operator** — the single first-order operator $\tilde{\nabla}$, a square root of $\Box$ — and what separates them is the **closure**, the Dirac field obeying the operator in the closed, self-acting way and the Maxwell field in the sourced way.

The corpus's chiral pair $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = k_m\,\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\,\tilde{Ξ}_{\mathrm{sp},R}$ is the same equation in the chiral variables — the second member carries $\tilde{\nabla}^{\natural}$ because the field with the minus value is the conjugate of the Lanczos $\tilde{Q}_2$ — and it displays the field split into its two parts, but not the direction that the Lanczos form makes explicit. Lanczos reached the Dirac equation from the pair by a superposition along an arbitrary axis (in the displays of this paragraph the letter $D$ is Lanczos's name for the Dirac field, not the spatial operator $D=i\vec\nabla$ of *An Explicit Dictionary with Conjugation in the Mass Term*)

$$
D = \tilde{Q}_1\tilde{\Pi} + \tilde{Q}_2^{*}\bar{\tilde{\Pi}},
$$

with $\tilde{\Pi}$ the projection along a unit vector $\vec{\nu}$ and $\bar{\tilde{\Pi}}$ its conjugate — so that one half of $\tilde{Q}_1$ and half of the conjugate of $\tilde{Q}_2$ are carried into the two **different** parts of the field, which is what makes the superposition a field carrying both values and not a field carrying one; the resulting single equation

$$
\boxed{\;\tilde{\nabla}D = D^{*}i\vec{\nu}\,k_m\;}
$$

is strictly equivalent to Dirac's equation. The unit vector on the right is the point of the display: it is the **spin quantization axis**, and it shows that Dirac's equation singles out an arbitrary but unique direction in ordinary space. The corpus's pair is written for a fixed frame and does not exhibit the axis; the Lanczos form shows that the axis is carried by the projection itself, and that any unit vector will do. The complex conjugation on the right-hand side is a second such fact: it is what makes the Dirac field **fermionic**, in contrast with the Maxwell and Proca fields, which are bosonic. The superposition is not unique: the source's second and equally covariant combination — Gürsey's, which the isospin reading makes the neutron to the proton — is recorded in *The Standard Model under the Biquaternion Framework — A Research Agenda*; the fermionic character above is what the two share.

**The other road to the same halving.** The superposition along the axis is not the only way the doubled system becomes Dirac's, and the source records a second one. "One can go from (1) to (3) by simply requiring that $A$ and $B$ are singular quaternions" — an observation the authors attribute to Blaton (1935), where (3) is the two-field pair $\partial L = mR$, $\partial R = mL$. The two routes reach the same place by different means: the superposition splits each field into its two parts and adds the halves *across* the two parts, whereas the singularity condition degenerates the fields themselves. The destination, however, is the corpus's own object — a singular biquaternion is a zero divisor — so this interpretation of the reduction says that the Dirac field is what the doubled Lanczos system becomes when both of its fields are confined to the singular set. The source is careful about what the halving alone does not buy: Dirac's system "does not only involve half as many components as Lanczos's system (1), it also incorporates the ingredients that make fermions essentially different from bosons", which are the complex conjugation and the singled-out direction recorded just above. That distinction is why the corpus keeps *N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors* and this article apart: the halving is a fact about the algebra, while the fermionic character is a fact about the superposition.

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

the two parts $f_\pm$ being the images of $f$ under the two complementary projections that the shifted-operator theory supplies, multiplying on the right. Each of the two is an equation of the form $(D + \alpha(\vec r))u = 0$ with a **scalar** coefficient. That equation is the subject of the monograph's §4.1.5, and the corpus already carries its solution: the **zero-divisor device** recorded in *Maxwell's Equations in Chiral Media*, in which a solution of the eikonal equation $(\nabla\xi)^2 = \alpha^2$ conjugates $D + \alpha$ into $D + \mathcal{Q}_+$ with $\mathcal{Q}_+ = \nabla\xi$ a zero divisor, and the solutions are built from the exponentials $\exp(\pm i\Theta)$ of the accumulated phase and analytic transverse functions. The chain therefore closes inside the corpus: pseudoscalar-potential Dirac equation $\to$ shifted operator with a scalar coefficient $\to$ eikonal conjugation by a zero divisor $\to$ explicit solutions. The exceptional case, $\omega^2$ a zero divisor (an isotropic $\omega$), is separate; the monograph handles it with a one-variable ansatz, because the two projections degenerate there.

**What this does and does not add.** It adds the observation that the pseudoscalar Dirac coupling is not new machinery: it is the shifted operator the corpus already possesses, read at a position-dependent parameter, and the corpus's zero-divisor device solves it. It does not supply solutions for the electric potential — the monograph reaches that case by the same conjugation, but the corpus treats electromagnetic coupling separately in *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism* — and it claims no new physics: the coupling list is standard, and it is surveyed in the encyclopaedic compendium the monograph cites for the classification of exact Dirac solutions up to the late 1980s, now recorded in the Further Reading below.

## The Dirac Equation and the Biquaternion Algebra

### Why the Algebra and Not an Array

The Dirac equation is usually carried by four arrays that anticommute in pairs and act on a column. The same anticommutation holds inside $\mathbb{B}$, and the biquaternion algebra is the even part of the algebra those four arrays generate, so the equation can be carried by $\mathbb{B}$ directly.

The advantage is that the algebra is the object and the array is a display of it. A biquaternion has four complex coefficients and the equation is one element acting on one element; the array needs a frame, a labelling of rows by the values and of columns by the letters of the units, and every identity is then a statement about one display. The corpus writes the element and prints the array only where a comparison wants it.

The price is a boundary case. A biquaternion acts on itself by left multiplication, so the field is a general element rather than a column, and the mass is a pairing of the two parts rather than an entry of a matrix; both are available in the algebra, and neither needs an extra object to hold the four numbers. What the array does better is bookkeeping: four rows make the four coefficients visible one by one, and a reader who is counting degrees of freedom will reach for it. That is why *The Legacy Pauli Gamma Formulation* keeps the arrays, from the article *Why AXF Matrices instead of Pauli and Gamma Matrices* onward, as a check on the algebra and not as its definition.

### What the Biquaternion Formulation Adds

The biquaternion formulation adds three things:

**1. A unified algebraic framework for Maxwell and Dirac.** The two equations are one operator acting in one algebra, and the two fields are two objects of that algebra. Nothing has to be added to pass from one to the other.

**2. A compact notation for the value.** The value of the field is a letter, $L$ or $R$. No index is written: the field is one element, its two parts are named by the letter they carry, and the mass is the pairing between them.

**3. A natural language for relativistic kinematics.** The four-velocity $\tilde{V}$, the four-momentum $\tilde{P}$, and the mass-shell relation $\tilde{P}\tilde{P}^{\natural} = -m^{2}\,c^{2}$ are all natural objects in the biquaternion algebra. The Dirac equation is naturally stated in terms of these objects, and the plane-wave solutions are naturally written in terms of the wave biquaternion $\frac{k_m\,\tilde{P}}{m\,c}$ and the four-position $\tilde R_\Phi$.

### The Mass as a Non-Integrable Phase

A change of variable on the same field makes the mass look like a *phase*. Liu Yu-Fen's observation is that the mass term of the massive Dirac equation can be written as a coupling to a four-vector built from the field itself, so that the massive equation is the massless equation with the ordinary derivative replaced by a derivative along that four-vector and the mass becomes a phase rather than a scalar. The source states the identity in its array form,

$$
k_m\,\tilde{Ξ}_{\mathrm{sp}}^{\dagger}iR_{\mathrm{axf},\vec e_x}\tilde{Ξ}_{\mathrm{sp}} = \tilde{Ξ}_{\mathrm{sp}}^{\dagger}iR_{\mathrm{axf},\vec e_x}\bigl(iK_t\,e_t\tilde{Ξ}_{\mathrm{sp}} \vec e_x + i\sum_k B_{\mathrm{boost},k}\,\vec e_k\tilde{Ξ}_{\mathrm{sp}} \vec e_y\bigr),
$$

with $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}iR_{\mathrm{axf},\vec e_x}$ the Dirac adjoint, written in the frame cell $iR_{\mathrm{axf},\vec e_x}$, and $U_{\mathrm{vec},\mu}$ a unit complex four-vector. The corpus records the display as the source's and does not restate it in cells: what the display carries is the shape, a four-vector built from the field and multiplying it from the right, and the shape survives the transcription while the array does not. The phase is **non-integrable**: if $U_{\mathrm{vec},\mu} = \partial/\partial R_\mu\,\theta$ were a gradient, the change of variable $\tilde{Ξ}_{\mathrm{sp}} \mapsto \exp(i\theta)\tilde{Ξ}_{\mathrm{sp}}$ would remove it and the field would be massless; the mass is exactly the statement that $K$ is not a gradient, and the obstruction is the field strength $\partial/\partial R_\mu K_\nu - \partial/\partial R_\nu U_{\mathrm{vec},\mu}$.

The on-shell content of the interpretation is verified and simple: for a plane wave of momentum $p_\mu$ satisfying the mass shell $p^2 = m^2$, the vector

$$
U_{\mathrm{vec},\mu} = \frac{p_\mu}{m}
$$

satisfies $\sum_\mu\varepsilon_\mu U_{\mathrm{vec},\mu} U_{\mathrm{vec},\mu} = 1$. The momentum per unit mass is a unit vector, and the source reads it as the unit vector that carries the mass term.

This interpretation is the origin of the *triality construction* recorded in the companion articles. The two parts of the field, the vector they combine into, and the unit vector $K$ are the three objects that the order-three map permutes; the mass term is the coupling that the order-three (cubic) form expresses. The reader who wants the construction itself is referred to *The s-Vector Representation of the Dirac Spinor in Biquaternionic Form*, *Triality and the Ding Construction for the Dirac Spinor in Biquaternionic Form*, and *Dual Equivalence of the Dirac and Topologically Massive Gauge Fields*. The present article records only the origin: the mass is a unit vector, a non-integrable phase, and it is the object the triality construction is built on.

## Open Questions

1. **The real structure $\flat$ and the electroweak interaction.** The conjugation $\flat = -{}^{*}$, whose fixed space is the anti-Hermitian sector $\mathbb{B}_{\Phi}$ and which is the algebra's real structure, has the shape of a Majorana-type pairing. Does that real structure have a natural interpretation in terms of the electroweak interaction — in particular, does it supply the real form in which the neutrino is distinguished from the charged fermions?

2. **The relation to the Standard Model.** The Standard Model describes fermions in the spinor representation of the Lorentz group. How does the biquaternion framework extend to the full Standard Model, including the gauge fields?

3. **The non-abelian generalization.** The biquaternionic Dirac equation is abelian (the field is a single biquaternion). How does the framework extend to non-abelian gauge theories, where the fermion field is a vector in a representation of the gauge group?

4. **The relation to the twistor program.** Twistor theory works in the complex four-dimensional space $\mathbb{C}^4$, which is the coefficient space of $\mathbb{B}$. How do the biquaternion Dirac equation and the twistor equation relate?

5. **The quantization.** The Dirac equation is the classical equation of motion for a fermion field. How does the biquaternion framework extend to the quantized theory (quantum field theory), and what is the role of the biquaternion structure in the quantized case?

6. **The relation to the biquaternion Maxwell equation.** The two equations have the same form. Is there a deeper sense in which the photon and the electron are the same biquaternion field in different representations, or is the identity purely formal? **Partly answered**, in the section *The Lanczos Route: Maxwell with Feedback*: the shared object is the **operator** and the Dirac equation is the **closed** (feedback) way of obeying it, so the identity is structural rather than merely formal, and the fermionic statistics follow from the complex conjugation in the Lanczos form. What remains open is the feedback itself — the framework represents the mass feedback but does not derive it.

7. **The minimal coupling to electromagnetism.** The standard Dirac equation couples to the electromagnetic field through the minimal coupling $\partial/\partial R_\mu \to \partial/\partial R_\mu -\frac{k_m\,iqA_{\mu}}{m\,c}$. How this coupling reads in the biquaternion framework, given the biquaternion form of the four-potential $\tilde{A} = i\,a'_t\,e_t + \vec A$, is treated in the companion article *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*.

These questions are open.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, $\gamma_0^2=I_4$ and $\gamma_k^2=-I_4$. The frame belongs to the coordinate, not to the array.

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

$\gamma_5$ is the fifth cell of the frame, the operator the maths article calls the chirality operator (*Operator Chirality on the Biquaternion Algebra*): the volume cell, $-iL_{e_t}R_{\vec e_z}$, which is the pure right multiplier $-iR_{\vec e_z}$ on the algebra. The two arrays above are its arrays in the two displays. The operator is neither array. It is the side, and the side is what the fifth cell of the frame adds to the four generators: the four multiply on the left, and the fifth multiplies on the right by the third direction.

The cell dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{\mathrm{axf},e_\mu}=C_{\Pi}L_{\mathrm{pau},e_\mu}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The Dirac equation in biquaternionic form is the chiral pair

$$
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = k_m\,\tilde{Ξ}_{\mathrm{sp},L}, \qquad \tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\,\tilde{Ξ}_{\mathrm{sp},R}
$$

for a field of mass $m$, where $\tilde{\nabla}$ is the biquaternionic gradient, $\tilde{Ξ}_{\mathrm{sp}} = \tilde{Ξ}_{\mathrm{sp},L} + \tilde{Ξ}_{\mathrm{sp},R}$ is one element of $\mathbb{B}$ whose parts carry the two values of the subscript, the coefficient of the mass term is $k_m$, the inverse reduced Compton wavelength, and the mass is the term that carries the field from one value to the other. At $m=0$ the pair decouples into the two one-sided equations

$$
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R}=0, \qquad \tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=0,
$$

one for each value; the single equation $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp}}=0$ is the one with the plus value. The two values are the letters $L$ and $R$ that every element carries; the value of a product is the value of its right factor, left multiplication keeps it, and the mass is the only term that carries the field from one value to the other. In the massless limit each part carries one helicity. The equation with the plus value has the same form as the source-free biquaternion Maxwell equation, and the other is its conjugate. The structural identity is the statement that both fields are read in the same algebra — no matrix, no column and no separate space. Each part satisfies the Klein–Gordon equation $(\Box - k_m^{2})\tilde{Ξ}_{\mathrm{sp},L,R} = 0$.

The relativistic kinematic relations are expressed in the same language: the four-velocity $\tilde{V} = \gamma(ic\, e_t + \vec v)$ satisfies $\tilde{V}\tilde{V}^{\natural} = -c^2$, the four-momentum $\tilde{P} =m\,\tilde{V}$ satisfies the mass-shell relation $\tilde{P}\tilde{P}^{\natural} = -m^{2}\,c^{2}$, and the four-position $\tilde R_\Phi = i c r'_t\, e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ gives the invariant interval $ds^2 = \langle d\tilde R_\Phi\rangle_{\natural} = d\tilde R_\Phi\,d\tilde{R}_\Phi^{\natural}$.

The plane-wave solutions of the massless equation with the plus value are $\tilde{Ξ}_{\mathrm{sp}} = \tilde{Ξ}_{\mathrm{sp},0}\exp\!\left(i\,\mathrm{Sc}\frac{k_m\,\tilde{P}\,\tilde{R}_{\Phi}^{\natural}}{m\,c}\right) = \tilde{Ξ}_{\mathrm{sp},0}\,\exp(\,i(\vec k\cdot(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)-\omega r'_t))$ with $\tilde{P}\tilde{Ξ}_{\mathrm{sp},0}/\hbar = 0$, nonzero only for null $\frac{k_m\,\tilde{P}}{m\,c}$, giving the two spin states of that value; the other value has the conjugate plane waves, and the two are the two helicities, which a massless plane wave fixes to $-\tfrac12$ and $+\tfrac12$. The massive plane waves satisfy the mass-shell condition $\tilde{P}\tilde{P}^{\natural}=-m^{2}\,c^{2}$; the two frequency branches are the particle and the antiparticle, and with the two spin states they give the four solutions the field carries.

The spherical and cylindrical solutions are constructed from harmonic functions by the completion $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp}}$, and they describe the angular momentum states of the fermion field and the waveguide modes.

A second form of the same equation is Kravchenko's, and it is two-sided: $\bigl(\frac{i}{c}\partial/\partial r'_t+\vec\nabla\bigr)F-i\,\overline{F}\,\vec e_z\,k_m=0$, whose free part is $-\tilde{\nabla}^{\natural}$ and whose mass term is a coefficient conjugation together with the right multiplication by the direction $\vec e_z$. The conjugation obstructs the analytic theory, so it is moved into the change of variable, and the conjugation-free operator

$$
R[F] = \vec\nabla F - \frac{1}{c}\frac{\partial F}{\partial r'_t}\,\vec e_x - F\,\vec e_y\,k_m
$$

has coefficients in the real quaternions. The real and imaginary parts of a solution of $R[F]=0$ are therefore separately solutions, so one quaternionic solution carries two Dirac solutions. With the conjugation removed, the time-harmonic amplitude obeys a shifted equation with a biquaternionic parameter, and the Cauchy integral formula, the Plemelj–Sokhotski formulas and the boundary-value criterion hold for it in the same shape as for the time-harmonic Maxwell field.

The same dictionary relates the massive Dirac equation with an electric or a scalar potential to the static sourceless Maxwell system of an inhomogeneous medium, $\epsilon = \exp(2G)$ with $dG/dr_x = g$; and on time-harmonic fields the Dirac field and the Maxwell field of a homogeneous medium share their projection identity exactly when $k^2 = \alpha^2$, which is the mass shell, $E^2 =\frac{m^{2}\,c^{2}\,\omega^{2}}{k_m^{2}}+m^{2}\,c^{4}$. The four potentials — scalar, pseudoscalar, electric and magnetic — are coefficients on four distinguished directions of the algebra, and the pseudoscalar one is the shifted operator that the corpus already solves.

The mass can be written as a non-integrable phase: $U_{\mathrm{vec},\mu} = p_\mu/m$ is a unit four-vector on shell, and the mass term is the statement that $K$ is not a gradient. That observation is the origin of the triality construction of the companion articles.

The biquaternion framework provides a compact and unified language for the Maxwell and Dirac equations, but it does not by itself derive the mass term or the electroweak structure. Those require additional physics beyond the algebraic framework.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\tilde{Q}_L$, $\tilde{Q}_R$ | An element with the value $L$ and with the value $R$; the subscript takes two values and only the zero element carries both |
| $\gamma_5$ | The fifth cell of the frame, the chirality cell; its array is printed in *The Legacy Pauli Gamma Formulation* |
| $i_1,i_2,i_3$ | The source's symbols for the quaternion units $\vec e_x,\vec e_y,\vec e_z$; the scalar imaginary is its $i$ as here |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum |
| $\vec v$ | Particle three-velocity |
| $\gamma = 1/\sqrt{1 - \vec v^2/c^2}$ | Lorentz factor |
| $\tilde R_\Phi = i c r'_t\,e_t + r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ | Four-position biquaternion |
| $\tilde{V} = \gamma(ic\,e_t + \vec v)$ | Four-velocity biquaternion |
| $\tilde{P} =m\,\tilde{V}$ | Four-momentum biquaternion, since $m\,c=mc$; the shell is $\tilde{P}\tilde{P}^{\natural}=-m^{2}\,c^{2}$ |
| $k_m=\dfrac{mc}{\hbar}$ | The mass wave number of the field, the one wave number of the article; $\mathsf{L}^{-1}$, the coefficient of the mass term, and $k_m^{2}$ the coefficient of the Klein–Gordon mass term. Its inverse $1/k_m=\hbar/(mc)$ is the reduced Compton wavelength. Defined in *The Three Wavenumbers of a Particle* |
| $\tilde{\nabla}$ | Biquaternionic gradient (Dirac operator), the first-order element of *Operator and Calculus Conventions* |
| $\tilde{\nabla}^{\natural}$ | Its quaternion conjugate |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural}$ | d'Alembertian, central scalar |
| $\tilde{\nabla}_\kappa = \tilde{\nabla} + \kappa$ | Shifted gradient, $\kappa \in \mathbb{C}$ central (companion d'Alembertian article) |
| $\tilde{Ξ}_{\mathrm{sp}} = \tilde{Ξ}_{\mathrm{sp},L} + \tilde{Ξ}_{\mathrm{sp},R}$ | The field: one element of $\mathbb{B}$, one part per value of the subscript |
| $\tilde{Ξ}_{\mathrm{sp}}^{\flat} = -\tilde{Ξ}_{\mathrm{sp}}^*$ | Anti-Hermitian conjugate (the algebra's real structure; not the mass term) |
| $\bar{\cdot}$, written $C$ by the source | Componentwise complex conjugation, $Q_\mu\mapsto\bar Q_\mu$ on the coefficients: an automorphism, $\mathbb{C}$-antilinear and not an anti-automorphism |
| $\vec\nabla = \sum_{k=1}^{3}\vec e_k\,\partial/\partial R_k$ | The spatial gradient, pure, $\vec\nabla^2=-\Delta$ and $\lvert\vec\nabla\rvert^2=\Delta$, with real quaternion coefficients on the material sector; the source writes it $D$ |
| $D = i\vec\nabla$ | The corpus's spatial operator of *Biquaternion Regular Functions*, $D^2=\Delta$ |
| $\mathcal{N} = \frac{i}{c}\partial/\partial r'_t + \vec\nabla - i\,\overline{\cdot}\,\vec e_z\,k_m$ | The two-sided Dirac operator with the conjugation in the mass term; its free part is $-\tilde{\nabla}^{\natural}$ |
| $R[F] = \vec\nabla F-\frac{1}{c}\partial F/\partial r'_t\,\vec e_x-F\vec e_y\,k_m$ | The conjugation-free operator of the same source; real, with coefficients in $\mathbb{H}$, so $R[\mathrm{Re}\,F]=R[\mathrm{Im}\,F]=0$ |
| $\epsilon = \exp(2G)$, $\vec{\nu} = \mathrm{grad}\,G$ | The Dirac potential $g=dG/dr_x$ read as the inhomogeneity of a static Maxwell medium |
| $k = \omega\sqrt{\epsilon\mu}$ | Maxwell wave number; the Dirac–Maxwell correspondence holds iff $k^2=\alpha^2$, equivalently $E^2=\frac{m^{2}\,c^{2}\,\omega^{2}}{k_m^{2}}+m^{2}\,c^{4}$ |
| $\vec\nabla+\cdot\,\alpha$ | The shifted operator for the time-harmonic amplitude, $\vec\nabla f+f\alpha=0$ at a constant $\alpha$ |
| $\xi_{\mathrm{scl}}$ | Scalar (pseudoscalar-potential) coefficient of the shifted Dirac operator |
| $\tfrac12(e_t\pm\alpha/\sqrt{\alpha^2})$ | The two complementary projections of the harmonic field, multiplying on the right; they split it into the two signs of the frequency, and in the source's reading the two helicities |
| $K_\omega$ | The Cauchy-type operator of the amplitude equation; the Cauchy integral formula, the Plemelj–Sokhotski formulas and the boundary-value criterion $\tilde{Ξ}_{\mathrm{sp}} = K_\omega\tilde{Ξ}_{\mathrm{sp}}$ on $\Gamma$ hold for it |
| $\frac{k_m\,\tilde{P}}{m\,c}$ | Wave biquaternion |
| $U_{\mathrm{vec},\mu}$ | Unit complex four-vector carrying the mass term, $k_m\tilde{Ξ}_{\mathrm{sp}}^{\dagger}iR_{\mathrm{axf},\vec e_x}\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}}^{\dagger}iR_{\mathrm{axf},\vec e_x}(iK_t\,e_t\tilde{Ξ}_{\mathrm{sp}} \vec e_x+i\sum_k B_{\mathrm{boost},k}\,\vec e_k\tilde{Ξ}_{\mathrm{sp}} \vec e_y)$; $U_{\mathrm{vec},\mu}=\frac{p_{\mu}}{m}$ on shell, $\sum_\mu\varepsilon_\mu U_{\mathrm{vec},\mu} U_{\mathrm{vec},\mu}=1$ |
| $iR_{\mathrm{axf},\vec e_x}$ | The timelike cell, the Dirac adjoint in the bilinear covariants |
| $\lvert F\rvert^2 = \langle F\rangle_{*} = \sum_\mu\lvert F_\mu\rvert^2$ | Hermitian norm of the biquaternion field, the definite one; the probability density of a complex field |
| $m$ | Fermion mass, equal to $m$; in the equations of this article it enters only through the length, so a display writes $k_m$ and never $m$ |
## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- [The Three Wavenumbers of a Particle](the-three-wavenumbers-of-a-particle.html), for the definition of the wave number $k_m=mc/\hbar$ and of the two state wave numbers $k_{\mathrm{mo}}$ and $k_E$, their values for the electron, the proton and the other particles, and the unit argument that fixes the coefficient of the mass term.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original Dirac equation.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the foundational treatment of the Dirac equation.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the standard physics treatment.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the historical background on Clifford algebras and the objects the literature calls spinors.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric algebra approach to the Dirac equation.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original formulation of the Dirac equation in geometric algebra.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the spinor formulation of the Dirac equation.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the regular functions of that tradition and its analysis of the Dirac operator.
- L. A. Alexeyeva, "Differential algebra of biquaternions. Dirac equation and its generalized solutions," *Progress in Analysis, Proceedings of the 8th Congress of the ISAAC* (Moscow, 2013), pp. 153–161, for the biquaternion formulation of the Dirac equation.
- V. V. Kassandrov and N. V. Markova, "New symmetries, conserved quantities and gauge nature of a free Dirac field," arXiv:2209.00460 (2022), for the free Dirac field read as the gauge-invariant strength of a quadruple of Klein–Gordon potentials fixed only up to a constrained gradient shift, for its own two-field form $b=(i/m)Wa$ in which one half is the derivative of the other, for the singular solutions of the shifted kernel — the spinorial Yukawa analogue, a string-like solution and a stationary solution of finite field charge — and for the remark that the potential-based transformation of the Dirac field is nonlinear and free of two-valuedness, recorded in §*The Field as the Gradient of a Scalar Potential* above as a boundary and not as a replacement of the canonical law.
- V. V. Kravchenko, "On a Biquaternionic Bag Model," *Zeitschrift für Analysis und ihre Anwendungen* **14** (1995), no. 1, 3–14, DOI 10.4171/ZAA/658, for the explicit real-linear dictionary from the four-component bispinors onto the biquaternions, with the timelike generator realized by complex conjugation — the images of the spatial generators, not readable from this source alone, are stated in the Doklady note of the next entry; for the biquaternionic Dirac operator $i\partial/\partial r'_t + D - miCM_{i_3}$, printed there at $c=1$ — the source's real time, the $r'_t$ of the material sector — the source's $D$ being the spatial gradient $\vec\nabla$ of this article, whose mass term carries the conjugation; for the removal of the conjugation by a change of variable, realised as the factorisation $\mathcal{N}=u^{+}Ru^{-}$ with the conjugation-free operator $R=P_1^{+}(i\partial/\partial r'_t+D)+P_1^{-}(-i\partial/\partial r'_t+D)-mM_{i_2}=D-\partial/\partial r'_tM_{i_1}-mM_{i_2}$; and for the two projections $\tfrac12(e_t\pm i\vec e_k)$ of that factorisation, which the source writes $P_k^{\pm}=\tfrac12 M_{(1\pm i i_k)}$.
- V. V. Kravchenko, "Quaternion-Valued Integral Representations of the Harmonic Electromagnetic and Spinor Fields," *Doklady Mathematics* **51** (1995), no. 2, 287–289 (translated from *Doklady Akademii Nauk* **341** (1995), no. 5, 603–605), for the dictionary of the preceding entry as a real-linear bijection with the mass term carrying complex conjugation, and for that dictionary in full — the components of $A$, and the images of the three timelike bivectors, $A(L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_z}Ξ)=-i\,i_1A(Ξ)$, $A(L_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_z}Ξ)=-i\,i_2A(Ξ)$, $A(L_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_z}Ξ)=+i\,i_3A(Ξ)$, with the volume element carried by a right multiplication through $i_3$; for the bijection between the solutions of the Dirac equation and the solutions of the quaternionic equation $i\partial/\partial r'_tF+DF-\mathrm{Im}(F)\,i=0$; for the time-harmonic field $F = P_+f(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\exp(i\omega r'_t)+P_-f(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\exp(-i\omega r'_t)$ with the two complementary projections and the helicity interpretation of the two parts; for the massless case $i\partial/\partial r'_tF+DF=0$, attributed there to Imaeda; and for the spinor-side integral representation recorded in the section *The Integral Representation of the Harmonic Field* — the amplitude operator $D_\omega\tilde{Ξ}_{\mathrm{sp}} = -\omega\,e_t\tilde{Ξ}_{\mathrm{sp}} \vec e_x+i\sum_{k=1}^{3}\vec e_k\,(\partial\tilde{Ξ}_{\mathrm{sp}}/\partial R_k)\,\vec e_y$, the Cauchy-type operator $K_\omega = A^{-1}KA$, and the three results that follow for it: the Cauchy integral formula, the Plemelj–Sokhotski formulas, and the boundary-value criterion $\tilde{Ξ}_{\mathrm{sp}} = K_\omega\tilde{Ξ}_{\mathrm{sp}}$ on $\Gamma$. The same note is the source of the unifying statement that one parametric system, at different values of its parameter, is the time-harmonic Maxwell system and the time-harmonic Dirac system; that statement is recorded in the companion *The Time-Harmonic Maxwell Operator and the Quaternionic Cauchy Integral*.
- K. Imaeda, "A new formulation of classical electrodynamics," *Il Nuovo Cimento B* **32** (1976) 138–162, for the quaternionic vacuum Maxwell equation $i\partial/\partial r'_tF+DF=0$, the equation the dictionary reduces to at vanishing mass.
- V. V. Kravchenko and M. V. Shapiro, *Integral Representations for Spatial Models of Mathematical Physics* (Pitman Research Notes in Mathematics 351, Addison-Wesley Longman, 1996), for the shifted operator $D_\alpha$ and its boundary-value theory, which is where the conjugated equation is taken once the conjugation has been removed.
- C. Lanczos, "Die tensoranalytischen Beziehungen der Diracschen Gleichung," *Zeitschrift für Physik* **57** (1929) 447–473, 474–483, 484–493 (arXiv:physics/0508002, physics/0508012, physics/0508013), for the coupled biquaternion system from which the Dirac equation descends and for the superposition along an axis that produces it.
- F. Gürsey, "Applications of Quaternions to Field Equations," PhD thesis, University of London, 1950, for the review of Lanczos's quaternionic theory and for the treatment of the scalar, vector, pseudoscalar and pseudovector equations as degenerate cases of it.
- A. Gsponer and J.-P. Hurni, "The physical heritage of Sir W. R. Hamilton," arXiv:math-ph/0201058, §8, for the interpretation of Lanczos's system as Maxwell's equation with feedback, for the spin-quantization-axis form $\tilde{\nabla}D=mD^{*}i\vec{\nu}$ of the Dirac–Lanczos equation, and for the complex-conjugation origin of the fermionic character.
- A. Gsponer and J.-P. Hurni, "Lanczos's Equation to Replace Dirac's Equation?", *Proceedings of the Cornelius Lanczos International Centenary Conference* (SIAM, 1994) 509–512 (arXiv:hep-ph/0112317), for Lanczos's coupled system as "Maxwell's equations with feed-back" and for the second route to Dirac's equation, the reduction by requiring the two fields to be singular quaternions, attributed there to J. Blaton, *Zeitschrift für Physik* **95** (1935) 337–354. Recorded as a claim: four pages, no derivation exhibited, and the title is a question; the arXiv version carries a *Note added in 1996* withdrawing the authors' charge-quantisation mechanism, which is recorded in *The Standard Model under the Biquaternion Framework — A Research Agenda*.
- V. V. Kravchenko, *Applied Quaternionic Analysis* (Research and Exposition in Mathematics 28, Heldermann, 2003), §§4.2.1–4.2.2.1, for the four standard Dirac potentials — electric, scalar, pseudoscalar, magnetic — in quaternionic form, for the single constant transformation that relates the classical and quaternionic Dirac operators with potentials, and for the reduction of the pseudoscalar-potential equation to a pair of scalar-coefficient equations.
- V. V. Kravchenko and M. P. Ramirez Tachiquin, "On a quaternionic reformulation of the Dirac equation and its relationship with Maxwell's system," *Bulletin de la Société des Sciences et des Lettres de Łódź* **53** (2003) 101–114, for the **reality** of the conjugation-free quaternionic Dirac operator — $R = D-\partial/\partial r'_tM_{i_1}-mM_{i_2}$, the source's $D$ being the spatial gradient $\vec\nabla$ of this article, with coefficients in the real quaternion algebra, hence $R[\mathrm{Re}\,F]=R[\mathrm{Im}\,F]=0$ — and for the **involutive symmetry** $Ξ_{\mathrm{inv}}=iZ_cΞ$ that follows, the symmetry itself attributed there to J. Niederle and A. G. Nikitin, "Involutive symmetries, supersymmetries and reductions of the Dirac equation," *J. Phys. A: Math. Gen.* **30** (1997) 999–1010; for the correspondence between the massive Dirac equation with an electric or a scalar potential and the static sourceless Maxwell system of an isotropic inhomogeneous medium, with the permittivity $\epsilon=\exp(2G(r_x))$, $dG/dr_x=g$; for the condition $k^2=\alpha^2$ under which the massive Dirac field and the time-harmonic Maxwell field share the same projection identity, that condition being the mass shell; and for the quaternionic current-conservation equation $\partial/\partial r'_t|F|^2 = -\frac{m\,c}{k_m}[(DF^{\dagger})F+F^{*}(DF)]$ with the identity $|F|^2=|Ξ|^2$ of the biquaternion modulus and the Dirac density. The paper's factors $u^{\pm}$ of the factorisation $\mathcal{N}=u^{+}Ru^{-}$ and its explicit action of $A^{-1}$ on $\mathrm{Re}\,F$ are quoted, not reproduced: the available copy is a scan without a text layer.
- V. G. Bagrov and D. M. Gitman, *Exact Solutions of Relativistic Wave Equations* (Kluwer, Dordrecht, 1990), for the encyclopaedic compendium and review of the known exact solutions of the Dirac equation up to the late 1980s.
- Liu Yu-Fen, "Triality, Biquaternion and Vector Representation of the Dirac Equation," arXiv:math-ph/0109008 (2001), for the interpretation of the mass term as a coupling $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}iR_{\mathrm{axf},\vec e_x}(iK_t\,e_t\tilde{Ξ}_{\mathrm{sp}} \vec e_x+i\sum_k B_{\mathrm{boost},k}\,\vec e_k\tilde{Ξ}_{\mathrm{sp}} \vec e_y)$ to a unit vector, hence as a non-integrable phase; and for the vector representation of the spinor built on it, recorded in the companion *The s-Vector Representation of the Dirac Spinor in Biquaternionic Form*.
- Liu Yu-Fen, "Triality and Dual Equivalence Between Dirac Field and Topologically Massive Gauge Field," arXiv:hep-th/0602275 (2006), for the same interpretation in the order-$\ell$ ding language, and for the parent-action duality recorded in *Dual Equivalence of the Dirac and Topologically Massive Gauge Fields*.
