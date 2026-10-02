
# __Positive Functionals and Self-Adjointness__

## Introduction

The involution of an ordered involutive algebra induces an involution on the dual space, $\varphi\mapsto\varphi^{*}$ with

$$
\varphi^{*}(a) = \overline{\varphi(a^{*})} ,
$$

and the functionals fixed by it are the **self-adjoint** (Hermitian) functionals, those with $\varphi(a^{*}) = \overline{\varphi(a)}$ for every $a$. The positive functionals are self-adjoint,

$$
\varphi\geq0 \implies \varphi = \varphi^{*} ,
$$

in a unital algebra, and this is the **self-adjointness of the positivity**: the positivity of a functional is a property of its **real** part, the imaginary part of a positive functional is invisible on the self-adjoint elements and vanishes, and the cone of the functionals is contained in the real vector space of the self-adjoint functionals. The article proves this, shows that the self-adjoint functionals form an ordered real vector space whose positive cone is the cone of the positive functionals, and describes the interaction of the self-adjointness with the positivity, the Cauchy–Schwarz inequality and the states.

The reason to isolate the self-adjointness is that it is the **dual** counterpart of the Hermitian elements: the involution acts on the algebra and on its dual, the self-adjoint elements are the fixed points of the first, the self-adjoint functionals the fixed points of the second, and the order lives on both. The positive functionals are the self-adjoint functionals that are positive on the cone, so the order of the algebra is the order of the self-adjoint functionals read through the duality $a\mapsto\varphi(a)$; this is the functional-level statement of *Self-Adjoint Elements and the Order*, and it is the reason the states of a physical theory are the positive **normalised** self-adjoint functionals.

The self-adjoint elements and their order are *Self-Adjoint Elements and the Order*; the positive functionals, the states and the extreme points are *The Cone of Positive Functionals*; the forms and the order are *Positive Definite Forms and the Order*; the Hermitian elements and the order unit are *Hermitian Elements and the Order Unit*; the ordered involution is *Ordered Involutive Algebras*; the Jordan order is *The Jordan Algebra of Self-Adjoint Elements*; the adjoint of a positive operator is *The Adjoint of a Positive Operator*; and the adjoint of the left multiplication is *The Adjoint of the Left Multiplication on an Ordered Algebra*. The operator-algebraic duality is *Operator Algebras* and *The Theory of von Neumann Algebras* of Part II.

## The Involution on the Dual

**Definition.** The **adjoint of a functional** is $\varphi^{*}(a) = \overline{\varphi(a^{*})}$; it is again linear, the map $\varphi\mapsto\varphi^{*}$ is **conjugate-linear** and an **involution** of the dual space, $(\varphi^{*})^{*} = \varphi$, and a functional is **self-adjoint** (or **Hermitian**) when $\varphi^{*} = \varphi$.

**Proposition (the decomposition of a functional).** Every functional decomposes uniquely as

$$
\varphi = \operatorname{Re}\varphi + i\operatorname{Im}\varphi , \qquad \operatorname{Re}\varphi = \tfrac12(\varphi + \varphi^{*}), \quad \operatorname{Im}\varphi = \tfrac1{2i}(\varphi - \varphi^{*}) ,
$$

into a sum of **self-adjoint** functionals; the self-adjoint functionals form a real vector space $A^{*}_{\mathrm{sa}}$, and the map $\varphi\mapsto\varphi^{*}$ is the identity on it and the reflection $\varphi\mapsto -\varphi$ on the imaginary direction.

*Proof.* The formulas are the standard decomposition of a complex-valued function into its real and imaginary parts with respect to the involution; the two summands are self-adjoint because $(\varphi^{*})^{*} = \varphi$ and $(\operatorname{Re}\varphi)^{*} = \operatorname{Re}\varphi$, $(\operatorname{Im}\varphi)^{*} = \operatorname{Im}\varphi$; the uniqueness is immediate from the definitions.

**Proposition (self-adjointness on the Hermitian elements).** A functional is self-adjoint if and only if it is **real** on the self-adjoint elements, $\varphi(h)\in\mathbb{R}$ for every $h = h^{*}$; consequently the self-adjoint functionals are the real-linear functionals on the Hermitian part extended conjugate-linearly to the algebra, and the duality between the self-adjoint elements and the self-adjoint functionals is the ordinary duality of real vector spaces.

*Proof.* If $\varphi = \varphi^{*}$ and $h = h^{*}$ then $\varphi(h) = \varphi^{*}(h) = \overline{\varphi(h^{*})} = \overline{\varphi(h)}$, so $\varphi(h)$ is real; conversely, if $\varphi$ is real on the self-adjoint elements then for arbitrary $a$ the decomposition $a = h + ik$ gives $\varphi(a^{*}) = \varphi(h - ik) = \varphi(h) - i\varphi(k)$ and $\overline{\varphi(a)} = \overline{\varphi(h) + i\varphi(k)} = \varphi(h) - i\varphi(k)$, so $\varphi(a^{*}) = \overline{\varphi(a)}$.

## The Self-Adjointness of the Positive Functionals

**Theorem (positivity implies self-adjointness).** In a unital involutive algebra with a positive functional $\varphi$ of $\varphi(1) > 0$, the functional is self-adjoint: $\varphi(a^{*}) = \overline{\varphi(a)}$ for every $a$.

*Proof.* For $\lambda\in\mathbb{C}$ the positivity gives $\varphi((\lambda + a)^{*}(\lambda + a))\geq0$, that is, $\lvert\lambda\rvert^{2}\varphi(1) + \lambda\varphi(a^{*}) + \bar\lambda\varphi(a) + \varphi(a^{*}a)\geq0$. For $\lambda = t$ real the left side is a real quadratic in $t$ that is nonnegative, so its linear coefficient $\varphi(a) + \varphi(a^{*})$ is **real**; for $\lambda = is$ real the coefficient is $i(\varphi(a^{*}) - \varphi(a))$, which is likewise **real**, so $\varphi(a^{*}) - \varphi(a)$ is purely imaginary. Hence $\operatorname{Im}\varphi(a^{*}) = -\operatorname{Im}\varphi(a)$ and $\operatorname{Re}\varphi(a^{*}) = \operatorname{Re}\varphi(a)$, which is $\varphi(a^{*}) = \overline{\varphi(a)}$.

**Corollary (the positive cone of the functionals).** The positive functionals form a convex cone in the real space of the self-adjoint functionals, and they are the self-adjoint functionals that are positive on the positive cone,

$$
A^{*}_{+} = A^{*}_{\mathrm{sa}}\cap\{\varphi : \varphi(A_+)\geq0\} ,
$$

so the order of the algebra is the order of the self-adjoint functionals restricted to the Hermitian elements.

*Proof.* The inclusion $A^{*}_+\subseteq A^{*}_{\mathrm{sa}}$ is the theorem; conversely a self-adjoint functional positive on $A_+$ is positive because $a^{*}a\in A_+$; the conic and convexity statements are immediate, and the order statement is the theorem that the order is the intersection of the forms.

**Proposition (the Cauchy–Schwarz inequality and the norm).** For a positive functional $\varphi$ the **Cauchy–Schwarz inequality**

$$
\lvert\varphi(b^{*}a)\rvert^{2}\leq\varphi(a^{*}a)\,\varphi(b^{*}b)
$$

holds, the functional is **continuous** for the order-unit norm, and in the unital case $\lVert\varphi\rVert = \varphi(1)$; the **states** are the positive functionals with $\varphi(1) = 1$, which are self-adjoint and are the normalised points of the cone.

*Proof.* The Cauchy–Schwarz inequality is that of *The Cone of Positive Functionals*; the continuity and the norm statement are the standard estimates $\lvert\varphi(a)\rvert\leq\varphi(1)\lVert a\rVert$ and the reverse bound; the identification of the states is the definition, together with the self-adjointness just proved.

## The Self-Adjointness and the Order

**Proposition (the order of the self-adjoint functionals).** The self-adjoint functionals form a real ordered vector space with the cone of the positive functionals as its positive cone; the order is

$$
\varphi\leq\psi \iff \psi - \varphi \ \text{ is positive} \iff \varphi(a)\leq\psi(a) \ \text{ for every } a\in A_+ ,
$$

and the order is **Archimedean** when the algebra has an order unit and the functionals are continuous for the order-unit norm; the order unit of the space of the functionals is the trace $\varphi\mapsto\operatorname{tr}(a)$, when it exists.

*Proof.* The definition of the cone order is the standard one; the equivalence is the definition of the positivity of the difference; the Archimedean property is the order-unit statement of *Ordered Vector Spaces and the Order Unit*; the order unit is the trace functional, positive and dominating by the definition of the trace.

**Theorem (the duality theorem for the order).** The order of the self-adjoint elements and the order of the self-adjoint functionals are the two sides of the same duality:

$$
a\geq0 \iff \varphi(a)\geq0 \ \text{ for every } \varphi\in A^{*}_{+} , \qquad \varphi\geq0 \iff \varphi(a)\geq0 \ \text{ for every } a\in A_+ ,
$$

and the **self-adjointness** is what makes the two readings consistent: on a non-self-adjoint functional the duality would fail on the imaginary directions of the algebra.

*Proof.* The first equivalence is the theorem that the order is the intersection of the forms of *Positive Definite Forms and the Order*; the second is the definition of the positivity of a functional; the consistency statement is the proposition above that a self-adjoint functional is real on the Hermitian elements, so the duality is a duality of real spaces.

**Corollary (the positive functionals and the adjoint).** The positive functionals are exactly the self-adjoint functionals that are **fixed** by the adjoint-involution and positive on the cone of the squares; the map $\varphi\mapsto\varphi^{*}$ preserves the positivity of the difference of two functionals, so the order on the self-adjoint functionals is compatible with the involution, exactly as the order on the self-adjoint elements is compatible with the involution of the algebra. This is the functional form of the self-adjointness of *Self-Adjoint Elements and the Order*.

*Proof.* The fixed-point statement is the definition of the self-adjointness; the compatibility of the order with the involution is that $\varphi\leq\psi\implies\varphi^{*}\leq\psi^{*}$, which holds because the cone of the positive functionals is contained in the fixed-point set; the identification with the element statement is the duality theorem.

## Worked Cases

### The Matrix Algebra

Let $A = M_n(\mathbb{C})$ with the trace form. The functionals are $a\mapsto\operatorname{tr}(\rho a)$ for a matrix $\rho$; the adjoint of the functional corresponds to the adjoint of $\rho$, and the self-adjoint functionals are those with $\rho$ self-adjoint. The positive functionals are the ones with $\rho\geq0$, they are automatically self-adjoint, and the states are the density matrices; the duality theorem is the ordinary duality of the Hermitian matrices. This is the finite-dimensional model.

### The Continuous Functions

Let $A = C(X,\mathbb{C})$ with the pointwise order. The functionals are the complex measures, the self-adjoint functionals are the real measures, and the positive functionals are the positive measures; the positive functionals are self-adjoint, and the duality theorem is the Riesz representation theorem: a continuous function is pointwise nonnegative if and only if every positive measure integrates it to a nonnegative value. The states are the probability measures.

### The Non-Unital Case

For an algebra without a unit the positivity of $\varphi(a^{*}a)$ alone does not force self-adjointness; the article's theorem uses the unit through the test elements $\lambda + a$. When the algebra has an approximate identity and the functional is bounded for the associated seminorm the self-adjointness is recovered, and in a $C^{*}$-algebra every positive functional is self-adjoint even without a unit. The commutative non-unital case $C_0(X)$ shows the mechanism: the positivity is tested at the points of $X$ and the self-adjointness follows pointwise.

## Summary

The involution of an ordered involutive algebra induces the **adjoint** $\varphi^{*}(a) = \overline{\varphi(a^{*})}$ on the dual, and the **self-adjoint functionals** are its fixed points; they are the functionals real on the self-adjoint elements and form a real vector space into which every functional decomposes as $\varphi = \operatorname{Re}\varphi + i\operatorname{Im}\varphi$. A **positive functional is self-adjoint** in a unital algebra (proved by the test elements $\lambda + a$), so the positive functionals form a convex cone in the space of the self-adjoint functionals, $A^{*}_+ = A^{*}_{\mathrm{sa}}\cap\{\varphi : \varphi(A_+)\geq0\}$; the **Cauchy–Schwarz** inequality, the continuity, the norm $\lVert\varphi\rVert = \varphi(1)$ and the identification of the **states** as the normalised positive functionals follow. The self-adjoint functionals are ordered by the cone of the positive functionals, the order is Archimedean for the continuous functionals, and the **duality theorem** $a\geq0\iff\varphi(a)\geq0$ for all positive $\varphi$ and $\varphi\geq0\iff\varphi(a)\geq0$ for all $a\geq0$ exhibits the order of the elements and the order of the functionals as two sides of one duality, made consistent by the self-adjointness. The self-adjoint elements are *Self-Adjoint Elements and the Order*; the positive functionals and the states are *The Cone of Positive Functionals*; the forms and the order are *Positive Definite Forms and the Order*; the Hermitian elements are *Hermitian Elements and the Order Unit*; the ordered involution is *Ordered Involutive Algebras*; the Jordan order is *The Jordan Algebra of Self-Adjoint Elements*; and the adjoints are *The Adjoint of a Positive Operator* and *The Adjoint of the Left Multiplication on an Ordered Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\varphi^{*}(a) = \overline{\varphi(a^{*})}$ | Adjoint of a functional |
| $\varphi = \varphi^{*}$ | Self-adjoint functional |
| $\varphi = \operatorname{Re}\varphi + i\operatorname{Im}\varphi$ | Decomposition into self-adjoint parts |
| $\varphi(h)\in\mathbb{R}$ for $h = h^{*}$ | Characterisation of self-adjointness |
| $\varphi\geq0\implies\varphi = \varphi^{*}$ | Positivity implies self-adjointness (unital) |
| $A^{*}_+ = A^{*}_{\mathrm{sa}}\cap\{\varphi(A_+)\geq0\}$ | Cone of the positive functionals |
| $\lvert\varphi(b^{*}a)\rvert^{2}\leq\varphi(a^{*}a)\varphi(b^{*}b)$ | Cauchy–Schwarz inequality |
| $\lVert\varphi\rVert = \varphi(1)$ | Norm of a positive functional |

## Further Reading

- Richard Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the positive functionals, the self-adjointness and the states.
- Gert K. Pedersen, *C\*-Algebras and their Automorphism Groups* (Academic Press, 1979), for the positive functionals, the Cauchy–Schwarz inequality and the norm.
- Jacques Dixmier, *Les C\*-algèbres et leurs représentations* (Gauthier-Villars, 1964), for the positive functionals, the states and the extreme points.
- Shoichiro Sakai, *C\*-Algebras and W\*-Algebras* (Springer, 1971), for the normal positive functionals and the duality.
- Charalambos D. Aliprantis and Owen Burkinshaw, *Positive Operators* (Academic Press, 1985), for the ordered dual, the positive functionals and the order-unit norm.
