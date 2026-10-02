# __Hermitian Adjoints on a Hilbert Algebra__

## Introduction

A Hilbert algebra carries an involution $\dagger$ and a positive definite form, tied by the adjoint axiom $\langle xy,z\rangle = \langle y,x^{\dagger}z\rangle$. The axiom says exactly that the involution computes the **adjoint** of the left multiplication for the form: reading $\langle L_xy,z\rangle = \langle y,x^{\dagger}z\rangle$ in operator form gives $L_{x^{\dagger}} = L_x^{*}$. This is the first and simplest statement of the theory of the group: the algebraic involution of a Hilbert algebra is the Hermitian adjoint operation for the form, and every adjoint statement about the multiplications is the adjoint axiom in operator notation.

Two adjoints then have to be distinguished, because they are not the same. The **algebraic involution** $x\mapsto x^{\dagger}$ acts on the algebra itself; the **Hilbert adjoint** $T\mapsto T^{*}$ acts on operators on the completed Hilbert space. The adjoint axiom says that the involution on the algebra induces the Hilbert adjoint on the corresponding left multiplications, and after completion this is an identity of bounded operators; but the involution is a bounded map of the completion only when the form is tracial, and in general it is closable rather than bounded. The distinction between the two adjoints is the source of the modular structure: the closure of the involution is the operator $S$, and the operator $S^{*}S$ is the modular operator.

This article fixes the two adjoints, the adjoint axiom as the identity $L_{x^{\dagger}} = L_x^{*}$, the self-adjoint elements and their relation to the positivity, and the behaviour of the involution on the completion.

The Hilbert algebra and its axioms are *Hilbert Algebras*; the completion and the closure of the involution are *The Completion of a Hilbert Algebra*; the multiplications are *The Left and the Right Regular Representation*; the modular operator and the conjugation are *The Modular Operator and Tomita-Takesaki Theory*; the positivity and the self-adjoint elements are *Self-Adjoint Elements and the Positive Cone*. Those are cited. The algebra is $A$ with involution $\dagger$ and form $\langle\cdot,\cdot\rangle$, and the completion is $H$.

## The Two Adjoints

**Definition.** On a Hilbert algebra $A$ the **algebraic involution** is the map $x\mapsto x^{\dagger}$; on the completion $H$ the **Hilbert adjoint** is the map $T\mapsto T^{*}$ of bounded operators. They are related by the adjoint axiom, and they are different maps living on different objects.

**Proposition (the adjoint axiom is the operator identity).** For every $x$ the left multiplication satisfies

$$
L_{x^{\dagger}} = L_x^{*} , \qquad R_{x^{\dagger}} = R_x^{*} ,
$$

the adjoints being the Hilbert adjoints on $H$; so the algebraic involution on the algebra is the Hilbert adjoint on the corresponding multiplications.

**Proof.** $\langle L_xy,z\rangle = \langle xy,z\rangle = \langle y,x^{\dagger}z\rangle = \langle y,L_{x^{\dagger}}z\rangle$ by the adjoint axiom; the right-multiplication identity is the same computation read in the other order.

**Proposition (the involution is an isometry exactly for a tracial form).** The involution is isometric for the form, $\langle x^{\dagger},y^{\dagger}\rangle = \langle y,x\rangle$, but it is bounded on the completion exactly when the form is tracial, $\langle xy,z\rangle = \langle y,xz\rangle$-symmetric; otherwise it is closable and unbounded.

**Proof.** $\langle x^{\dagger},y^{\dagger}\rangle = \langle y^{\dagger\dagger},x^{\dagger\dagger}\rangle$ by the adjoint axiom with the two sides exchanged, giving the isometry; the boundedness fails when the standard form has $\Delta\neq\mathrm{id}$, since the involution on $H$ is then the unbounded antilinear operator $S$.

## The Involution as an Adjoint

**Proposition (the adjoint of a general element).** The involution reverses products, $(xy)^{\dagger} = y^{\dagger}x^{\dagger}$, and it is the unique antilinear map with this property and $L_{x^{\dagger}} = L_x^{*}$; so the involution is determined by the form.

**Proof.** The product reversal is an axiom; if two antilinear maps have the same left-multiplication action then they agree at $1$, and hence everywhere in a unital algebra.

**Proposition (self-adjointness).** An element is **self-adjoint** when $x = x^{\dagger}$, and the self-adjoint elements are exactly those whose left multiplications are Hilbert-self-adjoint on the completion. The self-adjoint elements form the real form of the algebra, and the positive ones form the positive cone of *Self-Adjoint Elements and the Positive Cone*.

**Proof.** $x = x^{\dagger}$ is equivalent to $L_x = L_{x^{\dagger}} = L_x^{*}$ by the previous results; the real-form statement is *Self-Adjoint Elements and the Positive Cone*.

## Self-Adjoint Elements

**Proposition (positivity in the algebra).** The elements $y^{\dagger}y$ are self-adjoint, $\langle y^{\dagger}yu,u\rangle = \langle yu,yu\rangle\geq0$, and the positive cone generated by them is stable under the inner conjugations $x\mapsto y^{\dagger}xy$.

**Proof.** $(y^{\dagger}y)^{\dagger} = y^{\dagger}y$; the quadratic form is $\langle yu,yu\rangle$ by the adjoint axiom; the inner conjugation is $\langle y^{\dagger}xyu,u\rangle = \langle x(yu),yu\rangle$.

**Proposition (the modular image).** The map $x\mapsto x^{\dagger}$ on the algebra corresponds on the completion to the Tomita operator $S$: for $a = x\xi$ one has $a^{\dagger} = x^{*}\xi = Sa$, so the closure of the involution is exactly the modular antilinear operator, and its deviation from being an isometry is recorded by the modular operator through $S = J\Delta^{1/2}$.

**Proof.** The identification is the definition of the involution in the reconstructed algebra of *Von Neumann Algebras and the Hilbert Algebra Completeness*; the factorisation is the polar decomposition of *The Modular Operator and Tomita-Takesaki Theory*.

**Remark (the one distinction to keep).** The involution is a *bounded* adjoint operation on the algebra for the form, and it corresponds to an *unbounded* antilinear operator on the completion when the standard form is not tracial. Both statements are the same statement seen in the two pictures, and the operator that records the difference is the modular operator.

## Worked Cases

### The Group Algebra

For $A = \mathbb{C}[G]$ with the standard form the involution $g^{\dagger} = g^{-1}$ is isometric and the form is tracial, so the involution extends to a bounded antilinear isometry of the completion $\mathbb{C}^{G}$; the modular operator is the identity.

### Matrices

For $A = M_n(\mathbb{C})$ with the Hilbert–Schmidt form the involution is the conjugate transpose, the form is tracial, the left multiplications satisfy $L_{a^{*}} = L_a^{*}$, and the self-adjoint elements are the Hermitian matrices.

### A Non-Tracial Example

For the Hilbert algebra of the group von Neumann algebra of a non-abelian infinite group with a non-tracial vector state, the involution is closable but unbounded on the completion, and its polar decomposition has a nontrivial modular operator: the involution is still the adjoint on the algebra and is no longer a bounded operator on the completion.

## Summary

On a Hilbert algebra the **adjoint axiom** $\langle xy,z\rangle = \langle y,x^{\dagger}z\rangle$ is exactly the identity $L_{x^{\dagger}} = L_x^{*}$, so the **algebraic involution** is the **Hermitian adjoint** operation for the form, and the same holds on the right with $R_{x^{\dagger}} = R_x^{*}$. Two adjoints must be kept apart: the involution acts on the algebra and the Hilbert adjoint acts on the completed operators, and the involution is a bounded isometry of the completion exactly when the form is **tracial**; in general it is closable and its closure on the completion is the **Tomita operator** $S$, whose polar decomposition $S = J\Delta^{1/2}$ carries the modular operator and the modular conjugation. The **self-adjoint elements** $x = x^{\dagger}$ are those with Hilbert-self-adjoint left multiplications, they form the real form of the algebra, and the positive ones generate the cone of *Self-Adjoint Elements and the Positive Cone*; the elements $y^{\dagger}y$ are positive with $\langle y^{\dagger}yu,u\rangle = \langle yu,yu\rangle$. The axioms are *Hilbert Algebras*, the completion and the closure of the involution are *The Completion of a Hilbert Algebra*, and the modular objects are *The Modular Operator and Tomita-Takesaki Theory*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\dagger$ | Algebraic involution on the algebra |
| $^{*}$ | Hilbert adjoint on the completion |
| $L_{x^{\dagger}} = L_x^{*}$, $R_{x^{\dagger}} = R_x^{*}$ | The adjoint axiom as operator identity |
| $x = x^{\dagger}$ | Self-adjoint element, real form |
| $\langle y^{\dagger}yu,u\rangle = \langle yu,yu\rangle$ | Positivity of the elements $y^{\dagger}y$ |
| $S(x\xi) = x^{*}\xi$ | The involution on the completion |
| $S = J\Delta^{1/2}$ | Polar decomposition of the involution |
| Tracial form | Case in which the involution is a bounded isometry |

## Further Reading

- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for Hilbert algebras and the involution.
- Serban Stratila and László Zsidó, *Lectures on von Neumann Algebras* (Abacus Press, 1979), for the adjoint axiom and the regular representations.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 2 (Academic Press, 1986), for the Tomita operator and the modular structure.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the involution and the modular operator.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics*, vol. 1 (Springer, 1987), for the standard form and the involution.
