# __The Graded Algebra, Fermion Parity and the Two Sectors with Signed Inner Conjugation in Biquaternionic Form__

## Introduction

The biquaternion algebra is the even part of the Clifford algebra of Minkowski space, $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}$, and that identification is the whole source of the geometric content of the series. It has a second consequence that is used throughout the physics but stated nowhere in one place: the ambient algebra is **$\mathbb{Z}/2$-graded**, and the grading is the fermion parity of the theory. The even slot is the bosonic sector, and it is the biquaternion algebra; the odd slot is the fermionic sector, and it is the slot that carries the Dirac generators and the anticommuting mode operators. The physics is written in $\mathbb{B}$, and $\mathbb{B}$ alone is the bosonic sector of a graded algebra.

The point of stating this separately is that the parity is **not a second structure**. The signed inner conjugation $\mathrm{Ad}^{\alpha}_x(y)=\alpha(x)yx^{-1}$ of *Biquaternion Versors and the Orthogonal Group* is not a second conjugation beside the ordinary one, and the odd slot is not a second copy of the algebra: the two are tied by the multiplication rule odd $\times$ odd $=$ even, and that rule is what makes the reflection, the parity and the graded bracket work. Two statements make it sharp, and both are proved below. The first is that the twist $\alpha$ is itself a conjugation, by the volume element $\Omega=\gamma^0\gamma^1\gamma^2\gamma^3$: the parity twist is the conjugation by the pseudoscalar, so it is not new data but the grading read as an inner automorphism. The second is that two odd steps compose to an even one, so the composite of two signed conjugations by fermionic elements is an ordinary conjugation by a bosonic element — the two signs cancel. Two reflections compose to a rotation, and the composite element is an element of the biquaternion algebra.

The ambient algebra $\mathrm{Cl}_{1,3}$ is announced as $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$; the identification $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}$, the dictionary $e_1\mapsto\gamma^2\gamma^3$, $e_2\mapsto\gamma^3\gamma^1$, $e_3\mapsto\gamma^1\gamma^2$, $i\mapsto-\Omega$ and the chirality operator $\gamma^5=i\Omega$ are *The Clifford Structure of the Biquaternion Algebra*; the two slots of the envelope, the signed inner conjugation, the reflection and the determinants of the odd and even versors are *Biquaternion Versors and the Orthogonal Group*; the volume element and its two actions are the same article, where $\mathrm{Ad}^{\alpha}_\Omega(v)=-v$ is proved; the fermionic mode and the identity $(-1)^F=ie_3$ are *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*; and the parity of the state space, $\Gamma(-I)=(-1)^{\hat N}$, is *The Fermionic Fock Space in Biquaternionic Form*. Nothing owned by those articles is re-derived.

## The Grading of the Ambient Algebra

**Given.** The Clifford algebra of Minkowski space is graded by parity, $\mathrm{Cl}_{1,3}=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$, with $\mathrm{Cl}^i\mathrm{Cl}^j\subseteq\mathrm{Cl}^{i+j}$. The even part is $\mathbb{B}$, and the odd part is the slot containing the generators; the dictionary sends the algebra to the even slot, so every element of the algebra in which the series computes is even.

**The multiplication table, read physically.** The grading says

$$
\text{even}\cdot\text{even}=\text{even},\quad
\text{even}\cdot\text{odd}=\text{odd},\quad
\text{odd}\cdot\text{even}=\text{odd},\quad
\text{odd}\cdot\text{odd}=\text{even},
$$

that is, the parity of a product is the sum of the parities. The generators $\gamma^\mu$ are odd; the bivectors $\gamma^\mu\gamma^\nu$ and the volume element are even; the square $(\gamma^\mu)^2=\pm1$ is a scalar and hence even. The physical reading is the whole of the grading in one sentence: **a product of an odd number of fermionic objects is fermionic, a product of an even number is bosonic.** In particular two fermionic steps are bosonic, which is the statement of the next section but one.

**Remark.** The identification $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}$ is therefore not merely "$\mathbb{B}$ is a Clifford algebra"; it says *which* slot of the ambient graded algebra the biquaternion algebra is. The whole physics series computes in the bosonic sector. The fermionic sector is the other graded component, and the rest of this article says what it contributes.

## The Twist Is the Conjugation by the Pseudoscalar

The twist $\alpha$ of the signed inner conjugation is usually introduced as an abstract map, the grade involution, equal to $+1$ on the even slot and $-1$ on the odd slot. In the ambient algebra it is an ordinary conjugation.

**Theorem (the grade involution is a conjugation).** Let $\Omega=\gamma^0\gamma^1\gamma^2\gamma^3$ be the volume element of $\mathrm{Cl}_{1,3}$. Then $\Omega^2=-1$, $\Omega$ commutes with the even slot and anticommutes with every generator, and for every homogeneous $x$

$$
\Omega\,x\,\Omega^{-1}=(-1)^{\lvert x\rvert}\,x=\alpha(x).
$$

With the dictionary $i\mapsto-\Omega$, the same statement reads: **the grade involution is the conjugation by the central scalar imaginary**, which is the pseudoscalar read on the algebra.

**Proof.** The volume element of an even-dimensional Clifford algebra anticommutes with every generator, since moving $\gamma^{j}$ past the monomial $\Omega$ costs the sign $(-1)^{3}$; a monomial $x=\gamma^{\mu_1}\cdots\gamma^{\mu_k}$ therefore satisfies $\Omega x=(-1)^{k}x\Omega$, and $\Omega^{-1}$ exists because $\Omega^2=-1\neq0$. On the even slot $\lvert x\rvert$ is even and the conjugation is the identity. The dictionary is the one recorded by *The Clifford Structure of the Biquaternion Algebra*, and it identifies $i$ with $-\Omega$, so conjugation by $i$ agrees with conjugation by $\Omega$ on the ambient algebra; on the even slot both are the identity, which is the statement of *Biquaternion Versors and the Orthogonal Group* about the central imaginary.

**Corollary (the twist is not new data).** The signed inner conjugation is the ordinary conjugation with the left factor replaced by its pseudoscalar conjugate,

$$
\mathrm{Ad}^{\alpha}_x(y)=\bigl(\Omega\,x\,\Omega^{-1}\bigr)\,y\,x^{-1}=\alpha(x)\,y\,x^{-1},
$$

so the difference between the two conjugations is exactly one factor of the chirality element on the left. On the bosonic sector the factor is invisible and the two conjugations agree; on the fermionic sector it is the minus sign.

**Remark.** This is the precise sense in which the framework needs no second structure. The parity grading, the volume element and the chirality operator are the same element of the ambient algebra up to normalisation — $\gamma^5=i\Omega$, with $(\gamma^5)^2=+1$ and $\Omega^2=-1$ — and the twist is the conjugation by it. A theory written only in $\mathbb{B}$ retains the element $\Omega$ (it is even, it lies in the algebra) but loses the odd slot on which the twist has any effect.

## Two Fermionic Steps Are Bosonic

**Proposition (the signs cancel on composition).** For units $x,z$ of the ambient algebra,

$$
\mathrm{Ad}^{\alpha}_x\circ\mathrm{Ad}^{\alpha}_z=\mathrm{Ad}^{\alpha}_{xz},
$$

and if $x$ and $z$ are both odd then $xz$ is even and the composite is the **ordinary** inner conjugation $\mathrm{Ad}_{xz}$. The composite is signed exactly when the two factors have opposite parity.

**Proof.** The composition law is the one of the signed inner conjugation, $\mathrm{Ad}^{\alpha}_x\mathrm{Ad}^{\alpha}_z=\mathrm{Ad}^{\alpha}_{xz}$, and on an even element the twist is the identity, so $\mathrm{Ad}^{\alpha}_{xz}=\mathrm{Ad}_{xz}$ whenever $xz$ is even. The product of two odd elements is even by the grading table.

| $x$ | $z$ | $xz$ | composite |
|---|---|---|---|
| even | even | even | ordinary, $\mathrm{Ad}_{xz}$ |
| even | odd | odd | signed, $-\mathrm{Ad}_{xz}$ |
| odd | even | odd | signed, $-\mathrm{Ad}_{xz}$ |
| odd | odd | even | ordinary, $\mathrm{Ad}_{xz}$ |

**Physical reading: the parity word of an isometry.** An odd element is a product of an odd number of vectors and acts by an isometry of determinant $-1$; an even element acts by one of determinant $+1$; this is the theorem of the odd and even versors of *Biquaternion Versors and the Orthogonal Group*. The table above is therefore the algebra behind the reflection count: **two reflections compose to a rotation**, and the composite is carried by an element of the biquaternion algebra, a bosonic element. The element $xz$ of two odd vectors is a bivector, that is, an element of the even slot, and the difference between the two conjugations has disappeared in the product. The parity of the number of reflections is the $\mathbb{Z}/2$ that separates $O(1,3)$ from $SO(1,3)$, and the same $\mathbb{Z}/2$ is the quotient $\mathrm{Pin}/\mathrm{Spin}$ of the pin and spin groups of the maths corpus.

**Corollary (the square of an odd step is bosonic).** For odd $x$ one has $x^2$ even and $(\mathrm{Ad}^{\alpha}_x)^2=\mathrm{Ad}_{x^2}$; for a generator this reads $(\mathrm{Ad}^{\alpha}_{\gamma^\mu})^2=\mathrm{Ad}_{(\gamma^\mu)^2}$, and $(\gamma^\mu)^2=\pm1$ is a scalar, so the square of the signed conjugation by a generator is the identity.

## The Odd Slot Is a Coset, Not a Second Algebra

**Proposition (the odd slot is not closed).** The odd slot satisfies $\mathrm{Cl}^1\mathrm{Cl}^1\subseteq\mathbb{B}$, so it is not a subalgebra; it is a single coset of the even slot for the multiplication. Fix an odd unit $\gamma$; then every odd element is $\gamma s$ with $s$ even, and the odd slot is the copy $\mathbb{B}\gamma$ of the algebra inside the ambient one.

**Proof.** Odd $\times$ odd is even by the grading table; for the second statement, an odd $y$ is $y=\gamma(\gamma^{-1}y)$ and $\gamma^{-1}y$ is even.

**Remark (why the two copies are not independent).** The two slots are isomorphic as modules over the even part but are not two subalgebras, and the multiplication between them is the graded multiplication. Two independent copies $A,B\cong\mathbb{B}$ would have no rule for the product of two elements of $B$; the rule odd $\times$ odd $=$ even is exactly what is lost, and with it the reflection, the parity and the twist. The consistent object is the single graded algebra, and the framework's parity is the grading of that one algebra.

**Corollary (the algebra's own elements do not contain a reflection).** Every non-isotropic vector can be rescaled to a vector of square $\pm1$, and such a vector is odd, hence not an element of $\mathbb{B}$ — the corollary recorded by *Biquaternion Versors and the Orthogonal Group*. The reflection is therefore not in the algebra's even slot; it acts on the algebra through the signed conjugation by an element of the odd slot, which is a Clifford element and not a biquaternion. This is the same fact as the table of the previous section: reflections are the odd steps, rotations the even products of two of them.

## What the Grading Does and Does Not Explain

Several distinct $\mathbb{Z}/2$'s coexist in the framework, and the parity of the grading is only one of them. They are named here to keep them apart, in the manner of the warning of *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*.

| structure | what it grades | an algebra grading? |
|---|---|---|
| Clifford parity (this article) | $\mathrm{Cl}_{1,3}=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$, bosonic/fermionic | yes, of the ambient algebra only |
| chirality $L/R$ | the two minimal left ideals of $\mathbb{B}$, the operator $\gamma^5$ | a $\mathbb{Z}/2$ of the module structure |
| sector splitting $\mathbb{M}_+\oplus\mathbb{M}_-$ | the Hermitian dagger, informational/material | **no**; it grades the symmetrized product only |
| frame grading $\beta$ | large/small components, Foldy–Wouthuysen | no; a frame-dependent split |
| number grading $N$ | the Fock space by total particle number | a grading of the state space |

The first row is the grading of this article; the second is the grading the supersymmetry article uses, and *Supersymmetric Quantum Mechanics in the Biquaternion Framework* records that the chirality grading must not be conflated with the frame grading. The third row is explicitly **not** an algebra grading, because the product of two Hermitian elements need not be Hermitian; the counterexample $(ie_1)(ie_2)=-e_3$ is the one recorded in the three-gradings section of *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*. The fifth is a grading of the state space and never of the algebra.

**What the grading does not supply.** The parity of a many-mode field is a product over the modes, $\Gamma(-I)=(-1)^{\hat N}=\prod_{\text{modes}}ie_3^{(\text{mode})}$, and the product over modes is not an element of $\mathbb{B}$: the parity of the field is external to the algebra, which is the open item recorded by *The Fermionic Fock Space in Biquaternionic Form*. For one mode, $(-1)^F=ie_3$ is an element of the algebra and is even, as the grading requires of a parity operator: the operator that measures the fermion parity is itself bosonic.

## Worked Cases

### The Twist on the Two Slots

In $\mathrm{Cl}_{1,3}$, with the dictionary $e_1=\gamma^2\gamma^3$ of *The Clifford Structure of the Biquaternion Algebra*:

$$
\Omega\gamma^0\Omega^{-1}=-\gamma^0,\qquad
\Omega\gamma^1\gamma^2\Omega^{-1}=\gamma^1\gamma^2=e_3,\qquad
\Omega\,i\,\Omega^{-1}=i .
$$

The first is the twist on the odd slot, where it contributes $-1$; the second is the twist on a bosonic element, where it contributes $+1$; the third uses $i=-\Omega$ and is the statement that the central imaginary is fixed, which is the remark of *Biquaternion Versors and the Orthogonal Group* that the conjugation by the central imaginary is the identity on the even slot.

### Two Reflections and One Rotation

Let $u=\gamma^1$ and $w=\gamma^2$, both odd and both of square $-1$. Their signed conjugations are the reflections $\mathrm{Ad}^{\alpha}_{\gamma^1}=\rho_{\gamma^1}$ and $\mathrm{Ad}^{\alpha}_{\gamma^2}=\rho_{\gamma^2}$, and their composite is

$$
\mathrm{Ad}^{\alpha}_{\gamma^1}\circ\mathrm{Ad}^{\alpha}_{\gamma^2}
=\mathrm{Ad}^{\alpha}_{\gamma^1\gamma^2}
=\mathrm{Ad}_{e_3},
$$

the last equality because $\gamma^1\gamma^2=e_3$ is an element of the biquaternion algebra. The composite is an ordinary conjugation by a bosonic element and is a rotation. Two reflections of determinant $-1$ have composed to a rotation of determinant $+1$, and the composite element is a quaternion unit: the parity word of the isometry is the grading of the two factors.

### The Square of a Generator

For $x=\gamma^0$, odd with $(\gamma^0)^2=+1$, the composite of the signed conjugation with itself is

$$
\mathrm{Ad}^{\alpha}_{\gamma^0}\circ\mathrm{Ad}^{\alpha}_{\gamma^0}=\mathrm{Ad}^{\alpha}_{(\gamma^0)^2}=\mathrm{Ad}_{(\gamma^0)^2}=\mathrm{id},
$$

the identity on the ambient algebra. The reflection in a timelike direction therefore has order two as a conjugation but is not an involution of the signed kind: its square has forgotten the twist, exactly as the parity table says.

## Summary

The ambient Clifford algebra is $\mathbb{Z}/2$-graded, $\mathrm{Cl}_{1,3}=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$, with even part the biquaternion algebra $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}$ and odd part the slot that carries the Dirac generators. The even slot is the **bosonic sector** and is where the series computes; the odd slot is the **fermionic sector**, and the parity of a product is the sum of the parities, so a product of an even number of fermionic objects is bosonic. The odd slot is not a subalgebra but a single coset, $\mathrm{Cl}^1\mathrm{Cl}^1\subseteq\mathbb{B}$, and the two slots are not independent copies of the algebra but the two graded components of one algebra.

The twist $\alpha$ of the signed inner conjugation is a conjugation: by the volume element $\Omega=\gamma^0\gamma^1\gamma^2\gamma^3$, equivalently by the central scalar imaginary $i=-\Omega$, one has $\alpha(x)=\Omega x\Omega^{-1}=(-1)^{\lvert x\rvert}x$. The signed inner conjugation is therefore the ordinary conjugation with a chirality factor inserted on the left, and the factor is invisible on the bosonic sector and is the minus sign on the fermionic one. Two odd steps compose to an even one: $\mathrm{Ad}^{\alpha}_x\mathrm{Ad}^{\alpha}_z=\mathrm{Ad}^{\alpha}_{xz}$ with $xz$ even whenever $x$ and $z$ are odd, so the composite of two signed conjugations by fermionic elements is an ordinary conjugation by a bosonic element. Physically this is the reflection count: two reflections compose to a rotation, the composite element is a bivector and hence an element of the biquaternion algebra, and the parity of the reflection word is the $\mathbb{Z}/2$ behind $\mathrm{Pin}/\mathrm{Spin}$ and the split of $O(1,3)$ from $SO(1,3)$.

The grading is the parity of the theory, and it is one of several $\mathbb{Z}/2$'s in the framework: the chirality $L/R$ grading of the supersymmetry article, the sector splitting by the dagger, which is not an algebra grading, the frame grading $\beta$, and the number grading of the Fock space. The parity operator is itself bosonic, $(-1)^F=ie_3$ for one mode, and for the field it is a product over modes and therefore external to the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Cl}_{1,3}=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$ | The graded ambient algebra; $\mathrm{Cl}^0=\mathbb{B}$ |
| $\mathrm{Cl}^i\mathrm{Cl}^j\subseteq\mathrm{Cl}^{i+j}$ | Parity of a product is the sum of the parities |
| $\gamma^\mu$ odd, $\gamma^\mu\gamma^\nu$ even | Generators fermionic, bivectors bosonic |
| $\Omega=\gamma^0\gamma^1\gamma^2\gamma^3$ | Volume element, even, $\Omega^2=-1$, anticommutes with the generators |
| $\alpha(x)=\Omega x\Omega^{-1}=(-1)^{\lvert x\rvert}x$ | The twist as a conjugation by the pseudoscalar |
| $i=-\Omega$ | The dictionary; the central imaginary, conjugation by it is the twist |
| $\gamma^5=i\Omega$, $(\gamma^5)^2=+1$ | The chirality operator, the involution reading of the same element |
| $\mathrm{Ad}^{\alpha}_x=\alpha(x)\,(\ )\,x^{-1}$ | Signed inner conjugation, conjugation with a chirality factor on the left |
| $\mathrm{Ad}^{\alpha}_x\mathrm{Ad}^{\alpha}_z=\mathrm{Ad}^{\alpha}_{xz}$ | Composition; ordinary composite for two odd factors |
| $\mathrm{Ad}^{\alpha}_{\gamma^1}\mathrm{Ad}^{\alpha}_{\gamma^2}=\mathrm{Ad}_{e_3}$ | Two reflections give a rotation by a bosonic element |
| $\mathrm{Cl}^1=\mathbb{B}\gamma$ | The odd slot as a coset; not a subalgebra |
| $(-1)^F=ie_3$ | Parity of one mode, an even element; external for the field |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the parity grading, the volume element and the two conjugations.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the grade involution, the reflection count and the split of the orthogonal group.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the chirality element, the bosonic/fermionic grading and its use in field theory.
- Jean-Pierre Serre, *Algèbres de Lie semi-simples complexes* (Benjamin, 1966), for the graded structures and the parity conventions of the Clifford and spinor algebras.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the graded structure of a Clifford algebra over its even part.
