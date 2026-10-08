# __The Lie Algebra of the Antisymmetric Plain Algebra__

## Introduction

The antisymmetric part of the plain product of the biquaternions, introduced in *Introduction to the Antisymmetric Plain Algebra of Biquaternions*,

$$
\tilde P\wedge\tilde Q=\tfrac12\bigl(\tilde P\tilde Q-\tilde Q\tilde P\bigr)=\mathbf{P}\times\mathbf{Q},
$$

is $\mathbb{C}$-bilinear, alternating and satisfies the Jacobi identity, so it makes the underlying complex space $\mathbb{B}$ a Lie algebra, written

$$
\mathfrak{g}=\bigl(\mathbb{B},\wedge\bigr),
$$

of complex dimension four and real dimension eight. This article develops the structure of that Lie algebra: its centre, which is the centre $\mathbb{C}_{\mathbb{B}}$ of the biquaternion algebra, and the quotient by it; its derived algebra $\mathrm{Vect}(\mathbb{B})$, stable under the bracket, of complex dimension three and real dimension six; the identifications of that derived algebra with the cross-product algebra of $\mathbb{C}^3$ and with $\mathfrak{sl}(2,\mathbb{C})$; the readings of the quaternion subspace and the anti-Hermitian subspace on the real forms, carrying $\mathbb{R}e_0\oplus\mathfrak{su}(2)$ and $\mathfrak{u}(2)$; the derived series, the readings of solvability, nilpotency and simplicity; the ideals and the quotients; and the enveloping algebra.

The bracket and its Jacobi identity are established in *Introduction to the Antisymmetric Plain Algebra of Biquaternions* and are used here, not reproved. The general theory of Lie algebras, of their ideals, of their solvable and nilpotent series, of simplicity and of the enveloping algebra is *Lie Algebras* and *Structure of Lie Algebras*; the associativity of the plain product, from which the Jacobi identity descends, is *Associative Algebras* and *The Commutator Operator*; the six distinguished subspaces and their names are *Introduction to the Six Subspaces*, and their readings under the four products are *The Six Subspaces and the Four Complex Products*; the skew-Hermitian elements and the group of linear maps preserving their form are *The Unitary Lie Algebra*; and the splitting of the plain product into the two halves is *The Symmetric and Antisymmetric Parts of an Algebra Product*. The article reads the Lie algebra as a module over $\mathbb{C}$ with an alternating bracket, and no group, no exponential and no space enters.

## The Centre and the Quotient

### The Centre of the Bracket

**Definition.** The **centre** of $\mathfrak{g}$ is

$$
\mathfrak{z}(\mathfrak{g})=\{\tilde P\in\mathbb{B}:\tilde P\wedge\tilde X=0\text{ for all }\tilde X\in\mathbb{B}\}.
$$

**Theorem (the centre is the centre of the algebra).** For $\tilde P\in\mathbb{B}$ the following are equivalent: $\tilde P$ lies in $\mathfrak{z}(\mathfrak{g})$; its vector part is zero, $\mathbf{P}=0$; and $\tilde P$ lies in $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$, the centre of the biquaternion algebra. Hence

$$
\mathfrak{z}(\mathfrak{g})=\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0,
$$

of complex dimension one and real dimension two.

*Proof.* The bracket depends only on the vector parts, $\tilde P\wedge\tilde X=\mathbf{P}\times\mathbf{X}$, so it vanishes for every $\tilde X$ exactly when $\mathbf{P}\times\mathbf{X}=0$ for every vector $\mathbf{X}$. If $\mathbf{P}\neq0$, a vector $\mathbf{X}$ that is not parallel to $\mathbf{P}$ gives a nonzero cross product, so the condition forces $\mathbf{P}=0$; conversely $\mathbf{P}=0$ gives $\tilde P\in\mathbb{C}e_0$. The centre of the biquaternion algebra is $\mathbb{C}e_0$, the complex multiples of the unit, because the quaternion units anticommute off the scalar direction; the second equivalence is that standard fact. Verified: the operator $\tilde X\mapsto\tilde P\wedge\tilde X$ has rank zero exactly for the central elements and rank two otherwise. $\square$

**Remark.** The centre of the bracket and the centre of the algebra are therefore the same subspace, and it is the first structural coincidence of the block: **the elements the bracket cannot see are exactly the central elements of the multiplication, the complex multiples of $e_0$.** The centre is abelian under the bracket, and it is annihilated by the adjoint of every element.

### The Quotient

**Proposition.** The bracket induced on the quotient $\mathbb{B}/\mathbb{C}_{\mathbb{B}}$ is the cross product, and the projection $\mathbb{B}\to\mathbb{B}/\mathbb{C}_{\mathbb{B}}$ is a morphism of Lie algebras with kernel the centre.

*Proof.* The bracket of two cosets is well defined because the bracket vanishes on the centre in each slot; the representatives differ from one another by central elements and the bracket of a central element with anything is zero. The quotient is identified with the vector space of the vector parts, on which the induced bracket is the cross product. $\square$

**Remark (the bracket is the direct sum of a trivial centre and the vector part).** The centre and the vector subspace are complementary, $\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B})$, and the bracket never leaves the vector subspace. Hence $\mathfrak{g}$ is the direct sum of Lie algebras

$$
\mathfrak{g}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B}),
$$

the first an abelian Lie algebra of complex dimension one and the second the cross-product algebra of complex dimension three. **The bracket is a cross product on the vector part, and the scalar direction is a central summand.**

## The Derived Algebra and the Identifications

### The Vector Subspace is the Derived Algebra

**Theorem.** The image of the bracket is the vector subspace, and it is the derived algebra of $\mathfrak{g}$:

$$
[\mathfrak{g},\mathfrak{g}]=\mathrm{Vect}(\mathbb{B})=\mathbb{C}e_1\oplus\mathbb{C}e_2\oplus\mathbb{C}e_3,
$$

of complex dimension three and real dimension six; the bracket restricted to it is again the cross product, so $[\mathfrak{g},\mathfrak{g}]$ is stable under the bracket and is a Lie subalgebra of $\mathfrak{g}$.

*Proof.* Every value of the bracket has scalar part zero, by the scalar-part computation of *Introduction to the Antisymmetric Plain Algebra of Biquaternions*, so the image lies in the vector subspace; conversely $e_1\wedge e_2=e_3$, $e_2\wedge e_3=e_1$ and $e_3\wedge e_1=e_2$ generate the vector subspace, so the image and the derived algebra are equal to it. The bracket of two vector elements is a cross product and so a vector element, which is the stability. Computed exactly on the units and on general elements. $\square$

**Corollary.** The derived algebra is perfect for the vector part, $[\mathrm{Vect}(\mathbb{B}),\mathrm{Vect}(\mathbb{B})]=\mathrm{Vect}(\mathbb{B})$, and the derived algebra of the whole algebra is reached in one step, $[\mathfrak{g},\mathfrak{g}]=\mathrm{Vect}(\mathbb{B})$.

### The Identification with the Cross Product and with $\mathfrak{sl}(2,\mathbb{C})$

**Theorem.** The derived algebra is isomorphic, as a complex Lie algebra, to the cross-product algebra of $\mathbb{C}^3$ and hence to $\mathfrak{sl}(2,\mathbb{C})$:

$$
\bigl(\mathrm{Vect}(\mathbb{B}),\wedge\bigr)\cong\bigl(\mathbb{C}^3,\times\bigr)\cong\mathfrak{sl}(2,\mathbb{C}),
$$

of complex dimension three and real dimension six.

*Proof.* The assignment $P_1e_1+P_2e_2+P_3e_3\mapsto(P_1,P_2,P_3)$ carries the bracket to the cross product, since $e_1\wedge e_2=e_3$ and its cyclic analogues are the cross-product table. The cross-product algebra of $\mathbb{C}^3$ is the complex orthogonal algebra $\mathfrak{so}(3,\mathbb{C})$, and the classical isomorphism $\mathfrak{so}(3,\mathbb{C})\cong\mathfrak{sl}(2,\mathbb{C})$ of the structure theory of *Structure of Lie Algebras* applies; the isomorphism is exhibited in the two-dimensional matrix model in *The Antisymmetric Plain Algebra in the Matrix Representations*, where $\tilde P\wedge\tilde Q$ becomes $\tfrac12[\,\Phi(\tilde P),\Phi(\tilde Q)\,]$ on the trace-free matrices. Verified on the structure constants of the six-dimensional real basis. $\square$

**Remark (the two descriptions of the same Lie algebra).** The identification is the reason the block is called the Lie block: **the derived algebra of the antisymmetric plain algebra is $\mathfrak{sl}(2,\mathbb{C})$**, the smallest simple complex Lie algebra, and the whole algebra is $\mathfrak{sl}(2,\mathbb{C})$ with a one-dimensional central summand. The identification up to the factor two between the halved bracket and the matrix commutator is the one of *Introduction to the Antisymmetric Plain Algebra of Biquaternions*: the matrix commutator is twice the block's bracket, and the two presentations differ by the rescaling $\tilde P\mapsto2\tilde P$ of the Lie algebra.

### The Real Forms

**Theorem (the quaternion subspace).** On the real span $\mathbb{H}_{\mathbb{B}}$ of $e_0,e_1,e_2,e_3$, the quaternion subspace, the bracket is real and takes values in the real vector triple $\mathbf{B}_1=\mathbb{R}e_1\oplus\mathbb{R}e_2\oplus\mathbb{R}e_3$. Hence $\mathbb{H}_{\mathbb{B}}$ is a real Lie subalgebra of real dimension four, and

$$
\mathbb{H}_{\mathbb{B}}\cong\mathbb{R}e_0\oplus\mathfrak{su}(2),
$$

with $\mathbb{R}e_0$ central and $\mathbf{B}_1$ identified with $\mathfrak{su}(2)$.

*Proof.* The bracket of two real quaternions is the cross product of two real vectors and is therefore a real vector, so $\mathbb{H}_{\mathbb{B}}$ is stable and $[\mathbb{H}_{\mathbb{B}},\mathbb{H}_{\mathbb{B}}]=\mathbf{B}_1$. The real vector triple with the cross product is the real form $\mathfrak{so}(3,\mathbb{R})\cong\mathfrak{su}(2)$ of the derived algebra, and the scalar direction is central; the sum is direct. Computed on the real basis. $\square$

**Theorem (the anti-Hermitian subspace).** On the anti-Hermitian subspace

$$
\mathbb{M}_-=\mathbb{R}(ie_0)\oplus\mathbf{B}_1=\{Q_0e_0+\mathbf{Q}:Q_0\in i\mathbb{R},\ \mathbf{Q}\in\mathbb{R}^3\},
$$

of real dimension four, the bracket is real, takes values in $\mathbf{B}_1$ and makes $\mathbb{M}_-$ a real Lie subalgebra,

$$
\mathbb{M}_-\cong\mathfrak{u}(2),
$$

whose derived algebra is $[\mathbb{M}_-,\mathbb{M}_-]=\mathbf{B}_1\cong\mathfrak{su}(2)$.

*Proof.* An element of $\mathbb{M}_-$ has scalar part purely imaginary and vector part real. The bracket sees only the vector parts, so it is the cross product of two real vectors, a real vector in $\mathbf{B}_1$; hence $\mathbb{M}_-$ is stable and its derived algebra is $\mathbf{B}_1$. The real Lie algebra with a one-dimensional central direction and derived algebra $\mathfrak{su}(2)$ is $\mathfrak{u}(2)$, the Lie algebra of the skew-Hermitian matrices, by its standard description in *The Unitary Lie Algebra*, §*The Skew-Hermitian Part as a Lie Algebra*; the identification is read there on the skew-Hermitian elements, of which $\mathbb{M}_-$ is the biquaternion case. Computed on the real basis. $\square$

**Remark.** The two theorems are two real forms of the same complex situation: **the complex derived algebra $\mathfrak{sl}(2,\mathbb{C})$ restricts to $\mathfrak{su}(2)$ on the real vector triple, and the two real subspaces that contain that triple are the quaternion subspace and the anti-Hermitian subspace, carrying the central extension $\mathbb{R}e_0$ and the central extension $\mathbb{R}(ie_0)$ respectively.** The quaternion subspace is $\mathbb{R}e_0\oplus\mathfrak{su}(2)$ and the anti-Hermitian subspace is $\mathfrak{u}(2)=\mathbb{R}(ie_0)\oplus\mathfrak{su}(2)$; the two differ only in which central direction the scalar part occupies. The group of the linear maps preserving the form of the skew elements is not read here: it is *The Unitary Lie Algebra*.

## Ideals, Quotients and the Two Series

### The Ideals

**Theorem.** The ideals of $\mathfrak{g}$ are exactly

$$
0,\qquad \mathbb{C}_{\mathbb{B}},\qquad \mathrm{Vect}(\mathbb{B}),\qquad \mathfrak{g}.
$$

*Proof.* The centre and the derived algebra are ideals, because the bracket vanishes on the centre and the derived algebra is mapped into itself. For the converse, take a nonzero ideal $\mathfrak{a}$ and an element $\tilde P\in\mathfrak{a}$. If $\mathbf{P}=0$ then $\mathfrak{a}$ contains a nonzero central element, hence the whole centre. If $\mathbf{P}\neq0$, then $[\mathfrak{g},\tilde P]$ is the span of the cross products $\mathbf{X}\times\mathbf{P}$ over all vectors $\mathbf{X}$, which is the plane orthogonal to $\mathbf{P}$; and $[\mathfrak{g},[\mathfrak{g},\tilde P]]$ is all of $\mathrm{Vect}(\mathbb{B})$, since the cross product of two vectors in that plane generates the third direction. Hence an ideal that contains an element with nonzero vector part contains $\mathrm{Vect}(\mathbb{B})$, and then either it stops at $\mathrm{Vect}(\mathbb{B})$ or, if it also contains a nonzero central element, it is $\mathfrak{g}$. Computed on the ideal generated by $e_0$, by $e_1$ and by $e_0+e_1$, of complex dimensions one, three and four. $\square$

**Corollary (the quotients).** The quotients of $\mathfrak{g}$ by its ideals are

$$
\mathfrak{g}/\mathbb{C}_{\mathbb{B}}\cong\mathrm{Vect}(\mathbb{B})\cong\mathfrak{sl}(2,\mathbb{C}),\qquad
\mathfrak{g}/\mathrm{Vect}(\mathbb{B})\cong\mathbb{C}_{\mathbb{B}},\qquad
\mathrm{Vect}(\mathbb{B})/0\cong\mathfrak{sl}(2,\mathbb{C}),
$$

the first semisimple and the second abelian of complex dimension one.

### The Derived Series, Solvability and Nilpotency

**Theorem.** The derived series of $\mathfrak{g}$ is

$$
\mathfrak{g}^{(0)}=\mathfrak{g},\qquad \mathfrak{g}^{(1)}=[\mathfrak{g},\mathfrak{g}]=\mathrm{Vect}(\mathbb{B}),\qquad \mathfrak{g}^{(2)}=[\mathfrak{g}^{(1)},\mathfrak{g}^{(1)}]=\mathrm{Vect}(\mathbb{B}),
$$

and it is constant from the first step; the lower central series is likewise constant from the second step. Hence $\mathfrak{g}$ is neither solvable nor nilpotent, and it is not semisimple, its radical being the centre $\mathbb{C}_{\mathbb{B}}$.

*Proof.* The derived algebra is $\mathrm{Vect}(\mathbb{B})$ and it is perfect, so the derived series stabilises there and never reaches zero. The lower central series begins $\mathfrak{g}\supseteq\mathrm{Vect}(\mathbb{B})$ and $[\mathfrak{g},\mathrm{Vect}(\mathbb{B})]=\mathrm{Vect}(\mathbb{B})$ again, so it also stabilises away from zero. The radical is the largest solvable ideal; the only nonzero proper ideals are the centre, abelian and so solvable, and $\mathrm{Vect}(\mathbb{B})$, not solvable; hence the radical is the centre. Computed on the basis. $\square$

**Remark.** **The algebra is reductive and not semisimple.** It is the direct sum of an abelian Lie algebra and a simple one, so its radical is the centre and its quotient by the radical is simple; the Cartan reading of the same fact through the Killing form is *The Killing Form of the Antisymmetric Plain Algebra*, where the form is shown to be degenerate with the centre as its radical.

### Simplicity

**Theorem.** $\mathfrak{g}$ is not simple, because $\mathbb{C}_{\mathbb{B}}$ is a nonzero proper ideal. The derived algebra $\mathrm{Vect}(\mathbb{B})$ is simple: it has no nonzero proper ideal.

*Proof.* The centre is a nonzero proper ideal, so $\mathfrak{g}$ is not simple. In the identification $\mathrm{Vect}(\mathbb{B})\cong\mathfrak{sl}(2,\mathbb{C})$, the simplicity of $\mathfrak{sl}(2,\mathbb{C})$ is the first case of the classification of *Structure of Lie Algebras*; it is also read directly from the cross product, since a nonzero ideal of the cross-product algebra contains a plane of directions and the bracket of two directions in that plane generates the third. Computed on the ideal generated by $e_1$, which is the whole vector subspace. $\square$

## The Enveloping Algebra

**Theorem.** By the Poincaré–Birkhoff–Witt theorem, applied to the direct sum $\mathfrak{g}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B})$, the enveloping algebra of $\mathfrak{g}$ is, as a complex vector space,

$$
U(\mathfrak{g})\cong\mathbb{C}[z]\otimes_{\mathbb{C}}U\bigl(\mathfrak{sl}(2,\mathbb{C})\bigr),
$$

where $z$ is the central generator coming from the centre $\mathbb{C}_{\mathbb{B}}$.

*Proof.* The centre is an abelian Lie algebra of complex dimension one, and its enveloping algebra is the polynomial algebra $\mathbb{C}[z]$ in one indeterminate; the vector part has enveloping algebra $U(\mathfrak{sl}(2,\mathbb{C}))$. The Lie algebra is a direct sum, so the enveloping algebra of the sum is the tensor product of the enveloping algebras, by the Poincaré–Birkhoff–Witt theorem of *Lie Algebras*. $\square$

**Remark (the count).** The associated graded object of $U(\mathfrak{g})$ is the symmetric algebra of $\mathfrak{g}$,

$$
\operatorname{gr}U(\mathfrak{g})\cong S(\mathfrak{g})\cong \mathbb{C}[z]\otimes_{\mathbb{C}}\mathbb{C}[w_1,w_2,w_3],
$$

of which the degree-$n$ part has dimension $\binom{n+3}{3}$, the dimension of $S^n(\mathbb{C}^4)$, the degree-$n$ symmetric power of the four-dimensional space. The identity

$$
\sum_{k=0}^{n}\binom{k+2}{2}=\binom{n+3}{3}
$$

is the numerical form of the count, with $\binom{k+2}{2}$ the degree-$k$ part of $\mathbb{C}[w_1,w_2,w_3]$, and it was checked for $n=0,\dots,6$. **The centre contributes one polynomial variable and the derived algebra three scaled variables, and the four together are the degree count of the four-dimensional Lie algebra.** Over the reals the same statement reads $U_{\mathbb{R}}(\mathfrak{g})\cong\mathbb{R}[z_1,z_2]\otimes_{\mathbb{R}}U_{\mathbb{R}}(\mathfrak{sl}(2,\mathbb{C}))$, with the two real coordinates of the centre.

**Remark (the centre of the enveloping algebra).** The centre of $U(\mathfrak{g})$ is $\mathbb{C}[z]$ tensored with the centre of $U(\mathfrak{sl}(2,\mathbb{C}))$, which is the polynomial algebra in the Casimir element of the derived algebra; the Casimir element itself is computed in *The Killing Form of the Antisymmetric Plain Algebra*, where it is read on the vector subspace and on the matrix models. No further central element of $U(\mathfrak{sl}(2,\mathbb{C}))$ is independent, by the theorem on the centre of the enveloping algebra of a semisimple Lie algebra.

## Worked Examples

**A central bracket.** For $\tilde P=2e_0+3ie_0$ the vector part is zero, so $\tilde P\wedge e_1=0$: the two complex coordinates of the centre both stand in the kernel of the adjoint.

**A bracket with a scalar part.** For $\tilde P=e_0+e_1$ and $\tilde Q=e_0+e_2$ the bracket is $e_3$, computed in *Introduction to the Antisymmetric Plain Algebra of Biquaternions*; the scalar parts of the two elements do not enter, and the value lies in the derived algebra.

**The derived algebra in one step.** $(e_0+e_1)\wedge e_1=0$ and $e_1\wedge e_2=e_3$: the central direction of $\tilde P=e_0+e_1$ contributes nothing, and the derived algebra is generated by the vector parts alone.

**The quaternion real form.** For $\tilde q=e_0+e_1$ and $\tilde r=e_0+e_2$ in $\mathbb{H}_{\mathbb{B}}$ the bracket is $\tilde q\wedge\tilde r=e_3$, a real vector element: the quaternion subspace is stable, and its derived algebra is the real vector triple.

**The anti-Hermitian real form.** For $x=ie_0+e_1$ and $y=ie_0+e_2$ in $\mathbb{M}_-$ the bracket is $x\wedge y=e_3$, again a real vector element: the scalar directions $ie_0$ commute with everything and the derived algebra is again the real vector triple, which is the identification $\mathfrak{u}(2)$ with derived algebra $\mathfrak{su}(2)$.

**An element with rank-two adjoint.** For $\tilde P=e_1+ie_2$ the adjoint is the complex matrix of rank two on the four-dimensional space, with kernel the complex plane spanned by $e_0$ and $e_1+ie_2$, of complex dimension two; the rank and the kernel are read in *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra*.

## Summary

The antisymmetric plain algebra makes $\mathbb{B}$ a complex Lie algebra $\mathfrak{g}$ of dimension four, whose centre is the centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ of the algebra, of dimension one, and whose derived algebra is the vector subspace $\mathrm{Vect}(\mathbb{B})$, of complex dimension three and real dimension six, stable under the bracket and identified with the cross-product algebra of $\mathbb{C}^3$ and with $\mathfrak{sl}(2,\mathbb{C})$. The algebra is the direct sum $\mathfrak{g}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B})$, its quotient by the centre is $\mathfrak{sl}(2,\mathbb{C})$, its quotient by the derived algebra is the abelian centre, and its only ideals are $0$, the centre, the derived algebra and the whole algebra. The derived series and the lower central series stabilise at the derived algebra, so the algebra is neither solvable nor nilpotent; it is reductive and not semisimple, with the centre as radical, and its derived algebra is simple. On the real forms the quaternion subspace is $\mathbb{R}e_0\oplus\mathfrak{su}(2)$ and the anti-Hermitian subspace is $\mathfrak{u}(2)$, of derived algebra $\mathfrak{su}(2)$. By Poincaré–Birkhoff–Witt the enveloping algebra is $\mathbb{C}[z]\otimes_{\mathbb{C}}U(\mathfrak{sl}(2,\mathbb{C}))$ as a complex vector space, with associated graded object $\mathbb{C}[z]\otimes\mathbb{C}[w_1,w_2,w_3]$ and degree-$n$ dimension $\binom{n+3}{3}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathfrak{g}=(\mathbb{B},\wedge)$ | the Lie algebra of the antisymmetric plain algebra |
| $\tilde P\wedge\tilde Q=\mathbf{P}\times\mathbf{Q}$ | the bracket, the cross product of the vector parts |
| $\mathfrak{z}(\mathfrak{g})=\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ | the centre of the Lie algebra, the centre of the algebra |
| $\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B})$ | the splitting of the Lie algebra into the centre and the derived algebra |
| $[\mathfrak{g},\mathfrak{g}]=\mathrm{Vect}(\mathbb{B})$ | the derived algebra, of complex dimension three and real dimension six |
| $\mathrm{Vect}(\mathbb{B})\cong\mathbb{C}^3$ with $\times$ $\cong\mathfrak{sl}(2,\mathbb{C})$ | the identification of the derived algebra |
| $\mathbb{H}_{\mathbb{B}}\cong\mathbb{R}e_0\oplus\mathfrak{su}(2)$ | the quaternion subspace as a real Lie subalgebra |
| $\mathbb{M}_-\cong\mathfrak{u}(2)$, $[\mathbb{M}_-,\mathbb{M}_-]\cong\mathfrak{su}(2)$ | the anti-Hermitian subspace and its derived algebra |
| $0,\ \mathbb{C}_{\mathbb{B}},\ \mathrm{Vect}(\mathbb{B}),\ \mathfrak{g}$ | the ideals of $\mathfrak{g}$ |
| $U(\mathfrak{g})\cong\mathbb{C}[z]\otimes_{\mathbb{C}}U(\mathfrak{sl}(2,\mathbb{C}))$ | the enveloping algebra as a complex vector space |
| $\operatorname{gr}U(\mathfrak{g})\cong\mathbb{C}[z,w_1,w_2,w_3]$ | the associated graded object, of degree-$n$ dimension $\binom{n+3}{3}$ |

## Further Reading

- *Introduction to the Antisymmetric Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-plain-algebra-of-biquaternions.md`), for the bracket, its Jacobi identity and the sixteen brackets of the basis
- *The Killing Form of the Antisymmetric Plain Algebra* (`articles_maths/the-killing-form-of-the-antisymmetric-plain-algebra.md`), for the invariant form, its radical and the Casimir element
- *The Adjoint Operators and the Derivations of the Antisymmetric Plain Algebra* (`articles_maths/the-adjoint-operators-and-the-derivations-of-the-antisymmetric-plain-algebra.md`), for the adjoints, their kernels, the derivations and the automorphisms of the bracket
- *The Unitary Lie Algebra* (`articles_maths/the-unitary-lie-algebra.md`), for the skew-Hermitian elements, the unhalved commutator and the group of linear maps preserving their form
- *The Six Subspaces and the Four Complex Products* (`articles_maths/the-six-subspaces-and-the-four-complex-products.md`), for the six distinguished subspaces read under the four products
- *Lie Algebras* (`articles_maths/lie-algebras-a-general-introduction.md`), for the axioms, the ideals, the series, the simplicity and the enveloping algebra
- *Structure of Lie Algebras* (`articles_maths/structure-of-lie-algebras.md`), for the classical algebras, the isomorphism $\mathfrak{so}(3,\mathbb{C})\cong\mathfrak{sl}(2,\mathbb{C})$, the radical and the semisimplicity criteria
- *Associative Algebras* (`articles_maths/associative-algebras.md`) and *The Commutator Operator* (`articles_maths/the-commutator-operator.md`), for the associativity from which the Jacobi identity descends
