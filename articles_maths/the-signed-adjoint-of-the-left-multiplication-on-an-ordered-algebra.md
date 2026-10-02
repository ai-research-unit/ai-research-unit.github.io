
# __The Signed Adjoint of the Left Multiplication on an Ordered Algebra__

## Introduction

The **signed left multiplication** of a graded algebra is the one-sided operator

$$
L^{\alpha}_a : x\mapsto a\,\alpha(x) = (L_a\circ\Gamma)(x) ,
$$

the left multiplication with the argument twisted by the grade involution; its companion is the **signed right multiplication** $R^{\alpha}_a x = \alpha(x)a$. The article computes their **adjoints** for the trace form:

$$
\bigl(L^{\alpha}_a\bigr)^{*} = L^{\alpha}_{\alpha(a^{*})} , \qquad \bigl(R^{\alpha}_a\bigr)^{*} = R^{\alpha}_{\alpha(a^{*})} ,
$$

so the adjoint of a signed left multiplication is again a signed left multiplication, with the parameter replaced by the $\alpha$-twist of the adjoint. The computation has two ingredients: the adjoint of the grading operator, $\Gamma^{*} = \alpha$, which is the statement that the grade involution is **self-adjoint** for the trace form, and the adjoint of the unsigned left multiplication, $(L_a)^{*} = L_{a^{*}}$; the product rule then gives $(L_a\Gamma)^{*} = \Gamma^{*}L_{a^{*}} = \alpha L_{a^{*}} = L_{\alpha(a^{*})}\alpha = L^{\alpha}_{\alpha(a^{*})}$. The identity grade involution recovers $(L_a)^{*} = L_{a^{*}}$ of *The Adjoint of the Left Multiplication on an Ordered Algebra*.

The article states the formula, identifies the **self-adjoint** and the **skew-adjoint** signed left multiplications (the parameters with $a = \alpha(a^{*})$ and $a = -\alpha(a^{*})$), relates the result to the twisted composition law $L^{\alpha}_aL^{\alpha}_b = L_{a\alpha(b)}$ and to the reflection elements, and describes the interaction with the **order**: a signed left multiplication with a positive grade involution and a positive parameter is a positive operator, its adjoint is positive, and the **order detects the parity** exactly as it does for the sandwich, because on the odd part the signed operator is the negative of the unsigned one. The adjoint of the signed left multiplication is thus the one-sided counterpart of *The Signed Adjoint Sandwich on an Ordered Algebra* and of *The Signed Adjoint of the Reflection on an Ordered Algebra*.

The signed left multiplication is *The Signed Left Multiplication on an Ordered Algebra*; the reflections and the reflection elements are *Reflections as Signed Two-Sided Operators on an Ordered Algebra*; the signed sandwich and its adjoint are *The Signed Sandwich on an Ordered Algebra* and *The Signed Adjoint Sandwich on an Ordered Algebra*; the signed adjoint of the reflection is *The Signed Adjoint of the Reflection on an Ordered Algebra*; the unsigned left multiplication and its adjoint are *The Adjoint of the Left Multiplication on an Ordered Algebra*; the graded action is *The Graded Action on a Module over an Ordered Algebra*; the adjoint and the positivity are *The Adjoint of a Positive Operator*; the order of the elements is *Self-Adjoint Elements and the Order*; the order is *Ordered Vector Spaces and the Order Unit* and *Positive Operators on an Ordered Space*; the grading is *Superalgebras and Graded Structures* of Part I; and the algebra is *Ordered Involutive Algebras*.

## The Adjoint of the Signed One-Sided Multiplications

**Definition.** For $a\in A$ the **signed left multiplication** and the **signed right multiplication** are

$$
L^{\alpha}_a : A\to A, \quad L^{\alpha}_a x = a\,\alpha(x) , \qquad R^{\alpha}_a : A\to A, \quad R^{\alpha}_a x = \alpha(x)\,a ,
$$

and they factor as $L^{\alpha}_a = L_a\Gamma$ and $R^{\alpha}_a = R_a\Gamma$ through the grading operator $\Gamma = \alpha$ on the underlying vector space.

**Theorem (the adjoints).** For the trace form,

$$
\bigl(L^{\alpha}_a\bigr)^{*} = L^{\alpha}_{\alpha(a^{*})} , \qquad \bigl(R^{\alpha}_a\bigr)^{*} = R^{\alpha}_{\alpha(a^{*})} ,
$$

so the adjoint of a signed one-sided multiplication is a signed one-sided multiplication with the $\alpha$-twisted adjoint parameter, and the family of the signed one-sided multiplications is **closed under the adjoint**.

*Proof.* The grading operator is self-adjoint, $\Gamma^{*} = \alpha$: indeed $\langle\Gamma x,y\rangle = \operatorname{tr}((\alpha(x))^{*}y) = \operatorname{tr}(\alpha(x^{*})y) = \operatorname{tr}(x^{*}\alpha^{-1}(y)) = \langle x,\alpha(y)\rangle$, using that $\alpha$ commutes with the involution and preserves the trace. Hence $\bigl(L_a\Gamma\bigr)^{*} = \Gamma^{*}L_{a^{*}} = \alpha L_{a^{*}} = L_{\alpha(a^{*})}\alpha = L^{\alpha}_{\alpha(a^{*})}$, using $(L_a)^{*} = L_{a^{*}}$ of *The Adjoint of the Left Multiplication on an Ordered Algebra* and the relation $\alpha L_c = L_{\alpha(c)}\alpha$. The right-handed computation is the same.

**Corollary (the identity grade involution).** When $\alpha$ is the identity, $\bigl(L_a\bigr)^{*} = L_{a^{*}}$ and $\bigl(R_a\bigr)^{*} = R_{a^{*}}$, the unsigned case of *The Adjoint of the Left Multiplication on an Ordered Algebra*.

*Proof.* The formula with $\alpha = 1$.

**Corollary (the twisted composition and its adjoint).** The signed one-sided multiplications compose by the twisted law $L^{\alpha}_aL^{\alpha}_b = L_{a\alpha(b)}$, and the adjoint of a product is the product of the adjoints in the reverse order,

$$
\bigl(L^{\alpha}_aL^{\alpha}_b\bigr)^{*} = \bigl(L^{\alpha}_b\bigr)^{*}\bigl(L^{\alpha}_a\bigr)^{*} = L^{\alpha}_{\alpha(b^{*})}L^{\alpha}_{\alpha(a^{*})} = L_{\alpha(b^{*})a^{*}} ,
$$

which agrees with the direct computation $(L_{a\alpha(b)})^{*} = L_{(a\alpha(b))^{*}} = L_{\alpha(b^{*})a^{*}}$; hence the adjoint is compatible with the twisted composition law.

*Proof.* The composition law is that of *The Signed Left Multiplication on an Ordered Algebra*; the anti-homomorphism property is general for operators; the direct computation uses $(L_c)^{*} = L_{c^{*}}$ and $(a\alpha(b))^{*} = \alpha(b)^{*}a^{*} = \alpha(b^{*})a^{*}$; the two agree.

## Self-Adjointness and Skew-Adjointness

**Proposition (the self-adjoint signed one-sided multiplications).** The signed left multiplication is self-adjoint,

$$
\bigl(L^{\alpha}_a\bigr)^{*} = L^{\alpha}_a ,
$$

exactly when the parameter is **$\alpha$-Hermitian**, $a = \alpha(a^{*})$; it is **skew-adjoint**, $\bigl(L^{\alpha}_a\bigr)^{*} = -L^{\alpha}_a$, exactly when $a = -\alpha(a^{*})$.

*Proof.* The operator $L^{\alpha}_a$ is the left multiplication by $a$ of the graded structure; its adjoint is $L^{\alpha}_{\alpha(a^{*})}$, so the self-adjointness is $\alpha(a^{*}) = a$; the skew-adjointness is the equation with the minus sign.

**Corollary (the decomposition of a signed left multiplication).** Every signed left multiplication decomposes into the self-adjoint and the skew-adjoint parts,

$$
L^{\alpha}_a = \tfrac12\bigl(L^{\alpha}_a + L^{\alpha}_{\alpha(a^{*})}\bigr) + \tfrac12\bigl(L^{\alpha}_a - L^{\alpha}_{\alpha(a^{*})}\bigr) ,
$$

and it is **normal** exactly when the two parts commute; in particular the $\alpha$-Hermitian parameters give the self-adjoint signed left multiplications, which form a real vector space.

*Proof.* The decomposition is the standard one for an operator with an adjoint; the normality criterion is $TT^{*} = T^{*}T$; the linearity in the parameter gives the vector-space statement.

**Proposition (the reflection elements and the adjoint).** If $a$ is a reflection element, $\alpha(a) = a^{-1}$, then $L^{\alpha}_a$ is an involution of the underlying vector space and its adjoint is $L^{\alpha}_{\alpha(a^{*})}$, again an involution; the two-sided reflection of *Reflections as Signed Two-Sided Operators on an Ordered Algebra* is $\tau_a = L^{\alpha}_aR_{\alpha(a)^{-1}} = L^{\alpha}_aR_a$, and its adjoint is the product of the adjoints in the reverse order, which is the reflection $\tau_{\alpha(a^{*})}$ of *The Signed Adjoint of the Reflection on an Ordered Algebra*.

*Proof.* The involution statement is the square formula $(L^{\alpha}_a)^{2} = L_{a\alpha(a)}$ of *The Signed Left Multiplication on an Ordered Algebra*, which is the identity for a reflection element because $a\alpha(a) = 1$; the adjoint is the theorem; the factorisation of the reflection is the proposition of the same article, and the adjoint product is the anti-homomorphism applied to the two factors.

## The Adjoint and the Order

**Theorem (the order of the signed left multiplications).** If the grade involution is **positive** and $a\geq0$, then

$$
L^{\alpha}_a\geq0 \quad \text{and} \quad R^{\alpha}_a\geq0 , \qquad \bigl(L^{\alpha}_a\bigr)^{*}\geq0 \quad \text{and} \quad \bigl(R^{\alpha}_a\bigr)^{*}\geq0 ,
$$

so the signed one-sided multiplications of positive parameters are positive and their adjoints are positive; the family is **closed under the adjoint** and the adjoint is an order isomorphism of it.

*Proof.* The positivity of $L^{\alpha}_a$ and $R^{\alpha}_a$ is the positivity proposition of *The Signed Left Multiplication on an Ordered Algebra*; the positivity of the adjoints is the general positivity preservation of *The Adjoint of a Positive Operator*; the order-isomorphism statement is the two-sided preservation.

**Corollary (the order detects the parity).** On the even part the signed left multiplication agrees with the unsigned one, and on the odd part it is its negative, $L^{\alpha}_ax = \varepsilon_xL_ax$ for homogeneous $x$; hence the signed left multiplication is positive for all positive $a$ exactly when the grade involution is positive, and the adjoint transports the same parity, so the order is the invariant that detects the sign of the grading.

*Proof.* The parity formula is the definition of the signed left multiplication in the graded case; the positivity criterion is the theorem; the adjoint statement is the parity of the adjoint, which is the same because the adjoint of the even part is the even part.

**Corollary (the order interval at the identity).** If the family is generated by the $L^{\alpha}_a$ with $a\geq0$ and the grade involution is positive, then the order interval at the identity is the set of the $L^{\alpha}_a$ with $L^{\alpha}_a\leq I$, and the adjoint preserves the interval; the signed left multiplications of the $\alpha$-Hermitian parameters combine with the self-adjointness, so the interval is adjoint stable.

*Proof.* The interval is defined by the order of the operators; the preservation by the adjoint is the order isomorphism; the $\alpha$-Hermitian statement is the self-adjointness criterion.

## Worked Cases

### The Matrix Algebra

Let $A = M_n(\mathbb{C})$ with the trace form and the parity grading $\alpha(X) = UXU^{-1}$ for the diagonal sign matrix $U$. The signed left multiplication is $L^{\alpha}_a(X) = aUXU^{-1}$, and its adjoint is $L^{\alpha}_{\alpha(a^{*})}(X) = \alpha(a^{*})UXU^{-1}$; the self-adjoint signed left multiplications are the $\alpha$-Hermitian parameters, and the positivity is the positivity of $a$ together with the positivity of the grading. This is the finite-dimensional model.

### The Biquaternion Algebra

Let $A = \mathbb{B} = M_2(\mathbb{C})$ with the $\operatorname{diag}(1,-1)$ grading. The signed left multiplication is the ordinary left multiplication composed with the grading operator; because the grade involution is inner, it is the unsigned left multiplication at the shifted parameter, and its adjoint is the unsigned adjoint at the corresponding shifted parameter. The example shows that the signed and the unsigned adjoints agree after the inner shift, and that the $\alpha$-Hermiticity criterion is the appropriate one.

### The Clifford Algebra

Let $A = \mathrm{Cl}(V,q)$ with the parity grading and let $e$ be a vector with $e^2 = -1$, an odd reflection element. The signed left multiplication $L^{\alpha}_e$ is an involution, its adjoint is $L^{\alpha}_{\alpha(e^{*})} = L^{\alpha}_{-e^{*}}$, and the reflection $\tau_e = L^{\alpha}_eR_e$ has the adjoint $\tau_{\alpha(e^{*})}$ of *The Signed Adjoint of the Reflection on an Ordered Algebra*. The Clifford case is the geometric instance of the one-sided adjoint formula.

## Summary

The **signed left multiplication** $L^{\alpha}_ax = a\alpha(x) = (L_a\Gamma)x$ and the **signed right multiplication** $R^{\alpha}_ax = \alpha(x)a$ of a graded ordered involutive algebra have, for the trace form, the adjoints

$$
\bigl(L^{\alpha}_a\bigr)^{*} = L^{\alpha}_{\alpha(a^{*})} , \qquad \bigl(R^{\alpha}_a\bigr)^{*} = R^{\alpha}_{\alpha(a^{*})} ,
$$

because the grading operator is self-adjoint, $\Gamma^{*} = \alpha$; hence the family of the signed one-sided multiplications is **closed under the adjoint**, the identity grade involution recovers $(L_a)^{*} = L_{a^{*}}$, and the adjoint is compatible with the twisted composition law $L^{\alpha}_aL^{\alpha}_b = L_{a\alpha(b)}$. The signed left multiplication is **self-adjoint** exactly for the **$\alpha$-Hermitian** parameters, $a = \alpha(a^{*})$, and **skew-adjoint** for the skew ones; it decomposes into the self-adjoint and the skew-adjoint parts and is normal when these commute. With a positive grade involution and a positive parameter the signed one-sided multiplications are **positive** and so are their adjoints, so the adjoint is an **order isomorphism** of the family; the order **detects the parity**, since on the odd part the signed operator is the negative of the unsigned one. The signed left multiplication is *The Signed Left Multiplication on an Ordered Algebra*; the reflections are *Reflections as Signed Two-Sided Operators on an Ordered Algebra*; the sandwich and its adjoint are *The Signed Sandwich on an Ordered Algebra* and *The Signed Adjoint Sandwich on an Ordered Algebra*; the adjoint of the reflection is *The Signed Adjoint of the Reflection on an Ordered Algebra*; the unsigned case is *The Adjoint of the Left Multiplication on an Ordered Algebra*; the graded action is *The Graded Action on a Module over an Ordered Algebra*; the adjoint and the positivity are *The Adjoint of a Positive Operator*; the order is *Self-Adjoint Elements and the Order* and *Ordered Vector Spaces and the Order Unit*; and the grading is *Superalgebras and Graded Structures*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L^{\alpha}_ax = a\alpha(x)$, $R^{\alpha}_ax = \alpha(x)a$ | Signed one-sided multiplications |
| $L^{\alpha}_a = L_a\Gamma$ | Factorisation through the grading operator |
| $\Gamma^{*} = \alpha$ | The grade involution is self-adjoint |
| $(L^{\alpha}_a)^{*} = L^{\alpha}_{\alpha(a^{*})}$ | Adjoint of a signed left multiplication |
| $a = \alpha(a^{*})$ | $\alpha$-Hermitian parameter, the self-adjoint case |
| $a = -\alpha(a^{*})$ | Skew-adjoint case |
| $L^{\alpha}_aL^{\alpha}_b = L_{a\alpha(b)}$ | Twisted composition law |
| $L^{\alpha}_ax = \varepsilon_xL_ax$ | The order detects the parity |

## Further Reading

- Richard Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the left multiplications, the adjoints and the order.
- Gert K. Pedersen, *C\*-Algebras and their Automorphism Groups* (Academic Press, 1979), for the automorphisms, the graded structures and the positivity.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the graded left multiplications and the parity.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the graded operators and the reflection elements of a Clifford algebra.
- Erik M. Alfsen and Frederik W. Shultz, *State Spaces of Operator Algebras* (Birkhäuser, 2001), for the order, the positivity and the operator adjoints.
