# __Biquaternion Operator Representation Theory__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ has basis $e_0 = 1, e_1, e_2, e_3$, with $e_k^2 = -e_0$, $e_1e_2 = e_3$ and a central scalar imaginary $i$ satisfying $i^2 = -1$; a general element is $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$. The algebra, its conjugations, its six distinguished subspaces and its biquaternion norm $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ are those of *Biquaternion Algebra* and *Biquaternion Norm and Invertibility*, and the physical reading of the algebra is that of *Conventions in the Biquaternion Universe*.

Two different things can be done with an element, and the corpus keeps them apart.

The element can be used as an **element**. It is then a physical object: it is a four-vector of the material sector $\mathbb{M}_-$ or a rotor of the informational sector $\mathbb{M}_+$ (*The Anti-Hermitian Subspace M- as the Material Sector*, *The Hermitian Subspace M+ as the Informational Sector*), it lies on the light cone or it does not, and the question asked about it is *what it is*. Every article of the group *Focus on Element Representations* answers that question in a different coordinate system — the four coefficients, the $2 \times 2$ matrix, the $4 \times 4$ regular matrix, the polar word.

The element can also be used as an **operator**. It is then a rule: it takes an element and returns an element, and the question asked about it is *what it does*. The rule is the **Hermitian sandwich**

$$
\operatorname{H}_{\tilde{Q}} : \mathbb{B} \longrightarrow \mathbb{B}, \qquad \operatorname{H}_{\tilde{Q}}(x) = \tilde{Q}\, x\, \tilde{Q}^{\dagger},
$$

and the whole of its structure as a physical operator — its carrier, the eight real dimensions it moves, the proof that the dagger and not the inverse is the right second factor, its kernel, its action on the six distinguished subspaces, the two Hermitian sectors it preserves, its action on the material sector as the Lorentz transformation of a four-vector, its operators of a boost and of a rotation, the doubling of the rapidity and of the angle, and the polar dictionary of its scale, phase, boost and rotor — is established, once, in *Biquaternion Rotations and Lorentz Transformations*, with the restriction of the acting element to a subspace in *The Sandwich Action in Subspaces*. Those statements are cited here and not restated; the reader who wants the geometry of the sandwich should read them there.

What is left, and what this article and its three companions own, is the sandwich as a **linear map**: the algebra is a four-dimensional complex vector space, the sandwich is an element of $\operatorname{End}_{\mathbb{C}}(\mathbb{B}) \cong M_4(\mathbb{C})$, and the map therefore has a matrix, a determinant, a trace, a rank, a spectrum and a kernel in the linear-algebraic sense. Three things follow that the geometric treatment does not contain. The operator is **homogeneous of degree two** in its operand and blind to the central phase, which is why the whole group of units acts through a group one dimension smaller. It has two **invariants of its own**, the determinant $\lvert N(\tilde{Q})\rvert^{4}$ and the trace $4\lvert Q_0\rvert^{2}$, which are real and non-negative while the invariants of the element matrix are complex. And it has **two regimes**, separated by the light cone and by the single integer $\operatorname{rank}\operatorname{H}_{\tilde{Q}}$, the invertible observer transformation and the collapse of a null operand, whose square law $4\lvert Q_0\rvert^{2}$ is the sharpest statement about the cone the operator carries.

Every statement below is a statement about $\tilde{Q}$ and the algebraic operations alone, so each holds in every coordinate system the algebra admits, and it is the writing of the operator in those systems that the other articles of this section supply: the four coefficients, the coefficient column, the matrix algebra and the module.

**Conventions.** The matrix realization is $\Phi : \mathbb{B} \to M_2(\mathbb{C})$ of *The 2×2 Matrix Element Representation of Biquaternions*, fixed by $\Phi(e_k) = -i\sigma_k$ and $\Phi(i) = iI_2$, so that $\det \Phi(\tilde{Q}) = N(\tilde{Q})$ and $\operatorname{Tr}\Phi(\tilde{Q}) = 2Q_0$. The polar form, its four factors and its domain are *The Polar Element Representation of Biquaternions* and *The Polar Element Representation in Subspaces*. The group of units is $\mathbb{B}^{\times} \cong GL(2,\mathbb{C})$, the unit-norm slice is $\mathbb{B}^{\times}_1 \cong SL(2,\mathbb{C})$, and the two sectors are the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$.

## The Operator as a Linear Map

The sandwich is $\mathbb{C}$-linear in its argument, because left and right multiplications by fixed elements are, and it is homogeneous of degree two in its operand, because the operand occurs on both sides and once conjugated. Its algebra is therefore exhausted by three statements.

**Composition.** The identity $\operatorname{H}_{\tilde{Q}\tilde{R}} = \operatorname{H}_{\tilde{Q}} \circ \operatorname{H}_{\tilde{R}}$ holds, because $\operatorname{H}_{\tilde{Q}}(\operatorname{H}_{\tilde{R}}(x)) = \tilde{Q}(\tilde{R}x\tilde{R}^{\dagger})\tilde{Q}^{\dagger} = (\tilde{Q}\tilde{R})x(\tilde{Q}\tilde{R})^{\dagger}$ by $(\tilde{Q}\tilde{R})^{\dagger} = \tilde{R}^{\dagger}\tilde{Q}^{\dagger}$. Its geometric content is the composition of two frame changes, with the two orthogonal boosts and the Thomas precession worked out, in *Biquaternion Rotations and Lorentz Transformations*; what is used here is its algebraic form: $\tilde{Q} \mapsto \operatorname{H}_{\tilde{Q}}$ is a homomorphism of the multiplicative monoid of $\mathbb{B}$ into $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, and of the group of units into $GL(4,\mathbb{C})$. That is what makes the sandwich a **representation** rather than a family of maps, and it is the reason the operator has a kernel and an image in the group-theoretic sense at all.

**Proposition (the central rule).** For every central $z$ and every $x$,

$$
\operatorname{H}_{z\tilde{Q}}(x) = \lvert z\rvert^{2}\,\operatorname{H}_{\tilde{Q}}(x) .
$$

**Proof.** A central element commutes with everything and $z^{\dagger} = \bar{z}$, so $\operatorname{H}_{z\tilde{Q}}(x) = z\tilde{Q}x\tilde{Q}^{\dagger}\bar{z} = \lvert z\rvert^{2}\operatorname{H}_{\tilde{Q}}(x)$. $\square$

Two readings follow, and the phase is the sharp one. Taking $z = e^{i\theta}$ gives $\operatorname{H}_{e^{i\theta}\tilde{Q}} = \operatorname{H}_{\tilde{Q}}$: **the operator is blind to the scalar imaginary**, so the phase of a state is invisible to every operator the algebra carries. Taking $z = r > 0$ and combining the rule with the composition law gives the homogeneity $\operatorname{H}_{r\tilde{Q}} = r^{2}\operatorname{H}_{\tilde{Q}}$, which is the linear-algebraic form of the double counting of the scale recorded in the polar dictionary of *Biquaternion Rotations and Lorentz Transformations*. The kernel of the representation is exactly the circle of central phases, $\ker = \{e^{i\theta}e_0\} = U(1)$, which is the kernel theorem of that article read as a statement about the homomorphism above; the same theorem states that $\{\pm e_0\}$ is the kernel on the unit-norm slice, and that the two-to-one map onto the Lorentz group is the double cover.

**Why the dagger and not the inverse.** The two-sided maps $x \mapsto AxB$ with $A, B$ invertible are the general maps built from an element on both sides, and the sandwich is the case $B = A^{\dagger}$ normalised. The reason is that the dagger, and not the inverse, is the involution matched to the two sectors: for $B = \lambda\tilde{Q}^{\dagger}$ with $\lambda$ real, and only then, the image of a Hermitian $x$ is again Hermitian, so $\mathbb{M}_+$ and $\mathbb{M}_-$ are preserved for every unit. With $\tilde{Q}^{-1}$ in place of $\tilde{Q}^{\dagger}$ the map is the inner automorphism, which is an algebra automorphism but which preserves the fixed spaces of the involution $\dagger$ conjugated by the image of the identity, $z \mapsto \tilde{Q}\tilde{Q}^{\dagger}z^{\dagger}(\tilde{Q}\tilde{Q}^{\dagger})^{-1}$, so a Hermitian element is carried out of $\mathbb{M}_+$ as soon as the operand is not unitary. The formal statement of which subspaces each of the two maps preserves, with the six-subspace table, is *Biquaternion Rotations and Lorentz Transformations*; the inner automorphism is *Biquaternion Automorphisms and Derivations*.

## The Invariants of the Operator

The element has the invariants of its matrix, $\det\Phi(\tilde{Q}) = N(\tilde{Q})$ and $\operatorname{Tr}\Phi(\tilde{Q}) = 2Q_0$, both complex. The operator has two invariants of its own, and both are real.

**Theorem (the invariants of the operator).** For every $\tilde{Q}$,

$$
\det \operatorname{H}_{\tilde{Q}} = \lvert N(\tilde{Q})\rvert^{4}, \qquad \operatorname{Tr}\operatorname{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2} ,
$$

both real and non-negative.

**Proof.** Under $\Phi$ the operator is the endomorphism $T(X) = M X M^{\dagger}$ of $M_2(\mathbb{C})$ with $M = \Phi(\tilde{Q})$. In the basis of matrix units $E_{ij}$ its entries are $T_{(ij),(kl)} = M_{ik}\bar{M}_{jl}$, so $T$ is the Kronecker product $M \otimes \bar{M}$: indeed $(M \otimes \bar M)_{(ij),(kl)} = M_{ik}\bar M_{jl}$. The trace of a Kronecker product is the product of the traces and its determinant is $\det(M \otimes \bar M) = (\det M)^{2}(\det \bar M)^{2}$; hence

$$
\operatorname{Tr} T = (\operatorname{Tr} M)(\operatorname{Tr}\bar{M}) = \lvert\operatorname{Tr} M\rvert^{2} = \lvert 2Q_0\rvert^{2} = 4\lvert Q_0\rvert^{2},
\qquad
\det T = \bigl(\det M \cdot \det \bar M\bigr)^{2} = \lvert N(\tilde{Q})\rvert^{4} ,
$$

using $\det M = N(\tilde{Q})$ and $\operatorname{Tr} M = 2Q_0$ of *The 2×2 Matrix Element Representation of Biquaternions*. Both are real and non-negative. $\square$

**Corollary (invertibility is the light cone condition).** $\operatorname{H}_{\tilde{Q}}$ is invertible exactly when $N(\tilde{Q}) \neq 0$, and the modulus of the operator determinant is $\lvert N(\tilde{Q})\rvert$, the modulus of the element determinant squared.

The two invariants show what the operator keeps and what it discards. It keeps the **modulus** of each invariant of the element and loses the argument, which is the numerical form of the blindness to the phase: a central phase changes $\Phi(\tilde{Q})$ and its determinant and does not change the operator at all. The trace has a physical reading. The scalar part $Q_0$ of the operand is its time coordinate, $ict$ for a material element and $ct'$ for an informational one, so

$$
\operatorname{Tr}\operatorname{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2}
$$

is four times the squared time coordinate of the operand: the trace of the operator is a clock reading, and it is the only element datum besides the modulus of the norm that survives. The determinant is a volume: it is the fourth power of the interval scale, matching the fourth power of the scale by which the interval of an element is multiplied, and it is the statement that the sandwich is a similarity of the algebra and not an isometry off the unit-norm slice.

## The Two Regimes: the Rank and the Collapse

The sandwich is defined for **every** element, zero divisors included, because it is only a product. What changes on the light cone is not its existence but its size.

**Theorem (the rank of the operator).** For every $\tilde{Q}$,

$$
\operatorname{rank} \operatorname{H}_{\tilde{Q}} = \bigl(\operatorname{rank}\Phi(\tilde{Q})\bigr)^{2} .
$$

Consequently

$$
\operatorname{rank}\operatorname{H}_{\tilde{Q}} = \begin{cases} 4, & N(\tilde{Q}) \neq 0, \\ 1, & N(\tilde{Q}) = 0,\ \tilde{Q} \neq 0, \\ 0, & \tilde{Q} = 0 . \end{cases}
$$

**Proof.** Write the singular value decomposition $\Phi(\tilde{Q}) = P\Sigma V^{\dagger}$ with $P, V$ unitary and $\Sigma = \mathrm{diag}(\sigma_1,\sigma_2)$, $\sigma_j \geq 0$. On the matrix side the operator is $X \mapsto P\Sigma (V^{\dagger}XV)\Sigma P^{\dagger}$. As $X$ runs over $M_2(\mathbb{C})$ so does $V^{\dagger}XV$, and $\Sigma Y \Sigma$ has entries $\sigma_i\sigma_j Y_{ij}$, so the set $\{\Sigma Y\Sigma\}$ is exactly the coordinate subspace spanned by the matrix units $E_{ij}$ with $\sigma_i\sigma_j \neq 0$, of complex dimension $(\#\{j : \sigma_j \neq 0\})^{2}$. Conjugation by the fixed invertible $P$ is an isomorphism of vector spaces and does not change the dimension. The number of nonzero singular values is the rank of $\Phi(\tilde{Q})$, which is $2$ for $N \neq 0$, $1$ for a nonzero zero divisor, and $0$ only for $\tilde{Q} = 0$. $\square$

The two regimes are therefore the following, and they are as different as they can be.

**Outside the light cone, $N(\tilde{Q}) \neq 0$.** The operator is invertible, in $GL(4,\mathbb{C})$, of rank four: it preserves the rank of every argument and is an isomorphism of the algebra onto itself, with the invariants displayed above. Physically it is an observer transformation together with a change of units, the unit change being the dilatation $r^{2} = \lvert N(\tilde{Q})\rvert$ by which the operator is rescaled.

**On the cone, $N(\tilde{Q}) = 0$ and $\tilde{Q} \neq 0$.** The operator has rank **one**: it annihilates a three-dimensional subspace and maps the whole eight-dimensional algebra onto a single complex line. That line is not arbitrary. Writing $\Phi(\tilde{Q}) = p\,\sigma\,v^{\dagger}$ with $p$ the left singular vector of the unique nonzero singular value, the image of the operator is

$$
\operatorname{im}\operatorname{H}_{\tilde{Q}} = \mathbb{C}\cdot p\,p^{\dagger},
$$

the line spanned by a rank-one **Hermitian** matrix, that is, by a minimal idempotent of the algebra. In the algebra itself the generator of that line is the element $\tfrac12(e_0 + i\mathbf{n}\cdot\mathbf{e})$ for a unit vector $\mathbf{n}$ determined by $\tilde{Q}$ — Hermitian, idempotent, of norm zero (*Biquaternion Ideals and Peirce Decomposition*).

**Theorem (the square of a null operator).** If $N(\tilde{Q}) = 0$ then

$$
\operatorname{H}_{\tilde{Q}} \circ \operatorname{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2}\,\operatorname{H}_{\tilde{Q}} .
$$

**Proof.** The operator has rank one, so on its image it acts as a single scalar, and that scalar is its trace; the trace is $4\lvert Q_0\rvert^{2}$ by the theorem above. $\square$

The scalar is zero exactly when the scalar part of $\tilde{Q}$ vanishes, and then the operator is **nilpotent**: $\operatorname{H}_{\tilde{Q}} \circ \operatorname{H}_{\tilde{Q}} = 0$, so applying a null operator twice gives zero. When the scalar part does not vanish the operator is a **scaled projection**, and normalising $\tilde{Q}$ makes it a projection. The two cases are distinguished by the single number $Q_0$, and both occur inside the same cone.

A worked case fixes the picture. Take $\tilde{Q} = e_1 + ie_2$, of norm $1 + i^{2} = 0$ and with $Q_0 = 0$. Then

$$
\Phi(\tilde{Q}) = \begin{pmatrix} 0 & -2i \\ 0 & 0 \end{pmatrix}, \qquad
\begin{aligned}
e_0 &\mapsto 2e_0 + 2ie_3, \\
e_1 &\mapsto 0, \\
e_2 &\mapsto 0, \\
e_3 &\mapsto 2ie_0 - 2e_3,
\end{aligned}
$$

so that every image is a multiple of the idempotent $\tfrac12(e_0 + ie_3)$ and the second application gives zero. The same computation can be carried out in every coordinate system the algebra admits, and the coordinates always show the two coefficients $x^0 + ix^3$ surviving and the other two disappearing.

**Physical reading of the collapse.** Off the light cone the operand is a legitimate frame change and the operator is invertible. On the light cone the operand is a null direction and the operator it produces is singular: it can create nothing but a single lightlike Hermitian line, so a null element does not generate a motion. This is the operator form of the identification of the light cone with the zero-divisor locus of the algebra, whose causal use is *Biquaternion Rotations and Lorentz Transformations*.

## The Coordinate Systems of the Operator

The operator is one map, and it can be written in every coordinate system the algebra carries. In the four coefficients it is a component rule, quadratic in the operand and linear in the argument, and its action on the identity already exhibits the non-commutativity of the quaternion part. In the coefficient column it is a matrix, and then it has the determinant, the trace and the spectrum read above, and the product of the two regular maps that produces it shows why it is a congruence rather than a similarity. In the matrix algebra it is a congruence of $M_2(\mathbb{C})$, where the rank theorem becomes a statement about the rank of one matrix. On the simple module it is the operator version of the polar word, and then it has a twist and a domain. The four writings are taken up in turn by the other articles of this section, and each is the same operator.

Two cautions follow from the laws above. First, the **operator group and the element group are not the same group**: the element group acts by multiplication on a module, the operator group by congruence on the algebra, and the operator action loses the phase circle while the element action loses nothing. Second, the operator is **quadratic in the operand**: doubling $\tilde{Q}$ quadruples the operator, and it is the reason the sandwich doubles the boost and the rotation parameters of the polar word.

## Summary

An element of $\mathbb{B}$ can be used as an element or as an operator, and the corpus separates the two. The operator of $\tilde{Q}$ is the Hermitian sandwich $\operatorname{H}_{\tilde{Q}}(x) = \tilde{Q}x\tilde{Q}^{\dagger}$, whose definition, carrier, kernel, six-subspace table, Lorentz reading, boost and rotation operators, doubling of the parameters and polar dictionary belong to *Biquaternion Rotations and Lorentz Transformations* and to *The Sandwich Action in Subspaces*, and are cited here rather than restated.

This article owns the sandwich as a linear map, and three things follow. It composes, $\operatorname{H}_{\tilde{Q}\tilde{R}} = \operatorname{H}_{\tilde{Q}} \circ \operatorname{H}_{\tilde{R}}$, so it is a representation of the monoid of the algebra and of the group of units; it is homogeneous of degree two in the centre, $\operatorname{H}_{z\tilde{Q}} = \lvert z\rvert^{2}\operatorname{H}_{\tilde{Q}}$, so it is blind to the scalar imaginary and its kernel is the circle of central phases; and the dagger, and not the inverse, is the second factor because it is the involution matched to the two Hermitian sectors, the inner automorphism preserving instead the fixed spaces of the involution conjugated by the image of the identity.

The operator has two invariants of its own, both real and non-negative: $\det\operatorname{H}_{\tilde{Q}} = \lvert N(\tilde{Q})\rvert^{4}$ and $\operatorname{Tr}\operatorname{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2}$, obtained as the determinant and the trace of the Kronecker product $\Phi(\tilde{Q}) \otimes \overline{\Phi(\tilde{Q})}$. The element keeps the modulus of each of its own invariants and loses the argument, which is the blindness to the phase in numerical form; the trace is four times the squared time coordinate of the operand, and the determinant is the fourth power of the interval scale. The two regimes are separated by the light cone, and the separator is the rank: the rank of the operator is the square of the rank of the matrix of the element, so it is four outside the cone, one for every nonzero zero divisor and zero only at the origin. Outside the cone the operator is an invertible congruence; on the cone it collapses the algebra onto the line of a minimal idempotent and satisfies $\operatorname{H}_{\tilde{Q}} \circ \operatorname{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2}\operatorname{H}_{\tilde{Q}}$, so it is nilpotent when the scalar part of the operand vanishes and a scaled projection when it does not. The same operator is written in the coefficients, in the coefficient column, in the matrix algebra and on the module, and what differs between those writings is the coordinate system and with it the part of the operator that becomes visible.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, basis $e_0,e_1,e_2,e_3$ |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | general element; the operand of the operator |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2 = \det\Phi(\tilde{Q})$ | biquaternion norm |
| $\dagger$ | quaternion conjugation composed with complex conjugation |
| $\mathbb{M}_+, \mathbb{M}_-$ | informational and material sectors, the fixed spaces of $\dagger$ |
| $\operatorname{H}_{\tilde{Q}}(x) = \tilde{Q}x\tilde{Q}^{\dagger}$ | the Hermitian sandwich, the operator of $\tilde{Q}$ |
| $\operatorname{H}_{\tilde{Q}\tilde{R}} = \operatorname{H}_{\tilde{Q}}\circ\operatorname{H}_{\tilde{R}}$ | composition law; the operator is a representation |
| $\operatorname{H}_{z\tilde{Q}} = \lvert z\rvert^{2}\operatorname{H}_{\tilde{Q}}$, $z$ central | central rule; $\operatorname{H}_{i\tilde{Q}} = \operatorname{H}_{\tilde{Q}}$ |
| $\ker = \{e^{i\theta}e_0\} = U(1)$ | kernel of the representation: the central phases |
| $\Phi(\tilde{Q}) \otimes \overline{\Phi(\tilde{Q})}$ | Kronecker form of the operator on $M_2(\mathbb{C})$ |
| $\det\operatorname{H}_{\tilde{Q}} = \lvert N(\tilde{Q})\rvert^{4}$ | determinant of the operator; nonzero exactly off the cone |
| $\operatorname{Tr}\operatorname{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2}$ | trace of the operator; four times the squared time coordinate |
| $\operatorname{rank}\operatorname{H}_{\tilde{Q}} = (\operatorname{rank}\Phi(\tilde{Q}))^{2}$ | rank of the operator: $4$, $1$ or $0$ |
| $\operatorname{im}\operatorname{H}_{\tilde{Q}} = \mathbb{C}\cdot pp^{\dagger}$, $N(\tilde{Q}) = 0$ | the null collapse: one Hermitian line |
| $\operatorname{H}_{\tilde{Q}}\circ\operatorname{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2}\operatorname{H}_{\tilde{Q}}$, $N = 0$ | nilpotent if $Q_0 = 0$, scaled projection otherwise |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for versors, the sandwich action, and the difference between the conjugation and the dagger form.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for rotors, the sandwich by a versor, and the doubling of the half-angle.
- I. M. Gel'fand, R. A. Minlos, and Z. Ya. Shapiro, *Representations of the Rotation and Lorentz Groups and Their Applications* (Pergamon, 1963), for the Lorentz action on the algebra and the double cover.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2nd ed. 2013), for the singular value decomposition, the rank of a congruence, and the eigenvalue products $\lambda_i\bar{\lambda}_j$ of the map $X \mapsto MXM^{\dagger}$.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for group actions by linear maps, kernels and quotient groups.
