# __Adjoints of the Intertwiners of a Hilbert Algebra__

## Introduction

An intertwiner of a Hilbert algebra is an operator between two completions that commutes with the left multiplications, $T\bar L_x = \bar L'_xT$; and the adjoint of an intertwiner is again an intertwiner. The second statement is the algebraic content of the self-duality of the standard form, and it is what makes the intertwiners an algebra closed under adjunction: the commutant of a representation is a $\ast$-algebra, and the modular conjugation exchanges it with the algebra it commutes with. So the adjoint operation on intertwiners is the same operation as the involution on the algebra, seen from the other side of the standard form.

The article develops three consequences. First, the adjoint of an intertwiner of the left representations is an intertwiner of the left representations, so the class is closed under adjunction and the self-adjoint intertwiners form its real part. Second, the intertwiners of the standard representation with itself form the commutant of the algebra, and on that commutant the modular conjugation defines the **modular transpose** $T\mapsto T^{\flat} = \jmath T^{*}\jmath$, an antilinear involution that maps the commutant into the algebra and back; this is the operator form of the exchange between an algebra and its commutant. Third, the polar decomposition of an intertwiner stays inside the class, so a closed intertwiner has an intertwiner as its modulus and as its partial isometry, and the self-adjoint intertwiners are the self-adjoint part of the commutant.

This article fixes the adjoint of an intertwiner, the commutant as the algebra of intertwiners, the polar decomposition within the class, and the modular transpose of the standard form.

The Hilbert algebra, its involution and its completion are *Hilbert Algebras*, *Hermitian Adjoints on a Hilbert Algebra* and *The Completion of a Hilbert Algebra*; the representations and the adjoints of the multiplications are *The Left and the Right Regular Representation*, *The Adjoint of the Left and the Right Multiplication* and *The Adjoint of the Left Multiplication on a Hilbert Algebra*; the modular objects are *The Modular Operator and Tomita-Takesaki Theory*; the von Neumann algebra of the completion and the standard form are *Von Neumann Algebras and the Hilbert Algebra Completeness*; the positivity is *Self-Adjoint Elements and the Positive Cone*. Those are cited. The algebras are $A$ and $A'$ with completions $H$ and $H'$, and the representations are $x\mapsto\bar L_x$ and $x\mapsto\bar L'_x$.

## Intertwiners and Their Adjoints

**Definition.** A bounded operator $T : H\to H'$ is an **intertwiner** of the left representations when

$$
T\,\bar L_x = \bar L'_x\,T \qquad \text{for every } x\in A .
$$

**Theorem (the adjoint of an intertwiner is an intertwiner).** If $T$ is an intertwiner then $T^{*} : H'\to H$ is an intertwiner of the left representations in the reverse direction,

$$
T^{*}\,\bar L'_x = \bar L_x\,T^{*} \qquad \text{for every } x\in A .
$$

**Proof.** Taking adjoints in $T\bar L_x = \bar L'_xT$ gives $\bar L_x^{*}T^{*} = T^{*}\bar L'_x{}^{*}$, which by $\bar L_y^{*} = \bar L_{y^{\dagger}}$ is $\bar L_{x^{\dagger}}T^{*} = T^{*}\bar L'_{x^{\dagger}}$; since the involution is of order two and runs over the algebra, the identity holds with $x$ in place of $x^{\dagger}$.

**Corollary (the class is self-adjoint).** The intertwiners of the left representations form a vector space closed under adjunction; the self-adjoint intertwiners $T = T^{*}$ form its real part, and every intertwiner is $T_1+iT_2$ with $T_1, T_2$ self-adjoint intertwiners.

**Proof.** The first statement is the theorem; the decomposition is $T_1 = \tfrac12(T+T^{*})$, $T_2 = \frac{1}{2i}(T-T^{*})$, which are intertwiners by the theorem and self-adjoint by construction.

**Proposition (the modular conjugation exchanges the two commutation properties).** For the standard representation, an operator $T$ commutes with all the left multiplications exactly when $\jmath T\jmath$ commutes with all the right multiplications; equivalently

$$
\{\bar R_x\}' = \jmath\,\{\bar L_x\}'\jmath .
$$

**Proof.** $\jmath\bar L_x\jmath = \bar R_{x^{\dagger}}$ and $\jmath\bar R_x\jmath = \bar L_{x^{\dagger}}$ by *The Adjoint of the Left and the Right Multiplication*. Conjugating $T\bar L_x = \bar L_xT$ by $\jmath$ gives $\jmath T\jmath\,\bar R_{x^{\dagger}} = \bar R_{x^{\dagger}}\jmath T\jmath$, so $\jmath T\jmath$ commutes with every right multiplication; the converse is the same computation applied to $\jmath S\jmath$.

**Remark (the two commutation properties are not the same).** The commutation with the left multiplications and the commutation with the right multiplications are different conditions, related by the conjugation with $\jmath$ and not equal: the smallest case is a right multiplication $\bar R_y$, which commutes with every right multiplication and commutes with the left ones only when $y$ is central. So the two conditions are exchanged by the modular conjugation, and each of the two commutants is recovered from the other by conjugating back.

## The Commutant as the Algebra of Intertwiners

**Definition.** For a representation $\pi$ of $A$ on $H$ the **commutant** is

$$
\pi(A)' = \{\,T\in B(H) : T\pi(x) = \pi(x)T \text{ for every } x\,\} ,
$$

the set of intertwiners of the representation with itself.

**Theorem (the commutant is a $\ast$-algebra of intertwiners).** $\pi(A)'$ is a unital algebra closed in the weak operator topology and closed under adjunction; for the standard representation of a Hilbert algebra it is generated by the right multiplications, $\pi(A)' = \{\bar R_x : x\in A\}''$.

**Proof.** Closure under multiplication and adjunction is immediate from $T\pi(x) = \pi(x)T$ by taking adjoints as in the first theorem; the weak operator closure is the von Neumann bicommutant theorem of *Von Neumann Algebras and the Hilbert Algebra Completeness*; the generation by the right multiplications is the double commutant statement of *The Left and the Right Regular Representation*.

**Corollary (the adjoint is the involution seen from the commutant).** On the commutant the adjoint operation is the operation that the involution induces on the algebra, so the commutant of a Hilbert algebra is a Hilbert algebra in its own right, and the map $x\mapsto\bar R_x$ is a $\ast$-anti-isomorphism of $A$ onto the commutant's dense part.

**Proof.** $\bar R_x^{*} = \bar R_{x^{\dagger}}$ by *The Adjoint of the Left and the Right Multiplication*, so the anti-isomorphism carries the involution to the adjoint.

## The Polar Decomposition and the Standard Form

**Theorem (the polar decomposition stays in the class).** Let $T$ be a closed intertwiner. Then $T^{*}T$ is a positive self-adjoint intertwiner, $|T| = (T^{*}T)^{1/2}$ is an intertwiner, and the partial isometry $U$ of the polar decomposition $T = U|T|$ is an intertwiner; so the class of intertwiners is closed under the polar decomposition.

**Proof.** $T^{*}T$ commutes with the representation because $T$ and $T^{*}$ do, whence $|T|$ and hence $U = T|T|^{-1}$ on the orthogonal complement of the kernel commute with it too.

**Theorem (the modular transpose and the standard form).** Let $\jmath$ be the modular conjugation of the standard form. Then

$$
T\ \longmapsto\ T^{\flat} = \jmath\,T^{*}\jmath
$$

is an antilinear involution of the operator algebra that maps the commutant onto the algebra, $\{\jmath T^{*}\jmath : T\in\pi(A)'\} = \pi(A)$, and it satisfies $(ST)^{\flat} = T^{\flat}S^{\flat}$; so the modular conjugation implements the self-duality of the standard form and turns the adjoint of an intertwiner into the involution of the algebra.

**Proof.** $\jmath\pi(A)\jmath = \pi(A)'$ and $\jmath\pi(A)'\jmath = \pi(A)$ by *The Modular Operator and Tomita-Takesaki Theory*, whence the map takes the commutant onto the algebra; it is antilinear, involutive because $\jmath^{2} = \mathrm{id}$, and anti-multiplicative, $(ST)^{\flat} = T^{\flat}S^{\flat}$, because the adjoint reverses products; on the dense part $\jmath\bar R_x\jmath = \bar L_{x^{\dagger}}$, which is the involution of the algebra.

**Corollary (self-adjoint intertwiners are the fixed points of the transpose).** An intertwiner of the standard representation is self-adjoint exactly when $T^{\flat} = \jmath T\jmath$; the self-adjoint intertwiners are the real form of the commutant, and the positive intertwiners are the positive elements of the commutant, with the cone of *Self-Adjoint Elements and the Positive Cone*.

**Proof.** $T = T^{*}$ is equivalent to $T^{\flat} = \jmath T^{*}\jmath = \jmath T\jmath$; the real-form and positivity statements are the corresponding statements of the quotient algebra transported by the $\ast$-anti-isomorphism.

**Remark (what the adjoint of an intertwiner says).** The adjoint of an intertwiner is an intertwiner because the involution of the algebra is exactly the adjoint of the multiplications; the modular conjugation then turns this algebraic fact into the self-duality of the standard form: the algebra and its commutant are exchanged by $\jmath$, and the adjoint on one side is the involution on the other. There is one adjoint operation in the theory, and the intertwiners, the commutant and the algebra are three of its faces.

## Self-Adjoint Intertwiners

**Definition.** An intertwiner is **self-adjoint** when $T = T^{*}$, **positive** when $T$ is self-adjoint and $\langle T u,u\rangle\geq0$ for every $u$, and **unitary** when $T^{*}T = TT^{*} = \mathrm{id}$.

**Proposition (the spectral data of a self-adjoint intertwiner).** A self-adjoint intertwiner is a self-adjoint operator on $H$, and its spectral projections, its positive and negative parts and its modulus are intertwiners; the unitary intertwiners form a group.

**Proof.** The functional calculus of a self-adjoint operator is implemented by strong limits of polynomials in the operator, and a strong limit of intertwiners is an intertwiner; the unitary statement is $x\mapsto\bar L_x$ on the unitary group, or the corresponding statement in the commutant.

**Proposition (the commutant of the standard form is a Hilbert algebra).** With the involution $T\mapsto T^{*}$ and the form $(S,T) = \langle S\xi,T\xi\rangle$ the commutant is a Hilbert algebra whose completion is $H$, and its left regular representation is the right regular representation of $A$; the intertwiners of the commutant are the algebra itself.

**Proof.** The form is positive definite because $\xi$ is separating for the commutant; the involution is the adjoint $T\mapsto T^{*}$, which on the right multiplications is $\bar R_x\mapsto\bar R_{x^{\dagger}}$; the double commutant theorem gives $\pi(A)'' = \pi(A)'{}'$, whence the last statement.

## Worked Cases

### Matrices

For $A = M_n(\mathbb{C})$ with the Hilbert–Schmidt form, the commutant of the left action is the right action, the modular conjugation is $J(u) = u^{*}$, and an intertwiner is a map $T$ with $T(a u) = a T(u)$ for all $a$; the adjoint is again such a map and the modular transpose is $T^{\flat}(u) = T^{*}(u^{*})^{*}$, the entrywise conjugate transpose operation.

### The Group Algebra

For $A = \mathbb{C}[G]$ with the standard form, the commutant of the left regular representation is the right regular representation, and the modular conjugation is the bounded antiunitary $J(g\xi) = g^{-1}\xi$; the adjoint on the commutant is $\bar R_g^{*} = \bar R_{g^{-1}}$, while the modular transpose is $\bar R_g^{\flat} = \bar L_g$, the left multiplication, so the two operations coincide on the commutant exactly for the central involutions.

### The Non-Tracial Case

When the modular operator is not the identity the adjoint of an intertwiner and its modular transpose are different operations, related by the modular operator: $T^{\flat} = \jmath T^{*}\jmath$, while $T^{*}$ is the Hilbert adjoint on $H$ and $T^{*} = \Delta^{1/2}\,S\,T^{\flat}S\,\Delta^{-1/2}$ with $S = \jmath\Delta^{1/2}$; both are intertwiners, and they agree exactly when the form is tracial.

## Summary

An **intertwiner** of the left representations satisfies $T\bar L_x = \bar L'_xT$, and its **adjoint** is again an intertwiner, $T^{*}\bar L'_x = \bar L_xT^{*}$, because the involution of the algebra is the adjoint of the multiplications; so the intertwiners form a $\ast$-closed class with a real form of self-adjoint intertwiners. The intertwiners of a representation with itself form its **commutant**, a unital weakly closed $\ast$-algebra, generated by the right multiplications for the standard representation; on the commutant the adjoint is the involution of $A$ transported by the anti-isomorphism $x\mapsto\bar R_x$, so the commutant is itself a Hilbert algebra. The **polar decomposition** of a closed intertwiner stays in the class, and the **modular transpose** $T\mapsto T^{\flat} = \jmath T^{*}\jmath$ is an antilinear involutive $\ast$-anti-isomorphism of the commutant onto the algebra, which is the self-duality of the standard form: the adjoint on one side is the involution on the other, and the self-adjoint intertwiners are the real form of the commutant. The representations and the adjoint identities are *The Left and the Right Regular Representation* and *The Adjoint of the Left and the Right Multiplication*, the modular theory is *The Modular Operator and Tomita-Takesaki Theory*, and the standard form is *Von Neumann Algebras and the Hilbert Algebra Completeness*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T\bar L_x = \bar L'_xT$ | Intertwiner of the left representations |
| $T^{*}\bar L'_x = \bar L_xT^{*}$ | The adjoint is an intertwiner |
| $\pi(A)'$ | Commutant, the intertwiners of $\pi$ with itself |
| $\bar R_x^{*} = \bar R_{x^{\dagger}}$ | The adjoint as the involution on the commutant |
| $T = U|T|$ | Polar decomposition inside the class |
| $T^{\flat} = \jmath T^{*}\jmath$ | Modular transpose, $(ST)^{\flat} = T^{\flat}S^{\flat}$ |
| $\{\bar R_x\}' = \jmath\{\bar L_x\}'\jmath$ | The modular conjugation exchanges the two commutation properties |
| $\jmath\pi(A)\jmath = \pi(A)'$ | Self-duality of the standard form |
| $T = T^{*}$ | Self-adjoint intertwiner, real form |

## Further Reading

- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for intertwiners, commutants and the standard form.
- Serban Stratila and László Zsidó, *Lectures on von Neumann Algebras* (Abacus Press, 1979), for the commutant of a Hilbert algebra and its involution.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the polar decomposition of a closed operator and its invariance.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the modular conjugation and the self-duality of the standard form.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics*, vol. 1 (Springer, 1987), for intertwiners of the regular representation.
