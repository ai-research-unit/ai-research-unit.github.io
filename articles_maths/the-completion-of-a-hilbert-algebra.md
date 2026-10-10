# __The Completion of a Hilbert Algebra__

## Introduction

A Hilbert algebra is a $\ast$-algebra with a positive definite form tied to the product by the adjoint axiom $\langle xy,z\rangle = \langle y,x^{\dagger}z\rangle$, with left multiplications bounded. It is not complete: the form is an inner product, but the algebra is a pre-Hilbert space. **Completing** it gives a Hilbert space $H$, and the point of the completion is that the algebra does not disappear — the left multiplications extend to bounded operators on $H$, the involution extends to a closed antilinear operator, and the extension of the involution is the Tomita operator of the standard form. So the completion is the passage from an algebraic object to the Hilbert-space object that carries its operator algebra.

Two extensions have to be justified. The **left multiplication** $L_x$ is bounded on $A$ by hypothesis, hence extends by continuity to all of $H$, and the extension is a $\ast$-representation: this is what makes the completion a representation space. The **involution** $x\mapsto x^{\dagger}$ is an isometry on $A$ only when the form is tracial, and in general it is closable rather than bounded; the closure of its graph is the antilinear operator $S$ with $S(x) = x^{\dagger}$ on the algebra, which is exactly the Tomita operator $S\xi\mapsto x^{\dagger}\xi$ after the algebra is identified with its orbit in $H$. Completing a Hilbert algebra is therefore the same as building the Hilbert space of its standard form, and the involution carried by the completion is the modular antilinear operator.

This article fixes the completion, the Hilbert space it defines, the extension of the left multiplication, the extension of the involution and the identification of that extension with the Tomita operator.

The Hilbert algebra, its involution, its adjoint axiom and its positivity are *Hilbert Algebras*; the operator algebras generated after completion are *The Left and the Right Regular Representation* and *Von Neumann Algebras and the Hilbert Algebra Completeness*; the modular objects are *The Modular Operator and Tomita-Takesaki Theory*; the construction from a state is *The GNS Construction*. Those are cited. The algebra is $A$ with involution $\dagger$ and form $\langle\cdot,\cdot\rangle$, and the completion is $H$.

## The Completion

**Definition.** Let $A$ be a Hilbert algebra. Its **completion** $H$ is the Hilbert space obtained as the completion of $A$ for the norm $\|x\| = \langle x,x\rangle^{1/2}$, with $\iota : A\to H$ the canonical injection, injective because the form is positive definite.

**Proposition (the axioms used).** The completion uses exactly three of the axioms of a Hilbert algebra: the positivity of the form, the adjoint axiom $\langle xy,z\rangle = \langle y,x^{\dagger}z\rangle$, and the boundedness of the left multiplications. The associativity and the existence of a unit are not needed for the completion but are needed for the identification of the involution with the Tomita operator.

**Proof.** Positivity makes the norm; the adjoint axiom is what makes the left multiplications adjointable; boundedness is what lets them extend. The unit is used only to say that $A$ itself is an orbit, $A = L_A(1)$, whence the identification with $\mathcal{M}\xi$.

**Proposition (density and the unit).** The image $\iota(A)$ is dense in $H$ by construction; if $A$ has a unit $1$ then $\iota(A) = \{L_x(1) : x\in A\}$ and $H$ is the closure of the orbit of the vector $\xi = \iota(1)$ under the left multiplications.

**Proof.** Density is the definition of completion; the orbit statement is $L_x(1) = x$.

## The Left Multiplication on the Completion

**Theorem (the extension).** For each $x\in A$ the left multiplication $L_x$ is bounded on $A$ with $\|L_x\|\leq\|x\|$; it extends uniquely to a bounded operator $\bar L_x$ on $H$, the map $x\mapsto\bar L_x$ is a $\ast$-representation of $A$ on $H$, and $\bar L_{x^{\dagger}} = \bar L_x^{*}$.

**Proof.** Boundedness is an axiom; the extension is the density of $\iota(A)$ and the bounded linear extension theorem for normed spaces; multiplicativity is the associativity of $A$ on a dense set, hence everywhere; and the adjoint identity is the adjoint axiom on a dense set.

**Corollary (the completion carries the representation).** $H$ is a Hilbert module of the algebra in the sense that the assignment gives a non-degenerate $\ast$-representation whenever $A^{2}$ is dense in $A$; the pair $(H, \bar L)$ is the Hilbert-space representation attached to the algebra.

**Proof.** Non-degeneracy is $\overline{\bar L_A H} = H$, which follows from the density of $\iota(A)$ and $L_x(1) = x$.

## The Involution and the Tomita Operator

**Definition.** The **involution as a graph** is $\Gamma = \{(\iota(x),\iota(x^{\dagger})) : x\in A\}\subseteq H\oplus H$. Its closure is the graph of a closed antilinear operator when the closure is a graph, and that operator, when it exists, is written $S$ and called the **Tomita operator of the completion**.

**Proposition (closability).** The involution is closable, and its closure $S$ is antilinear, $S^{2} = \mathrm{id}$, and has dense domain containing $\iota(A)$.

**Proof.** Closability is the adjoint axiom together with positivity: if $x_n\to0$ and $x_n^{\dagger}\to u$ then $\langle u,y\rangle = \lim\langle x_n^{\dagger},y\rangle = \lim\langle x_n,y^{\dagger}\rangle = 0$ for all $y$, so $u = 0$. The involution identity is $S^{2} = \mathrm{id}$ on the dense set, and density of the domain is the density of $\iota(A)$.

**Theorem (the identification with the Tomita operator).** Let $\mathcal{M}$ be the von Neumann algebra generated by the extended left multiplications on $H$ and $\xi = \iota(1)$ its cyclic vector. Then $S$ coincides with the Tomita operator $S(x\xi) = x^{\dagger}\xi$ of *The Modular Operator and Tomita-Takesaki Theory*:

$$
S : \mathcal{M}\xi\to H, \qquad S(x\xi) = x^{\dagger}\xi .
$$

So the involution carried by the completion is precisely the modular antilinear operator, and the completion of a Hilbert algebra is the Hilbert space of its standard form.

**Proof.** $\mathcal{M}\xi$ contains $\iota(A)$ and the Tomita operator agrees with $S$ there, whence the equality of the closures.

**Remark (what the completion is).** The completion adds to the Hilbert algebra exactly two things: the limits of the left multiplications, which give the represented algebra, and the closure of the involution, which gives the modular operator. Everything modular about a Hilbert algebra is already present in its involution, and the completion is the device that makes the involution an operator.

## Worked Cases

### The Group Algebra

$A = \mathbb{C}[G]$ for a finite group with the standard form $\langle\sum a_g g,\sum b_h h\rangle = \sum a_g\bar b_g$ and involution $g^{\dagger} = g^{-1}$ is a Hilbert algebra; its completion is $\mathbb{C}^{G}$ and the left multiplications extend to the regular representation; the involution closes to the antilinear map $(\sum a_g g)^{\dagger} = \sum \bar a_g g^{-1}$ on the completion.

### Matrices

$A = M_n(\mathbb{C})$ with $\langle a,b\rangle = \mathrm{tr}(b^{*}a)$ and $\dagger$ the conjugate transpose is a Hilbert algebra, already complete: $H = M_n(\mathbb{C})$ with the Hilbert–Schmidt form, and the involution is bounded and closable (already closed). At $n=2$ the form reads

$$
a=\begin{pmatrix}1&i\\0&2\end{pmatrix},\qquad \lVert a\rVert^{2}=\operatorname{tr}(a^{*}a)=6,\qquad b=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad \langle a,b\rangle=\operatorname{tr}(b^{*}a)=\operatorname{tr}\begin{pmatrix}1&i\\0&0\end{pmatrix}=1 .
$$

### The Trivial Completion

$A = \mathbb{C}$ with the unit and the standard form is complete, the left multiplication is scalar and the Tomita operator is the identity; the completion adds nothing and the modular theory of $A$ is trivial.

## Summary

The **completion** of a Hilbert algebra $A$ is the Hilbert space $H$ obtained from the positive form $\langle\cdot,\cdot\rangle$ by completion, and the algebra survives in it: the **left multiplications** extend to a $\ast$-representation $x\mapsto\bar L_x$ on $H$, and the **involution** closes to an antilinear operator $S$ with $S^{2} = \mathrm{id}$. The closure of the involution is exactly the **Tomita operator** attached to the completion, so that upon identifying the image of the algebra with an orbit $\mathcal{M}\xi$ the objects of the theory are recovered: the completion of a Hilbert algebra is the Hilbert space of its **standard form**, and the involution it carries is the modular antilinear operator. The three axioms used are Positivity, the adjoint axiom and the boundedness of the left multiplications; the unit is used only to identify the algebra with the orbit of a vector. The algebra itself is *Hilbert Algebras*, the representation it defines is *The Left and the Right Regular Representation*, the completeness of the algebra with respect to the operator algebra is *Von Neumann Algebras and the Hilbert Algebra Completeness*, and the modular objects are *The Modular Operator and Tomita-Takesaki Theory*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$, $\dagger$, $\langle\cdot,\cdot\rangle$ | Hilbert algebra, involution, form |
| $H$, $\iota$ | Completion and the canonical injection |
| $L_x$, $\bar L_x$ | Left multiplication and its extension |
| $\Gamma$ | Graph of the involution |
| $S$, $S^{2} = \mathrm{id}$ | Tomita operator, closure of the involution |
| $\mathcal{M}$, $\xi = \iota(1)$ | Generated von Neumann algebra and cyclic vector |
| $S(x\xi) = x^{\dagger}\xi$ | The identification with the Tomita operator |
| $H$ = standard form space | What the completion is |

## Further Reading

- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for Hilbert algebras and their completion.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the modular theory of the completion.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 2 (Academic Press, 1986), for the standard form and the Tomita operator.
- Serban Stratila and László Zsidó, *Lectures on von Neumann Algebras* (Abacus Press, 1979), for the completion of a Hilbert algebra and the regular representations.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics*, vol. 1 (Springer, 1987), for the standard form and the modular objects.
