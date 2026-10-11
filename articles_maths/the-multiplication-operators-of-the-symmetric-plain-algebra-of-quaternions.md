# __The Multiplication Operators of the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra of $\mathbb{H}$ carries the Jordan product $\tilde p\bullet\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$ of *Introduction to the Symmetric Plain Algebra of Quaternions*. This article studies its **multiplication operators** $L^{\bullet}_{\tilde p}$, their **composition** and the operator form of the Jordan identity, the **coincidence of the left and right operators**, the **enveloping structure** they generate, and the **derivations** they exhibit, with the comparison with the biquaternion case.

**This is not the algebra $\mathbb{H}$.** The two algebras share the space, the addition, the real scalars and the unit, but $\bullet$ is a different multiplication and the projection onto the scalar line is not multiplicative. Throughout, the natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because $\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural sign and gives nothing new.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and $e_1^2=e_2^2=e_3^2=-e_0$. An element is $\tilde q=q_0e_0+\mathbf q$ with $\mathbf q=\sum_{k=1}^{3}q_ke_k$ and $q_\mu\in\mathbb{R}$; the plain left and right multiplications are $L_{\tilde p}\tilde q=\tilde p\tilde q$ and $R_{\tilde p}\tilde q=\tilde q\tilde p$, the two-sided operator is $M_{\tilde p,\tilde q}\tilde x=\tilde p\tilde x\tilde q$, the trace form is $\tau(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p\bullet\tilde q)$, and the derivations of the plain algebra are those of *The Multiplication Operators of the General Plain Algebra*.

## The Multiplication Operators

### The Definition and the Two-Sided Coincidence

**Definition.** The **left multiplication operator** of the block is $L^{\bullet}_{\tilde p}\tilde q=\tilde p\bullet\tilde q$; the **right** one is $R^{\bullet}_{\tilde p}\tilde q=\tilde q\bullet\tilde p$.

**Proposition (the half-sum).** The left multiplication of the block is the half-sum of the plain left and right multiplications,

$$
L^{\bullet}_{\tilde p}=\tfrac12\bigl(L_{\tilde p}+R_{\tilde p}\bigr),\qquad
L_{\tilde p}+R_{\tilde p}=2\,L^{\bullet}_{\tilde p}.
$$

*Proof.* $\tfrac12(L_{\tilde p}+R_{\tilde p})\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)=\tilde p\bullet\tilde q$. The stated sum is the operator of the **doubled** product and is not $L^{\bullet}_{\tilde p}$; the factor $\tfrac12$ is essential.

**Proposition (the two-sided coincidence).** The product is commutative, so the left and the right operators coincide:

$$
L^{\bullet}_{\tilde p}=R^{\bullet}_{\tilde p}.
$$

*Proof.* $R^{\bullet}_{\tilde p}\tilde q=\tilde q\bullet\tilde p=\tilde p\bullet\tilde q=L^{\bullet}_{\tilde p}\tilde q$ by commutativity. The block therefore carries **one** operator per element, not two, and there is no asymmetry of the two sides.

### Composition

**Theorem.** The composition of two multiplication operators is

$$
L^{\bullet}_{\tilde p}L^{\bullet}_{\tilde q}=\tfrac14\bigl(L_{\tilde p\tilde q}+R_{\tilde q\tilde p}+M_{\tilde p,\tilde q}+M_{\tilde q,\tilde p}\bigr),
$$

and its symmetrised form is

$$
L^{\bullet}_{\tilde p}L^{\bullet}_{\tilde q}+L^{\bullet}_{\tilde q}L^{\bullet}_{\tilde p}
=L^{\bullet}_{\tilde p\bullet\tilde q}+\tfrac12\bigl(M_{\tilde p,\tilde q}+M_{\tilde q,\tilde p}\bigr).
$$

*Proof.* Writing $L^{\bullet}_{\tilde p}=\tfrac12(L_{\tilde p}+R_{\tilde p})$ and expanding the product, $L_{\tilde p}L_{\tilde q}=L_{\tilde p\tilde q}$, $R_{\tilde p}R_{\tilde q}=R_{\tilde q\tilde p}$, $L_{\tilde p}R_{\tilde q}=M_{\tilde p,\tilde q}$ and $R_{\tilde p}L_{\tilde q}=M_{\tilde q,\tilde p}$, gives the first identity; adding it to the one with $\tilde p,\tilde q$ interchanged and using $L^{\bullet}_{\tilde p\bullet\tilde q}=\tfrac14(L_{\tilde p\tilde q}+R_{\tilde p\tilde q}+L_{\tilde q\tilde p}+R_{\tilde q\tilde p})$ gives the second.

**Remark (the composition is not the product of the parameters).** The block is not associative, so $L^{\bullet}_{\tilde p}L^{\bullet}_{\tilde q}\neq L^{\bullet}_{\tilde p\bullet\tilde q}$; the two-sided operators $M_{\tilde p,\tilde q}+M_{\tilde q,\tilde p}$ measure the failure, and they are what the plain operators contribute and the block keeps.

### The Kernel

**Theorem (injectivity).** The map $\tilde p\mapsto L^{\bullet}_{\tilde p}$ is injective: $L^{\bullet}_{\tilde p}=0$ if and only if $\tilde p=0$.

*Proof.* If $L^{\bullet}_{\tilde p}=0$ then $\tilde p\bullet\tilde q=0$ for every $\tilde q$, so $\tilde p$ is annihilated with everything; but a nonzero element annihilates only the plane of *Zero Divisors of the Symmetric Plain Algebra* when it is pure and nothing when it is non-pure, so $\tilde p=0$.

**Corollary.** The kernel of $L^{\bullet}_{\tilde p}$ is $\{0\}$ for a non-pure $\tilde p$ and the two-dimensional plane of *Zero Divisors of the Symmetric Plain Algebra* for a nonzero pure $\tilde p$; the operator is singular exactly at the zero divisors, with $\det L^{\bullet}_{\tilde p}=p_0^2N(\tilde p)$.

## The Jordan Relation

### The Operator Form of the Jordan Identity

**Theorem.** The Jordan identity of the block is equivalent to the operator commutation

$$
\bigl[\,L^{\bullet}_{\tilde p},\,L^{\bullet}_{\tilde p^{\,\bullet2}}\,\bigr]=0
\qquad\text{for every }\tilde p,
$$

and, more generally, $\bigl[L^{\bullet}_{\tilde p},L^{\bullet}_{\tilde q}\bigr]$ is a **derivation** of the block for all $\tilde p,\tilde q$.

*Proof.* The equivalence of the Jordan identity with $[L_{\tilde x},L_{\tilde x^{\bullet2}}]=0$ is the standard operator form quoted in *Jordan Algebras*; the derivation property of $[L^{\bullet}_{\tilde p},L^{\bullet}_{\tilde q}]$ is the same statement applied to the linearised identity, and both are the algebra of the symmetrisation.

### The Inner Derivations

**Definition.** The **inner derivations** of the block are the operators $D_{\tilde p,\tilde q}=[L^{\bullet}_{\tilde p},L^{\bullet}_{\tilde q}]$.

**Theorem.** The inner derivations span a three-dimensional real Lie algebra, isomorphic to $\mathfrak{so}(3)$; it acts on the vector subspace by its usual rotations and annihilates the scalar line.

*Proof.* The derivation algebra of a degree-two algebra is the skew part of the structure Lie algebra, and for the block it is the Lie algebra acting on the three-dimensional vector subspace by the rotations that preserve the Euclidean form, $\mathfrak{so}(3)$; the scalar line is central and every derivation annihilates $e_0$. A direct count from the four generators gives three independent brackets, $[L^{\bullet}_{e_1},L^{\bullet}_{e_2}]$, $[L^{\bullet}_{e_2},L^{\bullet}_{e_3}]$, $[L^{\bullet}_{e_3},L^{\bullet}_{e_1}]$.

## The Enveloping Structure

### The Enveloping Algebra Is Full

**Theorem.** The multiplication operators generate the **full** endomorphism algebra:

$$
\mathrm{alg}\bigl\{\,L^{\bullet}_{\tilde p}\,\bigr\}=\mathrm{End}_{\mathbb{R}}(\mathbb{H})\cong M_4(\mathbb{R}),
$$

of real dimension $16$; the span of the products of length at most two is already all of it.

*Proof.* The identity is $L^{\bullet}_{e_0}$; the four generators together with their products of length one span a $13$-dimensional space, and adjoining the products of length two completes it to $16$, by the computation of the block's operator span. Since $\mathrm{alg}$ contains the identity and is the whole of $M_4(\mathbb{R})$, it is irreducible.

**Corollary (the commutant).** The commutant of the family is the scalar operators, $\{L^{\bullet}_{\tilde p}\}'=\mathbb{R}\cdot\mathrm{id}$; the block is a **multiplication algebra** whose multiplications generate every linear map of the space, as the plain left and right multiplications do in *The Enveloping Operator Algebra of the General Plain Algebra and the Bi-module Structure*.

**Remark (the contrast with the plain algebra).** In the plain algebra the left and the right multiplications generate the two-sided multiplications but not all of $\mathrm{End}(\mathbb{H})$; the block, being commutative, has a single family and its products fill the whole matrix algebra. This is the specific-theory form of the coincidence $L^{\bullet}=R^{\bullet}$.

## The Derivations

### The Inner Derivations and Their Dimension

**Theorem.** Every derivation of the block is inner:

$$
\operatorname{Der}(\mathbb{H}^{\bullet})=\mathrm{span}\bigl\{[L^{\bullet}_{\tilde p},L^{\bullet}_{\tilde q}]\bigr\}\cong\mathfrak{so}(3),
\qquad \dim\operatorname{Der}=3,
$$

and no derivation is a multiplication by an element.

*Proof.* The derivation algebra is three-dimensional and coincides with the inner derivations by the general theory of degree-two Jordan algebras; an element-multiplication $L^{\bullet}_{\tilde a}$ is a derivation only if $\tilde a\bullet(\tilde p\bullet\tilde q)=( \tilde a\bullet\tilde p)\bullet\tilde q+\tilde p\bullet(\tilde a\bullet\tilde q)$ for all $\tilde p,\tilde q$, which forces $\tilde a=0$ by the non-associativity at $e_1,e_2$.

### Skewness for the Trace Form

**Theorem.** Every derivation is skew for the trace form:

$$
\tau(D\tilde p,\tilde q)+\tau(\tilde p,D\tilde q)=0 .
$$

*Proof.* The trace form is associative, $\tau(\tilde p\bullet\tilde q,\tilde r)=\tau(\tilde p,\tilde q\bullet\tilde r)$, and differentiating this identity along a derivation gives the skewness; the full argument is *The Trace Form and the Invariance of the Symmetric Plain Algebra*, where the invariance is owned.

## The Comparison with the Biquaternion Case

| | the symmetric plain algebra of $\mathbb{H}$ | the biquaternion symmetric plain algebra |
|---|---|---|
| $L^{\bullet}_{\tilde p}$ | $\tfrac12(L_{\tilde p}+R_{\tilde p})$ | $\tfrac12(L_{\tilde P}+R_{\tilde P})$ |
| left $=$ right | yes | yes |
| commutator $[L^{\bullet},L^{\bullet}]$ | a derivation | a derivation |
| derivation algebra | $\mathfrak{so}(3)$, of dimension $3$, all inner | the complex analogue, all inner |
| enveloping algebra | full $M_4(\mathbb{R})$ | the complex analogue |
| skewness for the trace form | yes | yes |

**Remark (what the field changes).** The half-sum, the coincidence of the sides, the derivation property of the bracket, the skewness for the trace form and the fullness of the enveloping algebra have the same shape over $\mathbb{R}$ and over $\mathbb{C}$; they are the operator part of the degree-two Common Theory of *The Two General Products of an Algebra with Involution*. What the field changes is the **dimension** read on $\mathbb{R}$: over $\mathbb{R}$ the derivation algebra is the compact $\mathfrak{so}(3)$ of the three-dimensional vector subspace, and over $\mathbb{C}$ the corresponding algebra is its complexification. The biquaternion operators are *The Multiplication Operators of the Symmetric Plain Algebra* of the biquaternion chapter.

## Summary

The multiplication operators of the block are $L^{\bullet}_{\tilde p}\tilde q=\tilde p\bullet\tilde q$, the half-sum $L^{\bullet}_{\tilde p}=\tfrac12(L_{\tilde p}+R_{\tilde p})$ of the plain left and right multiplications, and because the product is commutative the left and the right operators coincide, $L^{\bullet}_{\tilde p}=R^{\bullet}_{\tilde p}$; the map $\tilde p\mapsto L^{\bullet}_{\tilde p}$ is injective, with kernel $\{0\}$ at a non-pure element and a two-dimensional plane at a pure one. The composition is $L^{\bullet}_{\tilde p}L^{\bullet}_{\tilde q}=\tfrac14(L_{\tilde p\tilde q}+R_{\tilde q\tilde p}+M_{\tilde p,\tilde q}+M_{\tilde q,\tilde p})$, the operator form of the Jordan identity is $[L^{\bullet}_{\tilde p},L^{\bullet}_{\tilde p^{\,\bullet2}}]=0$, and every bracket $[L^{\bullet}_{\tilde p},L^{\bullet}_{\tilde q}]$ is a derivation. The operators generate the full endomorphism algebra $M_4(\mathbb{R})$, of dimension $16$, with commutant the scalars; the derivations are all inner and form the three-dimensional Lie algebra $\mathfrak{so}(3)$, and every derivation is skew for the trace form. Over $\mathbb{C}$ the same shapes hold, the field changing only the complexification of the derivation algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L^{\bullet}_{\tilde p}=R^{\bullet}_{\tilde p}$ | the one multiplication operator of the block |
| $L^{\bullet}_{\tilde p}=\tfrac12(L_{\tilde p}+R_{\tilde p})$ | the half-sum identity |
| $L^{\bullet}_{\tilde p}L^{\bullet}_{\tilde q}=\tfrac14(L_{\tilde p\tilde q}+R_{\tilde q\tilde p}+M_{\tilde p,\tilde q}+M_{\tilde q,\tilde p})$ | the composition |
| $[L^{\bullet}_{\tilde p},L^{\bullet}_{\tilde p^{\,\bullet2}}]=0$ | the operator form of the Jordan identity |
| $\operatorname{Der}\cong\mathfrak{so}(3)$ | the derivation algebra, of dimension $3$, all inner |
| $\mathrm{alg}\{L^{\bullet}_{\tilde p}\}=M_4(\mathbb{R})$ | the enveloping algebra |
| $\tau(D\tilde p,\tilde q)+\tau(\tilde p,D\tilde q)=0$ | skewness of the derivations |

## Further Reading

- *Introduction to the Symmetric Plain Algebra of Quaternions*, for the product.
- *Zero Divisors of the Symmetric Plain Algebra*, for the kernel and the determinant of the operator.
- *The Trace Form and the Invariance of the Symmetric Plain Algebra*, for the invariance and the skewness.
- *The Enveloping Operator Algebra of the General Plain Algebra and the Bi-module Structure*, for the plain operators against which the fullness is read.
- *Jordan Algebras*, for the operator form of the Jordan identity and the derivations of a Jordan algebra.
- *The Two General Products of an Algebra with Involution*, for the degree-two Common Theory specialised here.
