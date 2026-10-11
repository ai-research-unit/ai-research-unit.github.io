# __Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra $\mathbb{B}^{\bullet}$ is the complex space $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ under the Jordan product $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ of *Introduction to the Symmetric Plain Algebra of Biquaternions*. This article determines the elements $\tilde P$ with $\tilde P\bullet\tilde P=\lambda e_0$ for the three central values $\lambda=-1,0,+1$.

A root is a root of a product, and the equation names it. The square of the block is the **plain square**, $\tilde P\bullet\tilde P=\tilde P^2$, so the three equations are the three equations of the algebra, and the three root sets of the block **coincide** with the three sets of *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*. The reduction below proves the coincidence, and the classification of the algebra is the classification of the block; the article restates it, and adds the two readings the algebra article cannot give, the appearance of the roots of $+1$ as the indices of the idempotents and the behaviour of the roots under the zero-divisor theory.

A root is defined relative to a product, and the definition is stated once for a general product in *Definitions for the Study of the 12 Algebraic Structures*, §*The Root*; throughout this article the product is $\bullet$ and, unqualified, **root** means root of $\bullet$. The roots of the algebra are *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*; the general root problem is *Square Roots of a General Element in the Symmetric Plain Algebra*; the idempotents the roots of $+1$ index are *Idempotents of the Symmetric Plain Algebra*; and the annihilating elements among the roots are *Zero Divisors of the Symmetric Plain Algebra*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$, central scalar imaginary $i$ and coefficients in $\mathbb{C}$. An element is $\tilde P=P_0e_0+\mathbf{P}$ with $\mathbf{P}=\sum_kP_ke_k$ and $(\mathbf{P},\mathbf{P})=\sum_kP_k^2$. The product with the mark is $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$; the central square is $c(\tilde P)=\sum_\mu P_\mu^2=P_0^2+(\mathbf{P},\mathbf{P})$.

## The General Definition and the Reduction

**Definition (root of a product).** Let $\star$ be a product on $\mathbb{B}$ with a unit $e$, and let $\tilde Q$ be an element and $\lambda$ a scalar. Then $\tilde P$ is a **square root of $\lambda$ of $\star$**, written $\tilde P\star\tilde P=\lambda e$, when the equation holds; a **root of $\tilde Q$** of $\star$ is an element with $\tilde P\star\tilde P=\tilde Q$.

Throughout this article the product is the symmetric plain product $\bullet$ and the unit is $e_0$; the three equations are

$$
\tilde P\bullet\tilde P=-e_0,\qquad \tilde P\bullet\tilde P=0,\qquad \tilde P\bullet\tilde P=+e_0 .
$$

**Theorem (the reduction).** The three root sets of the block coincide with the three root sets of the general plain product:

$$
\{\tilde P:\tilde P\bullet\tilde P=\lambda e_0\}=\{\tilde P:\tilde P^2=\lambda e_0\},\qquad \lambda\in\{-1,0,+1\}.
$$

*Proof.* The square of the block is the plain square, $\tilde P\bullet\tilde P=\tfrac12(\tilde P^2+\tilde P^2)=\tilde P^2$, so the two equations are the same equation for each value of $\lambda$. The identity holds for every $\tilde P$ and every $\lambda$, and no further reduction is needed.

The reason the reduction is so short is that the symmetrisation only moves the antisymmetric part of the product, and the antisymmetric part vanishes on the diagonal: $\tilde P\wedge\tilde P=0$, so the block and the algebra see the same square (*Introduction to the Symmetric Plain Algebra of Biquaternions*). The classification of the algebra therefore transfers with its proof, and this article reads it on the block.

## The Roots of Minus One

**Theorem.** The roots of $-1$ in the block are exactly the elements of the three following families (*Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*).

**The trivial roots.** The two central elements

$$
\tilde P=+ie_0,\qquad \tilde P=-ie_0 .
$$

**The pure real roots.** The pure real quaternions of unit length, a two-real-parameter family,

$$
\tilde P=\boldsymbol{p}=p_1e_1+p_2e_2+p_3e_3,\qquad p_1^2+p_2^2+p_3^2=1,
$$

with the sign absorbed.

**The non-trivial roots.** The four-real-parameter family

$$
\tilde P=\boldsymbol{p}+i\boldsymbol{p}',\qquad \boldsymbol{p}'\neq0,\qquad
p_1^2+p_2^2+p_3^2-p_1'^2-p_2'^2-p_3'^2=1,\quad \boldsymbol{p}\cdot\boldsymbol{p}'=0,
$$

whose imaginary part $\boldsymbol{p}'$ is non-zero, so that the family is disjoint from the pure real one; the two pure families together are the set of pure $\mathbf{P}$ with $(\mathbf{P},\mathbf{P})=1$.

*Proof.* The reduction puts the equation at $\tilde P^2=-e_0$ of the algebra, whose classification is the stated one; the block's product reads it unchanged.

**Remark (the block's reading).** Every root of $-1$ has non-zero central square, $c(\tilde P)=1$ for the pure ones and $c(\pm ie_0)=-1$ for the trivial ones, so every root of $-1$ is **invertible** of the block. Among them, every pure root is a **zero divisor** of the block, whatever its central square, the block's pure family being the whole vector subspace; so the block has invertible roots of $-1$ that are not regular, which the algebra does not.

## The Roots of Zero

**Theorem.** The roots of $0$ in the block are exactly the following (*Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*).

**The origin.** $\tilde P=0$.

**The nilpotent cone.** The pure isotropic elements, the four-real-parameter family

$$
\tilde P=P_1e_1+P_2e_2+P_3e_3,\qquad P_1^2+P_2^2+P_3^2=0,
$$

whose non-zero elements are the nilpotents of the block.

*Proof.* The reduction puts the equation at $\tilde P^2=0$ of the algebra; the classification is the stated one.

**Remark (the block's reading).** The non-zero roots of $0$ are exactly the nilpotents of *Nilpotents of the Symmetric Plain Algebra*, and they are the elements of the pure family of the zero divisors whose vector part is isotropic; they are not invertible, and their left multiplication has index three, so the block's root of $0$ does not give the flag of the algebra.

## The Roots of Plus One

**Theorem.** The roots of $+1$ in the block are exactly the elements $\tilde P_+=\tilde P i$ with $\tilde P$ a root of $-1$, that is the three following families (*Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*).

**The trivial roots.** The two central elements $\tilde P_+=+e_0$ and $\tilde P_+=-e_0$.

**The pure real roots.** The elements $\tilde P_+=\pm\boldsymbol{p}i$ with $\boldsymbol{p}$ a pure real quaternion of unit length, a two-real-parameter family.

**The non-trivial roots.** The four-real-parameter family $\tilde P_+=\boldsymbol{p}i-\boldsymbol{p}'$ with $\boldsymbol{p}'\neq0$ and the two conditions $\boldsymbol{p}^2-\boldsymbol{p}'^2=1$ and $\boldsymbol{p}\cdot\boldsymbol{p}'=0$; the two pure families together are the set of pure $\mathbf{P}$ with $(\mathbf{P},\mathbf{P})=-1$.

*Proof.* $(\tilde P i)^2=\tilde P^2i^2=(-1)(-1)=1$, and the map $\tilde P\mapsto\tilde P i$ is a bijection from the roots of $-1$ to the roots of $+1$ because $i$ is invertible in the centre.

**Remark (the block's reading).** The **pure** roots of $+1$ are exactly the elements $\mathbf{u}$ of the vector subspace with $\mathbf{u}^2=e_0$, and they index the non-trivial idempotents of the block by $\mathbf{u}\mapsto\tfrac12(e_0+\mathbf{u})$; this bijection is *Idempotents of the Symmetric Plain Algebra*, and it does not exist in the algebra article, where the roots of $+1$ are used only for the exponential and the logarithm. Every root of $+1$ has non-zero central square, so every root of $+1$ is invertible, and every pure root is a zero divisor.

## The Three Sets Compared

| central value | the central roots | the pure family | the block's reading |
|---|---|---|---|
| $-1$ | $\pm ie_0$ | $(\mathbf{P},\mathbf{P})=1$ | all invertible; pure ones are zero divisors |
| $0$ | $0$ | $(\mathbf{P},\mathbf{P})=0$ | the nilpotent cone of the block |
| $+1$ | $\pm e_0$ | $(\mathbf{P},\mathbf{P})=-1$ | pure ones index the idempotents |

**Theorem (the three sets are disjoint).** No element of the block is a root of two different central values, and the three sets are disjoint.

*Proof.* A root of $\lambda$ and of $\mu$ with $\lambda\neq\mu$ would satisfy $\lambda e_0=\tilde P\bullet\tilde P=\mu e_0$, so $(\lambda-\mu)e_0=0$, impossible.

## The Coincidence with the General Plain Algebra

**Theorem.** The three root sets of the block coincide element by element with the three root sets of the general plain product, and the coincidence is the identity of the two squares.

*Proof.* The reduction above.

The three sets are therefore the degenerate data of the general root problem of the block, and the general problem is *Square Roots of a General Element in the Symmetric Plain Algebra*, where the same reduction holds and the classification of the algebra transfers in the same way.

## Summary

The square of the block is the plain square, so the three roots of $\pm1$ and $0$ of the block are exactly the three of the algebra, and the classification transfers without change. The roots of $-1$ are the two central elements $\pm ie_0$ and the pure elements $\mathbf{P}$ with $(\mathbf{P},\mathbf{P})=1$, among which the pure real quaternions of unit length are the subfamily with vanishing imaginary part; the roots of $0$ are the origin and the nilpotent cone $(\mathbf{P},\mathbf{P})=0$; the roots of $+1$ are the images $\tilde Pi$ of the roots of $-1$, with the pure family $(\mathbf{P},\mathbf{P})=-1$. The three sets are disjoint. The block's own reading adds two facts the algebra does not have: the pure roots of $+1$ are in bijection with the non-trivial idempotents by $\mathbf{u}\mapsto\tfrac12(e_0+\mathbf{u})$, and every pure root of $\pm1$ is a zero divisor though it is invertible, the pure family of the block's zero divisors being the whole vector subspace. The non-zero roots of $0$ are the nilpotents, whose operator has index three.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\bullet\tilde Q$ | the symmetric plain product, the multiplication of the block |
| $\tilde P\bullet\tilde P=\tilde P^2$ | the square of the block is the plain square |
| $(\mathbf{P},\mathbf{P})=P_1^2+P_2^2+P_3^2$ | the complex square of the vector part, deciding the pure families |
| $\pm ie_0,\pm e_0$ | the central roots of $-1$ and of $+1$ |
| $(\mathbf{P},\mathbf{P})=1,0,-1$ | the pure families of the roots of $-1$, $0$, $+1$ |
| $\tilde P_+=\tilde P i$ | the bijection from the roots of $-1$ to the roots of $+1$ |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures*, §*The Root*, for the product-relative definition.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*, for the classification the block restates.
- *Square Roots of a General Element in the Symmetric Plain Algebra*, for the general root problem.
- *Idempotents of the Symmetric Plain Algebra*, for the bijection between the pure roots of $+1$ and the non-trivial idempotents.
- *Nilpotents of the Symmetric Plain Algebra*, for the non-zero roots of $0$ and their index-three operator.
- *Zero Divisors of the Symmetric Plain Algebra*, for the pure roots as zero divisors.
