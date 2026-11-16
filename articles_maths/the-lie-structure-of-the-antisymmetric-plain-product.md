# __The Lie Structure of the Antisymmetric Plain Product__

## Introduction

The antisymmetrisation of the plain product is $\tilde Q_1\wedge\tilde Q_2=\tfrac12(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1)$, and its value is the cross product of the two vector parts, with no scalar part and no mixed part. It is the only one of the four brackets of the batch that satisfies the Jacobi identity on the whole algebra, and the only one whose exponential is an automorphism. The algebra it defines is $\mathfrak{so}(3,\mathbb{C})\oplus\mathbb{C}$: the vector subspace with the cross product, and the scalar line as a centre.

This article reads the Lie structure of that bracket: the antisymmetrisation and its coordinate rule, the Jacobi identity and its proof, the defect, which is empty, the bracket table on the basis, the ideals and the radical, the Killing form and its radical, the exponential and the versors, the rotor and its action, and the row of the bracket in the comparison of the four.

The setting is [The General Plain Bilinear Product](the-general-plain-bilinear-product.html), whose second half is this product, and [The Jordan Structure of the Symmetric Plain Product](the-jordan-structure-of-the-symmetric-plain-product.html), which reads the first half. The general theory is [Lie Algebras](lie-algebras-a-general-introduction.html), and the rotations are The Lie Algebra of the Antisymmetric Plain Algebra of the Biquaternions.

## The Antisymmetrisation

**Definition.** The **antisymmetric plain product** is
$$
\tilde Q_1\wedge\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1\bigr).
$$

**Theorem (the product is the cross product).** For all $\tilde Q_1,\tilde Q_2$,
$$
\boxed{\;\tilde Q_1\wedge\tilde Q_2=\vec Q_1\times\vec Q_2\;}
$$

*Proof.* In the plain product the scalar row $Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)$ is symmetric and the mixed rows $Q_{1t}\vec Q_2+Q_{2t}\vec Q_1$ are symmetric, so both cancel; the cross term $\vec Q_1\times\vec Q_2$ is antisymmetric and is doubled. Verified exactly on the sixteen pairs of the basis and on general elements.

**Corollary (the elementary properties).** The bracket is alternating, $\tilde Q\wedge\tilde Q=0$; it kills the scalar part on both sides, $\tilde Q_1\wedge e_t=e_t\wedge\tilde Q_2=0$; its image is the vector subspace, of complex dimension $3$; and it depends only on the vector parts.

*Proof.* The three items are read from the display. The image is spanned by $\vec e_x\wedge\vec e_y=\vec e_z$ and its cyclic companions.

**Remark (the bracket is a commutator).** The bracket is the commutator of the plain product, which is associative. That single fact decides the whole article: a commutator in an associative algebra satisfies the Jacobi identity, its adjoint maps are derivations of the bracket, and its exponential is an automorphism. The three theorems below are the three faces of that fact.

## The Jacobi Identity

**Theorem (the identity holds).** For all $\tilde Q_1,\tilde Q_2,\tilde Q_3$,
$$
\boxed{\;\bigl[\tilde Q_1,\tilde Q_2\bigr]\wedge\tilde Q_3+\bigl[\tilde Q_2,\tilde Q_3\bigr]\wedge\tilde Q_1+\bigl[\tilde Q_3,\tilde Q_1\bigr]\wedge\tilde Q_2=0\;}
$$

*Proof.* Write the bracket as $\tfrac12[\ ,\ ]$ with the commutator of the associative product. Then
$$
4\,J(\tilde Q_1,\tilde Q_2,\tilde Q_3)=\bigl[\bigl[\tilde Q_1,\tilde Q_2\bigr],\tilde Q_3\bigr]+\bigl[\bigl[\tilde Q_2,\tilde Q_3\bigr],\tilde Q_1\bigr]+\bigl[\bigl[\tilde Q_3,\tilde Q_1\bigr],\tilde Q_2\bigr],
$$
and the sum of the three iterated commutators vanishes identically in an associative algebra, because each of the twelve words appears twice with opposite signs. Verified on all sixty-four triples of the basis and on two thousand random complex triples, with a maximal deviation of zero.

**Corollary (the adjoint maps are derivations).** For every $\tilde Q_1$ the map $\operatorname{ad}\tilde Q_1\colon\tilde Q\mapsto\tilde Q_1\wedge\tilde Q$ is a derivation of the bracket:
$$
\tilde Q_1\wedge\bigl(\tilde Q_2\wedge\tilde Q_3\bigr)=\bigl(\tilde Q_1\wedge\tilde Q_2\bigr)\wedge\tilde Q_3+\tilde Q_2\wedge\bigl(\tilde Q_1\wedge\tilde Q_3\bigr).
$$

*Proof.* The Jacobi identity rearranged, using the alternation. Verified on general elements.

**Remark (the two readings on the vector subspace).** On $\mathbb{B}_V$ the bracket is the cross product, which is the Lie bracket of $\mathfrak{so}(3,\mathbb{C})$ under the identification of $\mathbb{C}^3$ with its adjoint representation. The identity therefore holds there for the structural reason, and it holds on the whole algebra because the scalar line is a centre: the only terms that could break it are the mixed ones, and there are none.

## The Defect

**Proposition (the defect is empty).** The span of the values of the Jacobi defect
$$
J(\tilde Q_1,\tilde Q_2,\tilde Q_3)=\bigl[\tilde Q_1,\tilde Q_2\bigr]\wedge\tilde Q_3+\bigl[\tilde Q_2,\tilde Q_3\bigr]\wedge\tilde Q_1+\bigl[\tilde Q_3,\tilde Q_1\bigr]\wedge\tilde Q_2
$$
is $\{0\}$, of dimension zero.

*Proof.* The identity of the previous section. Evaluated on the complex basis $\{e_\mu,ie_\mu\}$ and on random complex triples, the maximal value is zero and no direction is produced.

**Remark (the defect of the four brackets).** The four brackets have defects $0,3,3,3$ in the order plain, quaternionic, plain sesquilinear, quaternionic sesquilinear. This bracket is the zero of the row, and the three nonzero values measure the failure of the two conjugations when they are placed in a slot of a bracket. There is no defect here because there is no conjugation here.

**Remark (what the zero defect does and does not give).** The vanishing of the defect makes the bracket a Lie bracket; it does not make the algebra semisimple, because the scalar line is a centre. The two properties are independent, and the algebra of this article has the first without the second. The semisimple part is the vector subspace, and its structure is read in the next two sections.

## The Bracket on the Basis

**Proposition (the table).** In the coefficient basis the only nonzero brackets are
$$
[\vec e_x,\vec e_y]=\vec e_z,\qquad [\vec e_y,\vec e_z]=\vec e_x,\qquad [\vec e_z,\vec e_x]=\vec e_y,
$$
and their negatives; every bracket with $e_t$ vanishes.

*Proof.* $\vec e_x\vec e_y=\vec e_z$ and $\vec e_y\vec e_x=-\vec e_z$, so the half-difference is $\vec e_z$. The two cyclic companions are computed the same way, and $e_t$ commutes with everything in the plain product. Computed exactly.

| $\wedge$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $0$ | $0$ | $0$ | $0$ |
| $\vec e_x$ | $0$ | $0$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $0$ | $-\vec e_z$ | $0$ | $\vec e_x$ |
| $\vec e_z$ | $0$ | $\vec e_y$ | $-\vec e_x$ | $0$ |

**Corollary (the first row and column).** The element $e_t$ is central, so the table has a zero row and a zero column, and the bracket is the direct sum of the zero bracket on $\mathbb{C}e_t$ and the cross product on $\mathbb{B}_V$.

**Remark (the structure constants).** The structure constants are the Levi-Civita symbol, $c_{jk}^{i}=\varepsilon_{ijk}$, and they are the same as those of $\mathfrak{so}(3,\mathbb{C})$. The complexification does not change them: the bracket is $\mathbb{C}$-bilinear and the constants are real, so the algebra is the complexification of the real Lie algebra of rotations.

## The Ideals and the Radical

**Theorem (the ideals are the three).** The ideals of the algebra are $0$, the vector subspace $\mathbb{B}_V$ and $\mathbb{B}$.

*Proof.* $\mathbb{B}_V$ is closed under the bracket because the bracket of two vectors is a vector and the bracket with $e_t$ is zero. If an ideal contains an element with nonzero scalar part, it contains $e_t$ up to a vector, hence by subtracting a vector it contains $e_t$, and then it contains $\mathbb{B}_V$ by the table; so it is everything. An ideal contained in $\mathbb{B}_V$ that is nonzero contains some $\vec u$, and then contains $\vec e_x\wedge\vec u$, $\vec e_y\wedge\vec u$, $\vec e_z\wedge\vec u$; for $\vec u=\vec e_x$ these span $\mathbb{B}_V$. Verified by computing the invariant subspaces of the adjoint action.

**Corollary (the algebra is reductive).** The algebra is the direct sum of the simple algebra $\mathbb{B}_V$ and the abelian algebra $\mathbb{C}e_t$, and its radical is $\mathbb{C}e_t$.

*Proof.* The two summands are ideals, they commute, and $\mathbb{B}_V$ is simple by the theorem. The radical is the maximal solvable ideal, which is the abelian summand.

**Remark (the radical is the centre).** Here the radical and the centre coincide, both being the scalar line. That coincidence is not general: the other three brackets have no centre at all for two of them, and a centre that is not a radical for the remaining one. The four cases are compared in the last section.

## The Killing Form

**Definition.** $\kappa(\tilde Q_1,\tilde Q_2)=\operatorname{tr}\bigl(\operatorname{ad}\tilde Q_1\circ\operatorname{ad}\tilde Q_2\bigr)$.

**Theorem (the form in the coefficient basis).** The matrix of $\kappa$ is
$$
\kappa=-\!2\bigl(Q_{1x}Q_{2x}+Q_{1y}Q_{2y}+Q_{1z}Q_{2z}\bigr),
$$
that is $\operatorname{diag}(0,-2,-2,-2)$ in the coefficient basis, with radical the scalar line.

*Proof.* $\operatorname{ad}\vec e_x$ kills $e_t$ and acts on $\mathbb{B}_V$ by $\vec v\mapsto\vec e_x\times\vec v$, whose matrix in the basis $(\vec e_y,\vec e_z)$ is $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$; its square is $-1$ on that plane and $0$ on the line, so the trace of the square is $-2$. The three vector units give the same value and the mixed traces vanish by the cyclic companions. Computed exactly.

**Corollary (the form is invariant).** $\kappa(\tilde Q_1\wedge\tilde Q_2,\tilde Q_3)+\kappa(\tilde Q_2,\tilde Q_1\wedge\tilde Q_3)=0$ for all arguments.

*Proof.* The invariance of the Killing form of a Lie algebra, which follows from the Jacobi identity; verified numerically with a deviation of zero on general elements. It is the property that fails for the three other brackets, and its failure there is one more face of the failure of the Jacobi identity.

**Remark (the form is negative definite on the compact real form).** The restriction of $\kappa$ to $\mathbb{B}_V$ is $-2$ times the Euclidean form, so on the real vector subspace it is negative definite: the algebra $\mathbb{B}_V$ is the complexification of a compact Lie algebra, and its real form is $\mathfrak{so}(3)$. The sign is the one of the compact form, and it is the reason the exponential below is a rotation rather than a boost.

## The Exponential and the Versors

**Theorem (the exponential of the adjoint is an automorphism).** For every $\tilde Q$ and every $t$, the map $\exp(t\operatorname{ad}\tilde Q)$ is an automorphism of the bracket.

*Proof.* For a commutator bracket in an associative algebra, $\exp(t\operatorname{ad}\tilde Q)$ is the conjugation by $\exp(t\tilde Q)$ in the associative algebra, and a conjugation is an automorphism. The identity was verified numerically by summing the exponential series and comparing $\exp(t\operatorname{ad}\tilde Q)(\tilde Q_2\wedge\tilde Q_3)$ with the bracket of the images, for several random $\tilde Q$ and $t$.

**Proposition (the one-parameter group of a vector unit).** With $\tilde Q=\vec e_x$,
$$
\exp\bigl(t\operatorname{ad}\vec e_x\bigr)\vec e_y=\cos t\,\vec e_y+\sin t\,\vec e_z,\qquad
\exp\bigl(t\operatorname{ad}\vec e_x\bigr)\vec e_z=-\sin t\,\vec e_y+\cos t\,\vec e_z,
$$
and $e_t$ is fixed.

*Proof.* The matrix of $\operatorname{ad}\vec e_x$ on the plane of $\vec e_y,\vec e_z$ is $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, whose exponential is the rotation matrix of angle $t$. Verified numerically, and the series converges in two terms modulo the trigonometric identity.

**Definition (the versors).** A **versor** is an element $\tilde U$ with $N(\tilde U)=1$, where $N$ is the norm $N(\tilde Q)=\sum_\mu Q_\mu^2$. For such an element $\tilde U^{\natural}=\tilde U^{-1}$, since $\tilde U\tilde U^{\natural}=N(\tilde U)e_t=e_t$.

**Theorem (the versors act by automorphisms).** For every versor $\tilde U$ the map $\Phi_{\tilde U}\colon\tilde Q\mapsto\tilde U\tilde Q\tilde U^{\natural}$ is an automorphism of the algebra and therefore of the bracket, and the map $\tilde U\mapsto\Phi_{\tilde U}$ is a homomorphism whose kernel is $\{\pm e_t\}$.

*Proof.* $\Phi_{\tilde U}$ is the conjugation by an invertible element, so it preserves the product; the kernel is computed as in the classical theory of the quaternion units. Verified numerically on random versors and random pairs, with a deviation of zero for the product and for the bracket.

**Remark (the group).** The versors form the group $\mathrm{SL}(2,\mathbb{C})$, of complex dimension three, and the automorphism group of the bracket that they generate is $\mathrm{SO}(3,\mathbb{C})$, the group of the linear maps of $\mathbb{B}_V$ preserving the cross product and the Euclidean form. The map is two-to-one, and it is the classical spin cover of the rotation group, read over $\mathbb{C}$.

## The Rotor

**Definition.** The **rotor** of angle $\theta$ about the unit vector $\vec n\in\mathbb{B}_V$ is
$$
\tilde R=\cos\tfrac{\theta}{2}\,e_t+\sin\tfrac{\theta}{2}\,\vec n,\qquad N(\tilde R)=\cos^2\tfrac{\theta}{2}+\sin^2\tfrac{\theta}{2}=1 .
$$

**Theorem (the rotor rotates).** For every $\vec v\in\mathbb{B}_V$,
$$
\tilde R\,\vec v\,\tilde R^{\natural}=\cos\theta\,\vec v+\sin\theta\,(\vec n\times\vec v)+\bigl(1-\cos\theta\bigr)(\vec n,\vec v)\vec n ,
$$
the rotation of $\vec v$ about $\vec n$ through the angle $\theta$.

*Proof.* Expand $\tilde R\vec v\tilde R^{\natural}$ with $\tilde R^{\natural}=\cos\tfrac{\theta}{2}-\sin\tfrac{\theta}{2}\vec n$ and use $\vec n\vec v=-\bigl(\vec n,\vec v\bigr)+\vec n\times\vec v$ twice; the terms pair into the Rodrigues formula. Verified numerically: $\vec e_z$ about $\vec e_y$ through $0.7$ gives $\cos(0.7)\vec e_z+\sin(0.7)\vec e_x$, and $\vec e_x$ gives $\cos(0.7)\vec e_x-\sin(0.7)\vec e_z$, both to machine precision.

**Remark (the half angle and the double cover).** The rotor carries the half angle and the action carries the full angle, which is the local form of the two-to-one cover: $\tilde R$ and $-\tilde R$ give the same rotation, and the rotation group is recovered only up to sign. The rotor is the versor of the previous section written in the trigonometric parametrisation, and the composition of rotations is the product of rotors.

**Remark (the rotor and the bracket).** The rotor is the exponential of the bracket: $\tilde R=\exp\bigl(\tfrac{\theta}{2}\vec n\bigr)$ in the algebra, and the derivative at $\theta=0$ of the action is $\operatorname{ad}\vec n$. The bracket is therefore the infinitesimal rotation, the rotor is its integrated form, and the exponential theorem of the previous section is the statement that the two agree. The versor group acts on the algebra by automorphisms and the bracket is the derivative of that action at the identity.

## The Place among the Four

| | this bracket | $\wedge_{\natural}$ | $\wedge_{*}$ | $\wedge_{\natural*}$ |
|---|---|---|---|---|
| value on $\mathbb{B}_V$ | $\vec X\times\vec Y$ | $-\vec X\times\vec Y$ | $-\vec X\times\vec Y$ | $\vec X\times\overline{\vec Y}$ |
| mixed part | none | $Q_{1t}\vec Q_2-Q_{2t}\vec Q_1$ | $-Q_{1t}\overline{\vec Q_2}+\overline{Q_{2t}}\vec Q_1$ | none |
| Jacobi | holds | fails, defect $3$ | fails, defect $3$ | fails, defect $3$ |
| centre | $\mathbb{C}e_t$ | $0$ | $0$ | $\mathbb{C}e_t$ |
| Killing form | $\operatorname{diag}(0,-2,-2,-2)$ | $\operatorname{diag}(3,-2,-2,-2)$ | $\operatorname{diag}(3,-2,-2,-2)$ | $\operatorname{diag}(0,-2,-2,-2)$ |
| invariant form | yes | no | no | no |
| $\exp(\operatorname{ad})$ automorphism | yes | no | no | no |

**Remark (the column that is a Lie algebra).** This is the only column of the batch that is a Lie algebra, the only one with an invariant trace form, and the only one whose exponential is an automorphism. The three properties are one property, and it is the property of being a commutator in an associative algebra. The three other columns agree with this one on the real vector subspace, up to sign; the two with a mixed part fail already there, and the sesquilinear quaternionic one fails only off it.

## Summary

The antisymmetric plain product is $\tilde Q_1\wedge\tilde Q_2=\vec Q_1\times\vec Q_2$, the commutator of the plain product, with image the vector subspace, zero scalar part, and zero mixed part.

It satisfies the Jacobi identity, with a defect of dimension zero, because it is a commutator in an associative algebra. The algebra is $\mathfrak{so}(3,\mathbb{C})\oplus\mathbb{C}$: the vector subspace with the cross product and the scalar line as a centre. The ideals are $0$, $\mathbb{B}_V$ and $\mathbb{B}$, and the radical is the scalar line.

The Killing form is $\operatorname{diag}(0,-2,-2,-2)$, invariant, of radical the scalar line, negative definite on the real vector subspace. The exponential $\exp(t\operatorname{ad}\tilde Q)$ is an automorphism for every $\tilde Q$ and $t$, the versors of norm one act by $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{\natural}$ and form $\mathrm{SL}(2,\mathbb{C})$ covering $\mathrm{SO}(3,\mathbb{C})$ two-to-one, and the rotor $\cos\tfrac{\theta}{2}+\sin\tfrac{\theta}{2}\vec n$ acts by the rotation of angle $\theta$ about $\vec n$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $\tilde Q=Q_te_t+\vec Q$ | the element, its scalar part and its vector part |
| $\tilde Q_1\wedge\tilde Q_2$ | the antisymmetric plain product |
| $[\ ,\ ]$ | the bracket $\tilde Q_1\wedge\tilde Q_2$ |
| $\operatorname{ad}\tilde Q$ | the map $\tilde Q_2\mapsto\tilde Q_1\wedge\tilde Q_2$ |
| $\kappa$ | the Killing form |
| $N(\tilde Q)=\sum_\mu Q_\mu^2$ | the norm |
| $\tilde U$ versor | an element with $N(\tilde U)=1$ |
| $\tilde R$ rotor | $\cos\tfrac{\theta}{2}e_t+\sin\tfrac{\theta}{2}\vec n$ |
| $\mathbb{B}_V$ | the vector subspace |
| $\mathfrak{so}(3,\mathbb{C})$ | the simple part of the algebra |

## Further Reading

- [The General Plain Bilinear Product](the-general-plain-bilinear-product.html), for the product of which this is the antisymmetrisation.
- [The Jordan Structure of the Symmetric Plain Product](the-jordan-structure-of-the-symmetric-plain-product.html), for the other half of the same product.
- [The Lie Structure of the Antisymmetric Quaternionic Product](the-lie-structure-of-the-antisymmetric-quaternionic-product.html), for the companion bracket with a defect.
- [Lie Algebras](lie-algebras-a-general-introduction.html), for the Jacobi identity, the Killing form and the exponential in general.
- [Biquaternion Lie Group and Exponential Structure](biquaternion-lie-group-and-exponential-structure.html), for the exponential and the spin cover.
