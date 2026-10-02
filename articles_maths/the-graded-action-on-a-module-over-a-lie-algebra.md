
# __The Graded Action on a Module over a Lie Algebra__

## Introduction

A **graded module** over a graded Lie algebra is a module with a decomposition compatible with the grading of the algebra, so that an element of parity $\epsilon$ carries the piece of parity $\delta$ to the piece of parity $\epsilon+\delta$; the compatibility of the action with the bracket then carries the **sign rule**, and it is the sign rule and not the grading alone that distinguishes the graded action from the action of a Lie algebra on a module. The graded module is the same object as a module over the enveloping algebra of the graded Lie algebra, and its sign rule is the one of the graded and the super structures.

This article treats the graded action on a module over a Lie algebra: the compatibility of the action with the grading and the sign rule it imposes. It is the eighth and last article of the `- Operator Theory` group of the category; the graded Lie algebra and its enveloping algebra are *Graded Lie Algebras and Lie Superalgebras* and *Superalgebras and Graded Structures*, the module structure is *Representations of Lie Algebras*, the graded action of a group on a module is *The Graded Action on a Module over a Group*, and the adjoint of the action is *The Graded Adjoint Action on a Module over a Lie Algebra* of the `- * Operator Theory` group, below in the category.

The article assumes the graded Lie algebra, the grade involution and the Koszul sign rule from *Graded Lie Algebras and Lie Superalgebras* and *Superalgebras and Graded Structures*, the module over a Lie algebra and the enveloping algebra from *Representations of Lie Algebras* and *Universal Enveloping Algebras*, the exterior and the symmetric algebras with their signs from *The Exterior Algebra* and *Superalgebras and Graded Structures*, and the graded action on a module over a group from *The Graded Action on a Module over a Group*, cited as the model. The Hermitian forms and the adjoints of the operators are deferred to the `- * Operator Theory` articles below; the present article fixes the action and its signs only.

## Graded Modules

### The Definition

**Definition.** Let $\mathrm{G} = \mathrm{G}^{+}\oplus\mathrm{G}^{-}$ be a graded Lie algebra over a field $k$ of characteristic different from $2$, with the grade involution $\alpha$ and the parity $\lvert x\rvert\in\{0,1\}$ of a homogeneous element. A **graded module** over $\mathrm{G}$ is a vector space with a decomposition

$$
M = M^{+}\oplus M^{-}
$$

and a bilinear action $\mathrm{G}\times M\to M$, $(x,m)\mapsto x\cdot m$, such that

$$
\mathrm{G}^{\epsilon}\cdot M^{\delta}\subseteq M^{\epsilon+\delta} \qquad (\epsilon,\delta\in\{0,1\}),
$$

and such that the action is compatible with the bracket in the graded sense,

$$
[x,y]\cdot m = x\cdot(y\cdot m) - (-1)^{\lvert x\rvert\lvert y\rvert}\,y\cdot(x\cdot m)
$$

for homogeneous $x,y$ and every $m\in M$.

**Definition.** The **parity operator** of $M$ is the involution $\beta$ equal to $+\mathrm{id}$ on $M^{+}$ and $-\mathrm{id}$ on $M^{-}$; it is the analogue on $M$ of the grade involution $\alpha$ on $\mathrm{G}$, and the grading of $M$ is the eigenspace decomposition of $\beta$.

**Proposition.** The compatibility condition is equivalent to the two statements

$$
x\cdot(\beta m) = (-1)^{\lvert x\rvert}\,\beta(x\cdot m), \qquad x\cdot M^{\delta}\subseteq M^{\delta+\lvert x\rvert} ,
$$

the first of which says that the action graded-commutes with the parity operator, $x\beta = (-1)^{\lvert x\rvert}\beta x$ as operators when $x$ is homogeneous; the odd elements of $\mathrm{G}$ reverse the grading of $M$ and the even elements preserve it.

*Proof.* For $m\in M^{\delta}$ one has $\beta m = (-1)^{\delta}m$ and $x\cdot m\in M^{\delta+\lvert x\rvert}$, so $\beta(x\cdot m) = (-1)^{\delta+\lvert x\rvert}x\cdot m = (-1)^{\lvert x\rvert}x\cdot(\beta m)$; the converse is the same computation read backwards. The last statement is the case distinction on $\lvert x\rvert$.

### The Sign Rule

**Theorem (the sign rule is forced).** Let $M$ be a graded module and let $x,y$ be homogeneous elements of odd parity. Then the two orders of application of $x$ and $y$ are related by

$$
x\cdot(y\cdot m) + y\cdot(x\cdot m) = [x,y]\cdot m ,
$$

and the anticommutator replaces the commutator; for two even elements the ordinary commutator appears, and for an even and an odd element the sign is $+1$. Hence the sign $(-1)^{\lvert x\rvert\lvert y\rvert}$ of the definition is the only sign for which the odd-odd case is consistent with the Jacobi identity of the bracket.

*Proof.* The displayed identity is the definition with both parities odd, where $(-1)^{\lvert x\rvert\lvert y\rvert} = -1$; the compatibility of the three parities with the graded Jacobi identity of $\mathrm{G}$ forces the sign, because the action is a representation and the graded Jacobi identity is the associativity of the action.

**Corollary.** The action extends to the enveloping algebra $U(\mathrm{G})$ with the graded product: $M$ is a module over the associative algebra $U(\mathrm{G})$, the multiplication of two odd elements acquiring the sign $-1$, and the parity operator $\beta$ is an automorphism of $M$ as a graded module in the sense of the graded-commutation above.

*Proof.* The universal property of $U(\mathrm{G})$ as the quotient of the tensor algebra by the relations $xy - (-1)^{\lvert x\rvert\lvert y\rvert}yx = [x,y]$ gives the extension; the compatibility of $\beta$ is the proposition.

## The Structure of the Graded Action

### The Even and the Odd Parts

**Proposition.** The even part $\mathrm{G}^{+}$ acts on $M$ by operators preserving the decomposition, and the odd part $\mathrm{G}^{-}$ acts by operators exchanging the two pieces; the action of $\mathrm{G}^{+}$ on $M^{+}$ and on $M^{-}$ are two modules over the even subalgebra, and the action of $\mathrm{G}^{-}$ is an intertwining between them.

*Proof.* The inclusion $\mathrm{G}^{\epsilon}\cdot M^{\delta}\subseteq M^{\epsilon+\delta}$ is the statement for the parities; the two modules over $\mathrm{G}^{+}$ are the restrictions of the action, and the odd action maps each into the other, intertwining the two $\mathrm{G}^{+}$-modules by the graded compatibility.

### The Submodules and the Quotients

**Definition.** A **graded submodule** is a subspace $N\subseteq M$ with $N = (N\cap M^{+})\oplus(N\cap M^{-})$ and $\mathrm{G}\cdot N\subseteq N$; the **quotient** $M/N$ is graded with the induced decomposition, and the **homomorphisms** of graded modules are the linear maps respecting the action and the grading, $f(M^{\delta})\subseteq N^{\delta}$.

**Theorem.** The graded modules over $\mathrm{G}$ form an abelian category with the exact sequences respecting the grading, every homomorphism has a kernel and a cokernel graded, and the category is equivalent to the category of the graded modules over the enveloping algebra $U(\mathrm{G})$.

*Proof.* The axioms are verified as for the modules over a ring, with the gradings carried along; the equivalence is the extension of the action to $U(\mathrm{G})$ of the corollary above, which is an equivalence on the objects and on the morphisms.

### The Free Module and the Basis

**Theorem.** The graded module $U(\mathrm{G})$ with the multiplication as the action is the free graded module of rank one; a graded module is free exactly when it has a homogeneous basis, and over a field every graded module has a homogeneous basis obtained by extending a basis of $M^{+}$ and one of $M^{-}$.

*Proof.* The action of $U(\mathrm{G})$ on itself by multiplication satisfies the compatibility by the associativity; the existence of the homogeneous basis is the extension of bases in a graded vector space, and the freeness is the universality of $U(\mathrm{G})$.

## The Enveloping Algebra and the Induced Structures

### The Graded Tensor Product

**Definition.** Let $M$ and $N$ be graded modules over the graded algebra $\mathrm{G}$. Their **graded tensor product** is the vector space $M\otimes N$ with the grading

$$
(M\otimes N)^{\epsilon} = \bigoplus_{\delta+\delta'=\epsilon} M^{\delta}\otimes N^{\delta'} ,
$$

the action

$$
x\cdot(m\otimes n) = (x\cdot m)\otimes n + (-1)^{\lvert x\rvert\lvert m\rvert}\,m\otimes(x\cdot n) ,
$$

and the **Koszul flip** $\tau(m\otimes n) = (-1)^{\lvert m\rvert\lvert n\rvert}n\otimes m$, which is an isomorphism of graded modules.

**Theorem.** The graded tensor product of two graded modules is a graded module, the action satisfies the graded Leibniz rule, and $\tau$ is an involution on the tensor square up to the identity; the parity of a product is the sum of the parities and the sign rule is preserved under the flip.

*Proof.* The compatibility $x\cdot(M\otimes N)^{\epsilon}\subseteq(M\otimes N)^{\epsilon+\lvert x\rvert}$ is the case distinction on the parities; the graded Leibniz rule and the sign of the flip are the associativity of the action with the sign of the definition, checked on homogeneous elements; $\tau^2 = \mathrm{id}$ because the sign $(-1)^{\lvert m\rvert\lvert n\rvert}$ is its own inverse.

### The Free Module

**Theorem.** For a graded vector space $V$ the module $U(\mathrm{G})\otimes V$ with the action by the left multiplication of the first factor is the **free graded module** on the generators $V$, and every graded module is a quotient of a free one; a graded module is free exactly when it has a homogeneous basis, and the rank is the graded dimension of $V$.

*Proof.* The action of $U(\mathrm{G})$ on the tensor product by the left multiplication is well defined and satisfies the compatibility; the universal property of the tensor product over the field gives the freeness, and the homogeneous basis is the one of $V$; the quotient statement is the standard presentation of a module by its relations, with the gradings carried along.

### The Graded Dual

**Definition.** The **graded dual** of a graded module $M$ is the graded module $M^{*}$ with the pieces $(M^{*})^{\epsilon} = (M^{\epsilon})^{*}$, the linear functionals of parity $\epsilon$, and the action

$$
(x\cdot f)(m) = -(-1)^{\lvert x\rvert\lvert f\rvert}\,f(x\cdot m) .
$$

**Theorem.** The graded dual is a graded module, the **transpose** of a homomorphism $u : M\to N$ is the homomorphism $u^{*} : N^{*}\to M^{*}$ with $u^{*}f = f\circ u$, and the canonical map $M\to M^{**}$ is injective, respects the grading and the action, and is an isomorphism in finite dimension.

*Proof.* The sign in the action is chosen so that the compatibility with the bracket holds: the two orders of $x$ and $y$ on $f$ produce the sign $(-1)^{\lvert x\rvert\lvert y\rvert}$ exactly as in the definition, which is the check of the graded Leibniz rule on the dual. The functoriality of the transpose and the injectivity of the double dual are the same as for the ungraded modules, with the gradings respected by construction.

## Examples

### The Adjoint Module

The algebra $\mathrm{G}$ itself is a graded module over $\mathrm{G}$ under the adjoint action $x\cdot m = [x,m]$; the compatibility is the graded Jacobi identity, $[x,[y,m]] - (-1)^{\lvert x\rvert\lvert y\rvert}[y,[x,m]] = [[x,y],m]$, and the parity operator is the grade involution $\alpha$. This is the module of the operator layer of the algebra, and its graded submodules are the graded ideals.

### The Exterior Algebra

Let $V$ be a vector space placed in odd parity and let $\mathrm{G}$ act on $V$; then the exterior algebra $\Lambda(V)$ is a graded module over $\mathrm{G}$ with the action extended as a graded derivation, and the sign rule of the action is the one of the Koszul sign of *Superalgebras and Graded Structures*; the odd elements of $\mathrm{G}$ act by the multiplication by their images, and the even elements act by derivations.

### The Clifford Module

Let $V$ carry a quadratic form and let $\mathrm{G}$ be the orthogonal Lie algebra of *The Orthogonal Lie Algebra*, graded by the involution that reverses the vector part; then the Clifford module of *Spin Representations and Clifford Modules with Inner Conjugation* is a graded module over $\mathrm{G}$, the even part preserving the chirality and the odd part exchanging the two chiralities, and the sign rule is the one of the Clifford relations.

### The Trivial Grading

If $\mathrm{G}$ is entirely even, the grade involution is the identity, the sign rule becomes the ordinary one, and the graded modules are the ordinary modules; the graded theory contains the ungraded one as the case of the trivial grading, and the general case is the one in which the odd part is nonzero and the signs of the odd-odd pairs are $-1$.

## Summary

A **graded module** over a graded Lie algebra is a module $M = M^{+}\oplus M^{-}$ with $\mathrm{G}^{\epsilon}\cdot M^{\delta}\subseteq M^{\epsilon+\delta}$ and the graded compatibility $[x,y]\cdot m = x\cdot(y\cdot m) - (-1)^{\lvert x\rvert\lvert y\rvert}y\cdot(x\cdot m)$; it carries the parity operator $\beta$ equal to $\pm\mathrm{id}$ on the two pieces, and the action graded-commutes with it, $x\beta = (-1)^{\lvert x\rvert}\beta x$, so the even elements preserve the grading and the odd elements reverse it. The sign $(-1)^{\lvert x\rvert\lvert y\rvert}$ is forced by the graded Jacobi identity: for two odd elements the anticommutator replaces the commutator, and there is no other consistent sign. The action extends to the enveloping algebra $U(\mathrm{G})$ with the graded product, so the graded modules are the graded modules over $U(\mathrm{G})$, and they form an abelian category with the graded submodules, the quotients and the homogeneous bases; the algebra itself is the adjoint module, the exterior algebra on an odd space is the module of the derivations, and the Clifford module of the orthogonal algebra is the module of the two chiralities. The trivial grading recovers the ungraded theory, and the interesting case is the one with a nonzero odd part, in which the sign rule is visible.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{G} = \mathrm{G}^{+}\oplus\mathrm{G}^{-}$ | the graded Lie algebra |
| $\alpha$ | the grade involution |
| $\lvert x\rvert\in\{0,1\}$ | the parity of a homogeneous element |
| $M = M^{+}\oplus M^{-}$ | the graded module |
| $x\cdot m$ | the bilinear action |
| $\mathrm{G}^{\epsilon}\cdot M^{\delta}\subseteq M^{\epsilon+\delta}$ | the compatibility with the grading |
| $[x,y]\cdot m = x(y m) - (-1)^{\lvert x\rvert\lvert y\rvert}y(x m)$ | the sign rule |
| $\beta$ | the parity operator, $x\beta = (-1)^{\lvert x\rvert}\beta x$ |
| $U(\mathrm{G})$ | the enveloping algebra, with the graded product |
| graded submodule, homogeneous basis | the submodules and the free modules |

## Further Reading

- Victor G. Kac, *Infinite Dimensional Lie Algebras* (Cambridge University Press, third edition, 1990), for the graded Lie algebras, the gradings and the modules with the sign rule.
- Manfred Scheunert, *The Theory of Lie Superalgebras* (Springer Lecture Notes in Mathematics 716, 1979), for the graded modules, the sign rule and the enveloping algebra.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the modules over a Lie algebra, the enveloping algebra and the ideals.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras*, Chapters 1--3 (Springer, 1989), for the universal enveloping algebra, the modules and the compatibility with the bracket.
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984), for the modules over a Lie algebra and the graded structures.
