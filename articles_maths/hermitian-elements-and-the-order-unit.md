
# __Hermitian Elements and the Order Unit__

## Introduction

The **Hermitian elements** of an involutive algebra are the fixed points of the involution, $H(A) = \{a : a^{*} = a\}$; they form a real vector subspace, and the positive cone of the algebra restricts to a cone in it, so that $H(A)$ is an **ordered vector space** with the order of *The Positive Cone of an Involutive Algebra*. When the algebra is unital and reduced the identity is Hermitian and positive, $1 = 1^{*}1 > 0$, and it is an **order unit**: for every Hermitian $h$ there is $\lambda>0$ with $-\lambda1\leq h\leq\lambda1$, the least such $\lambda$ being the **order-unit seminorm** of $h$, which in a $\ast$-normed algebra coincides with the norm. The order unit is therefore the bridge between the algebraic decomposition of an element and the order: it is the calibration against which the Hermitian elements are measured, and the **state space** of the algebra is its dual base, the set of the positive functionals that take the value $1$ at the order unit.

The article develops the **order and the decomposition**. Every element decomposes as $a = \operatorname{Re}a + i\operatorname{Im}a$ into two Hermitian elements, and every Hermitian element decomposes with respect to the order unit into its positive and negative parts, $h = h_+ - h_-$ with $h_+\geq0$, $h_-\geq0$ and $h_+h_- = 0$; the two decompositions are orthogonal in a precise sense, and the order interval $[-1,1]$ is the **unit ball** of the order-unit norm. The consequential facts are that the Hermitian part is an **ordered real vector space** whose order interval at the unit is the unit ball, that the involution is an order isomorphism, and that every Hermitian element is the difference of two commuting positive elements — the **Jordan decomposition** — which is what makes the order of an involutive algebra a lattice-like order on the commuting parts.

The ordered vector space and the order unit are *Ordered Vector Spaces and the Order Unit* and *The Order Unit as an Operator*; the positive cone and its closure properties are *The Positive Cone of an Involutive Algebra*; the states and the extreme points are *The Cone of Positive Functionals*; the ordered involutive algebra as a structure is *Ordered Involutive Algebras*; the Hilbert cone and its positivity are *The Hilbert Cone of an Involutive Algebra*; the self-adjoint elements of a C\*-algebra, the model of this article, are *The Jordan Algebra of Self-Adjoint Elements*; and the $JB$-structures are *JB\*-Algebras and the Gelfand–Naimark Theorem*.

## The Hermitian Part as an Ordered Space

**Definition.** The **Hermitian part** of the involutive algebra $A$ is $H(A) = \{a : a^{*} = a\}$; the **skew part** is $\{a : a^{*} = -a\} = iH(A)$. The **order** of $H(A)$ is that of the cone, $h\leq k\iff k - h\in A_+$.

**Proposition (the Hermitian part is an ordered real vector space).** $H(A)$ is a real vector subspace of $A$ of real dimension $\dim_{\mathbb{C}}A$, closed under the **symmetrised product** $\{h,k\} = \frac12(hk + kh)$, and the cone $H(A)\cap A_+$ is a proper cone when $A$ is reduced; the identity is Hermitian and positive, $1 = 1^{*}1\in A_+$.

*Proof.* If $h^{*} = h$ and $k^{*} = k$ then $(\alpha h + \beta k)^{*} = \alpha h + \beta k$ for real $\alpha,\beta$, so $H(A)$ is a real subspace, and its real dimension is that of $A$ over $\mathbb{C}$ because the map $a\mapsto\operatorname{Re}a$ is a real isomorphism onto $H(A)$; the symmetrised product of two Hermitian elements is Hermitian because $hk + kh$ is, using the anti-multiplicativity; the cone is proper by the reducedness; the identity is Hermitian and $1 = 1^{*}1$.

**Proposition (every element is a complex combination of two Hermitian elements).** Every $a\in A$ has a unique decomposition

$$
a = h + ik, \qquad h = \tfrac12(a + a^{*}) = \operatorname{Re}a, \quad k = \tfrac1{2i}(a - a^{*}) = \operatorname{Im}a ,
$$

with $h,k\in H(A)$; and $a$ is normal, Hermitian, or positive according as $hk = kh$, $k = 0$, or $k = 0$ and $h\geq0$.

*Proof.* The verification that $h$ and $k$ are Hermitian and that $a = h + ik$ is direct; conversely if $a = h + ik$ with $h,k$ Hermitian then $\tfrac12(a + a^{*}) = h$ and $\tfrac1{2i}(a - a^{*}) = k$, so the decomposition is unique. The normality criterion is $a^{*}a = aa^{*}$, which reads $hk = kh$ for the decomposition; the Hermitian and the positive cases are specialisations.

## The Order Unit

**Definition.** An **order unit** of $H(A)$ is an element $u > 0$ such that for every $h$ there is $\lambda>0$ with $-\lambda u\leq h\leq\lambda u$; an order unit is **strong** when in addition every nonempty majorised set has a least upper bound, and the **order-unit seminorm** is

$$
\lVert h\rVert_u = \inf\{\lambda>0 : -\lambda u\leq h\leq\lambda u\} .
$$

**Proposition (the identity is an order unit).** When $A$ is a unital reduced involutive algebra the identity is a positive order unit of $H(A)$; in a $\ast$-normed algebra with $\lVert a^{*}a\rVert = \lVert a\rVert^{2}$ the order-unit norm at the identity is the given norm, $\lVert h\rVert_1 = \lVert h\rVert$, and the order interval $[-1,1]$ is the unit ball of $H(A)$ in that norm.

*Proof.* $1>0$; for a Hermitian $h$ the bound $-\lVert h\rVert1\leq h\leq\lVert h\rVert1$ is the spectral bound in a $\ast$-normed algebra, so $1$ is an order unit and $\lVert h\rVert_1\leq\lVert h\rVert$; conversely the order interval estimate $-\lambda1\leq h\leq\lambda1$ gives $\lVert h\rVert\leq\lambda$ by the norm estimate on the positive cone, so $\lVert h\rVert = \lVert h\rVert_1$. The interval $[-1,1]$ is the set of Hermitian elements of norm at most one, which is the unit ball.

**Proposition (the states are the unit's dual base).** The **states**, the positive functionals with $\varphi(1) = 1$, are the base of the dual cone $A_+^{*}$ at the order unit, and they separate the points of $H(A)$; the order of $H(A)$ is the order of the evaluation functionals, $h\leq k\iff\varphi(h)\leq\varphi(k)$ for every state $\varphi$.

*Proof.* The normalisation $\varphi(1) = 1$ cuts the dual cone in a base because $\varphi(1)>0$ for every nonzero positive functional in the unital case; separation and the order representation are the Hahn–Banach theorem together with the fact that a Hermitian element that is nonpositive has a state seeing it, which is a consequence of the Hahn–Banach theorem applied in the ordered space $H(A)$ with the order unit.

## The Decomposition with Respect to the Order Unit

**Theorem (the Jordan decomposition).** Let $A$ be a unital reduced involutive algebra that is $\ast$-normed with $\lVert a^{*}a\rVert = \lVert a\rVert^{2}$, and let $h\in H(A)$. Then there are unique commuting positive elements $h_+,h_-$ with

$$
h = h_+ - h_-, \qquad h_+h_- = 0, \qquad \lVert h\rVert = \max(\lVert h_+\rVert,\lVert h_-\rVert) ,
$$

the **positive part** $h_+$ and the **negative part** $h_-$; the decomposition is produced by the functional calculus, $h_\pm = \tfrac12(\lvert h\rvert\pm h)$ with $\lvert h\rvert = (h^{2})^{1/2}$, and it is the decomposition of $h$ with respect to the order unit.

*Proof.* The element $\lvert h\rvert$ is defined by the functional calculus and commutes with $h$; then $h_\pm = \tfrac12(\lvert h\rvert\pm h)$ are positive, commute, satisfy $h_+ - h_- = h$ and $h_+h_- = \tfrac14(\lvert h\rvert^{2} - h^{2}) = 0$, so the decomposition exists; the norm identity is the spectral identity $\lVert h\rVert = \max(\lVert h_+\rVert,\lVert h_-\rVert)$, because the spectra are separated by the sign. Uniqueness: if $h = p - q$ with $p,q\geq0$ commuting and $pq = 0$, then $p - q = h$ and $p + q = \lvert h\rvert$ by the square $\lvert h\rvert^{2} = h^{2} = (p+q)^{2}$ and the positivity of $p+q$, so $p = \tfrac12(\lvert h\rvert + h) = h_+$ and $q = h_-$.

**Corollary (the order interval and the unit ball; the absolute value).** The order interval $[-1,1]$ consists of the Hermitian elements with $\lVert h\rVert\leq1$; every Hermitian element has an **absolute value** $\lvert h\rvert = (h^{2})^{1/2}$ with $\lvert h\rvert\geq\pm h$, and $a^{*}a\geq0$ for every $a$, so the absolute value of an element is $(\operatorname{Re}(a^{*}a))^{1/2}$.

*Proof.* The interval identification is the proposition above; the absolute value is the positive square root of $h^{2}$, which satisfies $\lvert h\rvert\pm h\geq0$ by the decomposition; and $a^{*}a\in A_+$ by the definition of the cone, with $a^{*}a$ Hermitian.

**Proposition (the involution preserves the order unit and the decomposition).** The involution fixes $1$, is an order isomorphism of $H(A)$, and carries the decomposition $a = h + ik$ to $a^{*} = h - ik$; on a Hermitian element it preserves the positive and the negative parts, $(h_+)^{*} = h_+$ and $(h_-)^{*} = h_-$.

*Proof.* $1^{*} = 1$ by the definition of the involution of a unital algebra; the order isomorphy is the positivity of the involution of *The Positive Cone of an Involutive Algebra*; the decomposition statement is the conjugate-linearity on the imaginary part and the Hermitian property of the parts.

## Worked Cases

### The Self-Adjoint Operators

Let $A = B(H)$ with the operator adjoint. The Hermitian elements are the self-adjoint operators, the order is the Loewner order, the order unit is the identity, and the Jordan decomposition is the spectral decomposition into the positive and the negative spectral parts: $h_+ = \int_{0}^{\infty}\lambda\, \mathrm{d}E_\lambda$ and $h_- = -\int_{-\infty}^{0}\lambda\, \mathrm{d}E_\lambda$ for the spectral measure $E$ of $h$. The order interval $[-1,1]$ is the set of the self-adjoint contractions, and the states are the density matrices. This is the model instance.

### The Continuous Functions

Let $A = C(X,\mathbb{C})$ with pointwise conjugation. The Hermitian elements are the real-valued continuous functions, the order is pointwise, the order unit is the constant function $1$, and the Jordan decomposition is the pointwise decomposition $h_+ = \max(h,0)$, $h_- = \max(-h,0)$. The Hermitian part is the **lattice-ordered** $C(X,\mathbb{R})$, in which every pair has a least upper bound; this is the commutative extreme, and in it the order unit is strong.

### The Group Algebra

Let $A = \mathbb{C}[G]$ with $g^{*} = g^{-1}$. The Hermitian elements are the elements with $a^{*} = a$, the order unit is the identity of the unit group, and the Jordan decomposition is the decomposition of a self-adjoint element of the group algebra into its positive and negative parts in the Hilbert cone of *The Hilbert Cone of an Involutive Algebra*; the states are the positive-definite functions on $G$ normalised to $1$ at the identity, which is the classical correspondence between the states and the positive-definite functions.

## Summary

The **Hermitian part** $H(A)$ of an involutive algebra is a real ordered vector space of real dimension $\dim_{\mathbb{C}}A$, closed under the symmetrised product, with the cone $H(A)\cap A_+$; every element decomposes uniquely as $a = \operatorname{Re}a + i\operatorname{Im}a$ into Hermitian parts. The identity is a positive **order unit** in the unital reduced algebra, $\lVert h\rVert_1 = \lVert h\rVert$ in a $\ast$-normed algebra, and the order interval $[-1,1]$ is the **unit ball**; the **states** are the base of the dual cone at the order unit and separate the points. Every Hermitian element has the **Jordan decomposition** $h = h_+ - h_-$ with $h_\pm\geq0$, $h_+h_- = 0$ and $\lVert h\rVert = \max(\lVert h_+\rVert,\lVert h_-\rVert)$, produced by the functional calculus through the **absolute value** $\lvert h\rvert = (h^{2})^{1/2}$, and the involution fixes the order unit and preserves the decomposition. The order and the order unit are *Ordered Vector Spaces and the Order Unit* and *The Order Unit as an Operator*; the cone is *The Positive Cone of an Involutive Algebra*; the states are *The Cone of Positive Functionals*; the ordered involutive algebra is *Ordered Involutive Algebras*; the Hilbert cone is *The Hilbert Cone of an Involutive Algebra*; the self-adjoint model is *The Jordan Algebra of Self-Adjoint Elements*; and the JB-theory is *JB\*-Algebras and the Gelfand–Naimark Theorem*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H(A) = \{a : a^{*} = a\}$ | Hermitian part, an ordered real vector space |
| $a = \operatorname{Re}a + i\operatorname{Im}a$ | Decomposition into Hermitian parts |
| $\lVert h\rVert_u = \inf\{\lambda : -\lambda u\leq h\leq\lambda u\}$ | Order-unit seminorm |
| $1$ | Order unit of the unital reduced algebra |
| $\lVert h\rVert_1 = \lVert h\rVert$ | The order-unit norm is the $\ast$-norm |
| $\lvert h\rvert = (h^{2})^{1/2}$ | Absolute value |
| $h = h_+ - h_-$ | Jordan decomposition, $h_+h_- = 0$ |
| $\varphi(1) = 1$ | State, the base of the dual cone |

## Further Reading

- Richard Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the Hermitian part, the order unit and the states of an operator algebra.
- Gert K. Pedersen, *C\*-Algebras and their Automorphism Groups* (Academic Press, 1979), for the functional calculus, the absolute value and the polar decomposition.
- Erik M. Alfsen and Frederik W. Shultz, *State Spaces of Operator Algebras* (Birkhäuser, 2001), for the order unit, the state space and its facial structure.
- Shoichiro Sakai, *C\*-Algebras and W\*-Algebras* (Springer, 1971), for the states, the positive functionals and the extreme points.
- Charalambos D. Aliprantis and Owen Burkinshaw, *Positive Operators* (Academic Press, 1985), for the order-unit seminorm and the ordered vector spaces of an involutive algebra.
