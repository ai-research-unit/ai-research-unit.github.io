# __The Unitary Group of the Reduced Biquaternion Algebra__

## Introduction

The reduced biquaternion algebra is the commutative algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$ of basis $1,i,j,ij$, with idempotent coordinates $(Q_{+},Q_{-})=(Q_{\blacktriangle}+Q_{\blacktriangledown},Q_{\blacktriangle}-Q_{\blacktriangledown})$ and element $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$. Its star ${}^{*}=\bar{\cdot}\circ{}_{\mathrm{ts}}$ acts by $\breve Q^{*}=\bar Q_{\blacktriangle}-j\bar Q_{\blacktriangledown}$, that is by $(Q_{+},Q_{-})\mapsto(\bar Q_{-},\bar Q_{+})$, and it carries two Hermitian forms: the plain sesquilinear form

$$
\langle \breve Q_{1},\breve Q_{2}\rangle_{*}=\mathrm{Sc}(\breve Q_{1}\breve Q_{2}^{*})=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}-Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown},
$$

whose quadratic form is $\langle \breve Q\rangle_{*}=|Q_{\blacktriangle}|^{2}-|Q_{\blacktriangledown}|^{2}$, indefinite of real signature $(2,2)$, and the tessarine sesquilinear form

$$
\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}*}=\mathrm{Sc}(\breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*})=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}+Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown},
$$

whose quadratic form is $\langle \breve Q\rangle_{\mathrm{ts}*}=|Q_{\blacktriangle}|^{2}+|Q_{\blacktriangledown}|^{2}=\mathrm{Sc}(\breve Q_{\mathrm{ts}}\breve Q^{*})$, positive definite. The **$*$-unitary group** of the algebra is the group of units that leave a Hermitian form invariant; because the algebra is a direct product of two complex lines, that group splits into two circles, and everything the article says about it follows from the coordinates.

The classical $*$-unitary condition reads $P_{\mathrm{ts}}P^{*}=1$, and in the idempotent coordinates it is the pair of unit-modulus conditions $|p|=|q|=1$: the $*$-unitary group of the definite form is the compact torus $\mathbb{T}^{2}$, the maximal compact subgroup of the group of units. The $*$-unitary group of the indefinite form is the complementary graph group $\{p\bar q=1\}\cong\mathbb{C}^{\times}$, non-compact. The two are the compact and the split object of the algebra, they meet in a circle, and the group of units retracts onto both, with different homotopy meaning: onto the torus as the maximal compact subgroup, onto the split group as a projection with non-contractible fibres.

The article owns the two $*$-unitary groups, the retraction of the unit group onto the compact one, the retraction of the norm-one group onto its compact part, and the homotopy invariants of all of them. The dagger and the involutions are *The Two Involutions and the Group of Involutions*; the four products and the four norms are *The Four Products, Their Forms and Their Algebraic Norms*; the group of units and its Lie structure are *The Group of Units of the Algebra of the Reduced Biquaternions* and *Reduced Biquaternion Lie Group and Exponential Structure*; the metric and the topology of the space are *Topology and Metric for Each of the Operations* and *The Euclidean Topology of the Reduced Biquaternion Algebra*; the norm-one group of the multiplication is *Norm and Invertibility in the Algebra of the Reduced Biquaternions*. The non-commutative companion, where the $*$-unitary group is $\mathrm{U}(2)$ and the topology of the unit group follows from it, is *The Unitary Group of the Biquaternion Algebra*.

## The $*$-Unitary Group of the Definite Form

**Proposition (the classical condition).** For a unit $P$ the following are equivalent: $P_{\mathrm{ts}}P^{*}=1$; $\langle P \breve Q\rangle_{\mathrm{ts}*}=\langle \breve Q\rangle_{\mathrm{ts}*}$ for every $\breve Q$; and $|p|=|q|=1$ in the idempotent coordinates $P=p\Pi_++q\Pi_-$.

**Proof.** In the idempotent coordinates the star sends $(p,q)$ to $(\bar q,\bar p)$ and the tessarine sign to $(q,p)$, so $P_{\mathrm{ts}}P^{*}=(|q|^{2},|p|^{2})$ and its scalar part is $\langle P\rangle_{\mathrm{ts}*}=\tfrac12(|p|^{2}+|q|^{2})$; and $\langle P \breve Q\rangle_{\mathrm{ts}*}=\tfrac12\bigl(|p|^{2}|Q_{+}|^{2}+|q|^{2}|Q_{-}|^{2}\bigr)$ because the idempotent coordinates multiply componentwise and $\langle\cdot\rangle_{\mathrm{ts}*}$ reads the two moduli squared. The condition $\langle P \breve Q\rangle_{\mathrm{ts}*}=\langle \breve Q\rangle_{\mathrm{ts}*}$ for all $\breve Q$ forces $|p|=|q|=1$, and under that condition it holds.

**Theorem (the $*$-unitary group is a torus).** The $*$-unitary group of the definite form,

$$
\boxed{\;
\mathrm{U}(\mathbb{B}_{\mathrm{r}})=\{P\in\mathbb{B}_{\mathrm{r}}^{\times}:P_{\mathrm{ts}}P^{*}=1\}=\{p\Pi_++q\Pi_-:|p|=|q|=1\}\cong \mathrm{U}(1)\times \mathrm{U}(1)=\mathbb{T}^{2}
\;},
$$

is a compact abelian real two-dimensional torus; it is the maximal compact subgroup and the maximal torus of the group of units, and it is the group of multiplicative isometries of $\langle\cdot\rangle_{\mathrm{ts}*}$.

**Proof.** By the proposition the condition is the two unit-modulus conditions, whose solution set is a product of two circles; it is closed and bounded hence compact; it is a subgroup because the product is componentwise. For maximality, every unit $P=(p,q)$ writes uniquely as $(r_{1}\sigma_{1},r_{2}\sigma_{2})$ with $r_{1}=|p|>0$, $r_{2}=|q|>0$ and $\sigma_{1},\sigma_{2}$ of modulus one, that is $P=RS$ with $R=(r_{1},r_{2})$ positive and $S\in\mathbb{T}^{2}$; the group of units is connected and abelian, so its maximal compact subgroup is unique and equals the product of the maximal compact subgroups of the two punctured lines, which are the two unit circles.

**Corollary (the decomposition).** The group of units is the direct product of the $*$-unitary torus and the positive part,

$$
\boxed{\;
\mathbb{B}_{\mathrm{r}}^{\times}=\mathbb{T}^{2}\times\mathbb{R}_{>0}^{2}
\;},
$$

through the polar decomposition $p=|p|\exp(i\theta_{1})$, $q=|q|\exp(i\theta_{2})$, and the topological norm of a unit is $\langle P\rangle_{\mathrm{ts}*}=\tfrac12(r_{1}^{2}+r_{2}^{2})$.

**Proof.** Each nonzero complex number has a unique polar form, and the multiplication is componentwise, so the map $\mathbb{T}^{2}\times\mathbb{R}_{>0}^{2}\to\mathbb{B}_{\mathrm{r}}^{\times}$ given by the componentwise product is a bijective group homomorphism.

## The $*$-Unitary Group of the Indefinite Form

**Proposition (the indefinite $*$-unitary group).** The units that preserve the indefinite Hermitian form $\langle\cdot,\cdot\rangle_{*}$ are

$$
\boxed{\;
\mathrm{U}(\mathbb{B}_{\mathrm{r}},H)=\{p\Pi_++q\Pi_-:p\bar q=1\}=\{p\Pi_++\bar p^{-1}\Pi_-\}\cong\mathbb{C}^{\times}
\;},
$$

a non-compact abelian group isomorphic to the multiplicative group of the complex field, homotopy equivalent to a circle.

**Proof.** $\langle P \breve Q\rangle_{*}=\mathrm{Re}\bigl(p\,Q_{+}\cdot\overline{q\,Q_{-}}\bigr)=\mathrm{Re}\bigl(p\bar q\,Q_{+}\bar Q_{-}\bigr)$, and $\langle \breve Q\rangle_{*}=\mathrm{Re}(Q_{+}\bar Q_{-})$, so the condition for all $\breve Q$ is $p\bar q=1$, which forces $q=\bar p^{-1}$; the map to $\mathbb{C}^{\times}$ by the first coordinate is an isomorphism, since the multiplication is $p\bar q=p(\bar p^{-1})^{-1}$.

**Corollary (the intersection of the two $*$-unitary groups).** The two $*$-unitary groups meet in the diagonal circle

$$
\mathrm{U}(\mathbb{B}_{\mathrm{r}})\cap \mathrm{U}(\mathbb{B}_{\mathrm{r}},H)=\{p\Pi_++q\Pi_-:p=q,\ |p|=1\}\cong \mathrm{U}(1),
$$

which is the unit circle of the scalar line $\mathbb{C}=\mathbb{R}\{1,i\}$, the fixed space of the tessarine sign.

**Proof.** The conditions $|p|=|q|=1$ and $q=\bar p^{-1}$ together give $q=p$, because $|p|=1$ makes $\bar p^{-1}=p$; an element of the intersection is therefore the complex scalar element $\breve Q=p$ with $|p|=1$.

**Remark (the naming).** The definite form $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ is the form of the classical $*$-unitary condition $\breve Q_{1,\mathrm{ts}}\breve Q_{1}^{*}=1$, and its $*$-unitary group is the compact torus; the indefinite form $\langle\cdot,\cdot\rangle_{*}$ is the form whose Hermitian pairing with the star is $\mathrm{Sc}(\breve Q_{1}\breve Q_{2}^{*})$, and its $*$-unitary group is the split group. In the biquaternion algebra the two roles fall differently, because there the form $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ is definite and its $*$-unitary group is the compact $\mathrm{U}(2)$; the difference is a sign in the tessarine sign, which is the sign of the hyperbolic unit $j$.

## The Retraction of the Unit Group

**Theorem (the retraction onto the $*$-unitary group).** The map

$$
r:\mathbb{B}_{\mathrm{r}}^{\times}\longrightarrow \mathrm{U}(\mathbb{B}_{\mathrm{r}}), \qquad (p,q)\longmapsto\bigl(p/|p|,\;q/|q|\bigr),
$$

is a strong deformation retraction of the group of units onto the $*$-unitary torus, and the deformation keeps the idempotent coordinates' arguments fixed and shrinks the moduli.

**Proof.** The homotopy $h_{t}(p,q)=\bigl(|p|^{1-t}p/|p|,\;|q|^{1-t}q/|q|\bigr)$ for $t\in[0,1]$ starts at the identity, ends at $r$, and fixes every point of the torus, and it is continuous on the punctured complex lines; it is not a group homomorphism for $t<1$ but it is a homotopy of the space.

**Corollary (the homotopy of the unit group).** $\mathbb{B}_{\mathrm{r}}^{\times}$ is homotopy equivalent to $\mathbb{T}^{2}$; it is connected, its fundamental group is $\mathbb{Z}^{2}$, and its homology in degree one is $\mathbb{Z}^{2}$.

**Proof.** A strong deformation retraction induces an isomorphism of homotopy groups, and the torus has the stated invariants.

**Remark (no retraction onto the split group).** The split $*$-unitary group $\mathrm{U}(\mathbb{B}_{\mathrm{r}},H)$ is not a deformation retract of the unit group: the projection $(p,q)\mapsto(p,\bar p^{-1})$ has fibres isomorphic to $\mathbb{C}^{\times}$, which are not contractible, so it is not a homotopy equivalence, and the fundamental groups $\mathbb{Z}$ and $\mathbb{Z}^{2}$ differ. The split group is a subgroup and a quotient in dimension, not a deformation retract.

## The Retraction of the Norm-One Group

**Theorem (the compact part of the norm-one group).** The norm-one group of the multiplication is $\{P:\langle P\rangle_{\mathrm{ts}}=1\}=\{Q_{+}\Pi_++Q_{+}^{-1}\Pi_-\}\cong\mathbb{C}^{\times}$; its intersection with the $*$-unitary torus is the diagonal circle $\{Q_{+}\Pi_++\bar Q_{+}\Pi_-:|Q_{+}|=1\}\cong S^{1}$, and the modulus map $Q_{+}\mapsto Q_{+}/|Q_{+}|$ is a strong deformation retraction

$$
\{\langle P\rangle_{\mathrm{ts}}=1\}\longrightarrow \{\langle P\rangle_{\mathrm{ts}}=1\}\cap \mathrm{U}(\mathbb{B}_{\mathrm{r}})\cong S^{1}.
$$

**Proof.** $\langle P\rangle_{\mathrm{ts}}=Q_{+}Q_{-}=1$ forces $Q_{-}=Q_{+}^{-1}$ and $Q_{+}\neq0$, and putting $|Q_{+}|=1$ gives $Q_{-}=\bar Q_{+}$, which is the diagonal circle; the homotopy sends $Q_{+}$ to $|Q_{+}|^{1-t}Q_{+}/|Q_{+}|$ and $Q_{+}^{-1}$ to $|Q_{+}|^{t}Q_{+}^{-1}$, so the product $Q_{+}Q_{-}$ stays equal to one.

**Corollary (the topology of the norm-one group).** The norm-one group is homotopy equivalent to a circle; its fundamental group is $\mathbb{Z}$, its element $Q_{+}=\exp(x+iy)$ has a logarithm defined modulo $2\pi i\mathbb{Z}$, and the universal covering is

$$
\mathbb{C}\longrightarrow\mathbb{C}^{\times}, \qquad x\longmapsto \exp(x),
$$

with kernel $2\pi i\mathbb{Z}$.

**Proof.** The polar decomposition of $\mathbb{C}^{\times}$ retracts it onto the circle, and the exponential is the universal covering of $\mathbb{C}^{\times}$ with the stated kernel.

## Homotopy Groups, Generators and the Universal Cover

**Theorem (the invariants of the unit group).** The universal covering of the group of units is

$$
\mathbb{C}^{2}\longrightarrow\mathbb{B}_{\mathrm{r}}^{\times}, \qquad (x,y)\longmapsto\bigl(\exp(x)\Pi_++\exp(y)\Pi_-\bigr),
$$

with kernel $2\pi i\mathbb{Z}^{2}$; the group of units has $\pi_{1}=\mathbb{Z}^{2}$ and $\pi_{n}=0$ for $n\geq2$; the $*$-unitary group has the same invariants, being a strong deformation retract.

**Proof.** The exponential of each complex coordinate is the universal covering of a punctured line, and the product of two coverings is the covering of the product; the torus has $\pi_{1}=\mathbb{Z}^{2}$ and no higher homotopy.

**Corollary (the generators).** The two generators of $\pi_{1}(\mathbb{B}_{\mathrm{r}}^{\times})$ are the two loops

$$
\gamma_{1}(s)=\Pi_++\exp(2\pi i s)\Pi_-, \qquad \gamma_{2}(s)=\exp(2\pi i s)\Pi_++\Pi_-, \qquad s\in[0,1],
$$

one in each idempotent line, based at the unit $1$; they commute, and every loop class is $m[\gamma_{1}]+n[\gamma_{2}]$ with integers $m,n$.

**Proof.** Under the isomorphism $\mathbb{B}_{\mathrm{r}}^{\times}\cong\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ and the retraction onto the torus, the two loops are the two standard generators of $\pi_{1}$ of the product of two circles.

**Remark (what the commutativity buys).** The group of units is abelian and its Lie algebra is abelian, so the exponential map is a covering and the whole topology is the topology of a product of two punctured planes. In the biquaternion algebra the same map is the non-abelian exponential of a matrix group, the group of units is not abelian, and the topology of its maximal compact subgroup is that of $S^{1}\times S^{3}$; the algebraic reason for the difference is the commutativity, and the analytic reason is that the exponential of a commutative algebra is diagonal in the idempotent coordinates.

## Comparison with the Biquaternion Case

**Remark (the two $*$-unitary groups).** In the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ the Hermitian form $\tilde Q\tilde Q^{*}$ is positive definite, its $*$-unitary group is $\mathrm{U}(2)$, compact of real dimension four, and it is the maximal compact subgroup of the group of units, which retracts onto it and then onto $S^{1}\times S^{3}$. In the reduced biquaternion algebra the same construction gives the torus $\mathbb{T}^{2}$, of real dimension two, and the group of units retracts onto the product of the two circles, with $\pi_{1}=\mathbb{Z}^{2}$. The dimensions drop from four to two and from three to one because the four quaternion directions of the biquaternion algebra collapse here to the two complex idempotent coordinates; the maximal compact subgroup is $\mathrm{U}(2)$ there and the torus here, and the fundamental group has rank one in the biquaternion algebra ($\mathbb{B}^{\times}\simeq S^{1}\times S^{3}$, $\pi_{1}=\mathbb{Z}$) and two in the reduced one ($\mathbb{B}_{\mathrm{r}}^{\times}\simeq\mathbb{T}^{2}$, $\pi_{1}=\mathbb{Z}^{2}$).

## Worked Examples

**A $*$-unitary element and a split element.** The element $\Pi_++i\Pi_-$ has $p=1$ and $q=i$, so it is $*$-unitary and its topological norm is $\langle\cdot\rangle_{\mathrm{ts}*}=1$; it is a unit, since $\langle\cdot\rangle_{\mathrm{ts}}=i\neq0$, and it is nevertheless isotropic for the indefinite form, because $Q_{\blacktriangle}=\tfrac12(1+i)$ and $Q_{\blacktriangledown}=\tfrac12(1-i)$ have equal moduli and $\langle\cdot,\cdot\rangle_{*}=0$. The null set of $\langle\cdot\rangle_{*}$ therefore contains units, and is not the set of zero divisors. The element $2\Pi_++\tfrac12\Pi_-$ has $\langle\cdot\rangle_{\mathrm{ts}}=1$, so it is a non-compact versor, with $\langle\cdot\rangle_{\mathrm{ts}*}=\tfrac12(4+\tfrac14)=\tfrac{17}{8}$, and it lies outside the $*$-unitary torus.

**The retraction in coordinates.** The unit $P=(3+4i,\;2i)$ retracts to $(3/5+4i/5,\;i)$, a point of the torus; the deformation path scales the radius of the first coordinate from five to one and the radius of the second from two to one, keeping the arguments.

**Verification.** The preservation of the definite form $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ by the torus $|p|=|q|=1$, the preservation of the indefinite form $\langle\cdot,\cdot\rangle_{*}$ by the group $p\bar q=1$, and the identification of the two $*$-unitary conditions with the coordinate conditions were checked by recomputation on random unit elements; the deviations found were at the level of the floating-point noise.

## Summary

The reduced biquaternion algebra carries two Hermitian forms with respect to its star. The definite one has quadratic form $\langle\cdot\rangle_{\mathrm{ts}*}=|Q_{\blacktriangle}|^{2}+|Q_{\blacktriangledown}|^{2}=\mathrm{Sc}(P^{*}P)$ and $*$-unitary group $\mathrm{U}(\mathbb{B}_{\mathrm{r}})=\{P:|p|=|q|=1\}\cong\mathbb{T}^{2}$, the compact abelian torus, which is the maximal compact subgroup and the maximal torus of the group of units and the group of multiplicative isometries of $\langle\cdot\rangle_{\mathrm{ts}*}$; the group of units is $\mathbb{T}^{2}\times\mathbb{R}_{>0}^{2}$ through the polar decomposition. The indefinite one has quadratic form $\langle\cdot\rangle_{*}=|Q_{\blacktriangle}|^{2}-|Q_{\blacktriangledown}|^{2}$ and $*$-unitary group $\{p\bar q=1\}\cong\mathbb{C}^{\times}$, a non-compact split group homotopy equivalent to a circle; the two $*$-unitary groups meet in the diagonal circle. The modulus map retracts the group of units onto the torus, so the unit group is homotopy equivalent to $\mathbb{T}^{2}$, with $\pi_{1}=\mathbb{Z}^{2}$ generated by the two idempotent circles, no higher homotopy and universal cover $\mathbb{C}^{2}$; the norm-one group $\{N=1\}\cong\mathbb{C}^{\times}$ retracts onto its compact part, the diagonal circle, with $\pi_{1}=\mathbb{Z}$ and universal cover the exponential of $\mathbb{C}$. The split $*$-unitary group is not a deformation retract but a complementary subgroup. The compact group is the analogue of the $*$-unitary group $\mathrm{U}(2)$ of the biquaternion algebra, with the real dimension lowered from four to two and the fundamental group enlarged from $\mathbb{Z}$ to $\mathbb{Z}^{2}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\breve Q^{*}=\overline{\breve Q_{\mathrm{ts}}}$ | the star, $(Q_{+},Q_{-})\mapsto(\bar Q_{-},\bar Q_{+})$ |
| $\langle \breve Q_{1},\breve Q_{2}\rangle_{*}=\mathrm{Sc}(\breve Q_{1}\breve Q_{2}^{*})$ | the plain sesquilinear Hermitian form, quadratic form $\langle\cdot\rangle_{*}$ |
| $\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}*}=\mathrm{Sc}(\breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*})$ | the tessarine sesquilinear Hermitian form, quadratic form $\langle\cdot\rangle_{\mathrm{ts}*}$ |
| $\langle \breve Q\rangle_{\mathrm{ts}*}=\lvert Q_{\blacktriangle}\rvert^{2}+\lvert Q_{\blacktriangledown}\rvert^{2}=\mathrm{Sc}(\breve Q_{\mathrm{ts}}\breve Q^{*})$ | the definite norm, the topological norm |
| $\langle \breve Q\rangle_{*}=\lvert Q_{\blacktriangle}\rvert^{2}-\lvert Q_{\blacktriangledown}\rvert^{2}$ | the indefinite norm |
| $\mathrm{U}(\mathbb{B}_{\mathrm{r}})=\{P_{\mathrm{ts}}P^{*}=1\}$ | the $*$-unitary group of the definite form, $\cong\mathbb{T}^{2}$ |
| $H=\langle\cdot,\cdot\rangle_{*}$ | the indefinite Hermitian form, the one the group $\mathrm{U}(\mathbb{B}_{\mathrm{r}},H)$ preserves |
| $\mathrm{U}(\mathbb{B}_{\mathrm{r}},H)=\{p\bar q=1\}$ | the $*$-unitary group of the indefinite form, $\cong\mathbb{C}^{\times}$ |
| $\mathbb{T}^{2}=\{\lvert p\rvert=\lvert q\rvert=1\}$ | the maximal compact torus of the group of units |
| $\mathbb{B}_{\mathrm{r}}^{\times}=\mathbb{T}^{2}\times\mathbb{R}_{>0}^{2}$ | the polar decomposition of the group of units |
| $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=Q_{+}Q_{-}$ | the reduced norm, the algebraic norm, distinct from $\langle\cdot\rangle_{\mathrm{ts}*}$ |

## Further Reading

- [Reduced Biquaternion Space](reduced-biquaternion-space.html), above this article in this category, for the idempotents and the two complex coordinates.
- [The Two Involutions and the Group of Involutions](the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions.html), above this article, for the star and the tessarine sign.
- [The Four Products, Their Forms and Their Algebraic Norms](the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.html), above this article, for the two Hermitian forms and their signatures.
- [The Group of Units of the Algebra of the Reduced Biquaternions](the-group-of-units-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), below this article, for the units as the complement of the zero divisors.
- [Reduced Biquaternion Lie Group and Exponential Structure](reduced-biquaternion-lie-group-and-exponential-structure.html), above this article, for the Lie algebra, the exponential and the norm-one group.
- [The Unitary Group of the Biquaternion Algebra](the-unitary-group-of-the-biquaternion-algebra.html), for the companion in which the $*$-unitary group is the compact $\mathrm{U}(2)$.
