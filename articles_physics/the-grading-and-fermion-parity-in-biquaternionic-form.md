# __The Grading, Fermion Parity and the Two Sectors in Biquaternionic Form__

## Introduction

The biquaternion algebra is the even part of the Clifford algebra of Minkowski space, $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}$, and that identification is the whole source of the geometric content of the series. It has a second consequence that is used throughout the physics articles but stated nowhere in one place: the ambient algebra is **$\mathbb{Z}/2$-graded**, and the grading is the fermion parity of the theory. The even slot is the bosonic sector, and it is the biquaternion algebra; the odd slot is the fermionic sector, and it is the slot that carries the Dirac generators and the anticommuting mode operators.

This article states the grading once, in the Hermitian form that the rest of the corpus uses. The operator is the **Hermitian sandwich**

$$
\Theta_x(y)=x\,y\,x^{*},
$$

with the Hermitian adjoint on the right and no second factor. The parity enters as the **sign character** $\varepsilon_x=(-1)^{\lvert x\rvert}$ of a homogeneous element, a scalar, and not as a factor of the operator. Two consequences follow at once and are used below. Every element of $\mathbb{B}$ is even, so $\varepsilon_x=+1$ on the algebra and every computation of the series is a computation with the unsigned sandwich. The signed operators of the maths corpus are maps on the full $\mathrm{Cl}_{1,3}$; on the even slot they reduce to $\Theta_x$, which is why the physics never needs them.

The generators are written as cells of the biquaternion algebra acting on itself on both sides. With $L_a\psi=a\psi$, $R_b\psi=\psi b$ and $L_aR_b\psi=a\psi b$, the four generator cells are $iL_{e_t}R_{\vec e_x}$, $iL_{\vec e_x}R_{\vec e_y}$, $iL_{\vec e_y}R_{\vec e_y}$ and $iL_{\vec e_z}R_{\vec e_y}$, and the chirality cell is $-iL_{e_t}R_{\vec e_z}=-iR_{\vec e_z}$. **Every generator cell carries one factor $i$, so a product of two carries $i^2=-1$ and a product of four carries $i^4=+1$**; the collapses below use this.

Three facts organise the article. The first is that the dagger is **even**: it preserves the parity, so the grading is a symmetry of the Hermitian structure, and the two sectors $\mathbb{M}_+$ and $\mathbb{M}_-$ of the corpus are its fixed and anti-fixed loci. The second is that the parity is a **scalar sign**, $\alpha(x)=\varepsilon_x x$, and that it is invisible on the algebra, because every element of $\mathbb{B}$ is even. The third is that the twist is a conjugation, by the volume element, $\alpha(x)=\Omega x\Omega^{-1}$; it sits on the element and never on the operator, so the sandwich is the only operator the physics uses.

The ambient graded algebra, the two slots, the dictionary $\vec e_x\mapsto L_{\vec e_x}R_{e_t}$ and $i\mapsto-\Omega$, and the chirality cell $-iR_{\vec e_z}=i\Omega$ are *Biquaternion Versors and the Orthogonal Group*, which also carries the Hermitian dagger, the sectors $\mathbb{M}_\pm$, the reflection and the determinants of the versors. The two sectors themselves, and their physical reading, are developed in *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* and *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, built on *Introduction to the Biquaternion Universe*. The fermionic mode and $(-1)^F=i\vec e_z$ are *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*; the parity of the state space, $\Gamma(-I)=(-1)^{N^{\mathrm{fop}}}$, is *The Fermionic Fock Space in Biquaternionic Form*. The graded bracket built on this parity is *The Superalgebra Reading and the Odd Extension in Biquaternionic Form*. The abstract algebra of the signed forms is the maths pair *The Grading of a Hermitian Algebra with Signed Hermitian Adjoint* and *Two-Sided Operators on a Hermitian Algebra with Signed Hermitian Adjoint*, cited for the ambient theory and not used as operators here.

## The Grading of the Ambient Algebra

**Given.** The Clifford algebra of Minkowski space is graded by parity, $\mathrm{Cl}_{1,3}=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$, with $\mathrm{Cl}^i\mathrm{Cl}^j\subseteq\mathrm{Cl}^{i+j}$. The even part is $\mathbb{B}$, and the odd part is the slot containing the generators; the dictionary sends the algebra to the even slot, so every element of the algebra in which the series computes is even.

The multiplication table, read physically, is the parity table,

$$
\text{even}\cdot\text{even}=\text{even},\quad
\text{even}\cdot\text{odd}=\text{odd},\quad
\text{odd}\cdot\text{even}=\text{odd},\quad
\text{odd}\cdot\text{odd}=\text{even},
$$

that is, the parity of a product is the sum of the parities. The generator cells $iL_{e_\mu}R_{\vec e_{\nu(\mu)}}$ are odd; the bivectors $iL_{e_\mu}R_{\vec e_{\nu(\mu)}}\,iL_{e_\nu}R_{\vec e_{\nu(\nu)}}=-L_{e_\mu}L_{e_\nu}R_{\vec e_{\nu(\mu)}}R_{\vec e_{\nu(\nu)}}$ and the volume element are even; the square $(iL_{e_\mu}R_{\vec e_{\nu(\mu)}})^2=\pm1$ is a scalar and hence even. The **physical interpretation** is the whole of the grading in one sentence: a product of an odd number of fermionic objects is fermionic; a product of an even number is bosonic.

Here $iL_{e_\mu}R_{\vec e_{\nu(\mu)}}$ is the generator cell of the coordinate $x_\mu$, with $\nu(t)=x$ and $\nu(k)=y$.

**Remark.** The identification $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}$ is therefore not merely "$\mathbb{B}$ is a Clifford algebra"; it says *which* slot of the ambient graded algebra the biquaternion algebra is. The whole physics series computes in the bosonic sector, and this is why the parity sign of the section after next is invisible in it.

## The Dagger Is Even

The Hermitian dagger of the algebra is the adjoint of the spinor form, and the first thing the grading says about it is that it is a symmetry of the grading.

**Proposition (the dagger preserves the parity and is an anti-involution).** The dagger is $\mathbb{C}$-antilinear, involutive and an anti-automorphism,

$$
(xy)^{*}=y^{*}x^{*},\qquad (x^{*})^{*}=x,
$$

and it preserves the degree modulo two, $(\mathrm{Cl}^k)^{*}\subseteq\mathrm{Cl}^k$, so $\lvert x^{*}\rvert=\lvert x\rvert$ on homogeneous elements.

*Proof.* The coefficient conjugation is a $\mathbb{C}$-antilinear automorphism that acts on the coefficients and not on the degree; the quaternion conjugation of the algebra is the reversion of the even slot, which reverses the order of the factors, so on a product $\tilde{H}_1\tilde{H}_2$ one has $(\tilde{H}_1\tilde{H}_2)^{*}=\tilde{H}_2^{*}\tilde{H}_1^{*}$; a product of $k$ generators is sent to a product of $k$ generators. For the odd slot this is the definition used in *The Reflection Read in the Hermitian Pairing* below.

**The two sectors of the corpus, in the language of the dagger.** The fixed and anti-fixed loci of the dagger are the two remarkable subspaces,

$$
\mathbb{M}_+=\{x:x^{*}=x\}=\mathrm{span}_{\mathbb{R}}\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\},\qquad
\mathbb{M}_-=\{x:x^{*}=-x\}=\mathrm{span}_{\mathbb{R}}\{ie_t,\vec e_x,\vec e_y,\vec e_z\},
$$

the informational and the material sector, and the algebra is their direct sum, $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$. This is the eigen-decomposition of the dagger, and it is **not** an algebra grading: the product of two Hermitian elements need not be Hermitian, and $(i\vec e_x)(i\vec e_y)=-\vec e_z$ is anti-Hermitian. The sector splitting is the Hermitian structure of the algebra read at its two eigenvalues, and the next section is precisely the warning that it must not be conflated with the parity.

**Proposition (the dagger and the inverse).** For every invertible $x\in\mathbb{B}$,

$$
\boxed{\;x^{*}=\sigma(\langle x\rangle_{\natural})\,\sigma(x)^{-1}\;}.
$$

*Proof.* The norm identity $\bar x=\langle x\rangle_{\natural}\,x^{-1}$ of the algebra, with $\bar x$ the quaternion conjugation, gives $x^{*}=\sigma(\bar x)=\sigma(\langle x\rangle_{\natural})\,\sigma(x)^{-1}$, the coefficient conjugation being an automorphism.

**Corollary (where the dagger is the inverse).** The dagger equals the inverse exactly when $\sigma(x)=\sigma(\langle x\rangle_{\natural})\,x$. In particular, on the real-quaternion slice of norm one — real coefficients with $\langle x\rangle_{\natural}=1$, the unit quaternions $\mathrm{SU}(2)$ — the two maps coincide, which is the agreement of the dagger with the Clifford conjugation on the real-quaternion slice recorded by *Biquaternion Versors and the Orthogonal Group*. Away from that condition the two differ by the scalar factor and the coefficient conjugation displayed in the boxed formula; a reader who replaces a dagger by an inverse is assuming the condition whether he says so or not.

**Remark (the norm factor of the sandwich).** The Hermitian sandwich multiplies the quaternionic norm by the modulus squared of the parameter,

$$
\boxed{\;\langle x\,y\,x^{*}\rangle_{\natural}=\lvert \langle x\rangle_{\natural}\rvert^{2}\,\langle y\rangle_{\natural}\;}
$$

so the operator scales the quaternionic norm by the factor $\lvert \langle x\rangle_{\natural}\rvert^{2}$, and it preserves the norm exactly on the norm-one slice $\lvert\langle x\rangle_{\natural}\rvert=1$. The inner conjugation $x\,y\,x^{-1}$ preserves the norm exactly, with ratio $1$. The two maps are related by $\Theta_x=\mathrm{Ad}_x\circ R_{x x^{*}}$, where $x x^{*}$ is Hermitian of norm $\lvert\langle x\rangle_{\natural}\rvert^{2}$; on the norm-one slice both preserve the norm, and as maps they coincide exactly when $x x^{*}=e_t$, that is on the $*$-unitary slice $\mathcal{U}=\{x:x^{*}x=1\}$ defined below.

## The Parity Sign Is the Conjugation by the Pseudoscalar

The sign $\varepsilon_x=(-1)^{\lvert x\rvert}$ is usually introduced as the abstract grade involution, equal to $+1$ on the even slot and $-1$ on the odd slot. In the ambient algebra it is an ordinary conjugation.

**Theorem (the grade involution is a conjugation).** The volume element of $\mathrm{Cl}_{1,3}$ is

$$
\Omega=iL_{e_t}R_{\vec e_x}\,iL_{\vec e_x}R_{\vec e_y}\,iL_{\vec e_y}R_{\vec e_y}\,iL_{\vec e_z}R_{\vec e_y}=-R_{\vec e_z}=-L_{e_t}R_{\vec e_z}.
$$

Then $\Omega^2=-1$, $\Omega$ commutes with the even slot and anticommutes with every generator, and for every homogeneous $x$

$$
\Omega\,x\,\Omega^{-1}=(-1)^{\lvert x\rvert}\,x=\alpha(x).
$$

Under the dictionary $i\mapsto-\Omega$, the same statement reads: the grade involution is the conjugation by $-\Omega$, the image of the central scalar imaginary.

**Proof.** The four factors of $\Omega$ carry $i^4=+1$. On the left, $L_{e_t}L_{\vec e_x}L_{\vec e_y}L_{\vec e_z}=L_{\vec e_x\vec e_y\vec e_z}=L_{-e_t}=-I$, because $\vec e_x\vec e_y=\vec e_z$ and $\vec e_z^2=-e_t$. On the right, $R_{\vec e_x}R_{\vec e_y}R_{\vec e_y}R_{\vec e_y}=R_{\vec e_y^3\vec e_x}=R_{\vec e_z}$ — the right multipliers compose in the reverse order, $R_aR_b=R_{ba}$ — because $\vec e_y^3=-\vec e_y$ and $-\vec e_y\vec e_x=\vec e_z$. Hence $\Omega=-R_{\vec e_z}$, and $\Omega^2=-1$. Moving one generator $iL_{e_\mu}R_{\vec e_{\nu(\mu)}}$ past the four factors of $\Omega$ costs the sign $(-1)^{3}=-1$: it anticommutes with the three factors other than its own square and commutes with that square. Hence $\Omega\,(iL_{e_\mu}R_{\vec e_{\nu(\mu)}})=-(iL_{e_\mu}R_{\vec e_{\nu(\mu)}})\,\Omega$ for every generator, and $\Omega^{-1}=-\Omega$ because $\Omega^2=-1$. A monomial of $k$ generators therefore satisfies $\Omega x=(-1)^{k}x\Omega$. Every element of $\mathbb{B}$ is a sum of monomials of even $k$, so $\Omega$ commutes with it, and the conjugation is the identity on the even slot.

**Remark (the sign is a scalar, not a factor of the operator).** The grade involution acts on the element, $\alpha(x)=\varepsilon_x x$, and $\varepsilon_x=\pm1$. It therefore never multiplies a sandwich: multiplying the parameter by $\varepsilon_x$ multiplies the sandwich by the same scalar, and on the algebra $\varepsilon_x=+1$ identically. The parity is a property of the parameter, which the operator may report as a sign, and not a second operator.

## The Parity Sign and the Composition

**Proposition (the parity sign).** For homogeneous $x$ the grade involution is the scalar sign character,

$$
\alpha(x)=\varepsilon_x\,x,\qquad \varepsilon_x=(-1)^{\lvert x\rvert}.
$$

**Corollary (the sign is invisible on the algebra).** Every element of $\mathbb{B}$ is even, so $\varepsilon_x=+1$ on it and

$$
\Theta_x(y)=x\,y\,x^{*}\qquad\text{for every }x\in\mathbb{B}.
$$

There is no signed Hermitian sandwich on the bosonic sector: the sign multiplies the parameter and not the operator.

**Proposition (the composition).** For all $x,z$,

$$
\boxed{\;\Theta_x\circ\Theta_z=\Theta_{xz}\;}
$$

with no correction factor.

*Proof.* $\Theta_{xz}(y)=x z\,y\,z^{*}x^{*}=\Theta_x(\Theta_z(y))$, the dagger being an anti-automorphism.

**Corollary (two odd steps give an even one).** If $x$ and $z$ are both odd then $xz$ is even and the composite is the sandwich by a bosonic parameter. The parity of the parameter is the sum of the parities; the operator itself carries no parity, and the composition needs no sign because the sign was never in the operator.

**Remark (what the corpus can and cannot see).** The parity table has a row and a column outside the algebra: to speak of an odd parameter one needs an odd element, and the algebra has none. Every computation of the series is therefore a computation with the unsigned sandwich, and no observable of the framework distinguishes it from the signed variant, which is the same map up to the scalar $\varepsilon_x$. The parity remains physical on the odd sector, where the fermions are, and the sections below read it there: as the sign of the reflection and as the parity word of an isometry.

## The Odd Slot Is a Coset, Not a Second Algebra

**Proposition (the odd slot is not closed).** The odd slot satisfies $\mathrm{Cl}^1\mathrm{Cl}^1\subseteq\mathbb{B}$, so it is not a subalgebra; it is a single coset of the even slot for the multiplication. Fix an odd unit $u$, a generator cell; then every odd element is $u s$ with $s$ even, and the odd slot is the copy $u\mathbb{B}$ of the algebra inside the ambient one.

*Proof.* Odd $\times$ odd is even by the parity table; for the second statement, an odd $y$ is $y=u(u^{-1}y)$ and $u^{-1}y$ is even.

**Remark (the Hermitian form on the odd slot).** The odd slot is a module over the algebra and it carries the Hermitian form induced by the module structure, which is scalar-valued: writing $\langle s,t\rangle=\mathrm{Sc}(s^{*}t)$ for even $s,t$,

$$
\langle su,tu\rangle=-q(u)\,\langle s,t\rangle,\qquad
\langle s,tu\rangle=0 ,
$$

verified for all four generators and on even samples: the form on the fermionic sector is the form on the algebra up to the scalar $-q(u)$, with $q$ the quadratic form of the Clifford algebra, and the two slots are orthogonal for the form, as the parity preservation of the dagger requires. One warning belongs here, because it is easy to get wrong: the corresponding *elementwise* identity $(su)^{*}(tu)=-q(u)s^{*}t$ is **false** in general — a generator need not commute with an even element of the algebra, and the contraction terms spoil it — so the odd slot carries a Hermitian form and not a copy of the algebra's product. The fermionic sector is not a second algebra but a single module generator with the algebra's own Hermitian form.

**Remark (why the two copies are not independent).** The two slots are isomorphic as modules over the even part but are not two subalgebras, and the multiplication between them is the graded multiplication. Two independent copies would have no rule for the product of two odd elements; the rule odd $\times$ odd $=$ even is exactly what is lost, and with it the reflection and the parity.

## The Reflection Read in the Hermitian Pairing

The odd slot is where the parity sign is visible, and the simplest odd elements are the generators, which are the vectors of Minkowski space. The Hermitian interpretation of the reflection count is therefore a statement about the action of the Hermitian sandwich on them.

**Definition (the dagger on the envelope).** On the ambient algebra the dagger is the map of the same formula as in the algebra, $x^{*}=\sigma(\alpha(x^{r}))$, the coefficient conjugation of the composite of the reversion and the grade involution. It restricts to the algebra's Hermitian conjugation on $\mathbb{B}$ and satisfies $\bigl(iL_{e_\mu}R_{\vec e_{\nu(\mu)}}\bigr)^{*}=-iL_{e_\mu}R_{\vec e_{\nu(\mu)}}$, so that the odd slot is where it parts company with the reversion: on a real vector $a$ the reversion is $\mathrm{rev}(a)=a$ while $a^{*}=-a$. The corpus's relation $\mathrm{rev}={}^{*}\circ\sigma$ therefore holds on the even slot and picks up the grade sign on the odd one, $\alpha\circ\mathrm{rev}={}^{*}\circ\sigma$. Read as arrays, the cells carry the array adjoint $\dagger$, distinct from the star, $(iL_{e_t}R_{\vec e_x})^{\dagger}=+iL_{e_t}R_{\vec e_x}$, $(iL_{\vec e_k}R_{\vec e_y})^{\dagger}=-iL_{\vec e_k}R_{\vec e_y}$ and $(-iR_{\vec e_z})^{\dagger}=-iR_{\vec e_z}$, the two marks being related by $x^{*}=S\,x^{\dagger}\,S^{-1}$ with $S=-iL_{e_t}R_{\vec e_y}$.

**Proposition (the vector identity).** Let $a,v$ be real vectors of the Minkowski space of the envelope, with $q$ the quadratic form, $B$ its polar form, $a^2=q(a)$ and $av+va=2B(a,v)$, and let $\rho_a(v)=v-2B(a,v)a/q(a)$ be the reflection. Then

$$
\boxed{\;\Theta_a(v)=q(a)\,\rho_a(v)\;}.
$$

*Proof.* $\Theta_a(v)=a\,v\,a^{*}=a\,v\,(-a)=-a\,v\,a=-2B(a,v)\,a+a^{2}v=q(a)\,v-2B(a,v)\,a=q(a)\,\rho_a(v)$, using $a^{*}=-a$ on the vectors and $a^{2}=q(a)$.

**Corollary (which reflection carries which sign).** The timelike generator has $q(iL_{e_t}R_{\vec e_x})=+1$ and satisfies $\Theta_{iL_{e_t}R_{\vec e_x}}=\rho_{iL_{e_t}R_{\vec e_x}}$ exactly, while the spatial generators, $(iL_{\vec e_k}R_{\vec e_y})^{2}=-1$, satisfy $\Theta_{iL_{\vec e_k}R_{\vec e_y}}=-\rho_{iL_{\vec e_k}R_{\vec e_y}}$. The sign is the signature of the vector, $q(a)=\pm1$, and it sits in front of the reflection; it is not a parity factor of the operator. This is the Hermitian form of the parity word of the last worked case, where two odd steps compose to a rotation.

**Remark (the same statement on the algebra).** The algebra has a Euclidean Clifford structure of its own, $\mathbb{B}\cong\mathrm{Cl}_{3,0}$, with vectors the Hermitian elements $i\vec e_k$ of the informational sector; there the vector identity reads $\Theta_{i\vec e_k}=-q(i\vec e_k)\rho_{i\vec e_k}=-\rho_{i\vec e_k}$ with $q(i\vec e_k)=+1$, so on the algebra the sandwich by a Hermitian unit vector is minus the reflection, and the sign is the one carried by the signature of the form and not by the grading. The two signs — the parity sign $\varepsilon_x$ of the parameter and the signature sign $q(a)$ of the vector — are the two signs a reader must not conflate, and this is where they part.

## What the Grading Does and Does Not Explain

Several distinct $\mathbb{Z}/2$'s coexist in the framework, and the parity of the grading is only one of them. They are named here to keep them apart, in the manner of the warning of *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*.

| structure | what it grades | an algebra grading? |
|---|---|---|
| Clifford parity (this article) | $\mathrm{Cl}_{1,3}=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$, bosonic/fermionic | yes, of the ambient algebra only |
| chirality (left/right) | the two minimal left ideals of $\mathbb{B}$, the chirality cell $-iR_{\vec e_z}$ | a $\mathbb{Z}/2$ of the module structure |
| sector splitting $\mathbb{M}_+\oplus\mathbb{M}_-$ | the Hermitian dagger, informational/material | **no**; it is the eigen-decomposition of the dagger and grades the symmetrized product only |
| frame grading $\beta$ | large/small components, Foldy–Wouthuysen | no; a frame-dependent split |
| number grading $N$ | the Fock space by total particle number | a grading of the state space |

The second row is the Hermitian structure of the algebra and not a grading, and the counterexample is the one already used above: $(i\vec e_x)(i\vec e_y)=-\vec e_z$ sends the product of two elements of $\mathbb{M}_+$ into $\mathbb{M}_-$. The dagger is even in the sense of the first row — it preserves the Clifford parity — and that is why the Hermitian form is the orthogonal sum of the forms on the two Clifford sectors, while the sector splitting of its own eigenvalues is a different $\mathbb{Z}/2$ that the multiplication does not respect.

**What the grading does not supply.** The parity of a many-mode field is a product over the modes, $\Gamma(-I)=(-1)^{N^{\mathrm{fop}}}=\prod_{\text{modes}}(i\vec e_z)^{(\text{mode})}$, with $\Gamma$ the Fock-space representation of the parity element, and the product over modes is not an element of $\mathbb{B}$: the parity of the field is external to the algebra. For one mode, $(-1)^F=i\vec e_z$ is an element of the algebra and is even, as the grading requires of a parity operator: the operator that measures the fermion parity is itself bosonic. In the Hermitian interpretation the same element is Hermitian, $(-1)^F=i\vec e_z\in\mathbb{M}_+$: the parity operator of one mode lies in the informational sector, and it is the same element that the Hilbert structure of the corpus singles out.

## Worked Cases

### The Dagger on the Basis

The Hermitian conjugation of the basis elements is the table of *Biquaternion Versors and the Orthogonal Group*, restated here because the whole article is the interpretation of it:

$$
e_t^{*}=e_t,\qquad \vec e_k^{*}=-\vec e_k,\qquad i^{*}=-i,\qquad (i\vec e_k)^{*}=i\vec e_k .
$$

The quaternion units are anti-Hermitian, the complex unit is anti-Hermitian, the boosts $i\vec e_k$ are Hermitian: $\mathbb{M}_+$ is spanned by $e_t$ and the boosts, $\mathbb{M}_-$ by $i$ and the quaternion units. The parity of the basis elements — all even, since they are elements of the algebra — is untouched by the dagger, as the evenness proposition says.

### The Two Slices of the Algebra: $*$-Unitary and Inverse

The $*$-unitary slice $\mathcal{U}=\{x:x^{*}x=1\}$ of the dagger is a group, and it contains more than the unit quaternions: the unit quaternions (real coefficients with $\langle x\rangle_{\natural}=1$), the unit complex scalars of the centre, and the boosts $i\vec e_k$ all satisfy $x^{*}x=1$. Its Lie algebra, by the sector decomposition, is $\mathbb{M}_-$: the anti-Hermitian elements are exactly those for which $\exp$ lands in $\mathcal{U}$, and the exponential of $\mathbb{M}_-$ was checked to lie in $\mathcal{U}$ on a sample. Since the dagger is the conjugate transpose in the matrix model $\mathbb{B}\cong M_2(\mathbb{C})$, the slice is the compact $*$-unitary group, $\mathcal{U}\cong \mathrm{U}(2)$. The **inverse** slice is the other one, the group of units of the algebra, and it is non-compact: this is the difference between the adjoint interpretation and the inverse interpretation in one line — the dagger selects the compact group, the inverse the group of units, and the Lorentz group of the corpus is reached by the inverse.

### The Norm Factor on a Boost

Let $x=i\vec e_x$, a boost, with $\langle x\rangle_{\natural}=-1$ and $x^{*}=x$. The dagger is the inverse here, $x^{-1}=i\vec e_x$ as well since $x^{2}=1$ — the boost of this normalisation is its own inverse — and the sandwich multiplies the norm by $\lvert \langle x\rangle_{\natural}\rvert^{2}=1$: the boost is on the norm-one slice. The unit quaternion $R=\vec e_x$, by contrast, has $\langle R\rangle_{\natural}=+1$ and $R^{*}=-\vec e_x=-R=R^{-1}$: on the real-quaternion slice the dagger is the inverse, and the sandwich is the rotor conjugation. The two examples are the two rows of the corpus's dictionary, and the difference between them is exactly the coefficient conjugation $\sigma$, which is the identity on one and not on the other.

### Two Fermionic Steps Compose to a Bosonic One

The generators $iL_{\vec e_x}R_{\vec e_y}$ and $iL_{\vec e_y}R_{\vec e_y}$ are both odd. Their Hermitian sandwiches are minus the reflections of the previous section, $\Theta_{iL_{\vec e_x}R_{\vec e_y}}=-\rho_{iL_{\vec e_x}R_{\vec e_y}}$ and $\Theta_{iL_{\vec e_y}R_{\vec e_y}}=-\rho_{iL_{\vec e_y}R_{\vec e_y}}$, because $q(iL_{\vec e_k}R_{\vec e_y})=-1$; the two minus signs multiply to $+1$ in the composite. The product of the two parameters reduces by $i^2=-1$,

$$
iL_{\vec e_x}R_{\vec e_y}\,iL_{\vec e_y}R_{\vec e_y}
=-L_{\vec e_x}L_{\vec e_y}R_{\vec e_y}R_{\vec e_y}
=-L_{\vec e_x\vec e_y}R_{\vec e_y^2}
=L_{\vec e_z},
$$

so

$$
\Theta_{iL_{\vec e_x}R_{\vec e_y}}\circ\Theta_{iL_{\vec e_y}R_{\vec e_y}}=\Theta_{\vec e_z},
$$

the Hermitian sandwich by the bosonic element $\vec e_z=L_{\vec e_z}R_{e_t}$: two fermionic steps have composed to a bosonic one, the reflection signs have cancelled in the product, and no correction factor is needed because the sign was never in the operator. The composite is a rotation by a quaternion unit, and the parity of the number of factors is the $\mathbb{Z}/2$ behind the split of $O(1,3)$ from $SO(1,3)$.

## The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{e_t}R_{\vec e_x},\quad \gamma_1=iL_{\vec e_x}R_{\vec e_y},\quad \gamma_2=iL_{\vec e_y}R_{\vec e_y},\quad \gamma_3=iL_{\vec e_z}R_{\vec e_y},\quad \gamma_5=-iL_{e_t}R_{\vec e_z} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality operator; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the body cites.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$,
$$
\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$
$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=g_{ac}\gamma_d-g_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4g_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(g_{\mu\nu}g_{\rho\sigma}-g_{\mu\rho}g_{\nu\sigma}+g_{\mu\sigma}g_{\nu\rho}\bigr).
$$
The four contraction sums, with the index $\mu$ summed over the frame, are, in the Euclidean frame where every generator squares to $+I_4$,

$$
\sum_\mu\gamma_\mu\gamma_\mu=4I_4,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\mu=-2\gamma_\alpha,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\mu=4\delta_{\alpha\beta}I_4,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\delta\gamma_\mu=-2\gamma_\delta\gamma_\beta\gamma_\alpha .
$$

They are frame statements because a cell's square depends on the frame: in the $\mathbb{M}_-$ frame the metric enters, the first sum becomes $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$, and the other three change with the signature.

## Summary

The ambient Clifford algebra is $\mathbb{Z}/2$-graded, $\mathrm{Cl}_{1,3}=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$, with even part the biquaternion algebra $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}$ and odd part the slot that carries the Dirac generators. The operator of the article is the **Hermitian sandwich** $\Theta_x(y)=x\,y\,x^{*}$: the Hermitian adjoint on the right, one parameter, and no second factor. The dagger is **even**, so it preserves the parity, and the two sectors $\mathbb{M}_\pm$ of the corpus are its fixed and anti-fixed loci, the eigen-decomposition of the Hermitian structure of the algebra and not an algebra grading.

The dagger is not the inverse: for invertible $x$ one has $x^{*}=\sigma(\langle x\rangle_{\natural})\sigma(x)^{-1}$, so the condition for equality is $\sigma(x)=\sigma(\langle x\rangle_{\natural})x$. In particular the two coincide on the real-quaternion slice of norm one, and the sandwich multiplies the quaternionic norm by $\lvert \langle x\rangle_{\natural}\rvert^{2}$, being norm-preserving exactly on the norm-one slice. The $*$-unitary slice is a compact group, $\mathbb{B}\cong M_2(\mathbb{C})$ with $\mathcal{U}\cong \mathrm{U}(2)$, while the inverse slice is the group of units and the route to the Lorentz group.

The parity is the scalar sign $\varepsilon_x=(-1)^{\lvert x\rvert}$, and the grade involution is its conjugation by the volume element, $\alpha(x)=\varepsilon_x x=\Omega x\Omega^{-1}$. It is **invisible on the algebra**, $\varepsilon_x=+1$ for $x\in\mathbb{B}$, so there is no signed sandwich on the bosonic sector and the composition $\Theta_x\Theta_z=\Theta_{xz}$ is exact. On the odd slot the sign is physical: on the vectors $\Theta_a=q(a)\rho_a$, so the time reflection is the sandwich exactly and the spatial reflections are minus it, with the sign carried by the signature $q(a)=\pm1$ and not by a parity factor of the operator.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Cl}_{1,3}=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$ | The graded ambient algebra; $\mathrm{Cl}^0=\mathbb{B}$ |
| $iL_{e_\mu}R_{\vec e_{\nu(\mu)}}$ odd, $iL_{e_\mu}R_{\vec e_{\nu(\mu)}}\,iL_{e_\nu}R_{\vec e_{\nu(\nu)}}=-L_{e_\mu}L_{e_\nu}R_{\vec e_{\nu(\mu)}}R_{\vec e_{\nu(\nu)}}$ even | Generator cells fermionic, bivectors bosonic |
| $x^{*}=\sigma(\alpha(x^{r}))$ | The Hermitian dagger; even, anti-involution |
| $\mathbb{M}_+,\mathbb{M}_-$ | Fixed and anti-fixed loci of the dagger; informational and material sectors |
| $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ | The eigen-decomposition of the dagger; not an algebra grading |
| $\langle\tilde{Q}\rangle_{\natural}=\sum_\mu Q_\mu^2$ | The quaternionic norm; $x^{*}=\sigma(\langle x\rangle_{\natural})\sigma(x)^{-1}$ |
| $\mathcal{U}=\{x:x^{*}x=1\}$ | The $*$-unitary slice; $\mathcal{U}\cong \mathrm{U}(2)$ in the matrix model, Lie algebra $\mathbb{M}_-$ |
| $\alpha(x)=\varepsilon_x x=\Omega x\Omega^{-1}$, $\varepsilon_x=(-1)^{\lvert x\rvert}$ | The grade involution as a scalar sign |
| $\Theta_x(y)=x\,y\,x^{*}$ | The Hermitian sandwich, the only operator used |
| $\Theta_x\Theta_z=\Theta_{xz}$ | Exact composition; no sign correction |
| $\Theta_a=q(a)\rho_a$ ($a\in V$) | The reflection read in the Hermitian pairing |
| $\mathrm{Cl}^1=u\mathbb{B}$, $\langle su,tu\rangle=-q(u)\langle s,t\rangle$ | The odd slot as a coset, with the induced form |
| $(-1)^F=i\vec e_z\in\mathbb{M}_+$ | Parity of one mode, an even Hermitian element |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the parity grading, the volume element and the two conjugations.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the grade involution, the reflection count and the split of the orthogonal group.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the involutions of a Clifford algebra, the $*$-unitary groups they define and the norm factor.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the chirality element, the bosonic/fermionic grading and its use in field theory.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (American Mathematical Society, 1956), for the adjoint of an anti-automorphism and the $*$-unitary group of an algebra with involution.
