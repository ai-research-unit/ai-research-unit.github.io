# __The Fermionic Path Integral in Biquaternionic Form__

## Introduction

The companion article *The Path Integral in Biquaternionic Form* settles what the biquaternion algebra can and cannot contribute to a path integral: the phase factor $e^{iS/\hbar}$ is a *central* unitary element, because the central scalar imaginary is the algebra's unique complex structure up to sign; the exponent lies along the $ict$ direction of the material sector $\mathbb{M}_-$; and the measure, the action and the space of paths are not supplied by the algebra, because $\mathbb{B}$ is finite-dimensional and the space of histories is not. The companion article *The Feynman Propagator in Biquaternionic Form* adds where the $i\epsilon$ lives and that the algebra names its axis without choosing its orientation. The companion article *The Wick Rotation in the Biquaternion Universe* adds that $t\to-i\tau$ is the relabeling of the imaginary-time coefficient as a real one, turning the material sector into the quaternion subspace.

This article applies those findings to the spin-$\tfrac12$ field, where the histories are **anticommuting**. The fermionic path integral differs from the bosonic one in exactly one structural place — the integration variables are odd, so the integral is Berezin's rather than Lebesgue's — and that one difference propagates into every formula. The article establishes:

- **The action and its sector.** The biquaternion Dirac action as a bilinear, the phase $iS$ as an element of $\mathbb{M}_-$ along the $ict$ axis, and the action as an even (bosonic) functional of the fermionic field.
- **The Berezin measure.** Fermionic histories are Grassmann-valued biquaternion fields; the measure is the Berezin measure of the coefficient algebra, and in the finite-mode reduction it is $\prod_k d\bar\psi_kd\psi_k$ with the convention fixed once.
- **The Gaussian integral and the determinant.** Completing the square in the Grassmann algebra gives the free generating functional, the two-point function as the inverse kernel, and the determinant of the Dirac operator; the finite-mode statements were recomputed exactly.
- **The Pfaffian and the real structure.** For a field whose quadratic form is antisymmetric — the Majorana case, which the algebra's real structure $\flat$ suggests — the integral is a Pfaffian, with $\mathrm{Pf}^2=\det$ and a sign that carries physical content.
- **The Euclidean integral and the parity sectors.** Wick rotation and the antiperiodic (Matsubara) boundary conditions, the decomposition of the measure into the two fermion-parity sectors, and the phase of the determinant.

The boundary with the neighbouring subjects is sharp and is stated where it occurs: the systematic evaluation of the functional determinant, the transformation of the measure under field redefinitions, and the anomalies that follow from it are not treated here.

**Conventions.** From the companion articles: $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, basis $e_0,e_1,e_2,e_3$, $e_k^2=-e_0$, central $i$ with $i^\dagger=-i$; $\tilde{Q}^\dagger=\bar{\tilde{Q}}^{\,*}$, $\flat=-\dagger$; $\mathbb{M}_-$ anti-Hermitian (material), $\mathbb{M}_+$ Hermitian (informational); norm form $N(\tilde Q)=\sum_\mu Q_\mu^2$; $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$; the mass term is the linear chirality-off-diagonal pair; on the module $(i\gamma^\mu\partial_\mu-m)\psi=0$, $\bar\psi=\psi^\dagger\gamma^0$, $g=\mathrm{diag}(+1,-1,-1,-1)$, $\eta=\mathrm{diag}(-1,+1,+1,+1)$; the $i\epsilon$ sits along the $ict$ axis of $\mathbb{M}_-$. **Grassmann conventions.** To each mode belong odd generators $\theta,\theta^*$ with $\theta^2=\theta^{*2}=0$, $\theta\theta^*=-\theta^*\theta$, and Berezin integration is normalized by $\int d\theta^*d\theta\,\theta\theta^*=1$; consequences are $\int d\theta^*d\theta\,e^{-\theta^*\theta}=1$ and $\int d\theta^*d\theta\,e^{-\theta^*M\theta}=M$.

## The Action in Biquaternion Form

The classical field theory is defined by the parent article's Lagrangian density,

$$
\mathcal{L}=\bar\psi\,(i\gamma^\mu\partial_\mu-m)\,\psi ,
$$

a real Lorentz scalar whose variation returns $(i\gamma^\mu\partial_\mu-m)\psi=0$, with conjugate momentum $\pi=i\psi^\dagger$. For the path integral this is the object whose integral is the phase.

**The biquaternion transcription, and what it does not fix.** On the module the kinetic operator is $i\gamma^\mu\partial_\mu$, and the dictionary companion identifies the Clifford vector with the Hermitian biquaternion through $x_\mu\gamma^\mu=\gamma^0\Phi(w)$, $w\in\mathbb{M}_+$, so that the $ict$ gradient of the series is the biquaternion transcription of $i\gamma^\mu\partial_\mu$:

$$
i\gamma^\mu\partial_\mu\;\longleftrightarrow\;\tilde{\nabla}=e_0\,\partial_{ict}+e_k\,\partial_k ,
\qquad
\bar\psi\,i\gamma^\mu\partial_\mu\psi\;\longleftrightarrow\;\mathrm{Sc}\big(\bar{\tilde\Psi}\,\tilde{\nabla}\tilde{\Psi}\big) ,
$$

with the scalar part as the natural pairing. The transcription is a candidate, not a derivation: the parent article is explicit that the $\mathbb{B}$-intrinsic Lagrangian — the real scalar built from $\tilde{\nabla}\tilde{\Psi}$, $\tilde{\Psi}$, their conjugates and the trace or norm pairing — is *not* fixed by the algebra alone, and that the module transcription is the working setting. The path integral inherits that status: everything below is exact for the module transcription, and the question of which $\mathbb{B}$-intrinsic action it corresponds to is open, exactly as it is in the parent.

Three properties of the action are used below.

**It is even.** The action is quadratic in the fermionic field, hence bosonic: it commutes with fermion parity and is a $c$-number functional of the field. This is why $e^{iS}$ is a genuine phase and not an operator.

**Its phase is central.** $iS$ is a central element of $\mathbb{C}_{\mathbb{B}}$. The generalities companion's finding applies unchanged: the phase of the fermionic path integral is canonical, and it is not a choice of a spin axis.

**Its kinetic part is Hermitian and its mass part is the linear chiral pair.** $\bar\psi\,i\not\partial\,\psi$ is Hermitian up to a total derivative; $\bar\psi m\psi$ couples the two chiralities, as the mass-term convention requires. At the level of the path integral this is the statement that the *Euclidean* continuation of the kinetic operator is anti-Hermitian and that of the mass is Hermitian, which is what makes the determinant real or complex in the two cases respectively.

### Sources

The sources are Grassmann-valued: the generating functional

$$
Z[\eta,\bar\eta]=\int\mathcal{D}\bar\psi\,\mathcal{D}\psi\;\exp\Big[iS+i\!\int d^4x\,\big(\bar\eta\psi+\bar\psi\eta\big)\Big]
$$

requires $\eta,\bar\eta$ to be odd, since they multiply $\psi,\bar\psi$ respectively and the linear terms must be even. This is the same requirement as at the one-mode level, now at the level of the functional: the source term is a bilinear in one external odd and one integration variable, hence even, and the sources consequently lie in the odd part of the same Grassmann extension.

## The Berezin Measure

The histories are $\mathbb{B}$-valued fields whose coefficients are Grassmann numbers: for each spacetime point and each module component, $\psi_a(x)$ and $\bar\psi_a(x)$ are odd elements of the Grassmann algebra generated by the countably many generators $\{\theta_{a,x},\theta^*_{a,x}\}$, one pair per component and point. The measure is the product of Berezin measures,

$$
\mathcal{D}\bar\psi\,\mathcal{D}\psi=\prod_{x}\prod_{a}d\bar\psi_a(x)\,d\psi_a(x) ,
$$

with the normalization of the conventions above, mode by mode. The product is formal, exactly as the sum over paths is; what is finite and exact is the reduction to a finite number of modes, which is what the computations below use.

Three consequences of oddness are worth isolating, because they are the whole difference between this integral and the bosonic one.

**The measure is not a positive measure.** Berezin integration is a linear functional, not integration against a weight. There is no positivity to lose and none to assume; the "measure" is an algebraic operation, and every statement below is a statement about a finite-dimensional integral in a Grassmann algebra.

**The Wick expansion terminates.** A Grassmann algebra element of degree $n$ has a top form, and products beyond the top degree vanish. For a finite number of modes the exponential truncates at the top degree, so every Gaussian below is an exact polynomial identity, not an asymptotic expansion. This is why the finite-mode checks are exact rather than approximate.

**Superselection is algebraic.** The Grassmann algebra splits into even and odd parts, and Berezin integration of an odd element vanishes: $\int d\theta\,1=0$. An integral of a monomial therefore vanishes unless the monomial has exactly the top degree, and the parity of that degree is fixed by the number of generators. This is the path-integral form of fermion-parity superselection: an amplitude between states of different parity receives a vanishing integral, and the two parity sectors of the boundary data never mix.

## The Gaussian Integral and the Determinant

For a finite set of modes, write the quadratic action as

$$
S_0=\sum_{a,b}\bar\psi_a M_{ab}\psi_b ,
$$

where $M$ is the matrix of the bilinear (for the field, the operator $i\not\partial-m$ between the source-free boundary conditions). The Gaussian Berezin integral is the determinant:

$$
\int\prod_ad\bar\psi_a\,d\psi_a\;e^{-\bar\psi M\psi}=\det M .
$$

The derivation is the terminating expansion: $e^{-\bar\psi M\psi}=1-\bar\psi M\psi+\tfrac12(\bar\psi M\psi)^2-\cdots$, and only the term with exactly one of every generator survives the integral, whose coefficient is the Leibniz sum that defines $\det M$. The identity was verified for a general complex $2\times2$ matrix in the stated convention: the two sides agree to machine precision, ratio $1+0i$.

**The two-point function.** Differentiating with respect to the sources, or dressing the Gaussian by one pair of fields, gives the inverse kernel:

$$
\langle\psi_a\,\bar\psi_b\rangle=\frac{\int\prod d\bar\psi d\psi\;e^{-\bar\psi M\psi}\,\psi_a\bar\psi_b}{\int\prod d\bar\psi d\psi\;e^{-\bar\psi M\psi}}=\big(M^{-1}\big)_{ab} .
$$

The index order is part of the statement and was checked: for a random complex $2\times2$ $M$, the four amplitudes are the four entries of $M^{-1}$, the field $\psi_a$ contracting with the second index and $\bar\psi_b$ with the first, to nine decimals. The order is the trace of the anticommutator in the integration: with the bilinear written $\bar\psi M\psi$ and the measure written $\prod_ad\bar\psi_ad\psi_a$, the two factors come back in the order in which they stand, not transposed, and the off-diagonal amplitudes are sensitive to it because $M$ need not be symmetric.

**The generating functional.** Completing the square in the Grassmann algebra — a finite algebraic operation, since the shift $\psi\to\psi-M^{-1}\eta$ is a shift by an odd constant — gives

$$
Z[\eta,\bar\eta]=\det M\;\exp\!\big[\bar\eta\,M^{-1}\eta\big],
$$

with the exponential terminating at second order in the sources. The result is the standard fermionic Gaussian and is recorded as such.

### A Finite-Mode Computation

The statements above are finite algebraic identities, and it is worth exhibiting one instance with explicit numbers. Take two complex modes — four generators $\bar\psi_1,\psi_1,\bar\psi_2,\psi_2$ — and the kernel

$$
M=\begin{pmatrix}1.3+0.2i & 0.4-0.1i\\ 0.7+0.3i & 0.9\end{pmatrix},
\qquad
\det M=0.86+0.13i .
$$

The representation used is the Grassmann algebra on the four generators with monomials represented by subsets and the Koszul sign carried by the reordering, and Berezin integration defined as the coefficient of the top form in the stated normalization. Then

$$
\int d\bar\psi_2d\psi_2d\bar\psi_1d\psi_1\;e^{-\bar\psi M\psi}=0.86+0.13i=\det M ,
$$

to machine precision (ratio $1+0i$), and the four two-point amplitudes divided by $\det M$, in the order $(a,b)=(0,0),(0,1),(1,0),(1,1)$, are $1.023132849-0.154659617i$, $-0.437541309+0.182419035i$, $-0.847323199-0.22075347i$ and $1.512227363+0.003965631i$, which are exactly $(M^{-1})_{00},(M^{-1})_{01},(M^{-1})_{10},(M^{-1})_{11}$. The index order $\langle\psi_a\bar\psi_b\rangle=(M^{-1})_{ab}$ is visible in the middle two entries, which differ: $M$ is not symmetric, and the anticommuting order of the measure fixes which index each of the two fields contracts with.

**For the field** the same computation gives the free generating functional

$$
Z_0[\eta,\bar\eta]=\det\big(i\not\partial-m\big)\;
\exp\Big[\,i\!\int d^4x\,d^4y\;\bar\eta(x)\,S_F(x-y)\,\eta(y)\Big],
$$

where $S_F$ is the propagator amplitude of the companion article in configuration space. The determinant, the trace-log and the systematic evaluation of the functional determinant are outside this article's subject; what belongs here is the biquaternion form of the result.

### The Biquaternion Form of the Kernel

Writing the wave biquaternion $\tilde k=iE\,e_0+\mathbf p$, so that $\tilde k\bar{\tilde k}=-p^2$, the momentum-space kernel is

$$
S_F(p)=-\frac{i(\not p+m)}{\tilde k\bar{\tilde k}+m^2-i\epsilon},
$$

the propagator companion's amplitude. The determinant is therefore the determinant of an operator whose inverse has the deformed mass-shell denominator, and the deformation lies along the $ict$ axis of the material sector:

$$
\det\big(i\not\partial-m\big)\;\longleftrightarrow\;\exp\Big[\int\frac{d^4p}{(2\pi)^4}\,\ln\big(\tilde k\bar{\tilde k}+m^2-i\epsilon\big)\Big],
$$

formally, with the standard subtractions understood. The generalities companion's finding is inherited: the algebra names the axis of the deformation, the boundary condition chooses its orientation, and the determinant does not distinguish them.

## The Pfaffian and the Real Structure

For a field whose quadratic form is antisymmetric, the Gaussian is a square root of a determinant. This is not a special case invented for the fermionic path integral; it is what the algebra's real structure suggests, because $\flat=-\dagger$ is a pairing of the field with its own conjugate, of exactly the shape of a Majorana mass.

**The integral of an antisymmetric form.** For $2N$ generators $\psi_1,\dots,\psi_{2N}$ and an antisymmetric matrix $A$,

$$
\int d\psi_{2N}\cdots d\psi_1\;e^{\,-\frac12\psi A\psi}=\mathrm{Pf}(A),
$$

with $\mathrm{Pf}$ the Pfaffian, and

$$
\mathrm{Pf}(A)^2=\det A .
$$

Both identities were recomputed. For a random complex antisymmetric $4\times4$ the Grassmann integral equals the closed-form Pfaffian $\mathrm{Pf}=A_{12}A_{34}-A_{13}A_{24}+A_{14}A_{23}$ with ratio $1.0000000000000002+2.3\times10^{-17}i$; and $\mathrm{Pf}^2-\det A$ vanishes to $5\times10^{-16}$. The Pfaffian is thus the exact result of a finite Berezin integral, and it is the natural output of the measure for a field that is its own conjugate.

**The sign of the Pfaffian.** Unlike $\det$, $\mathrm{Pf}$ has a sign that is not determined by the magnitudes, and the sign is fixed by the ordering of the generators — that is, by the *conventions of the measure*, not by the algebra. Two consequences are worth recording.

First, the sign is a genuine physical input wherever the Pfaffian is the answer: it is the relative sign of the two parity sectors of a Majorana field, and it changes when the convention $\int\theta\theta^*=1$ is replaced by $\int\theta^*\theta=1$. The article keeps the convention fixed and notes that the sign is not an algebra-invariant.

Second, the algebra's own statement is the *existence* of the antisymmetric pairing, not its sign. The real structure $\flat$ supplies a pairing; the measure normalizes it; the orientation is a convention. This is the same three-way division the propagator companion records for the $i\epsilon$, and the algebra's contribution is again the middle term.

**The biquaternion form.** Writing the antisymmetric pairing as the trace of $\tilde\Psi\wedge\tilde\Psi$ against the invariant antisymmetric form $\varepsilon=i\sigma_2$ of the two-dimensional module, the Pfaffian is the Berezin integral of the pairing, and its square is the determinant of the same kernel whose inverse is $S_F$. The Majorana quantization is therefore the statement that the pairing is available; the Dirac quantization is the statement that it is not used, the two chiralities being independent.

## The Euclidean Integral and the Boundary Conditions

**Wick rotation.** With $t\to-i\tau$ the $ict$ direction of $\mathbb M_-$ becomes the real quaternion direction, as the Wick-rotation companion establishes, and the oscillatory weight becomes a decaying one:

$$
e^{\,iS}\;\longrightarrow\;e^{\,-S_{\mathrm{E}}},
\qquad
S_{\mathrm{E}}=\int d\tau\,d^3x\;\bar\psi\big(\gamma^0\partial_\tau-i\boldsymbol\gamma\cdot\nabla+m\big)\psi ,
$$

with the kinetic operator now anti-Hermitian and the mass Hermitian, so that the quadratic form has a definite real part off the zero modes.

**Antiperiodic boundary conditions.** The Euclidean fermionic integral that computes a thermal trace is taken over fields on a circle of circumference $\beta=1/T$ with the fermions antiperiodic,

$$
\psi(\tau+\beta)=-\psi(\tau) ,
$$

which is the same statement as the Matsubara frequencies $\omega_n=(2n+1)\pi/\beta$, and the same sign as the anticommutator. The antiperiodicity was checked to nine decimals for $n=0,1,2$; the boundary condition is what makes the Euclidean determinant a product over half-integer Matsubara modes rather than integer ones, and it is the path-integral statement of the spin–statistics pairing.

**The partition function.** On the Euclidean circle the free integral is a determinant,

$$
Z(\beta)=\int_{\text{antiperiodic}}\mathcal{D}\bar\psi\mathcal{D}\psi\;e^{-S_{\mathrm{E}}}
=\det\big(\gamma^0\partial_\tau-i\boldsymbol\gamma\cdot\nabla+m\big)_{\text{AP}} ,
$$

whose logarithm is the free energy of the fermion gas. The identity is the standard finite-temperature reduction of the fermionic integral and is recorded, not recomputed; what the biquaternion framework adds is again only the location of the deformation and the centrality of the phase. The companion article *The KMS Condition and the Biquaternion Framework* treats the analytic structure that the antiperiodicity generates.

## Parity Sectors, the Phase and the Sign Problem

The measure carries the parity, and the two fermion-parity sectors appear as a **relative sign**, not as two integrands. An integral of an odd element vanishes, so the integrand of a Gaussian — the even element $\exp(-\bar\psi M\psi)$ — has no odd part to remove; what distinguishes the sectors is the *boundary condition* in imaginary time. The two basic traces are

$$
\mathrm{Tr}\,e^{-\beta\hat H}
=\int_{\text{antiperiodic}}\mathcal{D}\bar\psi\mathcal{D}\psi\;e^{-S_{\mathrm{E}}} ,
\qquad
\mathrm{Tr}\,(-1)^{\hat F}e^{-\beta\hat H}
=\int_{\text{periodic}}\mathcal{D}\bar\psi\mathcal{D}\psi\;e^{-S_{\mathrm{E}}} ,
$$

so the antiperiodic fields compute the ordinary thermal trace and the periodic fields the parity-weighted (Witten) trace; the two differ by the relative sign of the even and odd sectors. This is the path-integral form of the parity grading that the parent Fock-space article records, and it is also the reason a **Majorana** field's integral is a Pfaffian while a **Dirac** field's is a determinant: the Dirac field carries the two chiralities — and hence both parity sectors — independently, so its measure pairs $\psi$ with an independent $\bar\psi$ and yields a determinant; the Majorana field is its own conjugate, so its measure pairs the field with itself and yields the square root.

**Where the determinant sits.** The fermionic Gaussian produces $\det M$ in the *numerator* of every amplitude, whereas the bosonic Gaussian produces $1/\det M$; the two therefore enter loop corrections with opposite signs. This is not a bookkeeping accident but a consequence of the measure: the bosonic measure is a positive weight and the integral of a decaying Gaussian is small when the kernel is large, while the Berezin integral of a Gaussian is the determinant itself. It is the origin, at the level of the generating functional, of the opposite vacuum-energy contributions of bosons and fermions, and it was checked in the finite-mode computation above, where the integral returned $\det M$ rather than its inverse.

The phase of the determinant is where the fermionic integral's analytic content sits, and the generalities companion's finding governs it. For a Hermitian Euclidean kernel the determinant is real up to a sign; for a non-Hermitian one — a chemical potential, or a complex mass — it is complex, and in the finite-density case the phase is the origin of the sign problem of lattice fermions. The biquaternion reading is narrow and honest: the central $i$ fixes the *form* of the phase, the imaginary axis of $\mathbb M_-$ names the direction along which the determinant becomes complex, and the algebra does not evaluate the phase. The transformation of the measure under a chiral rotation, and the anomalies that follow when the measure fails to be invariant, are outside this article's subject.

## What Is Standard and What the Algebra's

**Standard, transcribed.** The Grassmann (Berezin) formulation of the fermionic integral; the Gaussian and its determinant; the two-point function as the inverse kernel; the generating functional with Grassmann sources; the Pfaffian for an antisymmetric form and $\mathrm{Pf}^2=\det$; the Wick rotation and the antiperiodic finite-temperature determinant; the parity decomposition and the phase (sign) problem. All of it is standard, and all of it is written in the parents' conventions.

**The algebra's own.**

- *The sector and centrality statements.* The phase $iS$ is central and lies in $\mathbb{M}_-$ along the $ict$ axis; the action is even; the sources are odd and live in the Grassmann extension. These are the generalities companion's findings applied to the fermionic case, and they are the only place where the algebra's structure enters.
- *The real structure as the source of the antisymmetric pairing.* That the algebra offers a field-to-its-own-conjugate pairing at all is the content of $\flat=-\dagger$; that the resulting integral is a Pfaffian is the consequence.
- *The Biquaternion form of the kernel* — the deformed mass-shell denominator inherited from the propagator companion.

**Open.**

- **The sign of the Pfaffian.** Fixed by the measure convention, not by the algebra. Whether some biquaternion-natural normalization of the measure fixes it is open.
- **The infinite-mode measure.** The Berezin measure is defined mode by mode; its continuum limit, its regularization and its transformation properties are not supplied by the algebra, as the generalities companion states.
- **The phase.** The evaluation of the determinant's phase, and the anomalies associated with the measure, require the standard methods and are outside the framework's reach at this level.
- **Empirical content.** Whether any of the transcribed formulas differs observably from the standard field theory is the framework's standing open question, and nothing here changes it.

## Companion Articles

- Companion article *The Feynman Propagator in Biquaternionic Form*, for the contour prescription and the propagator conventions used in the kernel.
- Companion article *The Path Integral in Biquaternionic Form*, for the bosonic generating functional whose Grassmann counterpart is constructed here.
- Companion article *The Wick Rotation in the Biquaternion Universe*, for the imaginary-time direction and the Euclidean formulation.
- Companion article *The KMS Condition and the Biquaternion Framework*, for the antiperiodic boundary condition and the Matsubara structure that the fermionic measure carries.

## Summary

The fermionic path integral of the biquaternion spin-$\tfrac12$ field is the Berezin integral over Grassmann-valued biquaternion histories of the phase $e^{iS}$, with the biquaternion Dirac action as the bilinear $S=\int\mathrm{Sc}(\bar{\tilde\Psi}\tilde\nabla\tilde\Psi)-\int m\,\mathrm{Sc}(\bar{\tilde\Psi}\tilde\Psi)$ and the sources odd. The phase is central and lies in $\mathbb{M}_-$ along the $ict$ axis; the action is even, so the parity sectors do not mix and an odd integral vanishes.

The Gaussian is the determinant, verified exactly for a general complex $2\times2$ matrix in the convention $\int d\theta^*d\theta\,\theta\theta^*=1$; the two-point function is the inverse kernel in the stated index order, $\langle\psi_a\bar\psi_b\rangle=(M^{-1})_{ab}$, verified to nine decimals; the generating functional is $Z[\eta,\bar\eta]=\det M\exp[\bar\eta M^{-1}\eta]$; and for the field the kernel is the propagator companion's $S_F(p)=-i(\not p+m)/(\tilde k\bar{\tilde k}+m^2-i\epsilon)$.

For an antisymmetric quadratic form the integral is a Pfaffian: $\int d\psi\,e^{-\frac12\psi A\psi}=\mathrm{Pf}(A)$ and $\mathrm{Pf}^2=\det A$, both recomputed (the first to $10^{-16}$, the second to $5\times10^{-16}$). This is the algebra's real-structure pairing at work: $\flat$ offers the field-to-its-own-conjugate pairing, the measure normalizes it, and the sign is a convention rather than an algebra invariant. The Wick rotation turns the oscillatory weight into a decaying one, and the thermal integral is a determinant with antiperiodic boundary conditions, $\psi(\tau+\beta)=-\psi(\tau)$, verified to nine decimals and equivalent to $\omega_n=(2n+1)\pi/\beta$.

The algebra contributes the centrality of the phase, the sector location of the deformation, and the existence of the pairing. It does not supply the measure, the evaluation of the determinant, or the phase, and the article says so.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S=\int d^4x\,\bar\psi(i\gamma^\mu\partial_\mu-m)\psi$ | Biquaternion Dirac action (bilinear) |
| $S=\int\mathrm{Sc}(\bar{\tilde\Psi}\tilde\nabla\tilde\Psi)-\int m\,\mathrm{Sc}(\bar{\tilde\Psi}\tilde\Psi)$ | Action as a trace pairing |
| $e^{iS}$ | Path-integral phase; central, in $\mathbb{C}_{\mathbb{B}}$, exponent along $ict$ |
| $\eta,\bar\eta$ | Odd (Grassmann) sources |
| $\mathcal{D}\bar\psi\mathcal{D}\psi=\prod_x\prod_ad\bar\psi_a(x)d\psi_a(x)$ | Berezin measure |
| $\int d\theta^*d\theta\,\theta\theta^*=1$ | Berezin normalization used throughout |
| $\int\prod d\bar\psi d\psi\,e^{-\bar\psi M\psi}=\det M$ | Gaussian = determinant |
| $\langle\psi_a\bar\psi_b\rangle=(M^{-1})_{ab}$ | Two-point function (inverse kernel, stated index order) |
| $Z[\eta,\bar\eta]=\det M\,\exp[\bar\eta M^{-1}\eta]$ | Free generating functional |
| $Z_0[\eta,\bar\eta]=\det(i\not\partial-m)\exp[i\!\int\bar\eta S_F\eta]$ | Field-level free functional |
| $S_F(p)=-\frac{i(\not p+m)}{\tilde k\bar{\tilde k}+m^2-i\epsilon}$ | Kernel in the deformed-mass-shell form |
| $\int d\psi_{2N}\cdots d\psi_1\,e^{-\frac12\psi A\psi}=\mathrm{Pf}(A)$, $\mathrm{Pf}^2=\det A$ | Pfaffian for an antisymmetric form |
| $\flat=-\dagger$ | Real structure; source of the field-to-conjugate pairing |
| $e^{iS}\to e^{-S_{\mathrm{E}}}$ | Wick rotation ($ict$ direction becomes real) |
| $\psi(\tau+\beta)=-\psi(\tau)$, $\omega_n=(2n+1)\pi/\beta$ | Antiperiodic thermal boundary condition |
| $Z(\beta)=\det(\gamma^0\partial_\tau-i\boldsymbol\gamma\cdot\nabla+m)_{\text{AP}}$ | Finite-temperature free partition function |

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
