# __The Spin of the Split-Complex Numbers: A Root Without a Ladder__

## Introduction

The split-complex algebra is the closest commutative algebra to a spin algebra. It has a nontrivial idempotent, a Peirce frame and a root $j$ with $j^2=1$ whose left multiplication has eigenvalues $\pm1$. It still has no spin pair, because the Peirce corners are zero and every element is central.

The table of cases in *The General Definition of Spin* has this entry.

| algebra | reason for no spin |
|---|---|
| $\mathbb{D}$ | commutative |

### The Result

**The split-complex numbers have no spin.** There is no spin pair, no spin triple and no carrier of nonzero spin.

**The root $j$ is not a spin element.** It satisfies $j^2=1$ and its left multiplication has eigenvalues $\pm1$, but it is central: $\operatorname{ad}_j=0$. A spin element must have $\operatorname{ad}_S\neq0$, because $[S,U]=U$ with $U\neq0$.

**The Peirce frame is not a spin pair.** The idempotents $e_\pm=\tfrac12(1\pm j)$ satisfy $e_+e_-=0$. The off-diagonal corners $e_+\mathbb{D}e_-$ and $e_-\mathbb{D}e_+$ are therefore zero, so a pair built from the frame has $U=V=0$.

**Every module is spinless.** $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$; its simple modules are the two lines $\mathbb{R}e_+$ and $\mathbb{R}e_-$, both one-dimensional over $\mathbb{R}$.

### The Contrast With the Biquaternion

The biquaternion $\mathbb{B}$ has a Peirce frame with nonzero corners, and that frame is its spin pair. The split-complex algebra has a Peirce frame with zero corners, and it has no pair. The difference is not the existence of a root or of idempotents. It is the commutativity of the algebra, which collapses the corners.

## The Algebra

### The Product

**Definition.** The split-complex algebra is

$$
\mathbb{D}=\mathbb{R}[j]/(j^2-1)=\{a+bj:a,b\in\mathbb{R}\},\qquad j^2=1.
$$

The product is

$$
(a+bj)(c+dj)=(ac+bd)+(ad+bc)j.
$$

The element $j$ is not $\pm1$; it is a new square root of $+1$. The algebra is commutative and associative, with unit $1$. It has zero divisors:

$$
(1+j)(1-j)=1-j^2=0.
$$

### The Idempotents

**Proposition.** The idempotents of $\mathbb{D}$ are $0$, $1$, $e_+$ and $e_-$, where

$$
e_+=\tfrac12(1+j),\qquad e_-=\tfrac12(1-j).
$$

*Proof.* Solve $(a+bj)^2=a+bj$: the equations are $a^2+b^2=a$ and $2ab=b$. The second gives $b=0$ or $a=\tfrac12$. With $b=0$ the first gives $a=0$ or $a=1$. With $a=\tfrac12$ the first gives $b^2=\tfrac14$, so $b=\pm\tfrac12$, which are $e_\pm$.

**The frame relations.** Direct computation gives

$$
e_+^2=e_+,\qquad e_-^2=e_-,\qquad e_+e_-=0,\qquad e_++e_-=1,\qquad e_+-e_-=j.
$$

**Result.** The pair $(e_+,e_-)$ is a complete orthogonal pair of idempotents, and $j=e_+-e_-$ is its root.

### The Direct Sum

The map

$$
\mathbb{D}\longrightarrow\mathbb{R}\oplus\mathbb{R},\qquad a+bj\longmapsto(a+b,\,a-b)
$$

is an isomorphism of algebras: it is bijective, and the product is componentwise. In this description $e_+\mapsto(1,0)$ and $e_-\mapsto(0,1)$.

**Result.** $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$. Every element is a pair of real numbers, and every module is a pair of real vector spaces.

## The Peirce Frame

### The Four Corners

For the idempotent $e_+$ the Peirce decomposition is

$$
\mathbb{D}=\mathbb{D}_{++}\oplus\mathbb{D}_{+-}\oplus\mathbb{D}_{-+}\oplus\mathbb{D}_{--},\qquad
\mathbb{D}_{ab}=e_a\mathbb{D}e_b.
$$

The diagonal corners are the lines $\mathbb{D}_{++}=\mathbb{R}e_+$ and $\mathbb{D}_{--}=\mathbb{R}e_-$. The off-diagonal corners vanish:

$$
\mathbb{D}_{+-}=e_+\mathbb{D}e_-=\mathbb{D}e_+e_-=0,\qquad
\mathbb{D}_{-+}=e_-\mathbb{D}e_+=0,
$$

because the algebra is commutative and $e_+e_-=0$.

**Result.** The Peirce decomposition collapses:

$$
\mathbb{D}=\mathbb{R}e_+\oplus\mathbb{R}e_-.
$$

There are no off-diagonal elements, so there is no element with corner signs $+$ and $-$.

### The Root

The root is $h=j=e_+-e_-$. Its square is

$$
h^2=e_+^2-2e_+e_-+e_-^2=e_++e_-=1.
$$

Left multiplication by $h$ on $\mathbb{D}$ has the matrix

$$
L_h=\begin{pmatrix}0&1\\1&0\end{pmatrix}
$$

in the basis $(1,j)$, with characteristic polynomial $\lambda^2-1$ and eigenvalues $+1$ and $-1$. The eigenvectors are $e_+$ and $e_-$.

**Result.** The root has the weight string $+1,-1$ under left multiplication. This is the closest the algebra comes to a spin structure, and it is not one: the operator $L_h$ is not the adjoint action of a triple.

### The Adjoint Action Is Zero

Because $\mathbb{D}$ is commutative, every element is central:

$$
\operatorname{ad}_x(y)=xy-yx=0\qquad\text{for all }x,y.
$$

In particular $\operatorname{ad}_h=0$, although $L_h$ has eigenvalues $\pm1$. The two operators are different: $L_h$ is left multiplication, $\operatorname{ad}_h$ is the commutator.

**Result.** No element of $\mathbb{D}$ has a nonzero adjoint action.

## Why There Is No Pair

### The Direct Proof

**Proposition.** There is no spin pair in $\mathbb{D}$.

*Proof.* Suppose $[U,V]\neq0$. But $\mathbb{D}$ is commutative, so $[U,V]=0$ for all $U,V$. Contradiction. Equivalently, the pair conditions with $[U,V]=0$ give $U=0$ and $V=0$, the excluded zero pair.

### The Peirce Proof

Suppose a triple $(S,U,V)$ is built from the frame, with $S=\tfrac12h$ and with $U,V$ in the off-diagonal corners. The corner decomposition forces

$$
U\in\mathbb{D}_{+-}=0,\qquad V\in\mathbb{D}_{-+}=0.
$$

Then $[U,V]=0$, while $2S=h\neq0$, so the third relation fails. The first two relations hold only in the degenerate sense $[S,0]=0$.

**Result.** The frame gives a root and two idempotents, but no ladder. A root without a ladder is not a spin element.

### The Weight String Without a Triple

It is tempting to read the eigenvalues $\pm1$ of $L_h$ as the weights of a spin-$1$ carrier, or the eigenvalues $\pm\tfrac12$ of $L_{h/2}$ as the weights of a spin-$\tfrac12$ carrier. The reading fails at the ladder. An element $U$ that shifted the weight would need $[h,U]=2U$; but $\mathbb{D}$ is commutative, so $[h,U]=0$. In the Peirce basis the only elements that could move $e_-$ to $e_+$ lie in the corner $\mathbb{D}_{+-}$, which is zero. The eigenvalues of a single operator are not a spin; the spin is the highest weight of an irreducible module of a triple.

**Result.** The string $+1,-1$ is a spectrum, not a spin content.

## The Modules

**Proposition.** The simple $\mathbb{D}$-modules are $\mathbb{R}e_+$ and $\mathbb{R}e_-$, both one-dimensional over $\mathbb{R}$.

*Proof.* Under the isomorphism $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$, a module is a pair $(V_+,V_-)$ of real vector spaces, with $(a,b)$ acting as $a$ on $V_+$ and $b$ on $V_-$. The simple pairs are $(\mathbb{R},0)$ and $(0,\mathbb{R})$.

**Result.** Every finite-dimensional module is a direct sum of copies of the two simple modules. Both are one-dimensional and spinless, because no triple acts.

**Remark (the regular module).** The left regular module is $\mathbb{D}=\mathbb{R}e_+\oplus\mathbb{R}e_-$. Left multiplication by $h$ acts as $+1$ on the first line and $-1$ on the second. The two lines are the simple modules; the eigenvalues of $L_h$ are the scalars by which $h$ acts on them.

## What Is Not a Spin Here

### The Root

$j$ is a root of $+1$ and the frame root of the pair $(e_+,e_-)$. The word "root" is not "spin". A spin element is the antisymmetric part of a product of two noncommuting elements; $j$ is central and is the difference of two commuting idempotents.

### The Idempotents

$e_+$ and $e_-$ are idempotents, and they give a Peirce frame. The frame is a decomposition of the algebra, not a triple. In the biquaternion the frame and the triple coincide; here the frame survives and the triple does not.

### The Value $0$

The algebra has no spin, so it has no spin-$0$ carrier either. A spin-$0$ carrier is a one-dimensional module of a nonzero triple; the triple is absent.

### The Hyperbolic Angle

The exponential $e^{j\theta}=\cosh\theta+j\sinh\theta$ parametrizes the hyperbola $a^2-b^2=1$, and the half-angle formulas for $\cosh$ and $\sinh$ are the hyperbolic analogues of the circular ones. They belong to the geometry of the hyperbola, not to a weight of a triple. There is no copy of $\mathfrak{sl}_2$ in the Lie algebra of $\mathbb{D}$, which is abelian.

**Result.** None of the four structures is a spin.

## Comparison With the Reduced Biquaternion

The complexification $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ is isomorphic to $\mathbb{C}\oplus\mathbb{C}$, the reduced biquaternion algebra $\mathbb{B}_{\mathrm{r}}$. It has a nontrivial Peirce frame, and its root is central in each factor, so it does not close to a pair. The split-complex algebra is the real two-dimensional model of the same phenomenon: a frame, a root, no ladder.

**Result.** $\mathbb{D}$ and $\mathbb{B}_{\mathrm{r}}$ are the commutative cases with a nontrivial frame. Both have a root; neither has a spin.

## Checks

| check | result |
|---|---|
| $j^2$ | $1$ |
| $e_+^2,e_-^2$ | $e_+,e_-$ |
| $e_+e_-$ | $0$ |
| $e_++e_-$ | $1$ |
| $e_+-e_-$ | $j$ |
| corners $e_+\mathbb{D}e_-$, $e_-\mathbb{D}e_+$ | $0$ |
| $[x,y]$ for $x,y\in\{1,j,e_+,e_-\}$ | $0$ |
| characteristic polynomial of $L_j$ | $\lambda^2-1$ |
| eigenvalues of $L_j$ | $+1,-1$ |
| spin pairs | none |
| simple modules | two, both one-dimensional |
| spin | none |

## Summary

- The split-complex algebra is commutative, so every commutator vanishes and no spin pair exists.
- It has the idempotents $e_\pm=\tfrac12(1\pm j)$ and the root $j=e_+-e_-$, with $j^2=1$.
- The Peirce corners $e_+\mathbb{D}e_-$ and $e_-\mathbb{D}e_+$ are zero, so the ladders a triple needs are forced to zero.
- The root is central, $\operatorname{ad}_j=0$, although left multiplication by $j$ has eigenvalues $\pm1$.
- The eigenvalues $\pm1$ are a spectrum of one operator, not a weight string of a triple.
- The modules are the two lines $\mathbb{R}e_\pm$, both spinless.
- The algebra is the real model of the reduced biquaternion: a frame and a root, but no spin.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{D}$ | split-complex algebra $\mathbb{R}[j]/(j^2-1)$ |
| $j$ | root, $j^2=1$ |
| $e_\pm$ | idempotents $\tfrac12(1\pm j)$ |
| $\mathbb{D}_{ab}$ | Peirce corner $e_a\mathbb{D}e_b$ |
| $h$ | root $e_+-e_-=j$ |
| $L_x$ | left multiplication by $x$ |
| $\operatorname{ad}_x$ | $y\mapsto xy-yx$ |
| $W_j$ | irreducible carrier of a triple, dimension $2j+1$ |

## Further Reading

- [The General Definition of Spin](../articles_maths/the-general-definition-of-spin.html), for the definition, the commutative case and the products.
- [The Spin of the Complex Numbers](the-spin-of-the-complex-numbers-the-absence-of-a-pair.html), for the commutative field with no frame at all.
- [The Spin of a Biquaternion](../articles_maths/the-spin-of-a-biquaternion.html), for the frame whose corners are nonzero and whose root is a spin element.
- [The Split-Complex Algebra](../articles_maths/split-complex-algebra.html), for the product and the idempotents.
- [The Peirce Basis of the Split-Complex Algebra](../articles_maths/the-peirce-basis-of-the-split-complex-algebra.html), for the Peirce decomposition.
