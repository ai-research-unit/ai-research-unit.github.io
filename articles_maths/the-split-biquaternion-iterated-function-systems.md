# __The Split-Biquaternion Iterated Function Systems__

## Introduction

An iterated function system on the split-biquaternion algebra is a finite family of contractions, and because the algebra is the product of two quaternion algebras the system, its attractor and its dimension all reduce to the quaternion case on two factors: the operator norm of a left multiplication is the maximum of the moduli of the two components, the attractor of a system with diagonal generators is the product of the two quaternion attractors, and the similarity dimension is the sum of the two quaternion dimensions. The algebra is also the Clifford algebra $\mathrm{Cl}(0,3)$, so a system has a parity structure: an even generator preserves the even and the odd parts, an odd generator exchanges them. The article states the contraction criterion, the product attractor and its dimension, the parity structure of the systems and the role of the zero-divisor generators, and compares the theory with the biquaternion systems, where the idempotents are not central and the attractor of a diagonal system is only a slice.

The split-biquaternion algebra, its idempotents and its norm are *Split-Biquaternion Algebra*, *Split-Biquaternion Idempotents and Projections* and *Split-Biquaternion Norm and Invertibility*; the product decomposition of the family is *The Split-Biquaternion Quadratic Family*; the parity grading and the volume element are *The Clifford Decomposition of the Split-Biquaternion Fractals*; the quaternion systems and their dimension are *The Quaternion Iterated Function Systems*; and the classical theory, the open set condition and the similarity dimension are *Fractal Geometry* of Part IV.

The article owns the operator norm of a split-biquaternion generator, the contraction criterion, the product attractor and the sum of the dimensions, the parity structure of the generator list, and the zero-divisor generators. It does not re-derive the classical theory or the quaternion systems.

**Standing convention.** $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ via $\tilde Q=\tilde Q_+\tilde\Pi_1+\tilde Q_-\tilde\Pi_2$, and a left-affine generator is $f_i(\tilde Q)=\tilde A_i\tilde Q+\tilde B_i$ with $\tilde A_i=\tilde A_i^+\tilde\Pi_1+\tilde A_i^-\tilde\Pi_2$; $\|\cdot\|_E$ is the Euclidean norm of $\mathbb{R}^8$ and $|\cdot|$ the quaternion modulus.

## The Operator Norm and the Contraction Criterion

**Proposition (the operator norm).** For $\tilde A=\tilde A_+\tilde\Pi_1+\tilde A_-\tilde\Pi_2$ the operator norm of left multiplication is

$$
\|L_{\tilde A}\|=\max\bigl(|\tilde A_+|,\ |\tilde A_-|\bigr) ,
$$

and the generator $f(\tilde Q)=\tilde A\tilde Q+\tilde B$ is a contraction exactly when $\max(|\tilde A_+|,|\tilde A_-|)<1$.

**Proof.** In the idempotent coordinates $L_{\tilde A}$ acts by $(\tilde Q_+,\tilde Q_-)\mapsto(\tilde A_+\tilde Q_+,\tilde A_-\tilde Q_-)$, so

$$
\|L_{\tilde A}\tilde Q\|_E^2=\tfrac12\bigl(|\tilde A_+|^2|\tilde Q_+|^2+|\tilde A_-|^2|\tilde Q_-|^2\bigr)\le\max(|\tilde A_+|,|\tilde A_-|)^2\cdot\tfrac12\bigl(|\tilde Q_+|^2+|\tilde Q_-|^2\bigr) ,
$$

using the norm identity $\|\tilde Q\|_E^2=\tfrac12(|\tilde Q_+|^2+|\tilde Q_-|^2)$; the bound is attained on a vector supported on the factor of the maximum, so the norm is the maximum. The Lipschitz constant of the generator is the operator norm of $\tilde A$, whence the criterion.

**Remark (the diagonal multipliers).** If $\tilde A=\tilde A_+=\tilde A_-$ is one quaternion, the generator multiplies both factors by the same quaternion and is a similarity of ratio $|\tilde A|$; if only one component is non-zero, the generator maps the algebra into one ideal and its restriction to that ideal is a quaternion similarity. **The general split-biquaternion generator is a pair of quaternion generators acting independently on the two factors.**

## The Product Attractor and Its Dimension

**Theorem (the attractor is a product).** Let $f_i(\tilde Q)=\tilde A_i\tilde Q+\tilde B_i$, $i=1,\dots,m$, be a system of contractions. Then the attractor is the product

$$
K=K^+\times K^-,
$$

where $K^\pm$ are the attractors of the two quaternion systems $\{(\tilde A_i^\pm,\tilde B_i^\pm)\}_i$, and for the dimension, if both quaternion systems are systems of similarities satisfying the open set condition with ratios $r_i^\pm=|\tilde A_i^\pm|$, then

$$
\dim_HK=s_++s_-\ , \qquad \sum_{i=1}^m(r_i^+)^{s_+}=1,\qquad \sum_{i=1}^m(r_i^-)^{s_-}=1 .
$$

**Proof.** The Hutchinson operator of the system is the product of the Hutchinson operators of the two quaternion systems in the idempotent coordinates, so its fixed point is the product of the two quaternion attractors (*The Quaternion Iterated Function Systems*). The dimension is the product formula $\dim_H(A\times B)=\dim_H A+\dim_HB$ together with the similarity dimension of each factor (*Fractal Geometry*).

**Corollary (the dimension of a split-biquaternion system).** The Hausdorff dimension of the attractor of a split-biquaternion system of similarities with the open set condition is the sum of the two quaternion similarity dimensions, one for each idempotent factor, and it is at most $2\cdot 4=8$ and equals $8$ only in the degenerate case of ratios summing to full dimension in both factors.

**Remark (the system is the pair of its factor systems).** Every question about a split-biquaternion system that is a product question — the dimension, the connectivity, the local structure, the measure — is answered by the two quaternion systems. **The split-biquaternion systems are the quaternion systems with an extra bookkeeping factor, and the article states the reduction rather than a separate theory.**

## Zero-Divisor Generators

**Proposition (a zero divisor can multiply a contraction).** Let $\tilde A=\tilde A_+\tilde\Pi_1$ be a zero divisor, so $\tilde A_-=0$. Then $\|L_{\tilde A}\|=|\tilde A_+|$ and the generator $f(\tilde Q)=\tilde A\tilde Q+\tilde B$ is a contraction whenever $|\tilde A_+|<1$, with image contained in the ideal $\mathbb{H}\tilde\Pi_1$.

**Proof.** The operator norm formula with $\tilde A_-=0$; the image of $L_{\tilde A}$ is contained in $\mathbb{H}\tilde\Pi_1$ because $\tilde A_-\tilde Q_-=0$ kills the second component. No invertibility of $\tilde A$ is required for the attractor theorem, which needs only the contraction.

**Remark (the contrast with the biquaternion systems).** In the biquaternion algebra a zero-divisor multiplier is a contraction whose image avoids a direction, and the image subspace can be a proper complex subspace; here a zero-divisor multiplier kills one whole idempotent factor, so the attractor of the system is contained in the corresponding ideal and is a copy of a quaternion attractor. **The zero divisors of the split-biquaternion algebra act coordinatewise, and their effect on a system is the loss of one factor, not a collapse of the norm.**

**Remark (the open set condition at the zero divisors).** A generator whose multiplier vanishes on one factor is constant on that factor: two points that differ only in the killed component have the same image, so the pieces of the attractor are not separated on the corresponding ideal and the open set condition can fail there. A system whose attractor meets an ideal in a set of positive dimension has no strictly separated pieces over the ideal, and its dimension must be computed inside the two factors, by the product formula, rather than by a single similarity equation for the whole system. **In the biquaternion case the same failure occurs at the zero-divisor cone (*The Biquaternion Iterated Function Systems*), and in the split-quaternion case of signature $(2,2)$ at the null cone of the indefinite norm (*The Split-Quaternion Quadratic Map and Its Julia Sets*); the split-biquaternion failure is the coordinatewise one of the two ideals.**

## The Parity Structure of the Systems

**Proposition (even and odd generators).** Let $\tilde A\in\mathbb{H}_{\mathbb{D}}$ be written $\tilde A=\tilde A^0+j\tilde A^1$ with $\tilde A^0$ even and $j\tilde A^1$ odd. Then

1. if $\tilde A$ is even ($\tilde A^1=0$), left multiplication by $\tilde A$ preserves the even part and the odd part;
2. if $\tilde A$ is odd ($\tilde A^0=0$), left multiplication by $\tilde A$ exchanges the even part and the odd part.

**Proof.** $\tilde A(\tilde C+j\tilde D)=\tilde A\tilde C+j\tilde A\tilde D$ in the even case, so the parity of the two terms is preserved; in the odd case $\tilde A=j\tilde A^1$ gives $j\tilde A^1\tilde C+\tilde A^1\tilde D$, whose first term is odd and second even, so the parities are exchanged.

**Corollary (parity-preserving systems).** A system whose generators all have even multipliers preserves the parity decomposition, and its attractor is the union of an even attractor and an odd attractor exchanged by the volume-element symmetry; a system with an odd multiplier moves mass between the two chiral sides and has an attractor that is not parity-split.

**Remark (the two gradings of a system).** A split-biquaternion system has the idempotent (product) structure and the parity (Clifford) structure, and the two are different: the first splits the attractor into two independent factors and is available for every system, the second constrains the generator list and describes how the system respects the division subalgebra of the even part. **The Clifford grading of the algebra is a constraint on the systems, and the product structure of the algebra is a reduction of the systems; the article states both.**

## Summary

The split-biquaternion iterated function systems reduce to quaternion systems on the two idempotent factors: the operator norm of a left multiplication is the maximum of the moduli of the two quaternion components, so a generator is a contraction exactly when both component multipliers have modulus below one; the attractor of a diagonal system is the product of the two quaternion attractors, and the similarity dimension is the sum of the two quaternion dimensions, by the product formula. A zero-divisor multiplier kills one factor, is a legitimate contraction and produces an attractor in the corresponding ideal. The Clifford parity grading constrains the systems: an even generator preserves the even and the odd parts, an odd generator exchanges them, and a parity-preserving system has its attractor split by the parity decomposition. The split-biquaternion systems are the quaternion systems read on two factors with the parity bookkeeping added, and the comparison with the biquaternion systems is the comparison of a product theory with a coupled one.

## Summary of Notation

| symbol | meaning |
|---|---|
| $f_i(\tilde Q)=\tilde A_i\tilde Q+\tilde B_i$ | a generator |
| $\tilde A_i^\pm$ | the two quaternion components of the multiplier |
| $\|L_{\tilde A}\|=\max(|\tilde A_+|,|\tilde A_-|)$ | the operator norm |
| $K=K^+\times K^-$ | the attractor |
| $s_\pm$ | the two quaternion similarity dimensions |
| $s_++s_-$ | the dimension of the split-biquaternion attractor |
| $\mathbb{H}\tilde\Pi_{1,2}$ | the ideals reached by zero-divisor generators |

## Further Reading

- *The Quaternion Iterated Function Systems* (`articles_maths/the-quaternion-iterated-function-systems.md`), for the two factor theories.
- *The Split-Biquaternion Quadratic Family* (`articles_maths/the-split-biquaternion-quadratic-family.md`), for the norm identity and the product decomposition used in the operator-norm computation.
- *The Clifford Decomposition of the Split-Biquaternion Fractals* (`articles_maths/the-clifford-decomposition-of-the-split-biquaternion-fractals.md`), for the parity grading of the generators.
- *Split-Biquaternion Zero Divisors* (`articles_maths/split-biquaternion-zero-divisors.md`), for the ideals of the zero-divisor generators.
- *Fractal Geometry* (`articles_maths/fractal-geometry.md`) and *Iterated Function Systems in the Complex Plane* (`articles_maths/iterated-function-systems-in-the-complex-plane.md`), for the attractor theorem, the similarity dimension and the product formula.
