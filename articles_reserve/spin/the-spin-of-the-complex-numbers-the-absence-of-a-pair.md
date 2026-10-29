# __The Spin of the Complex Numbers: The Absence of a Pair__

## Introduction

The table of cases in *The General Definition of Spin* has no spin row for $\mathbb{C}$. It has this entry instead.

| algebra | reason for no spin |
|---|---|
| $\mathbb{C}$ | commutative |

This article states the result, proves the obstruction, and separates the value $0$ from a spin.

### The Result

**The complex numbers have no spin.** There is no spin pair in $\mathbb{C}$, so there is no spin triple, no spin element, and no carrier of nonzero spin.

**Every module of $\mathbb{C}$ is spinless.** The algebra is a field; its only simple module is $\mathbb{C}$ itself, and every finite-dimensional module is a direct sum of copies of it.

**The value $0$ is not the spin of $\mathbb{C}$.** The zero pair is excluded by the definition, and a spinless module is not a spin-$0$ carrier.

**Complexification does not help.** $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$ is still commutative, so the complexified algebra has no pair either. This is the difference from the quaternion, whose pair appears only after complexification.

### The One-Line Obstruction

In a commutative algebra $[U,V]=0$ for all $U,V$. A spin pair requires $[U,V]\neq0$. So there is no pair.

## The Obstruction

### The Bracket Vanishes

**Proposition.** For all $z,w\in\mathbb{C}$, $[z,w]=zw-wz=0$.

*Proof.* Multiplication of complex numbers is commutative.

**Corollary (only the zero pair).** If a pair $(U,V)$ satisfies $[U,V]=0$ and $[[U,V],U]=2U$, then $0=2U$, so $U=0$; the relation $[[U,V],V]=-2V$ then gives $V=0$. The only pair satisfying the two double-commutator relations is the zero pair, and it is excluded by $[U,V]\neq0$.

**Result.** The set of spin pairs in $\mathbb{C}$ is empty.

### No Element Can Be a Spin Element

A spin element would be $S=\tfrac12[U,V]$. Since every bracket vanishes, $S=0$ for every pair. There is no nonzero element of $\mathbb{C}$ that is the antisymmetric part of a product.

**Result.** The algebra has no spin element.

### No Carrier

A carrier is a module for a copy of $\mathfrak{sl}_2$ spanned by $S,U,V$. There is no such triple, so there is no carrier of the triple, and hence no carrier of the algebra in the sense of the definition.

**Result.** No nonzero spin occurs on any module of $\mathbb{C}$.

## What the Algebra Does Have

The absence of a pair is not an absence of structure. The algebra has the following, and none of it is a spin pair.

**A field.** Every nonzero element is invertible. There are no zero divisors.

**Two idempotents.** The equation $z^2=z$ has the solutions $z=0$ and $z=1$. There is no nontrivial idempotent, so there is no Peirce decomposition and no corner.

**No nilpotents.** The equation $z^2=0$ has only $z=0$. There is no nilpotent ladder.

**The unit circle.** The elements of modulus $1$ form the group $U(1)$, and the map $\theta\mapsto e^{i\theta}$ is a group homomorphism from $\mathbb{R}$ onto it.

**Every element is central.** The adjoint action of any element is the zero operator, so the adjoint module has only the weight $0$, and it has it for the trivial reason that the operator is zero.

**Result.** The algebra is a field with two idempotents and no nilpotents. None of these structures supplies two elements with a nonzero commutator.

## What Is Not a Spin Here

### The Value $0$

It is tempting to say that the module $\mathbb{C}$ has spin $0$, because the only weight of the zero operator is $0$. That is not a spin in the sense of the definition. A spin-$0$ carrier is a one-dimensional module of a nonzero triple on which $S$ acts by $0$; the triple still has nonzero $U,V$ and a nonzero commutator. In $\mathbb{C}$ the triple itself is zero. The definition excludes the zero pair precisely to keep the two cases apart.

**Result.** "Spinless" and "spin $0$" are different. $\mathbb{C}$ is spinless; the centre of the biquaternion is spin $0$.

### The Eigenvalues of Multiplication

Left multiplication by $z\in\mathbb{C}$ on the real plane $\mathbb{C}$ has the matrix $\begin{pmatrix}a&-b\\b&a\end{pmatrix}$ for $z=a+ib$, with eigenvalues $a+ib$ and $a-ib$. These are the two complex eigenvalues of a real operator, not the weights of a triple: there is no $S$ with a spectrum $j,j-1,\dots,-j$ and no ladder relating the eigenvectors. The eigenvalues of multiplication by $z$ are $z$ and $\bar z$; they do not form a weight string of $\mathfrak{sl}_2$.

### The Half-Angle

Polar form writes $z=re^{i\theta}$, and the square root is $\sqrt r\,e^{i\theta/2}$. The half-angle is the parameter of the double cover

$$
U(1)\longrightarrow SO(2),\qquad e^{i\theta}\longmapsto R_{2\theta},
$$

and it is why a rotation by $2\pi$ acts as $-1$ on a spinor. That is a statement about a covering of groups, not about a weight of a triple on the algebra $\mathbb{C}$. The group $SO(2)$ is abelian, and $\mathfrak{sl}_2$ is not; no copy of $\mathfrak{sl}_2$ lies in the Lie algebra of $U(1)$. The half-angle belongs to the representation theory of the double cover, and the spin of this corpus belongs to the highest weight of a triple. They are different constructions, and the second is empty for $\mathbb{C}$.

**Result.** The half-angle $e^{i\theta/2}$ is not a spin of the algebra $\mathbb{C}$.

### The Centre of the Biquaternion

When $\mathbb{C}$ sits inside $\mathbb{B}$ as the centre $\mathbb{C}e_t$, the adjoint action of the biquaternion pair fixes it. The centre is then a spin-$0$ carrier of the biquaternion triple. That spin belongs to the pair in $\mathbb{B}$, not to the algebra $\mathbb{C}$: the acting triple is not contained in $\mathbb{C}$, and the carrier is a subspace of $\mathbb{B}$, not a module of $\mathbb{C}$ alone.

**Result.** The only spin associated with $\mathbb{C}$ is borrowed from a larger algebra.

## The Modules

**Proposition.** Every finite-dimensional $\mathbb{C}$-module is a direct sum of copies of $\mathbb{C}$.

*Proof.* The algebra is a field, so it is semisimple; its simple module is $\mathbb{C}$; every semisimple module is a direct sum of simple ones.

**Result.** The module theory of $\mathbb{C}$ is the theory of complex vector spaces. There is one simple module, it is one-dimensional over $\mathbb{C}$, and it carries no spin.

**Remark (the real picture).** Read over $\mathbb{R}$, the algebra $\mathbb{C}$ is two-dimensional and its left regular module is $\mathbb{C}$ itself, of real dimension $2$. The real endomorphism ring is $\mathbb{C}$. Neither number produces a spin: a carrier needs a triple, and the triple is absent.

## What Would Be Needed

A spin pair needs two elements with a nonzero commutator. Three constructions supply one.

- A noncommutative algebra, such as $M_2(\mathbb{C})$ or $\mathbb{B}$, with two matrix units $E_{12},E_{21}$.
- A noncommutative real algebra whose complexification is a matrix algebra, such as $\mathbb{H}$.
- A noncommutative algebra with a Peirce frame whose corners are nonzero, such as $\mathbb{B}$.

$\mathbb{C}$ has none of these properties. It is commutative, its only idempotents are $0$ and $1$, and its corners are zero.

**Result.** The smallest matrix algebra with a spin pair is $M_2(\mathbb{C})$, of dimension $4$. The real division algebras are $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$; only $\mathbb{H}$ is noncommutative, and its complexification is $M_2(\mathbb{C})$.

## Checks

| check | result |
|---|---|
| $[z,w]$ for $z,w\in\{1,i,2+3i,2-5i\}$ | $0$ |
| idempotents $z^2=z$ | $0,1$ |
| nilpotents $z^2=0$ | $0$ |
| spin pairs | none |
| noncentral elements | none |
| simple modules | one, $\mathbb{C}$ |
| complexification | $\mathbb{C}\oplus\mathbb{C}$, commutative |
| spin | none |

## Summary

- The complex numbers are commutative, so every commutator vanishes and no spin pair exists.
- The only pair satisfying the double-commutator relations is $U=V=0$, and the definition excludes it.
- There is no spin element, no spin triple and no carrier of nonzero spin.
- The value $0$ is not a spin: a spinless module and a spin-$0$ carrier are different.
- The half-angle $e^{i\theta/2}$ belongs to the double cover $U(1)\to SO(2)$, not to a weight of a triple on $\mathbb{C}$.
- When $\mathbb{C}$ is the centre of $\mathbb{B}$, its spin $0$ is carried by the biquaternion pair, not by $\mathbb{C}$.
- Complexification gives $\mathbb{C}\oplus\mathbb{C}$, still commutative, so it does not produce a pair.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}$ | complex numbers as an algebra over $\mathbb{R}$ |
| $[z,w]$ | $zw-wz$ |
| $\bar z$ | complex conjugate |
| $U(1)$ | unit circle, the double cover of $SO(2)$ |
| $W_j$ | irreducible carrier of a triple, dimension $2j+1$ |
| $S$ | $\tfrac12[U,V]$, the spin element a pair would give; absent here |

## Further Reading

- [The General Definition of Spin](../articles_maths/the-general-definition-of-spin.html), for the definition, the commutative case and the table of cases.
- [The Spin of a Biquaternion](../articles_maths/the-spin-of-a-biquaternion.html), for the centre as a spin-$0$ carrier of a larger pair.
- [The Spin of the Split-Complex Numbers](the-spin-of-the-split-complex-numbers-a-root-without-a-ladder.html), for the commutative algebra that does have a nontrivial Peirce frame.
- [The Complex Algebra](../articles_maths/complex-algebra.html), for the field structure.
- [Representations of Lie Algebras](../articles_maths/representations-of-lie-algebras.html), for the modules that a triple would need.
