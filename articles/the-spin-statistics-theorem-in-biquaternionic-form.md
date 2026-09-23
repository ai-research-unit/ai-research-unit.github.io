# __The Spin–Statistics Theorem in Biquaternionic Form__

## Introduction

The **spin–statistics theorem** is the statement that the spin of a field and the bracket that quantizes it are not independent. In a relativistic quantum field theory on Minkowski space whose inner product is positive definite and whose Hamiltonian is bounded below, a field of integer spin must be quantized with **commutators** and a field of half-integer spin with **anticommutators**: integer-spin fields are bosons, half-integer-spin fields are fermions. The theorem is a statement about the *choice of bracket*, not about the representation of the Lorentz group; the representation fixes the spin, and the theorem says that locality, positivity and Lorentz invariance together fix the bracket that goes with it.

The theorem is not among the results the companion articles derive. *Canonical Quantization of the Biquaternion Dirac Field* imposes anticommutation relations on the free biquaternion spinor field and lists the boundedness of the energy, together with microcausality and positivity, among the reasons the anticommutator is the appropriate one; it explicitly leaves the theorem itself to a dedicated article. *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* finds that the algebra $\mathbb{B}$ hosts exactly one fermionic mode and no bosonic mode, and is careful to say that this is a *realization* and not a derivation of fermionic statistics. *The KMS Condition and the Biquaternion Framework* identifies a $\mathbb{Z}/2$ grading of the operator algebra as an additional structure that the biquaternion algebra does not by itself supply. This article is the dedicated treatment those three forward references call for. It does not rederive the parents' quantizations, plane waves or spin sums, which are used unchanged.

The division between what is established and what is only transcribed is stated at the outset and kept explicit.

- **Established, and recomputed below.** The rotation group acts inside $\mathbb{B}$ through the rotor group of unit real quaternions, which is the double cover of $SO(3)$; the rotor through $2\pi$ about any axis is $-e_0$. Under the Lorentz action, the half-integer-spin representations are the spinor module and its tensor products, on which $-e_0$ acts as $-\mathrm{id}$, while the integer-spin representations descend to the Lorentz group, on which $-e_0$ acts as $+\mathrm{id}$. For the free spin-$\tfrac12$ field the equal-time **anticommutator** is a delta and the equal-time **commutator** is not: the former receives a $\delta^{(3)}(\boldsymbol\Delta)$ from the even part of the spin sum, the latter only a Bessel kernel that is nonzero at every spatial separation. In the single-mode truncation of the algebra the spin ladder operators *are* the mode ladder operators, $\tilde a=\tilde S_+/\hbar$, with $\{\tilde a,\tilde a^\dagger\}=e_0$, and the fermion-parity grading is the inner automorphism by the Hermitian involution $(-1)^F=ie_3=2\tilde S_3/\hbar$. The algebra hosts one such fermionic mode and no bosonic mode, for a reason that is a trace identity.
- **Transcribed, not derived.** The force of the theorem — that among the four pairings of spin class with bracket only two survive — is imported from relativistic quantum field theory. What the biquaternion presentation adds is that the two surviving pairings are the two *inequivalent structures the algebra actually carries*: the double-valued module for half-integer spin and the single-valued vector/adjoint representation for integer spin, together with the trace identity that decides which bracket the finite algebra can host.
- **Gap, left visible.** The article does not *derive* spin–statistics from the biquaternion algebra. The one-mode coincidence is exact but finite-dimensional, and it does not lift to the field. This gap is stated in the sections where it arises and collected in the open questions.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$ and $e_je_k=\epsilon_{jkl}e_l$ for $j\ne k$, and $i$ is the scalar imaginary with $i^2=-1$, commuting with every $e_k$. The fixed-point subspaces are $\mathbb{M}_-$ (anti-Hermitian, the material sector) and $\mathbb{M}_+$ (Hermitian, the informational sector); $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace, home of the rotation rotors, and $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_\mathbb{R}\{e_0,ie_0\}$ is the complex scalar subspace, the center of the algebra. The isomorphism with $M_2(\mathbb{C})$ is $\Phi(e_k)=-i\sigma_k$, so that $\Phi(ie_k)=\sigma_k$, and the trace formula $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ is inherited unchanged. In the field-theoretic sections we work in natural units $\hbar=c=1$ and use the gamma-matrix convention of the parents, $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I_4$ with $g=\mathrm{diag}(+1,-1,-1,-1)$, $\bar\psi=\psi^\dagger\gamma^0$, and $\not p=\gamma^0 E_{\mathbf p}-\boldsymbol\gamma\cdot\mathbf p$; the relative sign of this Clifford metric with the $ict$ gradient of the Maxwell articles is the convention the parents flag, and is not used here.

## The Theorem and Its Ingredients

The theorem has three independent inputs, and it is useful to record which of them the biquaternion framework supplies.

1. **The Lorentz representation.** Spin is a label of a representation of the double cover $SL(2,\mathbb{C})$ of the restricted Lorentz group. The covering homomorphism has kernel $\{\pm e_0\}$, so a representation either descends to $SO^+(1,3)$ — the integer-spin case — or is a genuine two-valued representation of the cover — the half-integer-spin case.
2. **Locality (microcausality).** Observables at spacelike separation must commute. Fermion fields are not observables; their bilinears are. If the field anticommutes with itself at spacelike separation, the bilinears commute; if it commutes, the bilinears do not. So locality does not by itself forbid either bracket for a spinor field: it forbids one of them only in conjunction with positivity.
3. **Positivity.** The inner product on the state space must be positive definite and the Hamiltonian bounded below. For a half-integer-spin field, commuting modes give negative-norm states and a Hamiltonian unbounded below; anticommuting modes give the positive-definite fermionic Fock space and a bounded Hamiltonian.

The third ingredient is what makes the theorem non-trivial: the two-valuedness of the spinor makes $\psi$ and $-\psi$ physically indistinguishable, so the sign that separates commuting from anticommuting quantization is invisible in the classical field. It is fixed by the quantum requirement of positivity.

The biquaternion framework supplies the first ingredient geometrically and the third ingredient only at the level of the finite single-mode algebra; it transcribes the second with the parents' plane-wave fields. The next three sections take these in order.

## Spin as a Representation of the Rotor Group

Rotations are realised in $\mathbb{B}$ by rotor conjugation. A rotation through $\theta$ about the unit axis $\hat n$ is generated by the unit real quaternion

$$
\tilde R(\theta,\hat n)=\cos\tfrac{\theta}{2}\,e_0+\sin\tfrac{\theta}{2}\,\hat n_ke_k\in\mathbb{H}_{\mathbb{B}},\qquad \tilde R\tilde R^\dagger=e_0,
$$

and $\tilde R$ is the exponential of the corresponding spin angular momentum, $\tilde R(\theta,\hat n)=\exp(-i\theta\,\hat n_k\tilde S_k/\hbar)$ with $\tilde S_k=\tfrac{\hbar}{2}ie_k\in\mathbb{M}_+$. Conjugation by $\tilde R$ rotates the vectors of the material sector $\mathbb{M}_-$ and the states of the informational sector; the map $\tilde X\mapsto\tilde R\tilde X\tilde R^\dagger$ on $\mathbb{M}_-$ has kernel $\{\pm e_0\}$ and is the covering homomorphism onto the rotation group. The rotation group is the quotient of the rotor group, which is $SU(2)$, by $\{\pm e_0\}$. These facts are established in the companion articles on angular momentum and on the Lorentz group, and are recalled here because the spin–statistics dichotomy is a statement about which side of the cover a representation lives on.

The relevant representations of the cover are the two-valued ones. The biquaternion algebra acts on itself by left multiplication, and this is where its irreducible modules live. As a module over $\mathbb{B}$, the algebra affords only $j=\tfrac12$ — the defining module $S$, since $\mathbb{B}\cong M_2(\mathbb{C})$ is simple and its left regular module is $S\oplus S$ — so the half-integer-spin structure is **native to the algebra as a module**, and it is double-valued, because $-e_0$ acts on a module element as $-\mathrm{id}$. The integer-spin representations do not appear as modules at all: the trivial $j=0$ is carried by the center under conjugation and the $j=1$ representation appears through the **adjoint action** on the imaginary quaternions, that is, on $\mathbb{M}_-$ by conjugation, and higher spins require tensor products. This is the precise algebraic form of the dichotomy.

| Representation | Carrier | Action of the rotor | Action of $-e_0$ | Spin |
|---|---|---|---|---|
| Defining spinor module | $\mathbb{C}^2$ (module) | left multiplication $\psi\mapsto\tilde\Lambda\psi$ | $-\mathrm{id}$ | half-integer ($\tfrac12$) |
| Vector (adjoint) | $\mathbb{M}_-$ | conjugation $\tilde X\mapsto\tilde\Lambda\tilde X\tilde\Lambda^\dagger$ | $+\mathrm{id}$ | integer ($1$) |
| Descended tensor powers | tensors over $\mathbb{M}_-$ | conjugation / tensor | $+\mathrm{id}$ | integer |
| Genuine spin tensor powers | tensors over the module | left multiplication | $(-1)^{2s}$ | half-integer |

The last two rows are the general pattern: on a representation of the cover with spin $s$, the nontrivial kernel element $-e_0$ acts as $(-1)^{2s}$, which is $+1$ for integer $s$ and $-1$ for half-integer $s$. This is the representation-theoretic content of the theorem's spin input, and it is the content of the companion article on the Lorentz group's classification, where the descent condition $m+n\in\mathbb{Z}$ separates the two cases.

## The Sign of the Two-Pi Rotation

Evaluate the rotor at $\theta=2\pi$ and $\theta=4\pi$:

$$
\tilde R(2\pi,\hat n)=\cos\pi\,e_0=-e_0,\qquad \tilde R(4\pi,\hat n)=\cos 2\pi\,e_0=e_0 .
$$

The $2\pi$ rotation is the nontrivial element of the kernel $\{\pm e_0\}$ of the covering, whatever the axis. Its action therefore separates the two columns of the table above in the sharpest possible way.

- On a **four-vector** $\tilde X\in\mathbb{M}_-$, conjugation by $-e_0$ is trivial, $(-e_0)\tilde X(-e_0)^\dagger=\tilde X$. A rotation by $2\pi$ returns a vector to itself; the vector representation is single-valued.
- On a **spinor** $\psi$ in the module, $2\pi$ means left multiplication by $-e_0$, so $\psi\mapsto-\psi$. The spinor representation is double-valued; only a rotation by $4\pi$ returns the spinor to itself.

The sign is not an artefact of a basis. It is the image of the nontrivial element of $\pi_1(SO^+(1,3))\cong\mathbb{Z}/2$ under the covering homomorphism, and it is why a spinor has no single-valued representative.

For an **observable** the sign cancels. The gauge-invariant bilinears of a spinor field are quadratic, $\bar\psi\,\Gamma\psi$, and under $\psi\mapsto-\psi$ they are unchanged. This is the precise sense in which $\psi$ and $-\psi$ are physically indistinguishable, and it is why the classical spinor field contains no information about whether its quanta are bosons or fermions. The $2\pi$ sign is a representation-theoretic fact about the spinor module; it is *half* of the spin–statistics connection, not the whole of it.

At the level of the operator algebra, the two transformations of the field are worth distinguishing. A rotation by $2\pi$ acts on the field by $\hat\psi\mapsto-\hat\psi$. On the single fermionic mode of the next section, conjugation by the fermion-parity element $(-1)^F$ acts on the field in exactly the same way, $(-1)^F\hat\psi\,(-1)^F=-\hat\psi$, because every term of the field expansion carries exactly one fermionic operator. Thus "a rotation by $2\pi$" and "multiplication by fermion parity" agree on the field; this agreement is the operator-level statement of $(-1)^{2s}=(-1)^F$ at $s=\tfrac12$. It is a consistency of two structures, and it does not yet say that the bracket *must* anticommute.

## The Algebra's Own One Fermionic Mode

The finite-dimensional algebra contains one fermionic mode, and the mode operators are the spin ladder operators. This is the finding of the Fock-space article, and it is the one place where the spin-$\tfrac12$ structure and the fermionic canonical relation are the same elements of $\mathbb{B}$ rather than two structures placed side by side.

The spin operators are $\tilde S_k=\tfrac{\hbar}{2}ie_k\in\mathbb{M}_+$, with the ladder combinations $\tilde S_\pm=\tfrac{\hbar}{2}(ie_1\mp e_2)$. The Fock-space article's truncated ladder is

$$
\tilde a=\tfrac12(ie_1-e_2)=\frac{\tilde S_+}{\hbar},\qquad
\tilde a^\dagger=\tfrac12(ie_1+e_2)=\frac{\tilde S_-}{\hbar},
$$

and direct computation gives

$$
\tilde a^2=0,\qquad (\tilde a^\dagger)^2=0,\qquad
\{\tilde a,\tilde a^\dagger\}=e_0,\qquad
[\tilde a,\tilde a^\dagger]=ie_3\ne e_0 .
$$

So the truncated ladder satisfies the **fermionic** canonical anticommutation relations exactly, with no truncation error, while its commutator fails the bosonic relation by a nonzero, non-central element. The number operator and the fermion-parity element are

$$
\tilde N=\tilde a^\dagger\tilde a=\tfrac12(e_0-ie_3)=P_-(e_3),\qquad
(-1)^F=e_0-2\tilde N=ie_3=\frac{2\tilde S_3}{\hbar},
$$

with $\tilde N^2=\tilde N$, so that $\tilde N$ is a pure-state projector and the single-mode occupation is valued in $\{0,1\}$. The parity element is Hermitian, squares to $e_0$, and gives the $\mathbb{Z}/2$ grading by inner automorphism,

$$
(-1)^F\tilde a\,(-1)^F=-\tilde a,\qquad
(-1)^F\tilde N\,(-1)^F=\tilde N .
$$

This is a sharp statement about the $\mathbb{Z}/2$ grading that the KMS article identifies as missing: for one mode it is not missing at all. It is realized **inside** $\mathbb{B}$ as conjugation by a Hermitian involution of the informational sector, and its odd subspace is the two-complex-dimensional span of $\tilde a$ and $\tilde a^\dagger$. What the KMS article requires for a field is a grading on the *operator algebra of all modes*; the single-mode element above is not that, and the field grading is not an element of $\mathbb{B}$ by the dimension count. The two statements are compatible: the grading is algebraic for one mode and external for the field.

The bosonic counterpart fails for a reason that is independent of dimension counting by hand and is worth recording, because it is a trace identity. In $\mathbb{B}$ a canonical commutator would have to be central, $[\tilde a,\tilde a^\dagger]=c\,e_0$ with $c\in\mathbb{C}$, since the center is $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$. But the trace of a commutator vanishes and $\mathrm{Tr}(e_0)=2\,\mathrm{Sc}(e_0)=2$, so

$$
0=\mathrm{Tr}\big([\tilde a,\tilde a^\dagger]\big)=c\,\mathrm{Tr}(e_0)=2c,
$$

and hence $c=0$. No pair in $\mathbb{B}$ realizes the Heisenberg relation. The algebra hosts one fermionic mode and no bosonic mode; the second relation, $\tilde a\tilde a^\dagger=e_0-\tilde a^\dagger\tilde a$, which a fermionic mode satisfies and a bosonic mode cannot, is the identity that decides it.

The dimension count makes the same point. $\dim_\mathbb{C}M_2(\mathbb{C})=4=\dim_\mathbb{C}\mathbb{B}$, and the Clifford algebra $\mathrm{Cl}(2)$ generated by $\tilde a,\tilde a^\dagger$ from the vacuum is all of $\mathbb{B}$; one mode saturates the algebra, so no second mode can be added. Whether the framework *selects* the fermionic structure, or merely has room for exactly one instance of it, is the open question the Fock-space article raises and this article does not decide. The single-mode coincidence is exact; it is a coincidence of dimensions until something more is said.

## Microcausality: The Equal-Time Brackets

The operator-level content of the theorem is a computation with the parents' free field. The mode expansion is

$$
\hat\psi(x)=\int\!\frac{d^3p}{(2\pi)^3}\,\frac{1}{\sqrt{2E_{\mathbf p}}}
\sum_r\Big[\hat a_r(\mathbf p)\,u^{(r)}(\mathbf p)\,e^{-ip\cdot x}
+\hat b_r^\dagger(\mathbf p)\,v^{(r)}(\mathbf p)\,e^{+ip\cdot x}\Big],
$$

with $\hat\psi^\dagger$ the adjoint and the parents' spinors and spin sums, $\sum_r u^{(r)}\bar u^{(r)}=\not p+m$ and $\sum_r v^{(r)}\bar v^{(r)}=\not p-m$, hence

$$
\sum_r u^{(r)}u^{(r)\dagger}=E_{\mathbf p}I_4+m\gamma^0+\gamma^0\boldsymbol\gamma\cdot\mathbf p,\qquad
\sum_r v^{(r)}v^{(r)\dagger}=E_{\mathbf p}I_4-m\gamma^0+\gamma^0\boldsymbol\gamma\cdot\mathbf p .
$$

The field is a spinor-module field; the biquaternion content is the module on which it is built and the notation, and the mode algebra is imposed. Two choices are available. The **Fermi choice** is
$\{\hat a_r(\mathbf p),\hat a_s^\dagger(\mathbf q)\}=(2\pi)^3\delta_{rs}\delta^{(3)}(\mathbf p-\mathbf q)$, and likewise for $\hat b$, with all other brackets vanishing; the **Bose choice** replaces the braces by brackets.

**The anticommutator (Fermi choice).** At equal times $x^0=y^0$ the two branches enter with opposite phases, and with $\theta=\mathbf p\cdot\boldsymbol\Delta$, $\boldsymbol\Delta=\mathbf x-\mathbf y$ (the sign of $\theta$ is fixed by the mode-expansion convention and drops out of the anticommutator, only $\cos\theta$ surviving there),

$$
\sum_r\Big[u^{(r)}u^{(r)\dagger}e^{+i\theta}+v^{(r)}v^{(r)\dagger}e^{-i\theta}\Big]
=2E_{\mathbf p}\cos\theta\,I_4
+2\cos\theta\,\gamma^0\boldsymbol\gamma\cdot\mathbf p
+2im\sin\theta\,\gamma^0 .
$$

The map $\mathbf p\mapsto-\mathbf p$ sends $\theta\mapsto-\theta$ and $\boldsymbol\gamma\cdot\mathbf p\mapsto-\boldsymbol\gamma\cdot\mathbf p$. The first term is even and the second and third are odd, so the odd terms vanish under symmetric integration and

$$
\{\hat\psi_a(x,t),\hat\psi_b^\dagger(y,t)\}=\delta_{ab}\,\delta^{(3)}(\mathbf x-\mathbf y).
$$

The spinorial part is the term $2\cos\theta\,\gamma^0\boldsymbol\gamma\cdot\mathbf p$ — the part that carries the spin structure through $\boldsymbol\gamma\cdot\mathbf p$. It is odd in $\mathbf p$ despite carrying the same $\cos\theta$ phase as the scalar term, and it cancels. Reading the two terms as "same phase, therefore same fate" is exactly the error the parity check is there to catch: the phase is even, but the spin factor $\boldsymbol\gamma\cdot\mathbf p$ is odd, and the product is odd. Division by $2E_{\mathbf p}$ leaves the even part $\cos\theta\,I_4$, which integrates to $\delta^{(3)}(\boldsymbol\Delta)$, and the anticommutator is local.

**The commutator (Bose choice for the same field).** Replacing the plus between the branches by a minus, the same spin sums give

$$
\sum_r\Big[u^{(r)}u^{(r)\dagger}e^{+i\theta}-v^{(r)}v^{(r)\dagger}e^{-i\theta}\Big]
=2iE_{\mathbf p}\sin\theta\,I_4
+2m\cos\theta\,\gamma^0
+2i\sin\theta\,\gamma^0\boldsymbol\gamma\cdot\mathbf p .
$$

Here the even part is the last two terms — $2iE_{\mathbf p}\sin\theta\,I_4$ is odd — and it does **not** vanish:

$$
[\hat\psi_a(x,t),\hat\psi_b^\dagger(y,t)]
=\int\!\frac{d^3p}{(2\pi)^3}\,\frac{1}{2E_{\mathbf p}}
\Big[2m\cos\theta\,\gamma^0+2i\sin\theta\,\gamma^0\boldsymbol\gamma\cdot\mathbf p\Big]_{ab},
$$

after the odd term is dropped. This remaining integral evaluates to

$$
[\hat\psi(x,t),\hat\psi^\dagger(y,t)]
=\gamma^0\big(m-i\boldsymbol\gamma\cdot\nabla_{\boldsymbol\Delta}\big)F(\boldsymbol\Delta),
\qquad
F(\boldsymbol\Delta)=\int\!\frac{d^3p}{(2\pi)^3}\,\frac{1}{E_{\mathbf p}}\cos(\mathbf p\cdot\boldsymbol\Delta),
$$

and for $m>0$ the kernel is $F(\boldsymbol\Delta)=\dfrac{m}{2\pi^2|\boldsymbol\Delta|}\,K_1\!\big(m|\boldsymbol\Delta|\big)$, the modified Bessel function of the second kind. The identity $\int_0^\infty\frac{p}{E}\sin(p\Delta)\,dp=mK_1(m\Delta)$ was checked numerically for $m=1$ and $\Delta=0.5,2,5,10$, to thirty digits. The kernel is nonzero for **every** $\boldsymbol\Delta\ne 0$; it decays exponentially for large separations, but it does not vanish. So at equal times and spatial separation $\boldsymbol\Delta\ne 0$ — a spacelike separation — the commutator of the spin-$\tfrac12$ field is nonzero, while the anticommutator is zero. The Bose choice fails microcausality for a half-integer-spin field.

The same content has a covariant shorthand. With the field quantized by anticommutators, the general two-point functions are

$$
\{\hat\psi(x),\bar{\hat\psi}(y)\}=(i\not\partial_x+m)\,\Delta_{\mathrm{A}}(x-y),
\qquad
\langle0|[\hat\psi(x),\bar{\hat\psi}(y)]|0\rangle=(i\not\partial_x+m)\,G_{\mathrm{S}}(x-y),
$$

where $\Delta_{\mathrm{A}}$ is the antisymmetric combination of the two branch phases — the Pauli–Jordan-type kernel, supported inside the light cone and vanishing for spacelike separation — and $G_{\mathrm{S}}$ is the symmetric combination, which does not vanish there. The anticommutator is a $c$-number and equals its own vacuum expectation; under anticommutation relations the commutator is not a $c$-number, and the second identity is its vacuum expectation, whose $c$-number part is what carries $G_{\mathrm{S}}$. The anticommutator inherits the vanishing of $\Delta_{\mathrm{A}}$; the commutator's vacuum expectation inherits the non-vanishing of $G_{\mathrm{S}}$. At equal times these reduce to the delta and to the Bessel kernel computed above. The exact normalizations of $\Delta_{\mathrm{A}}$ and $G_{\mathrm{S}}$ carry the conventional factor of $i$; the covariant form is the standard textbook identity and is recorded as such, and the equal-time form is what was recomputed here.

## The Energy and the Norm

The third ingredient is positivity, and it is where the finite algebra has a native statement. With the mode expansion, the Hamiltonian of the free spinor field is

$$
\hat H=\sum_r\int\!\frac{d^3p}{(2\pi)^3}\,E_{\mathbf p}\,
\big(\hat a_r^\dagger\hat a_r-\hat b_r\hat b_r^\dagger\big).
$$

The sign of the antiparticle term is decided by the bracket. With the **Fermi choice**, $\hat b\hat b^\dagger=e_0-\hat b^\dagger\hat b$, so after normal ordering

$$
\hat H=\sum_r\int\!\frac{d^3p}{(2\pi)^3}\,E_{\mathbf p}\,
\big(\hat a_r^\dagger\hat a_r+\hat b_r^\dagger\hat b_r\big)+E_0,
$$

which is non-negative on the Fock space up to the c-number $E_0$ that normal ordering removes. With the **Bose choice**, $\hat b\hat b^\dagger=e_0+\hat b^\dagger\hat b$, and the antiparticle contribution enters with the opposite sign, $\hat a^\dagger\hat a-\hat b^\dagger\hat b$: the energy is unbounded below as antiparticle number grows, and the vacuum is unstable. The same sign appears in the norm: the anticommutator gives the positive-definite fermionic Fock space, the commutator gives an indefinite metric. This is the parent quantization article's argument, and it is stated here because it is half of the theorem's force.

The finite algebra shows the same identity in miniature. The single fermionic mode satisfies $\tilde a\tilde a^\dagger=e_0-\tilde a^\dagger\tilde a$, so the normal-ordered Hamiltonian of one mode is $\hbar\omega\,\tilde a^\dagger\tilde a\ge 0$ on the module, with spectrum $\{0,\hbar\omega\}$ because $\tilde N$ is a projector. Its would-be bosonic partner would need $\tilde a\tilde a^\dagger=e_0+\tilde a^\dagger\tilde a$, i.e. $[\tilde a,\tilde a^\dagger]=e_0$, which the trace identity excludes. The positivity of the energy and the fermionic bracket are the same statement about the sign in $\tilde a\tilde a^\dagger=e_0\mp\tilde a^\dagger\tilde a$.

## The Four Quantizations

Collecting the two spin classes and the two brackets, four pairings are possible, and the theorem is the statement that two of them fail.

| Spin class | Bracket | Representation of the cover | Outcome |
|---|---|---|---|
| Integer | Commutator | descends, $-e_0\mapsto+1$ | consistent: scalar field, Maxwell field |
| Half-integer | Anticommutator | genuine spin rep, $-e_0\mapsto-1$ | consistent: Dirac field, positive norm, bounded energy |
| Half-integer | Commutator | genuine spin rep | fails microcausality (Bessel kernel above) and has unbounded energy |
| Integer | Anticommutator | descends | fails microcausality: the field itself is an observable, so its **commutator** must vanish at spacelike separation, but under anticommutation relations the commutator is no longer the $c$-number antisymmetric (Pauli–Jordan) kernel and does not vanish |

The integer-spin row is the parents' integer-spin case. The biquaternion Maxwell field lives in $\mathbb{M}_-$, the vector representation, on which $-e_0$ acts trivially, and its canonical quantization uses commutators; the scalar (Klein–Gordon) field has a commutator equal to the antisymmetric Pauli–Jordan kernel, which vanishes for spacelike separation, while its symmetric kernel does not. The half-integer rows are the spinor-module case computed above. The two surviving pairings are precisely the two inequivalent structures the algebra carries: the double-valued module paired with anticommutators, and the single-valued material-sector representation paired with commutators.

The table also displays what the framework does and does not explain. The *spin* column is algebraic: integer versus half-integer is the descent condition for the rotor action, and the $2\pi$ sign is the action of $-e_0$, both recomputed in $\mathbb{B}$. The *bracket* column is transcribed from field theory; the algebra does not, at the level developed here, force the pairing. And the two columns are tied together only through the theorem, which is why the one-mode coincidence of Section 5 is suggestive but not decisive: it exhibits one entry of the table — half-integer spin, anticommutator — inside $\mathbb{B}$, and says nothing about the other three.

## What the Framework Establishes and What It Only Transcribes

**Established, and recomputed.**

- The rotor group of unit real quaternions is the double cover of the rotation group; the rotor through $2\pi$ about any axis is $-e_0$, and through $4\pi$ is $e_0$.
- Under the rotor action, the half-integer-spin representations live on the spinor module and its tensor powers, where $-e_0$ acts as $(-1)^{2s}=-1$, while the integer-spin representations live on $\mathbb{M}_-$ and its tensor powers, where $-e_0$ acts as $+1$. The algebra affords $j=\tfrac12$ as a module, $j=0$ on the center under conjugation, and $j=1$ through the adjoint action on $\mathbb{M}_-$.
- The single-mode ladder operators are the spin ladder operators, $\tilde a=\tilde S_+/\hbar$, and satisfy $\{\tilde a,\tilde a^\dagger\}=e_0$; the number operator is the idempotent $P_-(e_3)$; and the fermion-parity grading is the inner automorphism by $(-1)^F=ie_3=2\tilde S_3/\hbar$, an element of $\mathbb{M}_+$.
- No bosonic mode exists in $\mathbb{B}$: a canonical commutator would be central and its trace would vanish, forcing it to zero.
- For the free spin-$\tfrac12$ field built on the module, the equal-time anticommutator is $\delta_{ab}\delta^{(3)}(\boldsymbol\Delta)$ and the equal-time commutator is a nonzero Bessel kernel at every $\boldsymbol\Delta\ne 0$. The spinorial part of the anticommutator, $2\cos\theta\,\gamma^0\boldsymbol\gamma\cdot\mathbf p$, is odd in $\mathbf p$ and cancels; this was checked independently of the terms that suggested it.
- The sign in $\tilde a\tilde a^\dagger=e_0\mp\tilde a^\dagger\tilde a$ is the sign of the antiparticle term in the Hamiltonian and the sign that decides positivity of the norm.

**Transcribed, not derived.**

- That the bracket is *forced* by the conjunction of locality, positivity and Lorentz invariance. The article exhibits the failure of the wrong choices; it does not prove that no other structure evades it.
- The covariant identities $\{\hat\psi,\bar{\hat\psi}\}=(i\not\partial+m)\Delta_{\mathrm{A}}$ and $[\hat\psi,\bar{\hat\psi}]=(i\not\partial+m)G_{\mathrm{S}}$, and the Pauli–Jordan-type and symmetric kernels.
- The scalar-field and Maxwell-field contrast, and the standard microcausality argument for integer spin.

**Gap, left visible.**

- The framework does not *derive* spin–statistics. The spin dichotomy is algebraic; the bracket pairing is imposed. The one-mode coincidence that relates the spin ladder to the fermionic mode is exact but finite-dimensional, and the field algebra is infinite-dimensional, where both the exterior and the symmetric algebra are available on the same footing.
- Higher spin is not algebraic in the same sense. The $j=1$ representation is the adjoint action, not a module, and higher spins need tensor products; whether the framework's integer-spin structure has a native quantization of its own is not established here.

## Open Questions

**1. Does the framework derive spin–statistics or only transcribe it?** The central question. The spin dichotomy is algebraic and the $2\pi$ sign is an element of the algebra; the bracket pairing is imported. The single-mode realization is the only place where the two meet inside $\mathbb{B}$, and it is finite-dimensional. Whether some structure of the algebra — a graded extension, a crossed product, or the full tensor algebra of the module — forces the pairing is open and is not decided here.

**2. Is the one-mode coincidence structural or dimensional?** $\dim_\mathbb{C}\mathbb{B}=4=\dim_\mathbb{C}\mathrm{Cl}(2)$ makes the single fermionic mode fit, and the same element that is the spin ladder is the fermionic mode ladder. Is this a reflection of the spin-$\tfrac12$ structure of the module, or a coincidence of dimensions? The article's honest answer is that it is a coincidence until something more is said.

**3. What is the grading for a field?** The single-mode parity $(-1)^F=ie_3$ is an element of $\mathbb{B}$; the field grading is not, by the dimension count, and the KMS article's requirement of a $\mathbb{Z}/2$ grading on the field algebra stands. Can an extension of $\mathbb{B}$ carry it, and does that extension have a biquaternion interpretation?

**4. Integer-spin quantization in the algebra.** The vector representation appears through the adjoint action on $\mathbb{M}_-$, and its quantization is standard and imported. Is there a native construction of the integer-spin Fock space from the algebra that mirrors the single-mode fermionic one, and if not, what obstructs it beyond the trace identity?

**5. The massless limit.** The microcausality failure of the commutator was computed at $m>0$, where the surviving kernel is the Bessel function $K_1$. As $m\to 0$ the kernel becomes $1/(2\pi^2|\boldsymbol\Delta|^2)$ and still does not vanish; the massless case is not qualitatively different, but the two helicity states of the Weyl field and the role of chirality in the theorem have not been developed here.

**6. Empirical content.** The construction reproduces standard field theory. Any deviation would have to appear where the algebra is used beyond transcription — for example in a modification of the one-mode identification or in the coupling to the material sector; none is visible at the level developed here.

## Summary

The spin–statistics theorem pairs half-integer spin with anticommutators and integer spin with commutators. In the biquaternion framework the spin half of the theorem is algebraic and exact: the rotor group of unit real quaternions is the double cover of the rotation group, the rotor through $2\pi$ is $-e_0$, half-integer-spin representations live on the spinor module where $-e_0$ acts as $-\mathrm{id}$, and integer-spin representations live on the material sector $\mathbb{M}_-$ where it acts as $+\mathrm{id}$. The framework's finite algebra also contains one fermionic mode, whose ladder operators are the spin ladder operators, $\tilde a=\tilde S_+/\hbar$, and whose parity grading is the Hermitian element $(-1)^F=ie_3=2\tilde S_3/\hbar$; no bosonic mode exists, because a canonical commutator would be central and traceless.

The statistics half is transcribed with the parents' field. For the free spin-$\tfrac12$ field, the equal-time anticommutator is $\delta_{ab}\delta^{(3)}(\boldsymbol\Delta)$, the spinorial term $2\cos\theta\,\gamma^0\boldsymbol\gamma\cdot\mathbf p$ cancelling as an odd function of $\mathbf p$; the equal-time commutator, by contrast, leaves the Bessel kernel $\gamma^0(m-i\boldsymbol\gamma\cdot\nabla)F(\boldsymbol\Delta)$ and fails to vanish at any spatial separation. The same sign that selects the anticommutator selects the positive sign in $\tilde a\tilde a^\dagger=e_0-\tilde a^\dagger\tilde a$, and hence a bounded Hamiltonian and a positive-definite norm.

What the framework establishes is that the two pairings which survive the theorem are the two inequivalent structures the algebra actually carries, and that the $2\pi$ sign which distinguishes them is an element of the algebra. What it does not establish is that the algebra forces the pairing; spin–statistics is exhibited in biquaternionic form, not derived from it. The one-mode coincidence is the visible edge of the question, and it is left as the article's central open problem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_je_k=\epsilon_{jkl}e_l$ $(j\ne k)$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}$ | Real-quaternion subspace; center $\mathbb{C}e_0$ |
| $\Phi(e_k)=-i\sigma_k$, $\Phi(ie_k)=\sigma_k$ | Isomorphism with $M_2(\mathbb{C})$ |
| $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ | Trace pairing of the informational sector |
| $\tilde R(\theta,\hat n)=\cos\tfrac{\theta}{2}e_0+\sin\tfrac{\theta}{2}\hat n_ke_k$ | Rotation rotor (unit real quaternion) |
| $\tilde R(2\pi,\hat n)=-e_0$, $\tilde R(4\pi,\hat n)=e_0$ | The two-valued sign of the spinor module |
| $\tilde S_k=\tfrac{\hbar}{2}ie_k$, $\tilde S_\pm=\tfrac{\hbar}{2}(ie_1\mp e_2)$ | Spin operators in $\mathbb{M}_+$; ladders in $\mathbb{B}$ (they are not Hermitian) |
| $\tilde a=\tfrac12(ie_1-e_2)=\tilde S_+/\hbar$, $\tilde a^\dagger=\tilde S_-/\hbar$ | Single fermionic mode ladder |
| $\tilde N=\tilde a^\dagger\tilde a=\tfrac12(e_0-ie_3)=P_-(e_3)$ | Single-mode number operator (idempotent) |
| $(-1)^F=ie_3=e_0-2\tilde N=2\tilde S_3/\hbar$ | Fermion parity; Hermitian involution in $\mathbb{M}_+$ |
| $\{\tilde a,\tilde a^\dagger\}=e_0$, $[\tilde a,\tilde a^\dagger]=ie_3$ | Fermionic mode relation; failure of the bosonic relation |
| $\hat\psi$, $\bar{\hat\psi}=\hat\psi^\dagger\gamma^0$ | Quantized spinor-module field and its Dirac adjoint |
| $\hat a_r(\mathbf p),\hat b_r^\dagger(\mathbf p)$ | Annihilation and antiparticle creation operators |
| $u^{(r)}(\mathbf p),v^{(r)}(\mathbf p)$ | Positive- and negative-frequency spinors (from the parents) |
| $\sum_r u^{(r)}u^{(r)\dagger}=E_{\mathbf p}I_4+m\gamma^0+\gamma^0\boldsymbol\gamma\cdot\mathbf p$ | Spin sum (likewise $v$ with $-m$) |
| $\theta=\mathbf p\cdot\boldsymbol\Delta$, $\boldsymbol\Delta=\mathbf x-\mathbf y$ | Phase and spatial separation in the equal-time brackets |
| $\{\hat\psi_a,\hat\psi_b^\dagger\}=\delta_{ab}\delta^{(3)}(\boldsymbol\Delta)$ | Local equal-time anticommutator |
| $[\hat\psi,\hat\psi^\dagger]=\gamma^0(m-i\boldsymbol\gamma\cdot\nabla)F(\boldsymbol\Delta)$ | Nonlocal equal-time commutator |
| $F(\boldsymbol\Delta)=\frac{m}{2\pi^2|\boldsymbol\Delta|}K_1(m|\boldsymbol\Delta|)$ | Surviving commutator kernel ($m>0$) |
| $\Delta_{\mathrm{A}}(x-y)$, $G_{\mathrm{S}}(x-y)$ | Antisymmetric (Pauli–Jordan-type) and symmetric two-point kernels |
| $\hat H=\sum_r\int\frac{d^3p}{(2\pi)^3}E_{\mathbf p}(\hat a_r^\dagger\hat a_r+\hat b_r^\dagger\hat b_r)+E_0$ | Normal-ordered Hamiltonian (Fermi choice) |

## Further Reading

- W. Pauli, "The Connection Between Spin and Statistics," *Physical Review* **58** (1940) 716–722, for the original theorem and the positivity argument.
- M. Fierz, "Über die relativistische Theorie kräftefreier Teilchen mit beliebigem Spin," *Helvetica Physica Acta* **12** (1939) 3–37, for the antecedent representation-theoretic analysis.
- G. Lüders and B. Zumino, "Connection between Spin and Statistics," *Physical Review* **110** (1958) 1450–1453, for the general proof in the axiomatic setting.
- R. F. Streater and A. S. Wightman, *PCT, Spin and Statistics, and All That* (Benjamin, 1964), for the Wightman-axiomatic treatment and the locality–positivity hypotheses.
- R. Haag, *Local Quantum Physics* (2nd ed., Springer, 1996), for the algebraic formulation and the role of the grading.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), and M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the standard equal-time and covariant two-point functions used here.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw–Hill, 1965), for the spin sums, the Pauli–Jordan function and the microcausality computation.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Clifford-algebra origin of the spin group and its double cover.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor realization of rotations and its two-valuedness.
- Companion articles: *Canonical Quantization of the Biquaternion Dirac Field*; *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*; *The Dirac Equation in Biquaternionic Form*; *Angular Momentum and Spin in Biquaternionic Form*; *The Lorentz Group in Biquaternionic Form — Structure and Representations*; *The Spinor Module in Biquaternionic Form and Its Lorentz Action*; *The Spinor Representation of the Lorentz Group in Biquaternionic Form*; *The KMS Condition and the Biquaternion Framework*; *Canonical Quantization of the Biquaternion Maxwell Field*; *The Klein–Gordon Equation in Biquaternionic Form*.
