# __The Fermionic Path Integral in Biquaternionic Form__

## Introduction

The companion article *The Path Integral in Biquaternionic Form* settles what the biquaternion algebra can and cannot contribute to a path integral: the phase factor $\exp(iS/\hbar)$ is a *central* $*$-unitary element, because the central scalar imaginary is the algebra's unique complex structure up to sign; the exponent lies along the $ict'$ direction of the material sector $\mathbb{M}_-$; and the measure, the action and the space of paths are not supplied by the algebra, because $\mathbb{B}$ is finite-dimensional and the space of histories is not. The companion article *The Feynman Propagator in Biquaternionic Form* adds where the $i\epsilon$ lives and that the algebra names its axis without choosing its orientation. The companion article *Interpretation of the Wick Rotation in the Biquaternion Universe* adds that $t'\to-i\tau$ is the relabeling of the imaginary-time coefficient as a real one, turning the material sector into the quaternion subspace.

This article applies those findings to the spin-$\tfrac12$ field, where the histories are **anticommuting**. The fermionic path integral differs from the bosonic one in exactly one structural place — the integration variables are odd, so the integral is Berezin's rather than Lebesgue's — and that one difference propagates into every formula. The article establishes:

- **The action and its sector.** The biquaternion Dirac action as a bilinear; the **one-sided** chiral pair, which is what the integral integrates, and the **two-sided** (Kravchenko) equation, which it does not; the phase $iS$ as an element of $\mathbb{M}_-$ along the $ict'$ axis; and the action as an even (bosonic) functional of the fermionic field.
- **The Berezin measure.** Fermionic histories are Grassmann-valued biquaternion fields; the measure is the Berezin measure on the Grassmann extension of the coefficient algebra, and in the finite-mode reduction it is $\prod_a d\bar\psi_a\,d\psi_a$ with the convention fixed once.
- **The Gaussian integral and the determinant.** Completing the square in the Grassmann algebra gives the free generating functional, the two-point function as the inverse kernel, and the determinant of the Dirac operator; the finite-mode statements were recomputed exactly.
- **The Pfaffian and the real structure.** For a field whose quadratic form is antisymmetric — the Majorana case, for which the algebra supplies the field-to-its-conjugate pairing — the integral is a Pfaffian, with $\mathrm{Pf}^2=\det$ and a sign that carries physical content.
- **The Euclidean integral and the parity sectors.** Wick rotation and the antiperiodic (Matsubara) boundary conditions, the two fermion-parity traces and the boundary conditions that select them, and the phase of the determinant.

The boundary with the neighbouring subjects is sharp and is stated where it occurs: the systematic evaluation of the functional determinant, the transformation of the measure under field redefinitions, and the anomalies that follow from it are not treated here.

## The Action in Biquaternion Form

Throughout, $i$ is the central scalar imaginary of $\mathbb{B}$, with $i^2=-1$. Wherever two imaginary units meet, they are multiplied to $-1$; a display that still shows both is the step before that reduction.

The classical field theory is defined by the parent article's Lagrangian density,

$$
\mathcal{L}=\bar\psi\,(\mathbb{D}-m)\,\psi ,
$$

a real Lorentz scalar whose variation returns $(\mathbb{D}-m)\psi=0$, with conjugate momentum $\pi=i\psi^\dagger$. For the path integral this is the object whose integral is the phase.

### The One-Sided Pair and the Two-Sided Equation

**The one-sided form.** The dynamics in the algebra is the chiral pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L,
$$

$$
\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R,
$$

two equations because there are two chiral halves. Both gradients act from the left, the field is the module-valued $\tilde\Psi=\tilde\Psi_L+\tilde\Psi_R$, the mass pairs the two chiral halves, and chirality is the cell $\gamma_5=-iR_{\vec e_z}^{\mathrm{axf}}$, the central grading of the complexified algebra being that operator's central form. The Lagrangian above is the spinor-module representative of this pair, not a second dynamics.

**Its module form.** On the module the pair becomes one equation, because the single cell operator $\mathbb{D}$ carries both gradients. The gradient operator is odd under the chirality grading — it carries each chiral half into the other — while the mass is a multiple of the identity on the pair and so is even; in the chiral basis $\mathbb{D}-m$ is therefore the block matrix with $-m$ on the diagonal and the two gradients off it,

$$
\mathbb{D}-m=\begin{pmatrix}-m & \tilde\nabla\\ \tilde\nabla^{\natural} & -m\end{pmatrix},
$$

whose vanishing on $\psi$ is the pair again. This is the operator whose determinant the path integral computes, and the block form is what makes that determinant a product over the two halves.

**The two-sided form.** Kravchenko's equation is a single equation on an algebra-valued field $F\in\mathbb{B}$,

$$
-\tilde\nabla^{\natural}F-m\,i\,\bar F\,\vec e_z=0,
$$

in which the time derivative and the spatial gradient act from the left, the mass acts from the right through $\vec e_z$, and the coefficient complex conjugate $\bar F$ supplies an antilinear part. Its chirality is carried by the right multiplication by $\vec e_z$, the dictionary's volume element; it is not the central grading of the one-sided pair. The distinction is one of operators, not of fields: the one-sided operator acts from the left only and needs the module and its two chiral halves; the two-sided operator acts from both sides and can be written on the algebra itself. It is a different operator, related to the pair by a real-linear dictionary and not by an identity; a functional integral written on it would carry the antilinear mass through every step, and is not attempted here.

### The Algebra Bilinear

With $\mathrm{Sc}$ as the trace pairing — the quaternionic form $\langle\tilde\Psi,\tilde\Phi\rangle_{\natural}=\mathrm{Sc}(\tilde\Psi^{\natural}\tilde\Phi)$ — the candidate algebra reading is

$$
S=\int \mathrm{Sc}\big(\tilde\Psi^{\natural}\tilde\nabla\tilde\Psi\big)-m\!\!\int\mathrm{Sc}\big(\tilde\Psi^{\natural}\tilde\Psi\big),
$$

whose spinor-module representative is the Lagrangian above. The mass term is the second integral; it is quadratic in the field and linear in the mass, and it couples the two chiral halves, as the parent article requires.

### The Pair Operator in Cells

On the module the pair operator is a cell operator. With $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and with $\nu(t)=x$ and $\nu(k)=y$, each coordinate frame cell is $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$. The operator also carries an explicit $i$ in every term, so two imaginary units meet; since $i^2=-1$,

$$
i\,\big(iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\big)=i^2L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}=-L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}.
$$

The cell form therefore carries no imaginary unit:

$$
\mathbb{D}=-L_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}\frac{\partial}{\partial t'}-\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\frac{\partial}{\partial Q_k}.
$$

The operator is the same dynamics, written once; the five frame cells are named in §*The Legacy Gamma Formulation*. Contractions below carry the frame's sign vector: with $\varepsilon_\mu=g_{\mu\mu}$ and $\varepsilon=(+1,-1,-1,-1)$, a contraction of two lower indices carries $\varepsilon_\mu$, so that $\sum_\mu\varepsilon_\mu L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}p_\mu=R_{\vec e_x}^{\mathrm{axf}}E-\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}p_k$. The sign is not decoration: the plane wave produces it. The transcription is a candidate, not a derivation: the parent article is explicit that the $\mathbb{B}$-intrinsic Lagrangian — the real scalar built from $\tilde{\nabla}\tilde{\Psi}$, $\tilde{\Psi}$, their conjugates and the trace or norm pairing — is *not* fixed by the algebra alone, and that the module transcription is the working setting. The path integral inherits that status: everything below is exact for the module transcription, and the question of which $\mathbb{B}$-intrinsic action it corresponds to is open, exactly as it is in the parent.

### Properties of the Action

Three properties of the action are used below.

**It is even.** The action is quadratic in the fermionic field, hence bosonic: it commutes with fermion parity and is a $c$-number functional of the field. This is why $\exp(iS)$ is a genuine phase and not an operator.

**Its phase is central.** $iS$ is a central element of $\mathbb{C}_{\mathbb{B}}$. The generalities companion's finding applies unchanged: the phase of the fermionic path integral is canonical, and it is not a choice of a spin axis.

**Its Hermiticity structure.** $\bar\psi\,\mathbb{D}\,\psi$ is Hermitian up to a total derivative and $\bar\psi m\psi$ is Hermitian. Both statements use the Dirac adjoint $\bar\psi=\psi^{\dagger}(iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}})$ of the parent article: the cell $iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ is Hermitian and converts the conjugate into a Hermitian bilinear, while the spatial cells $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ are anti-Hermitian, which is why the derivative term needs the total-derivative caveat. That same cell anticommutes with the chirality cell, so $\bar\psi$ sits in the chiral half opposite to $\psi$, and the mass bilinear $\bar\psi m\psi$ mixes the two halves even though the operator $m$ is even. After Wick rotation the kinetic operator is anti-Hermitian and the mass term remains Hermitian. The Euclidean kinetic operator anticommutes with the chirality grading (the central grading of the complexified algebra), so its spectrum is symmetric about zero; its eigenvalues are $\pm i\mu$ with $\mu$ real, and each pair contributes $(m+i\mu)(m-i\mu)=m^2+\mu^2$, so the determinant of $\mathbb{D}_{\mathrm{E}}+m$ is real and positive for real $m$. A non-Hermitian deformation — a chemical potential, or a complex mass — breaks that symmetry and gives the determinant a phase; the phase is the subject of §*Parity Sectors, the Phase and the Sign Problem*.

### Sources

The sources are Grassmann-valued: the generating functional

$$
Z[\eta,\bar\eta]=\int\mathcal{D}\bar\psi\,\mathcal{D}\psi\;\exp\Big[iS+i\!\int d^4x\,\big(\bar\eta\psi+\bar\psi\eta\big)\Big]
$$

requires $\eta,\bar\eta$ to be odd, since they multiply $\psi,\bar\psi$ respectively and the linear terms must be even. This is the same requirement as in the finite-mode reduction below, now at the level of the functional: the source term is a bilinear in one external odd and one integration variable, hence even, and the sources consequently lie in the odd part of the same Grassmann extension.

## The Berezin Measure

The histories are $\mathbb{B}$-valued fields whose coefficients are Grassmann numbers: for each spacetime point and each module component, $\psi_a(x)$ and $\bar\psi_a(x)$ are odd elements of the Grassmann algebra generated by the countably many generators $\{\theta_{a,x},\theta^*_{a,x}\}$, one pair per component and point. The measure is the product of Berezin measures,

$$
\mathcal{D}\bar\psi\,\mathcal{D}\psi=\prod_{x}\prod_{a}d\bar\psi_a(x)\,d\psi_a(x) ,
$$

with the normalization $\int d\bar\psi_a\,d\psi_a\;\psi_a\bar\psi_a=1$ for each pair, mode by mode. The product is formal, exactly as the sum over paths is; what is finite and exact is the reduction to a finite number of modes, which is what the computations below use.

Three consequences of oddness are worth isolating, because they are the whole difference between this integral and the bosonic one.

**The measure is not a positive measure.** Berezin integration is a linear functional, not integration against a weight. There is no positivity to lose and none to assume; the "measure" is an algebraic operation, and every statement below is a statement about a finite-dimensional integral in a Grassmann algebra.

**The Wick expansion terminates.** A Grassmann algebra element of degree $n$ has a top form, and products beyond the top degree vanish. For a finite number of modes the exponential truncates at the top degree, so every Gaussian below is an exact polynomial identity, not an asymptotic expansion. This is why the finite-mode checks are exact rather than approximate.

**Superselection is algebraic.** The Grassmann algebra splits into even and odd parts, and Berezin integration of a non-top element vanishes: $\int d\theta\,1=0$. An integral of a monomial therefore vanishes unless the monomial has exactly the top degree, and the parity of that degree is fixed by the number of generators. This is the path-integral form of fermion-parity superselection: an amplitude between states of different parity receives a vanishing integral, and the two parity sectors of the boundary data never mix.

## The Gaussian Integral and the Determinant

For a finite set of modes, write the quadratic action as

$$
S_0=\sum_{a,b}\bar\psi_a M_{ab}\psi_b ,
$$

where $M$ is the matrix of the bilinear. In Euclidean signature $M=\mathbb{D}_{\mathrm{E}}+m$, and in Minkowski signature $M=-i(\mathbb{D}-m)$; the factor $-i$ is a field-independent constant of unit modulus, so in Minkowski the determinant is that of $\mathbb{D}-m$ up to that constant. The Gaussian Berezin integral is the determinant:

$$
\boxed{\;\int\prod_ad\bar\psi_a\,d\psi_a\;\exp(-\bar\psi M\psi)=\det M\;}.
$$

The derivation is the terminating expansion: $\exp(-\bar\psi M\psi)=1-\bar\psi M\psi+\tfrac12(\bar\psi M\psi)^2-\cdots$, and only the term with exactly one of every generator survives the integral, whose coefficient is the Leibniz sum that defines $\det M$. The identity was verified for a general complex $2\times2$ matrix in the stated convention: the two sides agree to machine precision, ratio $1+0i$.

**The two-point function.** Dressing the Gaussian by one pair of fields gives the inverse kernel:

$$
\langle\psi_a\,\bar\psi_b\rangle=\frac{\int\prod d\bar\psi d\psi\;\exp(-\bar\psi M\psi)\,\psi_a\bar\psi_b}{\int\prod d\bar\psi d\psi\;\exp(-\bar\psi M\psi)}=\big(M^{-1}\big)_{ab} .
$$

The index order is part of the statement and was checked: for a random complex $2\times2$ $M$ the four amplitudes are the four entries of $M^{-1}$, in the order $\langle\psi_a\bar\psi_b\rangle=(M^{-1})_{ab}$, to nine decimals. The two off-diagonal amplitudes are sensitive to it because $M$ need not be symmetric: they are $(M^{-1})_{01}$ and $(M^{-1})_{10}$, and the anticommuting order of the measure is what fixes which field contracts with which index.

**The generating functional.** Completing the square in the Grassmann algebra — a finite algebraic operation, since the shift $\psi\to\psi+M^{-1}\eta$, $\bar\psi\to\bar\psi+\bar\eta M^{-1}$ is a shift by odd constants — gives the algebraic identity

$$
\boxed{\;\int\prod d\bar\psi\,d\psi\;\exp\!\big(-\bar\psi M\psi+\bar\eta\psi+\bar\psi\eta\big)=\det M\;\exp\!\big[\bar\eta\,M^{-1}\eta\big]\;},
$$

with the exponential terminating at the top degree in the sources: the bilinear $\bar\eta M^{-1}\eta$ has degree two, so the series stops at degree two for one mode and at degree $2N$ for $N$ modes.

The physical weight of §*Sources* replaces $-\bar\psi M\psi$ by $iS$ and $\bar\eta\psi+\bar\psi\eta$ by $i\!\int(\bar\eta\psi+\bar\psi\eta)$. Each source therefore carries an explicit $i$, and the two multiply to $i^2=-1$: the exponent of the result changes sign. With $M=-i(\mathbb{D}-m)$ and $M^{-1}=S_F$,

$$
Z[\eta,\bar\eta]=\det M\;\exp\!\big[-\bar\eta\,M^{-1}\eta\big]
=\det(\mathbb{D}-m)\;\exp\!\Big[-\int d^4x\,d^4y\;\bar\eta(x)\,S_F(x-y)\,\eta(y)\Big]
$$

up to a field-independent constant. The Euclidean functional, with weight $\exp(-S_{\mathrm E}+\bar\eta\psi+\bar\psi\eta)$, is the one that carries the plus sign.

### A Finite-Mode Computation

The statements above are finite algebraic identities, and it is worth exhibiting one instance with explicit numbers. Take two complex modes — four generators $\bar\psi_1,\psi_1,\bar\psi_2,\psi_2$ — and the kernel

$$
M=\begin{pmatrix}1.3+0.2i & 0.4-0.1i\\ 0.7+0.3i & 0.9\end{pmatrix},
\qquad
\det M=0.86+0.13i .
$$

The representation used is the Grassmann algebra on the four generators with monomials represented by subsets and the Koszul sign carried by the reordering, and Berezin integration defined as the coefficient of the top form in the stated normalization. Then

$$
\int d\bar\psi_2d\psi_2d\bar\psi_1d\psi_1\;\exp(-\bar\psi M\psi)=0.86+0.13i=\det M ,
$$

to machine precision (ratio $1+0i$), and the four two-point amplitudes divided by $\det M$, in the order $(a,b)=(0,0),(0,1),(1,0),(1,1)$, are $1.023132849-0.154659617i$, $-0.437541309+0.182419035i$, $-0.847323199-0.22075347i$ and $1.512227363+0.003965631i$, which are exactly $(M^{-1})_{00},(M^{-1})_{01},(M^{-1})_{10},(M^{-1})_{11}$. The middle two differ, as the index order requires: $M$ is not symmetric.

**For the field** the same result is the free generating functional of the propagator companion, with $S_F$ its configuration-space amplitude and the minus sign in the exponent the one just derived. The determinant, the trace-log and the systematic evaluation of the functional determinant are outside this article's subject; what belongs here is the biquaternion form of the result.

### The Biquaternion Form of the Kernel

Write the wave biquaternion $\tilde P=iE\,e_t+\vec p$, so that $\tilde P\tilde P^{\natural}=-p^2$, and write $\nu(t)=x$, $\nu(k)=y$. The momentum cell is the symbol of the cell operator $\mathbb{D}$ on the plane wave $\exp(-iEt'+i\vec p\cdot\vec x)$: the derivative brings $-i$ from $t'$ and $+i$ from each $Q_k$, and multiplication by the explicit $i$ of $\mathbb{D}$ gives $+1$ and $-1$ respectively, since $i^2=-1$. The symbol is the momentum contraction of the frame cells:

$$
\slashed p=\mathbb{D}_p=\sum_\mu\varepsilon_\mu\,iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}p_\mu=iR_{\vec e_x}^{\mathrm{axf}}E-i\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}p_k.
$$

The momentum-space kernel is

$$
S_F(p)=-\frac{i(\slashed p+m)}{\tilde P\tilde P^{\natural}+m^2-i\epsilon}.
$$

The prefactor $-i$ meets the $i$ already inside the momentum cell. By $i^2=-1$,

$$
-i(\slashed p+m)=-i\slashed p-im=\sum_\mu\varepsilon_\mu L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}p_\mu-im,
$$

so the same amplitude, with the two imaginary units reduced, is

$$
S_F(p)=\frac{\sum_\mu\varepsilon_\mu L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}p_\mu-im}{\tilde P\tilde P^{\natural}+m^2-i\epsilon}.
$$

Multiplying numerator and denominator by $-1$ gives the companion's standard form $i(\slashed p+m)/(p^2-m^2+i\epsilon)$; the two are the same amplitude, and this is the propagator companion's amplitude. The determinant is therefore that of the operator whose inverse is $S_F$, with the deformed mass-shell denominator; the deformation lies along the $ict'$ axis of the material sector. On the module $\mathbb{D}$ is block off-diagonal in the chiral basis and the two gradient blocks multiply to $\Box$, so the block determinant of $\mathbb{D}-m$ is $\det(m^2-\Box)$ on a single complex component. The module is two complex dimensions, each carrying one such factor, so the determinant on it is the square of the scalar one:

$$
\det\big(\mathbb{D}-m\big)=\big[\det\big(\Box-m^2\big)\big]^2
=\exp\Big[2\!\int\frac{d^4p}{(2\pi)^4}\,\ln\big(\tilde P\tilde P^{\natural}+m^2-i\epsilon\big)\Big],
$$

formally, up to a field-independent constant and with the standard subtractions understood; equivalently, the $4\times4$ real determinant is the square of the $2\times2$ complex one. The generalities companion's finding is inherited: the algebra names the axis of the deformation, the boundary condition chooses its orientation, and the determinant does not distinguish them.

## The Pfaffian and the Real Structure

For a field whose quadratic form is antisymmetric, the Gaussian is a square root of a determinant. This is not a special case invented for the fermionic path integral. The algebra supplies the possibility: $\flat=-{}^{*}$ is an antilinear involution whose fixed space is the material sector $\mathbb{M}_-$, and a coupling that pairs a field with its own conjugate, rather than with an independent second field, has the shape of a Majorana mass. The pairing itself is the invariant antisymmetric form of the two-component module. The reality condition $\psi^{\mathrm c}=\psi$ is the coefficient conjugation $\bar{\cdot}$, not $\flat$, and the companion article *The Neutrino and Majorana Fermions in Biquaternionic Form* keeps the two apart. What the algebra supplies here is the existence of the pairing, not its sign or its normalization.

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

**The biquaternion form.** Contracting $\tilde\Psi\wedge\tilde\Psi$ with the invariant antisymmetric form of the two-dimensional module, whose matrix is $i\sigma_2$, the Pfaffian is the Berezin integral of the pairing, and its square is the determinant of the Dirac kernel whose inverse is $S_F$. The Majorana quantization is therefore the statement that the pairing is available; the Dirac quantization is the statement that it is not used, the two chiralities being independent.

## The Euclidean Integral and the Boundary Conditions

**Wick rotation.** With $t'\to-i\tau$ the $ict'$ direction of $\mathbb{M}_-$ becomes the real quaternion direction, as the Wick-rotation companion establishes, and the oscillatory weight becomes a decaying one:

$$
\exp(\,iS)\;\longrightarrow\;\exp(\,-S_{\mathrm{E}}),
\qquad
S_{\mathrm{E}}=\int d\tau\,d^3x\;\bar\psi\big(\mathbb{D}_{\mathrm{E}}+m\big)\psi ,
$$

with the kinetic operator anti-Hermitian and the mass term Hermitian. The Euclidean determinant is therefore real, and positive for real $m$; a continuous phase appears only when a non-Hermitian deformation is added.

**Antiperiodic boundary conditions.** The Euclidean fermionic integral that computes a thermal trace is taken over fields on a circle of circumference $\beta=1/T$ with the fermions antiperiodic,

$$
\psi(\tau+\beta)=-\psi(\tau) ,
$$

which is the same statement as the Matsubara frequencies $\omega_n=(2n+1)\pi/\beta$, and the same sign as the anticommutator. The identity $e^{i\omega_n\beta}=-1$ holds exactly for every integer $n$; it was checked for $n=0,1,2$. The boundary condition is what makes the Euclidean determinant a product over half-integer Matsubara modes rather than integer ones, and it is the path-integral statement of the spin–statistics pairing.

**The partition function.** On the Euclidean circle the free integral is a determinant,

$$
Z(\beta)=\int_{\text{antiperiodic}}\mathcal{D}\bar\psi\mathcal{D}\psi\;\exp(-S_{\mathrm{E}})
=\det\big(\mathbb{D}_{\mathrm{E}}+m\big)_{\text{AP}} ,
$$

whose logarithm gives the free energy up to the factor $-\beta$. The identity is the standard finite-temperature reduction of the fermionic integral and is recorded, not recomputed; what the biquaternion framework adds is again only the location of the deformation and the centrality of the phase. The companion article *The KMS Condition and the Biquaternion Framework* treats the analytic structure that the antiperiodicity generates.

## Parity Sectors, the Phase and the Sign Problem

The measure carries the parity, and the two fermion-parity sectors appear as a **relative sign**, not as two integrands. In the paired measure an integral of an odd element vanishes, so the Gaussian integrand $\exp(-\bar\psi M\psi)$, being even, is the same functional in both sectors; what distinguishes them is the *boundary condition* in imaginary time. The two basic traces are

$$
\boxed{\;\mathrm{Tr}\,\exp(-\beta H^{\mathrm{fop}})
=\int_{\text{antiperiodic}}\mathcal{D}\bar\psi\mathcal{D}\psi\;\exp(-S_{\mathrm{E}}) ,
\qquad
\mathrm{Tr}\,(-1)^{F^{\mathrm{fop}}}\exp(-\beta H^{\mathrm{fop}})
=\int_{\text{periodic}}\mathcal{D}\bar\psi\mathcal{D}\psi\;\exp(-S_{\mathrm{E}})\;},
$$

so the antiperiodic fields compute the ordinary thermal trace and the periodic fields the parity-weighted (Witten) trace; the two differ by the relative sign of the even and odd sectors. This is the path-integral form of the parity grading that the parent Fock-space article records. It is also the reason a **Majorana** field's integral is a Pfaffian while a **Dirac** field's is a determinant: the Dirac field's $\psi$ and $\bar\psi$ are independent, so its measure pairs two independent sets of generators and yields a determinant; the Majorana field is its own conjugate, so the same pairing is antisymmetric within one set and yields the square root. Chirality enters separately, through the mass term, which couples the two chiral halves.

**Where the determinant sits.** The fermionic partition function carries $\det M$ in the numerator, whereas a bosonic one carries $(\det M)^{-1/2}$ for a real field or $(\det M)^{-1}$ for a complex field. In the exponent of $Z$ the fermion therefore contributes $+\mathrm{Tr}\ln M$ and a complex boson $-\mathrm{Tr}\ln K$ (a real boson $-\tfrac12\mathrm{Tr}\ln K$), so the two enter loop corrections with opposite signs. This is not a bookkeeping accident but a consequence of the measure: the bosonic measure is a positive weight and the integral of a decaying Gaussian is small when the kernel is large, while the Berezin integral of a Gaussian is the determinant itself. It is the origin, at the level of the generating functional, of the opposite vacuum-energy contributions of bosons and fermions, and it was checked in the finite-mode computation above, where the integral returned $\det M$ rather than its inverse.

The phase of the determinant is where the fermionic integral's analytic content sits, and the generalities companion's finding governs it. A kernel that is Hermitian, or anti-Hermitian and graded by chirality, has a determinant real up to a sign; a genuinely non-Hermitian one — a chemical potential, or a complex mass — has a complex determinant, and in the finite-density case its phase is the origin of the sign problem of lattice fermions. The biquaternion interpretation is narrow and honest: the central $i$ fixes the *form* of the phase, the imaginary axis of $\mathbb{M}_-$ is where the $i\epsilon$ deformation sits, and the algebra does not evaluate the phase. The transformation of the measure under a chiral rotation, and the anomalies that follow when the measure fails to be invariant, are outside this article's subject.

## What Is Standard and What Is the Algebra's Own

**Standard, transcribed.** The Grassmann (Berezin) formulation of the fermionic integral; the Gaussian and its determinant; the two-point function as the inverse kernel; the generating functional with Grassmann sources; the Pfaffian for an antisymmetric form and $\mathrm{Pf}^2=\det$; the Wick rotation and the antiperiodic finite-temperature determinant; the parity traces and the phase (sign) problem. All of it is standard, and all of it is written in the parents' conventions.

**The algebra's own.**

- *The sector and centrality statements.* The phase $iS$ is central and lies in $\mathbb{M}_-$ along the $ict'$ axis; the action is even; the sources are odd and live in the Grassmann extension. These are the generalities companion's findings applied to the fermionic case, and they are the only place where the algebra's structure enters.
- *The real structure that makes the pairing available.* That the algebra offers a field-to-its-own-conjugate pairing at all is what $\flat=-{}^{*}$ makes available; that the resulting integral is a Pfaffian is the consequence.
- *The biquaternion form of the kernel.* The deformed mass-shell denominator inherited from the propagator companion, with the frame's sign vector $\varepsilon_\mu$ carried by the contraction.

**Open.**

- **The sign of the Pfaffian.** Fixed by the measure convention, not by the algebra. Whether some biquaternion-natural normalization of the measure fixes it is open.
- **The infinite-mode measure.** The Berezin measure is defined mode by mode; its continuum limit, its regularization and its transformation properties are not supplied by the algebra, as the generalities companion states.
- **The phase.** The evaluation of the determinant's phase, and the anomalies associated with the measure, require the standard methods and are outside the framework's reach at this level.
- **Empirical content.** Whether any of the transcribed formulas differs observably from the standard field theory is the framework's standing open question, and nothing here changes it.

## Companion Articles

- Companion article *The Feynman Propagator in Biquaternionic Form*, for the contour prescription and the propagator conventions used in the kernel.
- Companion article *The Path Integral in Biquaternionic Form*, for the bosonic generating functional whose Grassmann counterpart is constructed here.
- Companion article *The Dirac Equation in Biquaternionic Form*, for the one-sided pair, the two-sided dictionary, and the frame in which the mass couples the chiral halves.
- Companion article *The Neutrino and Majorana Fermions in Biquaternionic Form*, for the reality condition $\psi^{\mathrm c}=\psi$ and for the distinction between $\flat$ and the coefficient conjugation.
- Companion article *The Functional Determinant in Biquaternionic Form*, for the module determinant and its product over modes.
- Companion article *Interpretation of the Wick Rotation in the Biquaternion Universe*, for the imaginary-time direction and the Euclidean formulation.
- Companion article *The KMS Condition and the Biquaternion Framework*, for the antiperiodic boundary condition and the Matsubara structure that the fermionic measure carries.

## The Legacy Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. They are written with the left and right multiplications of the module, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and with $I_4=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ the identity on it:

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

They obey the Clifford relations of the frame — $\gamma_\mu\gamma_\nu+\gamma_\nu\gamma_\mu=2g_{\mu\nu}I_4$ with $g=\mathrm{diag}(+1,-1,-1,-1)$ — and $\gamma_5^2=I_4$ with $\{\gamma_5,\gamma_\mu\}=0$. The relations were checked on the cells, so the frame is the body's cell algebra in another notation, not a larger one.

The pair operator of the body is the same cell operator, written in gammas:

$$
\mathbb{D}=i\gamma_0\frac{\partial}{\partial t'}+i\sum_k\gamma_k\frac{\partial}{\partial Q_k},
\qquad
\slashed p=\gamma_0E-\sum_k\gamma_kp_k .
$$

Each term $i\gamma_\mu=i\,(iL_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}})=i^2L_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}=-L_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}$ has already spent the product $i^2=-1$, so the cell form has no imaginary unit left. The collapse removes the $i$, not the cell: $i\gamma_0=-R_{\vec e_x}^{\mathrm{pau}}\neq-I_4$, so the time derivative is multiplied by the right multiplication by $\vec e_x$, not by a number.

$\gamma_5$ is the reference-frame cell of the chirality $\Gamma$; the central grading $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi_{\mathrm{ad}}^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The fermionic path integral of the biquaternion spin-$\tfrac12$ field is the Berezin integral over Grassmann-valued biquaternion histories of the phase $\exp(iS)$, with the biquaternion Dirac action as the bilinear $S=\int\mathrm{Sc}(\tilde\Psi^{\natural}\tilde\nabla\tilde\Psi)-\int m\,\mathrm{Sc}(\tilde\Psi^{\natural}\tilde\Psi)$ and the sources odd. The equation integrated is the **one-sided** chiral pair; Kravchenko's **two-sided** equation is a different operator, related to it by a real-linear dictionary, and is not integrated here. The phase is central and lies in $\mathbb{M}_-$ along the $ict'$ axis; the action is even, so the parity sectors do not mix and an odd integral vanishes.

The Gaussian is the determinant, verified exactly for a general complex $2\times2$ matrix in the convention $\int d\theta^*d\theta\,\theta\theta^*=1$; the two-point function is the inverse kernel in the stated index order, $\langle\psi_a\bar\psi_b\rangle=(M^{-1})_{ab}$, verified to nine decimals; the generating functional is $Z[\eta,\bar\eta]=\det M\exp[-\bar\eta M^{-1}\eta]$ in the Minkowski weight, with the plus sign in the Euclidean one; and for the field the kernel is the propagator companion's

$$
S_F(p)=\frac{\sum_\mu\varepsilon_\mu L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}p_\mu-im}{\tilde P\tilde P^{\natural}+m^2-i\epsilon},
$$

with the two imaginary units of $-i(\slashed p+m)$ multiplied to $-1$. The determinant of the pair operator is the square of the scalar determinant, $\det(\mathbb D-m)=[\det(\Box-m^2)]^2$, because the block determinant is $\det(m^2-\Box)$ on each of the module's two complex dimensions.

For an antisymmetric quadratic form the integral is a Pfaffian: $\int d\psi\,\exp(-\frac12\psi A\psi)=\mathrm{Pf}(A)$ and $\mathrm{Pf}^2=\det A$, both recomputed (the first to $10^{-16}$, the second to $5\times10^{-16}$). This is the algebra's real-structure pairing at work: $\flat$ makes available the field-to-its-own-conjugate pairing, the measure normalizes it, and the sign is a convention rather than an algebra invariant. The Wick rotation turns the oscillatory weight into a decaying one, and the thermal integral is a determinant with antiperiodic boundary conditions, $\psi(\tau+\beta)=-\psi(\tau)$; the identity $e^{i\omega_n\beta}=-1$ is exact for every integer $n$ and equivalent to $\omega_n=(2n+1)\pi/\beta$.

The algebra contributes the centrality of the phase, the sector location of the deformation, and the existence of the pairing. It does not supply the measure, the evaluation of the determinant, or the phase, and the article says so.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S=\int d^4x\,\bar\psi(\mathbb{D}-m)\psi$ | Biquaternion Dirac action (bilinear) |
| $S=\int\mathrm{Sc}(\tilde\Psi^{\natural}\tilde\nabla\tilde\Psi)-\int m\,\mathrm{Sc}(\tilde\Psi^{\natural}\tilde\Psi)$ | Action as a trace reading of the Hermitian form |
| $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$, $\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R$ | One-sided chiral pair; the equation integrated |
| $-\tilde\nabla^{\natural}F-mi\,\bar F\,\vec e_z=0$ | Two-sided (Kravchenko) equation; different operator, not integrated |
| $\exp(iS)$ | Path-integral phase; central, in $\mathbb{C}_{\mathbb{B}}$, exponent along $ict'$ |
| $\eta,\bar\eta$ | Odd (Grassmann) sources |
| $\mathcal{D}\bar\psi\mathcal{D}\psi=\prod_x\prod_ad\bar\psi_a(x)d\psi_a(x)$ | Berezin measure |
| $\int d\theta^*d\theta\,\theta\theta^*=1$ | Berezin normalization used throughout |
| $\int\prod d\bar\psi d\psi\,\exp(-\bar\psi M\psi)=\det M$ | Gaussian = determinant |
| $\langle\psi_a\bar\psi_b\rangle=(M^{-1})_{ab}$ | Two-point function (inverse kernel, stated index order) |
| $Z[\eta,\bar\eta]=\det M\,\exp[-\bar\eta M^{-1}\eta]$ | Free generating functional in the Minkowski weight; the Euclidean one carries $+\bar\eta M^{-1}\eta$ |
| $Z_0[\eta,\bar\eta]=\det(\mathbb{D}-m)\exp[-\int\bar\eta S_F\eta]$ | Field-level free functional |
| $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}p_\mu$, $\varepsilon=(+1,-1,-1,-1)$ | Frame cells; the sign vector $\varepsilon_\mu=g_{\mu\mu}$ carried by every contraction of two lower indices, so that $\sum_\mu\varepsilon_\mu iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}p_\mu=iR_{\vec e_x}^{\mathrm{axf}}E-i\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}p_k$ |
| $\mathbb{D}=-L_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}\partial/\partial t'-\sum_kL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\partial/\partial Q_k$ | Pair operator in cells; the explicit $i$ and the $i$ of the cell multiply to $-1$ |
| $S_F(p)=\frac{\sum_\mu\varepsilon_\mu L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}p_\mu-im}{\tilde P\tilde P^{\natural}+m^2-i\epsilon}$ | Kernel; the two imaginary units of $-i(\slashed p+m)$ multiply to $-1$ |
| $\det(\mathbb{D}-m)=[\det(\Box-m^2)]^2$ | Determinant; the module's two complex dimensions give the square of the scalar determinant |
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
