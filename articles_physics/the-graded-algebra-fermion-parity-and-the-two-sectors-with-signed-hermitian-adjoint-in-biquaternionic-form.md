# __The Graded Algebra, Fermion Parity and the Two Sectors with Signed Hermitian Adjoint in Biquaternionic Form__

## Introduction

The biquaternion algebra is the even part of the Clifford algebra of Minkowski space, $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}$, and that identification is the whole source of the geometric content of the series. It has a second consequence that is used throughout the physics but stated nowhere in one place: the ambient algebra is **$\mathbb{Z}/2$-graded**, and the grading is the fermion parity of the theory. The even slot is the bosonic sector, and it is the biquaternion algebra; the odd slot is the fermionic sector, and it is the slot that carries the Dirac generators and the anticommuting mode operators.

This article is the **Hermitian reading** of that grading. In *The Graded Algebra, Fermion Parity and the Two Sectors with Signed Inner Conjugation in Biquaternionic Form* the operator that carries the parity is the signed inner conjugation $\mathrm{Ad}^{\alpha}_x(y)=\alpha(x)yx^{-1}$, whose right factor is the inverse: the factor that belongs to the group of units, to the isometries and to the Lorentz group. Here the right factor is the **Hermitian adjoint** $x^{*}$, the adjoint of the spinor form of the framework, and the operator is the **signed Hermitian sandwich**

$$
\Theta^{\alpha}_x(y)=\alpha(x)\,y\,x^{*}.
$$

The two right factors are different maps. The dagger is the inverse exactly on the unit slice of the real quaternions and differs from it elsewhere by the coefficient-conjugated norm, $x^{*}=\sigma(N(x))\,\sigma(x)^{-1}$, so the inverse reading belongs to the isometries and the adjoint reading to the unitarity. The physics of the two is therefore not the same, and the difference is a norm, that is a scalar, in every case in which the corpus computes.

Three facts organise the Hermitian reading. The first is that the dagger is **even**: it preserves the parity, so the grading is a symmetry of the Hermitian structure, and the two sectors $\mathbb{M}_+$ and $\mathbb{M}_-$ of the corpus are its fixed and anti-fixed loci. The second is the sharpest statement of the article: the sign that separates the signed Hermitian sandwich from the unsigned one is the parity itself, $\Theta^{\alpha}_x=\varepsilon_x\Theta_x$, and it is **invisible on the algebra**, because every element of $\mathbb{B}$ is even. On the algebra the signed and the unsigned Hermitian sandwich are the same operator, $\Theta^{\alpha}_x=\Theta_x$ for $x\in\mathbb{B}$; the *signed* of the title is therefore exactly the **fermionic** sector, and the entire physics of the series, computed in $\mathbb{B}$, is the physics of the unsigned member. The third is that the twist is again a conjugation, by the volume element, $\alpha(x)=\Omega x\Omega^{-1}$; this reading is unchanged from the inverse article, because the twist sits in the **left** factor and the adjoint in the right one: parity on the left and adjointness on the right are independent structures, and the article keeps them apart.

The ambient graded algebra, the two slots, the dictionary $e_1\mapsto\gamma^2\gamma^3$, $i\mapsto-\Omega$ and the chirality operator $\gamma^5=i\Omega$ are *The Clifford Structure of the Biquaternion Algebra*; the Hermitian dagger, the sectors $\mathbb{M}_\pm$, the reflection and the determinants of the versors are *Biquaternion Versors and the Orthogonal Group*; the fermionic mode and $(-1)^F=ie_3$ are *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*; the parity of the state space, $\Gamma(-I)=(-1)^{\hat N}$, is *The Fermionic Fock Space in Biquaternionic Form*. The inverse-conjugation reading is cited and never reused; the graded bracket built on this parity is *The Superalgebra Reading and the Odd Extension with Signed Hermitian Adjoint in Biquaternionic Form*; the abstract algebra of the operator is the maths pair *The Grading of a Hilbert Algebra with Signed Hermitian Adjoint* and *Two-Sided Operators on a Hilbert Algebra with Signed Hermitian Adjoint*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; the Hermitian dagger is \tilde{Q}^{*}=\overline{\tilde{Q}^{\natural}}, the coefficient conjugation composed with the quaternion conjugation; the norm is $N(\tilde{Q})=\sum_\mu Q_\mu^2=\tilde{Q}\tilde{Q}^{\natural}$; $\sigma$ is the coefficient conjugation, fixing the quaternion units and negating $i$; $\mathrm{Cl}_{1,3}$ is the ambient algebra of the Dirac matrices in the mostly-minus convention, $\Omega=\gamma^0\gamma^1\gamma^2\gamma^3$; the twist is the grade involution, $\alpha(x)=\varepsilon_x x$ with $\varepsilon_x=(-1)^{\lvert x\rvert}$; and the two operators are $\Theta^{\alpha}_x(y)=\alpha(x)\,y\,x^{*}$ and $\Theta_x(y)=x\,y\,x^{*}$.

## The Grading of the Ambient Algebra

**Given.** The Clifford algebra of Minkowski space is graded by parity, $\mathrm{Cl}_{1,3}=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$, with $\mathrm{Cl}^i\mathrm{Cl}^j\subseteq\mathrm{Cl}^{i+j}$. The even part is $\mathbb{B}$, and the odd part is the slot containing the generators; the dictionary sends the algebra to the even slot, so every element of the algebra in which the series computes is even.

The multiplication table, read physically, is the parity table,

$$
\text{even}\cdot\text{even}=\text{even},\quad
\text{even}\cdot\text{odd}=\text{odd},\quad
\text{odd}\cdot\text{even}=\text{odd},\quad
\text{odd}\cdot\text{odd}=\text{even},
$$

that is, the parity of a product is the sum of the parities. The generators $\gamma^\mu$ are odd; the bivectors $\gamma^\mu\gamma^\nu$ and the volume element are even; the square $(\gamma^\mu)^2=\pm1$ is a scalar and hence even. The physical reading is the whole of the grading in one sentence: a product of an odd number of fermionic objects is fermionic, a product of an even number is bosonic.

**Remark.** The identification $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}$ is therefore not merely "$\mathbb{B}$ is a Clifford algebra"; it says *which* slot of the ambient graded algebra the biquaternion algebra is. The whole physics series computes in the bosonic sector, and this is why the parity sign of the next but one section is invisible in it.

## The Dagger Is Even

The Hermitian dagger of the algebra is the adjoint of the spinor form, and the first thing the grading says about it is that it is a symmetry of the grading.

**Proposition (the dagger preserves the parity and is an anti-involution).** The dagger is $\mathbb{C}$-antilinear, involutive and an anti-automorphism,

$$
(xy)^{*}=y^{*}x^{*},\qquad (x^{*})^{\dagger}=x,
$$

and it preserves the degree modulo two, $(\mathrm{Cl}^k)^{\dagger}\subseteq\mathrm{Cl}^k$, so $\lvert x^{*}\rvert=\lvert x\rvert$ on homogeneous elements.

*Proof.* The coefficient conjugation is a $\mathbb{C}$-antilinear automorphism that acts on the coefficients and not on the degree; the quaternion conjugation of the algebra is the reversion of the even slot, which reverses the order of the factors, so on a product $\tilde{P}\tilde{Q}$ one has $(\tilde{P}\tilde{Q})^{*}=\tilde{Q}^{*}\tilde{P}^{*}$; a product of $k$ generators is sent to a product of $k$ generators. For the odd slot this is the definition used in *The Reflection Read in the Hermitian Pairing* below.

**The two sectors of the corpus, in the language of the dagger.** The fixed and anti-fixed loci of the dagger are the two distinguished subspaces,

$$
\mathbb{M}_+=\{x:x^{*}=x\}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_1,ie_2,ie_3\},\qquad
\mathbb{M}_-=\{x:x^{*}=-x\}=\mathrm{span}_{\mathbb{R}}\{ie_0,e_1,e_2,e_3\},
$$

the informational and the material sector, and the algebra is their direct sum, $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$. This is the eigen-decomposition of the dagger, and it is **not** an algebra grading: the product of two Hermitian elements need not be Hermitian, and $(ie_1)(ie_2)=-e_3$ is anti-Hermitian. The sector splitting is the Hermitian structure of the algebra read at its two eigenvalues, and the next section of the grading article is precisely the warning that it must not be conflated with the parity.

**Proposition (the dagger and the inverse).** For every invertible $x\in\mathbb{B}$,

$$
x^{*}=\sigma(N(x))\,\sigma(x)^{-1}.
$$

*Proof.* The norm identity $\bar x=N(x)\,x^{-1}$ of the algebra gives $x^{*}=\sigma(\bar x)=\sigma(N(x))\,\sigma(x)^{-1}$, the coefficient conjugation being an automorphism.

**Corollary (where the dagger is the inverse).** The dagger equals the inverse exactly when $\sigma(x)=\sigma(N(x))\,x$. In particular, on the unit slice of the real quaternions — real coefficients with $N(x)=1$, the unit quaternions $\mathrm{SU}(2)$ — the two maps coincide, which is the agreement of the dagger with the Clifford conjugation on the real-quaternion slice recorded by *Biquaternion Versors and the Orthogonal Group*. Everywhere else they differ by the coefficient-conjugated norm, and a reader who replaces a dagger by an inverse is computing on that slice whether he says so or not.

**Remark (the norm factor of the sandwich).** The Hermitian sandwich multiplies the norm by the modulus squared of the parameter,

$$
N\bigl(x\,y\,x^{*}\bigr)=\lvert N(x)\rvert^{2}\,N(y),
$$

so the operator is a similarity of the spinor form of ratio $\lvert N(x)\rvert^{2}$ and an isometry exactly on the unit slice $\lvert N\rvert=1$. The signed **inner** conjugation of the companion article, $\alpha(x)\,y\,x^{-1}$, preserves the norm exactly, its ratio being $1$; the two readings therefore differ on the norm by the scalar $\lvert N(x)\rvert^{2}$, and they differ only by a phase of the parameter on the unit slice. That scalar is the whole difference between the two readings of the parity below.

## The Twist Is the Conjugation by the Pseudoscalar

The twist $\alpha$ of the signed Hermitian sandwich is usually introduced as the abstract map, the grade involution, equal to $+1$ on the even slot and $-1$ on the odd slot. In the ambient algebra it is an ordinary conjugation, and the statement is the one of the inverse article, because it concerns the left factor.

**Theorem (the grade involution is a conjugation).** Let $\Omega=\gamma^0\gamma^1\gamma^2\gamma^3$ be the volume element of $\mathrm{Cl}_{1,3}$. Then $\Omega^2=-1$, $\Omega$ commutes with the even slot and anticommutes with every generator, and for every homogeneous $x$

$$
\Omega\,x\,\Omega^{-1}=(-1)^{\lvert x\rvert}\,x=\alpha(x).
$$

With the dictionary $i\mapsto-\Omega$, the same statement reads: the grade involution is the conjugation by the central scalar imaginary.

**Proof.** The volume element of an even-dimensional Clifford algebra anticommutes with every generator, since moving $\gamma^{j}$ past the monomial $\Omega$ costs the sign $(-1)^{3}$; a monomial $x=\gamma^{\mu_1}\cdots\gamma^{\mu_k}$ therefore satisfies $\Omega x=(-1)^{k}x\Omega$, and $\Omega^{-1}$ exists because $\Omega^2=-1\neq0$. On the even slot $\lvert x\rvert$ is even and the conjugation is the identity.

**Remark (the left factor and the right factor are different structures).** The twist is a statement about the left factor of $\Theta^{\alpha}$: it is the parity of the parameter. The dagger is a statement about the right factor: it is the unitarity of the parameter. Nothing forces the two to be related, and the corpus's physics uses them independently — the twist in the reflection count and in the parity of the graded bracket, the dagger in the spinor form and in the probability. A reader who reads $\Theta^{\alpha}$ as "one conjugation with a correction" loses this: it is a parity on the left times an adjointness on the right.

## The Parity Sign and the Composition

**Proposition (the parity sign).** For homogeneous $x$ the twist is the sign character on the left factor, so

$$
\Theta^{\alpha}_x=\varepsilon_x\,\Theta_x,\qquad \varepsilon_x=(-1)^{\lvert x\rvert}.
$$

**Corollary (the sign is invisible on the algebra).** Every element of $\mathbb{B}$ is even, so $\alpha$ is the identity on it and

$$
\Theta^{\alpha}_x=\Theta_x\qquad\text{for every }x\in\mathbb{B}.
$$

The signed and the unsigned Hermitian sandwich are the same operator on the bosonic sector. The sign of the title is not a second operator on the algebra; it is the fermionic sector, and it is visible only on odd elements, that is only outside $\mathbb{B}$.

**Proposition (the composition).** For all $x,z$,

$$
\Theta^{\alpha}_x\circ\Theta^{\alpha}_z=\Theta^{\alpha}_{xz}=\varepsilon_x\varepsilon_z\,\Theta_{xz},
$$

so for homogeneous parameters the composite is the **ordinary** Hermitian sandwich exactly when the parities agree, and in particular it is ordinary whenever both factors are odd.

*Proof.* The dagger is an anti-automorphism and the twist an automorphism: $\Theta^{\alpha}_{xz}(y)=\alpha(x)\alpha(z)\,y\,z^{\dagger}x^{*}=\Theta^{\alpha}_x(\Theta^{\alpha}_z(y))$. Substituting the parity-sign identity for the three parameters and using $\varepsilon_x\varepsilon_z=\varepsilon_{xz}$ gives the second form.

| $x$ | $z$ | $xz$ | composite |
|---|---|---|---|
| even | even | even | ordinary Hermitian sandwich, $\Theta_{xz}$ |
| even | odd | odd | signed, $-\,\Theta_{xz}$ |
| odd | even | odd | signed, $-\,\Theta_{xz}$ |
| odd | odd | even | ordinary Hermitian sandwich, $\Theta_{xz}$ |

**Corollary (two odd steps give an ordinary step).** If $x$ and $z$ are both odd then $xz$ is even and

$$
\Theta^{\alpha}_x\circ\Theta^{\alpha}_z=\Theta_{xz},
$$

an ordinary Hermitian sandwich. Physically: two fermionic steps compose to a bosonic one, and the composite operator is the unsigned one, because the two parity signs have cancelled.

**Remark (what the corpus can and cannot see).** The parity table has a row and a column outside the algebra: to exhibit a signed Hermitian sandwich one needs an odd element, and the algebra has none. Two statements follow, and both matter for the physics. First, every computation of the series performed inside $\mathbb{B}$ — and that is all of them — is a computation with the unsigned Hermitian sandwich, so the difference between the two readings of this article cannot be detected by any observable of the framework. Second, the difference is nevertheless physically meaningful on the odd sector, which is where the fermions are: it is the sign of the fermionic reflection, and the remainder of this article reads it there.

## The Odd Slot Is a Coset, Not a Second Algebra

**Proposition (the odd slot is not closed).** The odd slot satisfies $\mathrm{Cl}^1\mathrm{Cl}^1\subseteq\mathbb{B}$, so it is not a subalgebra; it is a single coset of the even slot for the multiplication. Fix an odd unit $\gamma$; then every odd element is $\gamma s$ with $s$ even, and the odd slot is the copy $\mathbb{B}\gamma$ of the algebra inside the ambient one.

*Proof.* Odd $\times$ odd is even by the parity table; for the second statement, an odd $y$ is $y=\gamma(\gamma^{-1}y)$ and $\gamma^{-1}y$ is even.

**Remark (the Hermitian form on the odd slot).** The odd slot is a module over the algebra and it carries the Hermitian form induced by the module structure, which is scalar-valued: writing $\langle s,t\rangle=\mathrm{Sc}(s^{*}t)$ for even $s,t$,

$$
\langle s\gamma,t\gamma\rangle=-q(\gamma)\,\langle s,t\rangle,\qquad
\langle s,t\gamma\rangle=0 ,
$$

verified for all four generators and on even samples: the form on the fermionic sector is the form on the algebra up to the scalar $-q(\gamma)$, and the two slots are orthogonal for the form, as the parity preservation of the dagger requires. One warning belongs here, because it is easy to get wrong: the corresponding *elementwise* identity $(s\gamma)^{*}(t\gamma)=-q(\gamma)s^{*}t$ is **false** in general — a generator need not commute with an even element of the algebra, and the contraction terms spoil it — so the odd slot carries a Hermitian form and not a copy of the algebra's product. The fermionic sector is not a second algebra but a single module generator with the algebra's own Hermitian form.

**Remark (why the two copies are not independent).** The two slots are isomorphic as modules over the even part but are not two subalgebras, and the multiplication between them is the graded multiplication. Two independent copies would have no rule for the product of two odd elements; the rule odd $\times$ odd $=$ even is exactly what is lost, and with it the reflection, the parity and the twist.

## The Reflection Read in the Hermitian Pairing

The odd slot is where the parity sign is visible, and the simplest odd elements are the generators, which are the vectors of Minkowski space. The Hermitian reading of the reflection count is therefore a statement about the action of the signed Hermitian sandwich on them.

**Definition (the dagger on the envelope).** On the ambient algebra the dagger is the map of the same formula as in the algebra, $x^{*}=\sigma(\alpha(x^{r}))$, the coefficient conjugation of the composite of the reversion and the grade involution. It restricts to the algebra's Hermitian conjugation on $\mathbb{B}$ and satisfies $\gamma^{\mu{}^{*}}=-\gamma^{\mu}$, so that the odd slot is where it differs from the reversion: on the vectors the two differ by the sign, and the corpus's relation $\mathrm{rev}={}^{*}\circ\sigma$ is exactly this statement.

**Proposition (the vector identity).** Let $u,v$ be vectors of the Minkowski space of the envelope, $u^2=q(u)$ and $uv+vu=2B(u,v)$, and let $\rho_u(v)=v-2B(u,v)u/q(u)$ be the reflection. Then

$$
\Theta^{\alpha}_u(v)=-q(u)\,\rho_u(v).
$$

*Proof.* The derivation is the one of the maths article: $\Theta^{\alpha}_u(v)=\alpha(u)\,v\,u^{\dagger}=(-u)\,v\,(-u)=u\,v\,u=2B(u,v)\,u-u^{2}v=2B(u,v)u-q(u)v=-q(u)\rho_u(v)$, using $\alpha(u)=-u$ on the odd slot, $u^{\dagger}=-u$ on the vectors, and $u^{2}=q(u)$.

**Corollary (which reflection each member realises).** The generators of square $-1$ — the spatial ones, $(\gamma^{k})^{2}=-1$ — satisfy $\Theta^{\alpha}_{\gamma^{k}}=\rho_{\gamma^{k}}$ exactly, while the timelike generator satisfies $\Theta^{\alpha}_{\gamma^{0}}=-\rho_{\gamma^{0}}$. The **unsigned** member does the opposite: $\Theta_{\gamma^{0}}=\rho_{\gamma^{0}}$ and $\Theta_{\gamma^{k}}=-\rho_{\gamma^{k}}$. So the reflection in a spatial hyperplane is carried by the signed Hermitian sandwich and the time reflection by the unsigned one, and the parity sign exchanged the two; this is the Hermitian form of the parity word of the next article, where two odd steps compose to a rotation.

**Remark (the same statement on the algebra).** The algebra has a Euclidean Clifford structure of its own, $\mathbb{B}\cong\mathrm{Cl}_{3,0}$, with vectors the Hermitian elements $ie_k$ of the informational sector; there the vector identity reads $\Theta_{ie_k}=-q(ie_k)\rho_{ie_k}=-\rho_{ie_k}$ with $q(ie_k)=+1$, so on the algebra the sandwich by a Hermitian unit vector is minus the reflection, and the sign is the one carried by the signature of the form and not by the grading. The two signs — the parity sign of $\Theta^{\alpha}$ and the signature sign of the reflection — are the two signs a reader must not conflate, and this is where they part.

## What the Grading Does and Does Not Explain

Several distinct $\mathbb{Z}/2$'s coexist in the framework, and the parity of the grading is only one of them. They are named here to keep them apart, in the manner of the warning of *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*.

| structure | what it grades | an algebra grading? |
|---|---|---|
| Clifford parity (this article) | $\mathrm{Cl}_{1,3}=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$, bosonic/fermionic | yes, of the ambient algebra only |
| chirality $L/R$ | the two minimal left ideals of $\mathbb{B}$, the operator $\gamma^5$ | a $\mathbb{Z}/2$ of the module structure |
| sector splitting $\mathbb{M}_+\oplus\mathbb{M}_-$ | the Hermitian dagger, informational/material | **no**; it is the eigen-decomposition of the dagger and grades the symmetrized product only |
| frame grading $\beta$ | large/small components, Foldy–Wouthuysen | no; a frame-dependent split |
| number grading $N$ | the Fock space by total particle number | a grading of the state space |

The third row is the Hermitian structure of the algebra and not a grading, and the counterexample is the one already used above: $(ie_1)(ie_2)=-e_3$ sends the product of two elements of $\mathbb{M}_+$ into $\mathbb{M}_-$. The dagger is even in the sense of the first row — it preserves the Clifford parity — and that is why the Hermitian form is the orthogonal sum of the forms on the two Clifford sectors, while the sector splitting of its own eigenvalues is a different $\mathbb{Z}/2$ that the multiplication does not respect.

**What the grading does not supply.** The parity of a many-mode field is a product over the modes, $\Gamma(-I)=(-1)^{\hat N}=\prod_{\text{modes}}ie_3^{(\text{mode})}$, and the product over modes is not an element of $\mathbb{B}$: the parity of the field is external to the algebra. For one mode, $(-1)^F=ie_3$ is an element of the algebra and is even, as the grading requires of a parity operator: the operator that measures the fermion parity is itself bosonic. In the Hermitian reading the same element is Hermitian, $(-1)^F=ie_3\in\mathbb{M}_+$: the parity operator of one mode lies in the informational sector, and it is the same element that the Hilbert structure of the corpus singles out.

## Worked Cases

### The Dagger on the Basis

The Hermitian conjugation of the basis elements is the table of *Biquaternion Versors and the Orthogonal Group*, restated here because the whole article is the reading of it:

$$
e_0^{\dagger}=e_0,\qquad e_k^{*}=-e_k,\qquad i^{*}=-i,\qquad (ie_k)^{*}=ie_k .
$$

The quaternion units are anti-Hermitian, the complex unit is anti-Hermitian, the boosts $ie_k$ are Hermitian: $\mathbb{M}_+$ is spanned by $e_0$ and the boosts, $\mathbb{M}_-$ by $i$ and the quaternion units. The parity of the basis elements — all even, since they are elements of the algebra — is untouched by the dagger, as the evenness proposition says.

### The Unit Slice and the Two Slices of the Algebra

The slice $U=\{x:x^{*}x=1\}$ of the dagger is a group, and it contains more than the unit quaternions: the unit quaternions (real coefficients with $N=1$), the unit complex scalars of the centre, and the boosts $ie_k$ all satisfy $x^{*}x=1$. Its Lie algebra, by the sector decomposition, is $\mathbb{M}_-$: the anti-Hermitian elements are exactly those for which $\exp$ lands in $U$, and the exponential of $\mathbb{M}_-$ was checked to lie in $U$ on a sample. Since the dagger is the conjugate transpose in the matrix model $\mathbb{B}\cong M_2(\mathbb{C})$, the slice is the compact unitary group, $U\cong U(2)$. The **inverse** slice is the other one, the group of units of the algebra, and it is non-compact: this is the difference between the adjoint reading and the inverse reading in one line — the dagger selects the compact group, the inverse the group of units, and the Lorentz group of the corpus is reached by the inverse.

### The Norm Factor on a Boost

Let $x=ie_1$, a boost, with $N(x)=-1$ and $x^{*}=x$. The dagger is not the inverse here, $x^{-1}=ie_1$ as well since $x^{2}=1$ — the boost of this normalisation is its own inverse — and the sandwich multiplies the norm by $\lvert N(x)\rvert^{2}=1$: the boost is on the unit slice. The unit quaternion $R=e_1$, by contrast, has $N(R)=+1$ and $R^{*}=-e_1=-R=R^{-1}$: on the real-quaternion slice the dagger is the inverse, and the sandwich is the rotor conjugation. The two examples are the two rows of the corpus's dictionary, and the difference between them is exactly the coefficient conjugation $\sigma$, which is the identity on one and not on the other.

### Two Fermionic Steps Compose to a Bosonic One

Let $u=\gamma^1$ and $w=\gamma^2$, both odd. Their signed Hermitian sandwiches are the reflections of the previous section, $\Theta^{\alpha}_{\gamma^1}=\rho_{\gamma^1}$ and $\Theta^{\alpha}_{\gamma^2}=\rho_{\gamma^2}$, and their composite is

$$
\Theta^{\alpha}_{\gamma^1}\circ\Theta^{\alpha}_{\gamma^2}
=\Theta^{\alpha}_{\gamma^1\gamma^2}
=\Theta_{e_3},
$$

an ordinary Hermitian sandwich by the bosonic element $e_3=\gamma^1\gamma^2$: two fermionic steps have composed to a bosonic one and the two signs have cancelled. The composite is a rotation by a quaternion unit, and the parity of the number of factors is the $\mathbb{Z}/2$ behind the split of $O(1,3)$ from $SO(1,3)$.

## Summary

The ambient Clifford algebra is $\mathbb{Z}/2$-graded, $\mathrm{Cl}_{1,3}=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$, with even part the biquaternion algebra $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}$ and odd part the slot that carries the Dirac generators. The Hermitian reading replaces the inverse of the signed inner conjugation by the **Hermitian adjoint**: the signed Hermitian sandwich is $\Theta^{\alpha}_x(y)=\alpha(x)\,y\,x^{*}$. The dagger is **even**, so it preserves the parity, and the two sectors $\mathbb{M}_\pm$ of the corpus are its fixed and anti-fixed loci, the eigen-decomposition of the Hermitian structure of the algebra and not an algebra grading.

The dagger is not the inverse: for invertible $x$ one has $x^{*}=\sigma(N(x))\sigma(x)^{-1}$, so the two coincide exactly on the real-quaternion slice of unit norm and differ elsewhere by the coefficient-conjugated norm, and the sandwich multiplies the norm by $\lvert N(x)\rvert^{2}$, being an isometry exactly on the unit slice. The adjoint slice is a compact group, $\mathbb{B}\cong M_2(\mathbb{C})$ with $U\cong U(2)$, while the inverse slice is the group of units and the route to the Lorentz group.

The twist $\alpha$ is the conjugation by the volume element, $\alpha(x)=\Omega x\Omega^{-1}$, unchanged from the inverse article because it is the **left** factor; the parity sign is $\Theta^{\alpha}_x=\varepsilon_x\Theta_x$ and it is **invisible on the algebra**, $\Theta^{\alpha}_x=\Theta_x$ for $x\in\mathbb{B}$, since every element of the algebra is even. The sign is therefore exactly the fermionic sector, and the composition $\Theta^{\alpha}_x\Theta^{\alpha}_z=\Theta^{\alpha}_{xz}=\varepsilon_x\varepsilon_z\Theta_{xz}$ is ordinary whenever the two parities agree, so two fermionic steps compose to a bosonic one. On the vectors the parity sign is visible: $\Theta^{\alpha}_u=-q(u)\rho_u$, so the spatial reflections are carried by the signed member and the time reflection by the unsigned one, and their exchange is the parity word of the reflection count.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Cl}_{1,3}=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$ | The graded ambient algebra; $\mathrm{Cl}^0=\mathbb{B}$ |
| $\gamma^\mu$ odd, $\gamma^\mu\gamma^\nu$ even | Generators fermionic, bivectors bosonic |
| $x^{*}=\sigma(\alpha(x^{r}))$ | The Hermitian dagger; even, anti-involution |
| $\mathbb{M}_+,\mathbb{M}_-$ | Fixed and anti-fixed loci of the dagger; informational and material sectors |
| $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ | The eigen-decomposition of the dagger; not an algebra grading |
| $N(\tilde{Q})=\sum_\mu Q_\mu^2$ | The norm; $x^{*}=\sigma(N(x))\sigma(x)^{-1}$ |
| $U=\{x:x^{*}x=1\}$ | The unit slice; $U\cong U(2)$ in the matrix model, Lie algebra $\mathbb{M}_-$ |
| $\alpha(x)=\varepsilon_x x=\Omega x\Omega^{-1}$ | The twist as a conjugation by the pseudoscalar |
| $\Theta^{\alpha}_x(y)=\alpha(x)\,y\,x^{*}$ | Signed Hermitian sandwich; $=\Theta_x$ on $\mathbb{B}$ |
| $\Theta^{\alpha}_x=\varepsilon_x\Theta_x$ | Parity sign; invisible on the even algebra |
| $\Theta^{\alpha}_x\Theta^{\alpha}_z=\Theta^{\alpha}_{xz}=\varepsilon_x\varepsilon_z\Theta_{xz}$ | Composition; ordinary for equal parities |
| $\Theta^{\alpha}_u=-q(u)\rho_u$ ($u\in V$) | The reflection read in the Hermitian pairing |
| $\mathrm{Cl}^1=\mathbb{B}\gamma$, $\langle s\gamma,t\gamma\rangle=-q(\gamma)\langle s,t\rangle$ | The odd slot as a coset, with the induced form |
| $(-1)^F=ie_3\in\mathbb{M}_+$ | Parity of one mode, an even Hermitian element |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the parity grading, the volume element and the two conjugations.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the grade involution, the reflection count and the split of the orthogonal group.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the involutions of a Clifford algebra, the unitary groups they define and the norm factor.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the chirality element, the bosonic/fermionic grading and its use in field theory.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (American Mathematical Society, 1956), for the adjoint of an anti-automorphism and the unitary group of an algebra with involution.
