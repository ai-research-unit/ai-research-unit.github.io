# __The Fermionic Path Integral in Biquaternionic Form__

## Introduction

The companion article *The Path Integral in Biquaternionic Form* settles what the biquaternion algebra can and cannot contribute to a path integral: the phase factor $\exp(iS/\hbar)$ is a *central* $*$-unitary element, because the central scalar imaginary is the algebra's unique complex structure up to sign; the exponent lies along the $ict'$ direction of the material sector $\mathbb{M}_-$; and the measure, the action and the space of paths are not supplied by the algebra, because $\mathbb{B}$ is finite-dimensional and the space of histories is not. The companion article *The Feynman Propagator in Biquaternionic Form* adds where the $i\epsilon$ lives and that the algebra names its axis without choosing its orientation. The companion article *Interpretation of the Wick Rotation in the Biquaternion Universe* adds that $t'\to-i\tau$ is the relabeling of the imaginary-time coefficient as a real one, turning the material sector into the quaternion subspace.

This article applies those findings to the spin-$\tfrac12$ field, where the histories are **anticommuting**. The fermionic path integral differs from the bosonic one in exactly one structural place — the integration variables are odd, so the integral is Berezin's rather than Lebesgue's — and that one difference propagates into every formula. The article establishes:

- **The action and its sector.** The biquaternion Dirac action as a bilinear; the **one-sided** pair over the two parts of the field, which is what the integral integrates, and the **two-sided** (Kravchenko) equation, which it does not; the phase $iS$ as an element of $\mathbb{M}_-$ along the $ict'$ axis; and the action as an even (bosonic) functional of the fermionic field.
- **The Berezin measure.** Fermionic histories are Grassmann-valued biquaternion fields; the measure is the Berezin measure on the Grassmann extension of the coefficient algebra, and in the finite-mode reduction it is $\prod_a d\psi_a^{\dagger}\,d\psi_a$ with the convention fixed once.
- **The Gaussian integral and the determinant.** Completing the square in the Grassmann algebra gives the free generating functional, the two-point function as the inverse kernel, and the determinant of the pair operator; the finite-mode statements were recomputed exactly.
- **The Pfaffian and the real structure.** For a field whose quadratic form is antisymmetric — the Majorana case, for which the algebra supplies the field-to-its-conjugate pairing — the integral is a Pfaffian, with $\mathrm{Pf}^2=\det$ and a sign that carries physical content.
- **The Euclidean integral and the parity sectors.** Wick rotation and the antiperiodic (Matsubara) boundary conditions, the two fermion-parity traces and the boundary conditions that select them, and the phase of the determinant.

The boundary with the neighbouring subjects is sharp and is stated where it occurs: the systematic evaluation of the functional determinant, the transformation of the measure under field redefinitions, and the anomalies that follow from it are not treated here.

## The Action in Biquaternion Form

Throughout, $i$ is the central scalar imaginary of $\mathbb{B}$, with $i^2=-1$. Wherever two imaginary units meet, they are multiplied to $-1$; a display that still shows both is the step before that reduction.

Every derivative in this article is the corpus gradient. It is the element

$$
\tilde\nabla=e_t\frac{\partial}{\partial Q_t}+\vec e_x\frac{\partial}{\partial Q_x}+\vec e_y\frac{\partial}{\partial Q_y}+\vec e_z\frac{\partial}{\partial Q_z},
\qquad
\tilde\nabla^{\natural}=e_t\frac{\partial}{\partial Q_t}-\vec e_x\frac{\partial}{\partial Q_x}-\vec e_y\frac{\partial}{\partial Q_y}-\vec e_z\frac{\partial}{\partial Q_z},
$$

read on the material sector $\mathbb{M}_-$ as $\tilde\nabla|_{\mathbb{M}_-}=-\frac{i}{c}e_t\,\partial/\partial t'+\sum_k\vec e_k\,\partial/\partial Q_k$, and it composes with its conjugate to the d'Alembertian, $\tilde\nabla\tilde\nabla^{\natural}=\tilde\nabla^{\natural}\tilde\nabla=\Box=\partial^2/\partial Q_t^2+\Delta_Q$, read on that sector as $\Delta-c^{-2}\partial^2/\partial t'^2$. No derivative below is written in any other form.

The classical field theory is defined by the parent article's Lagrangian density. The field is $\psi$, with the two parts $\tilde\Psi_L$ and $\tilde\Psi_R$, and its **Dirac adjoint** is the right multiplication of $\psi^{\dagger}$ by the single element $i\vec e_x$,

$$
\bar\psi=\psi^{\dagger}i\vec e_x ,
\qquad
\bar\Psi_L=\tilde\Psi_L^{\dagger}i\vec e_x,\quad \bar\Psi_R=\tilde\Psi_R^{\dagger}i\vec e_x ,
$$

the time direction entering through it alone, because $e_t$ is the unit. With $\mathbb{D}$ the pair operator of *Operator and Calculus Conventions*, $\mathbb{D}(\tilde\Psi_L,\tilde\Psi_R)=(\tilde\nabla\tilde\Psi_R,\tilde\nabla^{\natural}\tilde\Psi_L)$, the density is

$$
\mathcal{L}=\mathrm{Sc}\big(\bar\Psi_L\,\tilde\nabla\tilde\Psi_R+\bar\Psi_R\,\tilde\nabla^{\natural}\tilde\Psi_L\big)-m\,\mathrm{Sc}\big(\bar\Psi_L\tilde\Psi_L+\bar\Psi_R\tilde\Psi_R\big),
$$

a real Lorentz scalar whose variation returns the two equations of the pair, with conjugate momentum $\pi=i\psi^\dagger$. For the path integral this is the object whose integral is the phase.

### The One-Sided Pair and the Two-Sided Equation

**The one-sided form.** The dynamics in the algebra is the pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L,
\qquad
\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R,
$$

two equations because the field has two parts. The subscript has two values, and only the zero element is both: $\tilde\Psi_L$ is the element of value minus one and $\tilde\Psi_R$ the element of value plus one. The field is their sum, $\tilde\Psi=\tilde\Psi_L+\tilde\Psi_R$. Both gradients act from the left, and the mass pairs the two parts. The Lagrangian above is the same dynamics, written once, not a second one.

**Its elimination.** The two equations are one system, and either part can be eliminated. The gradients compose to the d'Alembertian, $\tilde\nabla^{\natural}\tilde\nabla=\tilde\nabla\tilde\nabla^{\natural}=\Box$, so applying $\tilde\nabla^{\natural}$ to the first and using the second gives

$$
\Box\tilde\Psi_R=\tilde\nabla^{\natural}m\tilde\Psi_L=m^2\tilde\Psi_R,
$$

and the same step gives $(\Box-m^2)\tilde\Psi_L=0$. Each part of the field therefore solves the massive wave equation, and the operator whose determinant the path integral computes is the pair; the count of that determinant is taken in §*The Biquaternion Form of the Kernel*.

**The two-sided form.** Kravchenko's equation is a single equation on an algebra-valued field $F\in\mathbb{B}$,

$$
-\tilde\nabla^{\natural}F-m\,i\,\bar F\,\vec e_z=0,
$$

in which the gradient acts from the left, the mass acts from the right through $\vec e_z$, and the coefficient complex conjugate $\bar F$ supplies an antilinear part. Its mass multiplies on the other side from the mass of the pair above. The distinction is one of operators, not of fields: the pair acts from the left only and needs the two parts of the field; this operator acts from both sides and can be written on the algebra itself. It is a different operator, related to the pair by a real-linear dictionary and not by an identity; a functional integral written on it would carry the antilinear mass through every step, and is not attempted here.

### The Algebra Bilinear

With $\mathrm{Sc}$ the trace pairing and $\langle\cdot,\cdot\rangle_{\natural}$ the quaternionic form of the conventions, the action is the integral of the density above,

$$
S=\int \mathrm{Sc}\big(\bar\Psi_L\,\tilde\nabla\tilde\Psi_R+\bar\Psi_R\,\tilde\nabla^{\natural}\tilde\Psi_L\big)-m\!\!\int\mathrm{Sc}\big(\bar\Psi_L\tilde\Psi_L+\bar\Psi_R\tilde\Psi_R\big),
$$

and each kinetic term is one equation of the pair. The single-element form $\mathrm{Sc}(\tilde\Psi^{\natural}\tilde\nabla\tilde\Psi)$ with $\tilde\Psi=\tilde\Psi_L+\tilde\Psi_R$ is a different object, because it carries the two diagonal terms as well; the pair form is the one used here. The mass term is the second integral; it is quadratic in the field and linear in the mass, and it couples the two parts, as the parent article requires.

### The Pair Operator on the Algebra

The pair operator acts on the pair, not on one element. The conventions define it on $\mathbb{B}\oplus\mathbb{B}$,

$$
\mathbb{D}:\ (\tilde\Psi_L,\tilde\Psi_R)\longmapsto\big(\tilde\nabla\tilde\Psi_R,\ \tilde\nabla^{\natural}\tilde\Psi_L\big),
$$

the two gradients of the pair above, and its square is the d'Alembertian on each part, $\mathbb{D}^2=\Box I$, because the two gradients compose to $\Box$. Read on one element of the algebra the same object would need the derivative acting on both sides of that element; that reading is not the gradient, and it is not used here.

**The gradient is not scalar.** Written as a product of elements, $\tilde\nabla^2$ is not $\Box$: $e_t$ commutes with the three spatial units, so the mixed derivatives survive. Only the composition with the conjugate is scalar, and it is second order. The free equation therefore stays first order on one field, $\tilde\nabla\tilde F=0$, and the massive equation is the pair, with the mass pairing the two parts. No one-field first-order massive equation is written here, and none exists in this algebra.

**The symbol.** On the plane wave $\psi=\psi_0\exp(-iEt'+i\vec p\cdot\vec x)$ the gradient acts as left multiplication by the momentum element

$$
\tilde K=i\tilde P=-E\,e_t+i\vec p ,
\qquad
\tilde K\tilde K^{\natural}=E^2-|\vec p|^{2}=p^{2} ,
$$

with $\tilde P=iE\,e_t+\vec p$ the wave biquaternion. The derivatives bring $-E$ from the time coordinate, through $\partial/\partial Q_t=-i\partial/\partial t'$ followed by $\partial/\partial t'\to-iE$, and $+ip_k$ from each spatial one. The symbol of the pair is therefore

$$
\mathbb{D}_p:\ (w_L,w_R)\longmapsto\big(\tilde K\,w_R,\ \tilde K^{\natural}w_L\big),
$$

whose square is $p^2$ times the identity: each component is left multiplication by an element whose product with its conjugate is the scalar $p^2$, and the two orders of the pair agree. The square of the element is not the scalar, $\tilde K^2=E^2+|\vec p|^{2}-2E\,i\vec p$: its scalar part is $E^2+|\vec p|^{2}$ rather than $p^2$, and its vector part does not cancel. Only the composition with the conjugate returns $p^2$.

The transcription is a candidate, not a derivation: the parent article is explicit that the $\mathbb{B}$-intrinsic Lagrangian — the real scalar built from $\tilde{\nabla}\tilde{\Psi}$, $\tilde{\Psi}$, their conjugates and the trace or norm pairing — is *not* fixed by the algebra alone, and that the transcription above is the working setting. The path integral inherits that status: everything below is exact for it, and the question of which $\mathbb{B}$-intrinsic action it corresponds to is open, exactly as it is in the parent.

### Properties of the Action

Three properties of the action are used below.

**It is even.** The action is quadratic in the fermionic field, hence bosonic: it commutes with fermion parity and is a $c$-number functional of the field. This is why $\exp(iS)$ is a genuine phase and not an operator.

**Its phase is central.** $iS$ is a central element of $\mathbb{C}_{\mathbb{B}}$. The generalities companion's finding applies unchanged: the phase of the fermionic path integral is canonical, and it is not a choice of a spin axis.

**Its Hermiticity structure.** $\bar\psi\,\tilde\nabla\,\psi$ is Hermitian up to a total derivative and $\bar\psi\,m\,\psi$ is Hermitian. Both statements use the Dirac adjoint $\bar\psi=\psi^{\dagger}i\vec e_x$ of the parent article: the right multiplication by $i\vec e_x$ is Hermitian, $(i\vec e_x)^{*}=i\vec e_x$ and $(i\vec e_x)^2=e_t$, and it converts the conjugate into a Hermitian bilinear, the time direction entering through it alone because $e_t$ is the unit. The derivative is the caveat: the gradient is not self-adjoint, only self-adjoint up to the total derivative that integration by parts leaves, so the kinetic term carries the qualification and the mass term does not. After Wick rotation the kinetic operator is anti-Hermitian and the mass term remains Hermitian. The Euclidean operator squares to the d'Alembertian, which is scalar, so its eigenvalues are the square roots of the d'Alembertian's: purely imaginary, in pairs $\pm i\mu$ with $\mu^2=-\Box_{\mathrm{E}}>0$; a pair contributes $(m+i\mu)(m-i\mu)=m^2+\mu^2$ to $\det(\mathbb{D}_{\mathrm{E}}+m)$, with $\mathbb{D}_{\mathrm{E}}$ the pair of §*The Pair Operator on the Algebra* read at $t'=-i\tau$, and that determinant is real and positive for real $m$. A non-Hermitian deformation — a chemical potential, or a complex mass — breaks the pairing and gives the determinant a phase; the phase is the subject of §*Parity Sectors, the Phase and the Sign Problem*.

### Sources

The sources are Grassmann-valued: the generating functional

$$
Z[\eta,\bar\eta]=\int\mathcal{D}\psi^{\dagger}\,\mathcal{D}\psi\;\exp\Big[iS+i\!\int d^4x\,\big(\bar\eta\psi+\psi^{\dagger}i\vec e_x\eta\big)\Big]
$$

requires $\eta,\bar\eta$ to be odd, since they multiply $\psi,\psi^{\dagger}i\vec e_x$ respectively and the linear terms must be even. This is the same requirement as in the finite-mode reduction below, now at the level of the functional: the source term is a bilinear in one external odd and one integration variable, hence even, and the sources consequently lie in the odd part of the same Grassmann extension.

## The Berezin Measure

The histories are $\mathbb{B}$-valued fields whose coefficients are Grassmann numbers: for each spacetime point and each of the four coefficients, $\psi_a(x)$ and $\psi_a^{\dagger}(x)i\vec e_x$ are odd elements of the Grassmann algebra generated by the countably many generators $\{\theta_{a,x},\theta^*_{a,x}\}$, one pair per coefficient and point. The measure is the product of Berezin measures,

$$
\mathcal{D}\psi^{\dagger}\,\mathcal{D}\psi=\prod_{x}\prod_{a}d\psi_a^{\dagger}(x)\,d\psi_a(x) ,
$$

with the normalization $\int d\psi_a^{\dagger}\,d\psi_a\;\psi_a\psi_a^{\dagger}=1$ for each pair, mode by mode. The right multiplication by $i\vec e_x$ in the Dirac adjoint is one fixed involution of determinant one, so it changes no determinant; the finite-mode identities below are written on the coefficients. The product is formal, exactly as the sum over paths is; what is finite and exact is the reduction to a finite number of modes, which is what the computations below use.

Three consequences of oddness are worth isolating, because they are the whole difference between this integral and the bosonic one.

**The measure is not a positive measure.** Berezin integration is a linear functional, not integration against a weight. There is no positivity to lose and none to assume; the "measure" is an algebraic operation, and every statement below is a statement about a finite-dimensional integral in a Grassmann algebra.

**The Wick expansion terminates.** A Grassmann algebra element of degree $n$ has a top form, and products beyond the top degree vanish. For a finite number of modes the exponential truncates at the top degree, so every Gaussian below is an exact polynomial identity, not an asymptotic expansion. This is why the finite-mode checks are exact rather than approximate.

**Superselection is algebraic.** The Grassmann algebra splits into even and odd parts, and Berezin integration of a non-top element vanishes: $\int d\theta\,1=0$. An integral of a monomial therefore vanishes unless the monomial has exactly the top degree, and the parity of that degree is fixed by the number of generators. This is the path-integral form of fermion-parity superselection: an amplitude between states of different parity receives a vanishing integral, and the two parity sectors of the boundary data never mix.

## The Gaussian Integral and the Determinant

For a finite set of modes, write the quadratic action as

$$
S_0=\sum_{a,b}\psi_a^{\dagger}M_{ab}\psi_b ,
$$

where $M$ is the matrix of the bilinear, the right multiplication by $i\vec e_x$ in the adjoint being the involution just noted. In Euclidean signature the kernel is $\mathbb{D}_{\mathrm{E}}+m$, and in Minkowski signature $-i(\mathbb{D}-m)$; the factor $-i$ is a field-independent constant of unit modulus, so in Minkowski the determinant is that of $\mathbb{D}-m$ up to that constant. The Gaussian Berezin integral is the determinant:

$$
\boxed{\;\int\prod_ad\psi_a^{\dagger}\,d\psi_a\;\exp(-\psi^{\dagger}M\psi)=\det M\;}.
$$

The derivation is the terminating expansion: $\exp(-\psi^{\dagger}M\psi)=1-\psi^{\dagger}M\psi+\tfrac12(\psi^{\dagger}M\psi)^2-\cdots$, and only the term with exactly one of every generator survives the integral, whose coefficient is the Leibniz sum that defines $\det M$. The identity was verified for a general complex $2\times2$ matrix in the stated convention: the two sides agree to machine precision, ratio $1+0i$.

**The two-point function.** Dressing the Gaussian by one pair of fields gives the inverse kernel:

$$
\langle\psi_a\,\psi_b^{\dagger}\rangle=\frac{\int\prod d\psi^{\dagger}d\psi\;\exp(-\psi^{\dagger}M\psi)\,\psi_a\psi_b^{\dagger}}{\int\prod d\psi^{\dagger}d\psi\;\exp(-\psi^{\dagger}M\psi)}=\big(M^{-1}\big)_{ab} ,
$$

in the coefficient variables; the right multiplication by $i\vec e_x$ in the adjoint is the same involution of determinant one in the numerator and in the normalization of the measure, so it cancels from the amplitude.

The index order is part of the statement and was checked: for a random complex $2\times2$ $M$ the four amplitudes are the four entries of $M^{-1}$, in the order $\langle\psi_a\psi_b^{\dagger}\rangle=(M^{-1})_{ab}$, to nine decimals. The two off-diagonal amplitudes are sensitive to it because $M$ need not be symmetric: they are $(M^{-1})_{01}$ and $(M^{-1})_{10}$, and the anticommuting order of the measure is what fixes which field contracts with which index.

**The generating functional.** Completing the square in the Grassmann algebra — a finite algebraic operation, since the shift $\psi\to\psi+M^{-1}\eta$, $\psi^{\dagger}\to\psi^{\dagger}+\bar\eta M^{-1}$ is a shift by odd constants — gives the algebraic identity

$$
\boxed{\;\int\prod d\psi^{\dagger}\,d\psi\;\exp\!\big(-\psi^{\dagger}M\psi+\bar\eta\psi+\psi^{\dagger}\eta\big)=\det M\;\exp\!\big[\bar\eta\,M^{-1}\eta\big]\;},
$$

with the exponential terminating at the top degree in the sources: the bilinear $\bar\eta M^{-1}\eta$ has degree two, so the series stops at degree two for one mode and at degree $2N$ for $N$ modes.

In the physical weight of §*Sources*, $-\psi^{\dagger}M\psi$ becomes $iS$ and the sources become the odd ones of that section, $\bar\eta\psi+\psi^{\dagger}i\vec e_x\eta$. Each source therefore carries an explicit $i$, and the two multiply to $i^2=-1$: the exponent of the result changes sign. With $M=-i(\mathbb{D}-m)$ and $M^{-1}=S_F$,

$$
Z[\eta,\bar\eta]=\det M\;\exp\!\big[-\bar\eta\,M^{-1}\eta\big]
=\det(\mathbb{D}-m)\;\exp\!\Big[-\int d^4x\,d^4y\;\bar\eta(x)\,S_F(x-y)\,\eta(y)\Big]
$$

up to a field-independent constant. The Euclidean functional, with weight $\exp(-S_{\mathrm E}+\bar\eta\psi+\psi^{\dagger}i\vec e_x\eta)$, is the one that carries the plus sign.

### A Finite-Mode Computation

The statements above are finite algebraic identities, and it is worth exhibiting one instance with explicit numbers. Take two complex modes — four generators $\psi_1^{\dagger},\psi_1,\psi_2^{\dagger},\psi_2$ — and the kernel of entries

$$
M_{00}=1.3+0.2i,\quad M_{01}=0.4-0.1i,\quad M_{10}=0.7+0.3i,\quad M_{11}=0.9,
\qquad
\det M=0.86+0.13i .
$$

The representation used is the Grassmann algebra on the four generators with monomials represented by subsets and the Koszul sign carried by the reordering, and Berezin integration defined as the coefficient of the top form in the stated normalization. Then

$$
\int\prod_{a=1}^2 d\psi_a^{\dagger}\,d\psi_a\;\exp(-\psi^{\dagger}M\psi)=0.86+0.13i=\det M ,
$$

to machine precision (ratio $1+0i$), and the four two-point amplitudes divided by $\det M$, in the order $(a,b)=(0,0),(0,1),(1,0),(1,1)$, are $1.023132849-0.154659617i$, $-0.437541309+0.182419035i$, $-0.847323199-0.22075347i$ and $1.512227363+0.003965631i$, which are exactly $(M^{-1})_{00},(M^{-1})_{01},(M^{-1})_{10},(M^{-1})_{11}$. The middle two differ, as the index order requires: $M$ is not symmetric.

**For the field** the same result is the free generating functional of the propagator companion, with $S_F$ its configuration-space amplitude and the minus sign in the exponent the one just derived. The determinant, the trace-log and the systematic evaluation of the functional determinant are outside this article's subject; what belongs here is the biquaternion form of the result.

### The Biquaternion Form of the Kernel

Write the wave biquaternion $\tilde P=iE\,e_t+\vec p$, so that $\tilde P\tilde P^{\natural}=-p^2$. The symbol of the pair on the plane wave $\exp(-iEt'+i\vec p\cdot\vec x)$ is the left multiplication by $\tilde K=i\tilde P$ of §*The Pair Operator on the Algebra*, with $\tilde K\tilde K^{\natural}=p^2$, so the symbol squares to $p^2$ times the identity, $(\mathbb{D}_p-m)(\mathbb{D}_p+m)=(p^2-m^2)I$, and the kernel of $\mathbb{D}-m$ at momentum $p$ is $(\mathbb{D}_p+m)/(p^2-m^2)$. The Gaussian weight of the finite-mode section carries $M=-i(\mathbb{D}-m)$, so the free two-point amplitude is

$$
S_F(p)=\frac{i(\mathbb{D}_p+m)}{p^2-m^2+i\epsilon}=-\frac{i(\mathbb{D}_p+m)}{\tilde P\tilde P^{\natural}+m^2-i\epsilon}.
$$

The propagator companion writes its own amplitude as $\mathcal{A}_p+m$ over the same denominator, with $\mathcal{A}_p$ an action whose energy term multiplies $\vec e_x$ on the right and whose momentum terms multiply $\vec e_k$ on the left and $\vec e_y$ on the right, and the symbol here is the left action of the gradient on each part of the pair. The two are not the same map, and they share the pole set because the square of each is multiplication by $p^2$. Written with the units, the numerator $-i(\mathbb{D}_p+m)(w_L,w_R)$ has its two imaginary units multiplied to $-1$ and becomes

$$
S_F(p):\ (w_L,w_R)\longmapsto\frac{\big(\tilde P\,w_R-im\,w_L,\ \tilde P^{\natural}w_L-im\,w_R\big)}{\tilde P\tilde P^{\natural}+m^2-i\epsilon},
$$

its denominator being $-p^2+m^2-i\epsilon$; multiplying numerator and denominator by $-1$ returns the preceding form.

The determinant is therefore that of the operator whose inverse is $S_F$ up to the overall $i$ that the Minkowski weight carries, with the deformed mass-shell denominator; the deformation lies along the $ict'$ axis of the material sector. The pair squares to the d'Alembertian, $\mathbb{D}^2=\Box I$, so its eigenvalues on a plane wave are $\pm\mu$ with $\mu^2=p^2$, in four opposite pairs, and each pair contributes $(\mu-m)(-\mu-m)=m^2-\mu^2$. The determinant is thus the fourth power of the scalar mode factor,

$$
\det\big(\mathbb{D}-m\big)=\big(p^2-m^2\big)^4=\det\big(\Box-m^2\big)
=\exp\Big[4\!\int\frac{d^4p}{(2\pi)^4}\,\ln\big(\tilde P\tilde P^{\natural}+m^2-i\epsilon\big)\Big],
$$

formally, up to a field-independent constant and with the standard subtractions understood; the fourth power is a count of the four pairs of opposite eigenvalues, not of any decomposition of the field. The generalities companion's finding is inherited: the algebra names the axis of the deformation, the boundary condition chooses its orientation, and the determinant does not distinguish them.

## The Pfaffian and the Real Structure

For a field whose quadratic form is antisymmetric, the Gaussian is a square root of a determinant. This is not a special case invented for the fermionic path integral. The algebra supplies the possibility: $\flat=-{}^{*}$ is an antilinear involution whose fixed space is the material sector $\mathbb{M}_-$, and a coupling that pairs a field with its own conjugate, rather than with an independent second field, has the shape of a Majorana mass. The pairing itself is the antisymmetric part of the product of the field with its conjugate, which is the form $\flat$ puts at the disposal of the algebra. The reality condition $\psi^{\mathrm c}=\psi$ is the coefficient conjugation $\bar{\cdot}$, not $\flat$, and the companion article *The Neutrino and Majorana Fermions in Biquaternionic Form* keeps the two apart. What the algebra supplies here is the existence of the pairing, not its sign or its normalization.

**The integral of an antisymmetric form.** For $2N$ generators $\psi_1,\dots,\psi_{2N}$ and an antisymmetric matrix $A$,

$$
\boxed{\;\int d\psi_{2N}\cdots d\psi_1\;\exp(\,-\frac12\psi A\psi)=\mathrm{Pf}(A)\;},
$$

with the normalization $\int d\psi_{2N}\cdots d\psi_1\,\psi_{2N}\cdots\psi_1=1$, and with $\mathrm{Pf}$ the Pfaffian. The ordering of the differentials is what fixes the sign: reversing the order of $2N$ generators has sign $(-1)^{N(2N-1)}=(-1)^N$, so the right-hand side is multiplied by $(-1)^N$. The square is convention-independent,

$$
\mathrm{Pf}(A)^2=\det A .
$$

For a random complex antisymmetric $4\times4$ the Grassmann integral equals the closed-form Pfaffian $\mathrm{Pf}=A_{12}A_{34}-A_{13}A_{24}+A_{14}A_{23}$ with ratio $1.0000000000000002+2.3\times10^{-17}i$; and $\mathrm{Pf}^2-\det A$ vanishes to $5\times10^{-16}$. The Pfaffian is thus the exact result of a finite Berezin integral, and it is the natural output of the measure for a field that is its own conjugate.

**The sign of the Pfaffian.** Unlike $\det$, $\mathrm{Pf}$ has a sign that is not determined by the magnitudes, and the sign is fixed by the ordering of the generators — that is, by the *conventions of the measure*, not by the algebra. Two consequences are worth recording.

First, the sign is a genuine physical input wherever the Pfaffian is the answer: it is the sign that separates the two parity sectors of a Majorana field, and it flips under an odd permutation of the generators (equivalently, of the differentials). The article keeps the order fixed and records that the sign is not an algebra-invariant.

Second, the algebra's own statement is the *existence* of the antisymmetric pairing, not its sign. The real structure $\flat$ supplies the existence of a field-to-its-conjugate pairing; the measure normalizes it; the orientation is a convention. This is the same three-way division the propagator companion records for the $i\epsilon$, and the algebra's contribution is again the middle term.

**The biquaternion form.** The pairing is the antisymmetric form that the algebra puts on the field and its own conjugate, the object $\flat$ makes available, and the Pfaffian is its Berezin integral; its square is the determinant of the pair operator whose inverse is $S_F$. The Majorana quantization is therefore the statement that the pairing is available; the Dirac quantization is the statement that it is not used, the two parts of the field being independent.

## The Euclidean Integral and the Boundary Conditions

**Wick rotation.** With $t'\to-i\tau$ the $ict'$ direction of $\mathbb{M}_-$ becomes the real quaternion direction, as the Wick-rotation companion establishes, and the oscillatory weight becomes a decaying one:

$$
\exp(\,iS)\;\longrightarrow\;\exp(\,-S_{\mathrm{E}}),
\qquad
S_{\mathrm{E}}=\int d\tau\,d^3x\;\mathrm{Sc}\big(\bar\Psi_L\,\tilde\nabla_{\mathrm{E}}\tilde\Psi_R+\bar\Psi_R\,\tilde\nabla_{\mathrm{E}}^{\natural}\tilde\Psi_L+m\,(\bar\Psi_L\tilde\Psi_L+\bar\Psi_R\tilde\Psi_R)\big),
$$

with $\tilde\nabla_{\mathrm{E}}$ the same gradient read at $t'=-i\tau$, the kinetic operator anti-Hermitian and the mass term Hermitian, and the plus sign on the mass the one that makes the kernel $M=\mathbb{D}_{\mathrm{E}}+m$ of the Gaussian. The Euclidean determinant is therefore real, and positive for real $m$; a continuous phase appears only when a non-Hermitian deformation is added.

**Antiperiodic boundary conditions.** The Euclidean fermionic integral that computes a thermal trace is taken over fields on a circle of circumference $\beta=1/T$ with the fermions antiperiodic,

$$
\psi(\tau+\beta)=-\psi(\tau) ,
$$

which is the same statement as the Matsubara frequencies $\omega_n=(2n+1)\pi/\beta$, and the same sign as the anticommutator. The identity $e^{i\omega_n\beta}=-1$ holds exactly for every integer $n$; it was checked for $n=0,1,2$. The boundary condition is what makes the Euclidean determinant a product over half-integer Matsubara modes rather than integer ones, and it is the path-integral statement of the spin–statistics pairing.

**The partition function.** On the Euclidean circle the free integral is a determinant,

$$
Z(\beta)=\int_{\text{antiperiodic}}\mathcal{D}\psi^{\dagger}\mathcal{D}\psi\;\exp(-S_{\mathrm{E}})
=\det\big(\mathbb{D}_{\mathrm{E}}+m\big)_{\text{AP}} ,
$$

whose logarithm gives the free energy up to the factor $-\beta$. The identity is the standard finite-temperature reduction of the fermionic integral and is recorded, not recomputed; what the biquaternion framework adds is again only the location of the deformation and the centrality of the phase. The companion article *The KMS Condition and the Biquaternion Framework* treats the analytic structure that the antiperiodicity generates.

## Parity Sectors, the Phase and the Sign Problem

The measure carries the parity, and the two fermion-parity sectors appear as a **relative sign**, not as two integrands. In the paired measure an integral of an odd element vanishes, so the Gaussian integrand $\exp(-\psi^{\dagger}i\vec e_xM\psi)$, being even, is the same functional in both sectors; what distinguishes them is the *boundary condition* in imaginary time. The two basic traces are

$$
\boxed{\;\mathrm{Tr}\,\exp(-\beta H^{\mathrm{fop}})
=\int_{\text{antiperiodic}}\mathcal{D}\psi^{\dagger}\mathcal{D}\psi\;\exp(-S_{\mathrm{E}}) ,
\qquad
\mathrm{Tr}\,(-1)^{F^{\mathrm{fop}}}\exp(-\beta H^{\mathrm{fop}})
=\int_{\text{periodic}}\mathcal{D}\psi^{\dagger}\mathcal{D}\psi\;\exp(-S_{\mathrm{E}})\;},
$$

so the antiperiodic fields compute the ordinary thermal trace and the periodic fields the parity-weighted (Witten) trace; the two differ by the relative sign of the even and odd sectors. This is the path-integral form of the parity split that the parent Fock-space article records. It is also the reason a **Majorana** field's integral is a Pfaffian while a **Dirac** field's is a determinant: the Dirac field's $\psi$ and $\psi^{\dagger}i\vec e_x$ are independent, so its measure pairs two independent sets of generators and yields a determinant; the Majorana field is its own conjugate, so the same pairing is antisymmetric within one set and yields the square root. The subscript enters separately, through the mass term, which couples the two parts of the field.

**Where the determinant sits.** The fermionic partition function carries $\det M$ in the numerator, whereas a bosonic one carries $(\det M)^{-1/2}$ for a real field or $(\det M)^{-1}$ for a complex field. In the exponent of $Z$ the fermion therefore contributes $+\mathrm{Tr}\ln M$ and a complex boson $-\mathrm{Tr}\ln K$ (a real boson $-\tfrac12\mathrm{Tr}\ln K$), so the two enter loop corrections with opposite signs. This is not a bookkeeping accident but a consequence of the measure: the bosonic measure is a positive weight and the integral of a decaying Gaussian is small when the kernel is large, while the Berezin integral of a Gaussian is the determinant itself. It is the origin, at the level of the generating functional, of the opposite vacuum-energy contributions of bosons and fermions, and it was checked in the finite-mode computation above, where the integral returned $\det M$ rather than its inverse.

The phase of the determinant is where the fermionic integral's analytic content sits, and the generalities companion's finding governs it. A kernel that is Hermitian, or anti-Hermitian with a real square, has a determinant real up to a sign; a genuinely non-Hermitian one — a chemical potential, or a complex mass — has a complex determinant, and in the finite-density case its phase is the origin of the sign problem of lattice fermions. The biquaternion interpretation is narrow and honest: the central $i$ fixes the *form* of the phase, the imaginary axis of $\mathbb{M}_-$ is where the $i\epsilon$ deformation sits, and the algebra does not evaluate the phase. The transformation of the measure under an axial rotation, and the anomalies that follow when the measure fails to be invariant, are outside this article's subject.

## What Is Standard and What Is the Algebra's Own

**Standard, transcribed.** The Grassmann (Berezin) formulation of the fermionic integral; the Gaussian and its determinant; the two-point function as the inverse kernel; the generating functional with Grassmann sources; the Pfaffian for an antisymmetric form and $\mathrm{Pf}^2=\det$; the Wick rotation and the antiperiodic finite-temperature determinant; the parity traces and the phase (sign) problem. All of it is standard, and all of it is written in the parents' conventions.

**The algebra's own.**

- *The sector and centrality statements.* The phase $iS$ is central and lies in $\mathbb{M}_-$ along the $ict'$ axis; the action is even; the sources are odd and live in the Grassmann extension. These are the generalities companion's findings applied to the fermionic case, and they are the only place where the algebra's structure enters.
- *The real structure that makes the pairing available.* That the algebra offers a field-to-its-own-conjugate pairing at all is what $\flat=-{}^{*}$ makes available; that the resulting integral is a Pfaffian is the consequence.
- *The biquaternion form of the kernel.* The deformed mass-shell denominator inherited from the propagator companion, with the symbol of the gradient written on the units, $w\mapsto\tilde K w$ on each part of the pair, and its square the mass shell.

**Open.**

- **The sign of the Pfaffian.** Fixed by the measure convention, not by the algebra. Whether some biquaternion-natural normalization of the measure fixes it is open.
- **The infinite-mode measure.** The Berezin measure is defined mode by mode; its continuum limit, its regularization and its transformation properties are not supplied by the algebra, as the generalities companion states.
- **The phase.** The evaluation of the determinant's phase, and the anomalies associated with the measure, require the standard methods and are outside the framework's reach at this level.
- **Empirical content.** Whether any of the transcribed formulas differs observably from the standard field theory is the framework's standing open question, and nothing here changes it.

## Companion Articles

- Companion article *The Feynman Propagator in Biquaternionic Form*, for the contour prescription and the propagator conventions used in the kernel.
- Companion article *The Path Integral in Biquaternionic Form*, for the bosonic generating functional whose Grassmann counterpart is constructed here.
- Companion article *The Dirac Equation in Biquaternionic Form*, for the one-sided pair, the two-sided dictionary, and the frame in which the mass couples the two parts.
- Companion article *The Neutrino and Majorana Fermions in Biquaternionic Form*, for the reality condition $\psi^{\mathrm c}=\psi$ and for the distinction between $\flat$ and the coefficient conjugation.
- Companion article *The Functional Determinant in Biquaternionic Form*, for the determinant and its product over modes.
- Companion article *Interpretation of the Wick Rotation in the Biquaternion Universe*, for the imaginary-time direction and the Euclidean formulation.
- Companion article *The KMS Condition and the Biquaternion Framework*, for the antiperiodic boundary condition and the Matsubara structure that the fermionic measure carries.

## Summary

The fermionic path integral of the biquaternion spin-$\tfrac12$ field is the Berezin integral over Grassmann-valued biquaternion histories of the phase $\exp(iS)$, with the biquaternion Dirac action as the bilinear $S=\int\mathrm{Sc}(\bar\Psi_L\tilde\nabla\tilde\Psi_R+\bar\Psi_R\tilde\nabla^{\natural}\tilde\Psi_L)-\int m\,\mathrm{Sc}(\bar\Psi_L\tilde\Psi_L+\bar\Psi_R\tilde\Psi_R)$ and the sources odd. The equation integrated is the **one-sided** pair over the two parts of the field; Kravchenko's **two-sided** equation is a different operator, related to it by a real-linear dictionary, and is not integrated here. The phase is central and lies in $\mathbb{M}_-$ along the $ict'$ axis; the action is even, so the parity sectors do not mix and an odd integral vanishes.

The Gaussian is the determinant, verified exactly for a general complex $2\times2$ matrix in the convention $\int d\theta^*d\theta\,\theta\theta^*=1$; the two-point function is the inverse kernel in the stated index order, $\langle\psi_a\psi_b^{\dagger}\rangle=(M^{-1})_{ab}$, verified to nine decimals; the generating functional is $Z[\eta,\bar\eta]=\det M\exp[-\bar\eta M^{-1}\eta]$ in the Minkowski weight, with the plus sign in the Euclidean one; and for the field the kernel is the companion's amplitude carried on the two parts of the field

$$
S_F(p):\ (w_L,w_R)\longmapsto\frac{\big(\tilde P\,w_R-im\,w_L,\ \tilde P^{\natural}w_L-im\,w_R\big)}{\tilde P\tilde P^{\natural}+m^2-i\epsilon},
$$

with the two imaginary units of $-i(\mathbb{D}_p+m)$ multiplied to $-1$. The determinant of the pair operator is $(p^2-m^2)^4$, which is $\det(\Box-m^2)$ on the same carrier, because the pair squares to $p^2$, so its eigenvalues are $\pm\mu$ in four opposite pairs and each pair contributes $m^2-\mu^2$.

For an antisymmetric quadratic form the integral is a Pfaffian: $\int d\psi\,\exp(-\frac12\psi A\psi)=\mathrm{Pf}(A)$ and $\mathrm{Pf}^2=\det A$, both recomputed (the first to $10^{-16}$, the second to $5\times10^{-16}$). This is the algebra's real-structure pairing at work: $\flat$ makes available the field-to-its-own-conjugate pairing, the measure normalizes it, and the sign is a convention rather than an algebra invariant. The Wick rotation turns the oscillatory weight into a decaying one, and the thermal integral is a determinant with antiperiodic boundary conditions, $\psi(\tau+\beta)=-\psi(\tau)$; the identity $e^{i\omega_n\beta}=-1$ is exact for every integer $n$ and equivalent to $\omega_n=(2n+1)\pi/\beta$.

The algebra contributes the centrality of the phase, the sector location of the deformation, and the existence of the pairing. It does not supply the measure, the evaluation of the determinant, or the phase, and the article says so.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{L}=\mathrm{Sc}\big(\bar\Psi_L\tilde\nabla\tilde\Psi_R+\bar\Psi_R\tilde\nabla^{\natural}\tilde\Psi_L\big)-m\,\mathrm{Sc}\big(\bar\Psi_L\tilde\Psi_L+\bar\Psi_R\tilde\Psi_R\big)$ | Biquaternion Dirac density (bilinear action), written on the two parts of the field |
| $\bar\psi=\psi^{\dagger}i\vec e_x$ | Dirac adjoint: a single right multiplication by $i\vec e_x$ |
| $\tilde\nabla$, $\tilde\nabla^{\natural}$, $\Box=\tilde\nabla\tilde\nabla^{\natural}$ | The corpus gradient, its conjugate and the d'Alembertian; the only derivative in the article |
| $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$, $\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R$ | One-sided pair; the equation integrated |
| $-\tilde\nabla^{\natural}F-mi\,\bar F\,\vec e_z=0$ | Two-sided (Kravchenko) equation; different operator, not integrated |
| $\exp(iS)$ | Path-integral phase; central, in $\mathbb{C}_{\mathbb{B}}$, exponent along $ict'$ |
| $\eta,\bar\eta$ | Odd (Grassmann) sources |
| $\mathcal{D}\psi^{\dagger}\mathcal{D}\psi=\prod_x\prod_ad\psi_a^{\dagger}(x)\,d\psi_a(x)$ | Berezin measure |
| $\int d\theta^*d\theta\,\theta\theta^*=1$ | Berezin normalization used throughout |
| $\int\prod d\psi^{\dagger}d\psi\,\exp(-\psi^{\dagger}M\psi)=\det M$ | Gaussian = determinant |
| $\langle\psi_a\psi_b^{\dagger}\rangle=(M^{-1})_{ab}$ | Two-point function (inverse kernel, stated index order); the adjoint's right multiplication cancels from the ratio |
| $Z[\eta,\bar\eta]=\det M\,\exp[-\bar\eta M^{-1}\eta]$ | Free generating functional in the Minkowski weight; the Euclidean one carries $+\bar\eta M^{-1}\eta$ |
| $Z_0[\eta,\bar\eta]=\det(\mathbb{D}-m)\exp[-\int\bar\eta S_F\eta]$ | Field-level free functional |
| $\tilde K=i\tilde P=-E\,e_t+i\vec p$, $\tilde K\tilde K^{\natural}=p^2$ | Symbol of the gradient on a plane wave |
| $\mathbb{D}_p:\ (w_L,w_R)\mapsto(\tilde K\,w_R,\tilde K^{\natural}w_L)$ | Symbol of the pair operator; its square is $p^2$ times the identity, with $p^2=E^2-|\vec p|^{2}$ |
| $\mathbb{D}:\ (\tilde\Psi_L,\tilde\Psi_R)\mapsto(\tilde\nabla\tilde\Psi_R,\tilde\nabla^{\natural}\tilde\Psi_L)$ | The pair operator on $\mathbb{B}\oplus\mathbb{B}$, that is $\mathbb{D}_{\tilde\nabla}$: the factor is the material gradient, which is why no subscript is written; $\mathbb{D}^2=\Box I$ |
| $S_F(p):\ (w_L,w_R)\mapsto\frac{(\tilde P\,w_R-im\,w_L,\ \tilde P^{\natural}w_L-im\,w_R)}{\tilde P\tilde P^{\natural}+m^2-i\epsilon}$ | Kernel; the two imaginary units of $-i(\mathbb{D}_p+m)$ multiply to $-1$ |
| $\mathbb{D}_{\mathrm{E}}:\ (\tilde\Psi_L,\tilde\Psi_R)\mapsto(\tilde\nabla_{\mathrm{E}}\tilde\Psi_R,\ \tilde\nabla_{\mathrm{E}}^{\natural}\tilde\Psi_L)$ | The pair read at $t'=-i\tau$; $\mathbb{D}_{\mathrm{E}}^2=\Box_{\mathrm{E}}I$ |
| $\det(\mathbb{D}-m)=(p^2-m^2)^4=\det(\Box-m^2)$ | Determinant; the four opposite eigenvalue pairs of the pair give the fourth power of the scalar mode factor |
| $\int d\psi_{2N}\cdots d\psi_1\,\exp(-\frac12\psi A\psi)=\mathrm{Pf}(A)$, $\mathrm{Pf}^2=\det A$ | Pfaffian for an antisymmetric form |
| $\flat=-{}^{*}$ | Real structure; makes the field-to-conjugate pairing available |
| $\exp(iS)\to \exp(-S_{\mathrm{E}})$ | Wick rotation ($ict'$ direction becomes real) |
| $\psi(\tau+\beta)=-\psi(\tau)$, $\omega_n=(2n+1)\pi/\beta$ | Antiperiodic thermal boundary condition |
| $Z(\beta)=\det(\mathbb{D}_{\mathrm{E}}+m)_{\text{AP}}$ | Finite-temperature free partition function |

## Further Reading

- F. A. Berezin, *The Method of Second Quantization* (Academic Press, 1966), for Berezin integration, the Gaussian determinant, and the fermionic path integral.
- L. D. Faddeev and A. A. Slavnov, *Gauge Fields: Introduction to Quantum Theory* (Benjamin/Cummings, 1980), for the fermionic functional integral, the determinant, and its relation to the effective action.
- J. W. Negele and H. Orland, *Quantum Many-Particle Systems* (Addison-Wesley, 1988), for the Grassmann path integral, the generating functional, and the Matsubara boundary conditions.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the fermionic path integral, the determinant of the Dirac operator, and the sources in the convention used here.
- J. Zinn-Justin, *Quantum Field Theory and Critical Phenomena* (Oxford, 2002), for the systematic treatment of the fermionic determinant and its phase.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 2 (Cambridge, 1996), for the functional-integral formulation, anomalies and the transformation of the measure.
- J. Polchinski, *String Theory*, Vol. 1 (Cambridge, 1998), for the Pfaffian of an antisymmetric quadratic form and its use for Majorana fermions.
- E. Witten, "Fermion path integrals and topological phases," *Reviews of Modern Physics* **88** (2016) 035001, for the Pfaffian, its sign, and the parity sectors of a fermionic integral.
- M. Lüscher, "Properties and uses of the Wilson flow in lattice QCD," *Journal of High Energy Physics* **08** (2010) 071, and P. de Forcrand, "Simulating QCD at finite density," *Proceedings of Science* **LAT2009** (2009) 010, for the phase (sign) problem of the finite-density determinant.
