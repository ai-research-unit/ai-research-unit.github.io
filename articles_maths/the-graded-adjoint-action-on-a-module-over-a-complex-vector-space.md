
# __The Graded Adjoint Action on a Module over a Complex Vector Space__

## Introduction

The endomorphism algebra $E = \operatorname{End}_{\mathbb C}(V)$ of a complex space with a grade involution $\alpha(X) = TXT$, $T$ a unitary self-adjoint involution, is a **graded algebra**: it splits into the eigenspaces of $\alpha$,
$$
E = E_0\oplus E_1, \qquad E_0 = \{X : \alpha(X) = X\}, \quad E_1 = \{X : \alpha(X) = -X\},
$$
the **even** and **odd** parts, with $E_iE_j \subseteq E_{i+j}$; equivalently each $X$ has a degree $|X| \in \{0,1\}$ and $XY$ has degree $|X|+|Y|$. A **graded module** over $E$ is a module $M = M_0\oplus M_1$ with $E_iM_j \subseteq M_{i+j}$, and the **adjoint action** on the $E$-linear endomorphisms of $M$ is the graded commutator
$$
\mathrm{ad}_X(f) = Xf - (-1)^{|X|\,|f|}\,fX ,
$$
the dot action of the graded algebra on itself and on its modules. The adjoint action is compatible with the grading — $\mathrm{ad}_{E_i}$ raises the degree by $i$ — it obeys the **sign rule** in the form of the graded antisymmetry $[X,Y] = -(-1)^{|X||Y|}[Y,X]$, the graded Jacobi identity and the graded Leibniz rule, and its **adjoint** for the Hermitian trace form $\langle X,Y\rangle = \operatorname{tr}(X^{\dagger}Y)$ is the adjoint action of the adjoint element,
$$
\mathrm{ad}_X^{*} = \mathrm{ad}_{X^{\dagger}} ,
$$
so that the even self-adjoint elements generate self-adjoint adjoint actions and the graded structure is preserved by the passage to the adjoint.

The article has three sections: the graded algebra and the graded module, and the sign rule; the adjoint action, its compatibility with the grading and the graded identities; and the adjoint of the adjoint action for the trace form. The grade involution is *The Involution on a Complex Vector Space* and *The Signed Sandwich on a Complex Vector Space*; the adjoint laws are *The Adjoint of the Left Multiplication on a Complex Vector Space* and *The Signed Adjoint Sandwich on a Complex Vector Space*, the latter the preceding article of this group; the endomorphism algebra and the trace form are *Algebras of Endomorphisms* and *Grassmann Variables and Berezin Integration*; the graded Lie algebras and the superalgebras are *Graded Lie Algebras and Lie Superalgebras* and *Superalgebras and Graded Structures*; the adjoint of a Hermitian operator is *The Adjoint of a Hermitian Operator*. None of that is re-derived.

Throughout, $V$ is a finite-dimensional complex vector space with a positive-definite Hermitian form $h$, $E = \operatorname{End}_{\mathbb C}(V)$, $T$ is a unitary self-adjoint involution, $\alpha(X) = TXT$ with eigenspaces $E_0,E_1$, $A^{\dagger}$ is the $h$-adjoint, $M = M_0\oplus M_1$ is a graded $E$-module, and $\langle X,Y\rangle = \operatorname{tr}(X^{\dagger}Y)$ is the Hermitian trace form of $E$.

## The Graded Algebra, the Graded Module and the Sign Rule

**Proposition (the graded algebra).** The eigenspaces $E_0$ and $E_1$ of $\alpha$ satisfy
$$
E_0E_0 \subseteq E_0, \qquad E_0E_1 \subseteq E_1, \qquad E_1E_0 \subseteq E_1, \qquad E_1E_1 \subseteq E_0 ,
$$
so $E$ is a $\mathbb{Z}_2$-graded algebra with degree $|X| = 0$ on $E_0$ and $1$ on $E_1$; the $\mathbb{C}$-subalgebra $E_0$ is the commutant of $T$, and $E_1$ is its odd complement, $E_1 = E_0T$.

**Proof.** For $X \in E_{|X|}$ and $Y \in E_{|Y|}$ one has $\alpha(XY) = \alpha(X)\alpha(Y) = (-1)^{|X|}(-1)^{|Y|}XY = (-1)^{|X|+|Y|}XY$, so $XY$ has degree $|X|+|Y|$ modulo $2$; the commutant statement is $TX = XT$ if and only if $\alpha(X)=X$, and $T$ itself is odd, so $E_1 = E_0T$. This is *The Involution on a Complex Vector Space* and *Superalgebras and Graded Structures*.

**Definition (graded module).** A **graded $E$-module** is an $E$-module $M$ with a decomposition $M = M_0\oplus M_1$ such that $E_iM_j \subseteq M_{i+j}$; an element of $M_j$ is homogeneous of degree $j$, and an $E$-linear map $f : M \to M$ is homogeneous of degree $|f|$ when $f(M_j) \subseteq M_{j+|f|}$.

**Proposition (the sign rule).** The graded commutator
$$
[X, Y] = XY - (-1)^{|X||Y|}YX
$$
on homogeneous elements is graded antisymmetric, $[X,Y] = -(-1)^{|X||Y|}[Y,X]$, satisfies the graded Jacobi identity
$$
(-1)^{|X||Z|}\bigl[X,[Y,Z]\bigr] + (-1)^{|Y||X|}\bigl[Y,[Z,X]\bigr] + (-1)^{|Z||Y|}\bigl[Z,[X,Y]\bigr] = 0,
$$
and the graded Leibniz rule $[X,YZ] = [X,Y]Z + (-1)^{|X||Y|}Y[X,Z]$; the commutator is the ordinary one on the even part and the anticommutator on the odd part.

**Proof.** The antisymmetry is $XY - (-1)^{|X||Y|}YX = -(-1)^{|X||Y|}(YX - (-1)^{|X||Y|}XY)$; the Jacobi identity and the Leibniz rule are the standard expansions of associativity, with the signs collected by the rule that a homogeneous element crosses another with the Koszul sign $(-1)^{|X||Y|}$; for $X,Y$ odd the formula is $XY+YX$, the anticommutator. This is *Graded Lie Algebras and Lie Superalgebras* and *Superalgebras and Graded Structures*.

## The Adjoint Action and Its Compatibility with the Grading

**Definition.** The **adjoint action** of $E$ on itself and on its modules is
$$
\mathrm{ad}_X(Y) = [X, Y] = XY - (-1)^{|X||Y|}YX ;
$$
it is the graded adjoint representation of the graded Lie algebra $E$.

**Proposition (compatibility with the grading).** The adjoint action is a **graded derivation** of $E$ and a graded map of degree $|X|$,
$$
\mathrm{ad}_X(E_j) \subseteq E_{j+|X|}, \qquad \mathrm{ad}_X(YZ) = \mathrm{ad}_X(Y)\,Z + (-1)^{|X||Y|}Y\,\mathrm{ad}_X(Z),
$$
so an even adjoint action preserves the degree and an odd adjoint action exchanges the two degrees; the graded Jacobi identity is the statement that $\mathrm{ad}$ is a representation, $\mathrm{ad}_{[X,Y]} = [\mathrm{ad}_X,\mathrm{ad}_Y]$, with the graded commutator of the operators on the right.

**Proof.** The degree statement is that $[E_i,E_j]\subseteq E_{i+j}$, which is the graded-algebra proposition and the sign-free part of the graded commutator; the Leibniz rule is the graded Leibniz of the previous proposition; the representation identity is the graded Jacobi identity rewritten in terms of the adjoint action, $\mathrm{ad}_X\mathrm{ad}_Y - (-1)^{|X||Y|}\mathrm{ad}_Y\mathrm{ad}_X = \mathrm{ad}_{[X,Y]}$. This is *Graded Lie Algebras and Lie Superalgebras* and *The Lie Correspondence and the Adjoint Representation*.

**Corollary (the even and odd adjoint actions).** The even adjoint actions $\mathrm{ad}_X$ with $X \in E_0$ form the Lie algebra of the commutant and preserve every graded piece of $M$; the odd adjoint actions with $X \in E_1$ exchange $M_0$ and $M_1$ and are the odd part of the graded Lie algebra; the whole adjoint action is the graded Lie algebra $\mathfrak{gl}(M)$ of the graded endomorphisms.

**Proof.** The degree statement of the proposition gives the preservation for even $X$ and the exchange for odd $X$; the commutator $[E_0,E_0]\subseteq E_0$ makes $E_0$ a Lie subalgebra, acting on each graded piece, and the odd part is the complement. This is *Graded Lie Algebras and Lie Superalgebras* and *The Lie Correspondence and the Adjoint Representation*.

## The Adjoint of the Adjoint Action

**Proposition (the adjoint of the adjoint action).** For the ordinary commutator $\mathrm{ad}_X(Y) = XY-YX$ and the Hermitian trace form of $E$,
$$
\mathrm{ad}_X^{*} = \mathrm{ad}_{X^{\dagger}}
$$
for every $X$, so the adjoint of the adjoint action of $X$ is the adjoint action of the adjoint element; in particular the adjoint action of a Hermitian element is self-adjoint, and that of an anti-Hermitian element is anti-Hermitian. For the graded commutator the same identity holds when $X$ is even, and for odd $X$ the adjoint acquires the sign $(-1)^{|X|}$.

**Proof.** $\langle \mathrm{ad}_X(Y), Z\rangle = \operatorname{tr}((XY-YX)^{\dagger}Z) = \operatorname{tr}(Y^{\dagger}X^{\dagger}Z) - \operatorname{tr}(X^{\dagger}Y^{\dagger}Z)$. Cyclically moving $X^{\dagger}$ in the second term, $\operatorname{tr}(X^{\dagger}Y^{\dagger}Z) = \operatorname{tr}(Y^{\dagger}ZX^{\dagger})$, so the sum is $\operatorname{tr}(Y^{\dagger}(X^{\dagger}Z - ZX^{\dagger})) = \operatorname{tr}(Y^{\dagger}[X^{\dagger},Z]) = \langle Y, \mathrm{ad}_{X^{\dagger}}Z\rangle$, which is the identity; the Hermitian and anti-Hermitian statements are $X^{\dagger}=\pm X$. For the graded commutator the same computation leaves the factor $(-1)^{|X||Y|}$ on the second term, which equals $(-1)^{|X||Z|}$ when $X$ is even and differs by $(-1)^{|X|}$ when $X$ is odd. This is *The Adjoint of the Left Multiplication on a Complex Vector Space* and *The Adjoint of a Hermitian Operator*.

**Corollary (the self-adjoint adjoint actions).** The adjoint action of a Hermitian even element is a self-adjoint degree-preserving graded derivation; the adjoint action of an anti-Hermitian odd element is an anti-Hermitian degree-exchanging graded derivation; the graded commutator of the adjoint actions corresponds to the graded commutator of the elements, so $\mathrm{ad}$ is a graded Lie algebra homomorphism compatible with the adjoint.

**Proof.** The self-adjointness and the anti-Hermitian nature are the proposition applied to $X = X^{\dagger}$ and $X = -X^{\dagger}$; the degree behaviour is the compatibility with the grading, and the algebra homomorphism is the graded Jacobi identity. This is *Graded Lie Algebras and Lie Superalgebras* and *The Lie Correspondence and the Adjoint Representation*.

**Example (the even and odd adjoint actions of a reflection).** For the grade involution of a reflection $r$, the even part $E_0$ is the commutant of $r$ and the odd part $E_1 = E_0r$; the adjoint action of an element $X$ of the commutant is the ordinary commutator $[X,Y]$ and preserves the two eigenspaces of $\mathrm{ad}_X$; the adjoint action of the odd element $r$ is the graded commutator $[r,Y] = rY-(-1)^{|Y|}Yr$, which for even $Y$ is the anticommutator $rY+Yr$ and exchanges the graded pieces. This is *The Signed Adjoint of the Reflection on a Complex Vector Space*.

**Remark (the graded trace form).** The Hermitian trace form of $E$ restricts to the even part as an invariant form of the Lie algebra $E_0$, and the invariance of the trace under the cyclic permutation is what makes the adjoint formula $\mathrm{ad}_X^{*} = \mathrm{ad}_{X^{\dagger}}$ hold; the graded refinement replaces the trace by the supertrace on the odd part, with the sign rule of the graded structure, and the adjoint formula persists with the adjoints taken in the graded sense. This is *Graded Lie Algebras and Lie Superalgebras* and *Algebras of Endomorphisms*.

## Summary

The endomorphism algebra $E$ of a complex space with a grade involution is a $\mathbb{Z}_2$-graded algebra $E = E_0\oplus E_1$, with the commutant of the involution as the even part and $E_1 = E_0T$ as the odd part; a graded module splits accordingly, and the graded commutator $[X,Y] = XY-(-1)^{|X||Y|}YX$ obeys the sign rule, the graded antisymmetry, the graded Jacobi identity and the graded Leibniz rule. The adjoint action $\mathrm{ad}_X(Y) = [X,Y]$ is a graded derivation of degree $|X|$, preserving the degree for even $X$ and exchanging for odd $X$, and it is a representation of the graded Lie algebra; for the Hermitian trace form its adjoint is $\mathrm{ad}_X^{*} = \mathrm{ad}_{X^{\dagger}}$, so the adjoint action of a Hermitian element is self-adjoint and that of an anti-Hermitian element is anti-Hermitian, and the whole construction is the graded Lie algebra of the graded endomorphisms. The grade involution is *The Involution on a Complex Vector Space* and *The Signed Sandwich on a Complex Vector Space*; the adjoint laws are *The Adjoint of the Left Multiplication on a Complex Vector Space* and *The Signed Adjoint Sandwich on a Complex Vector Space*; the graded structures are *Graded Lie Algebras and Lie Superalgebras*, *Superalgebras and Graded Structures* and *Grassmann Variables and Berezin Integration*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E=E_0\oplus E_1$ | the graded algebra, eigenspaces of $\alpha$ |
| $|X|\in\{0,1\}$ | the degree of a homogeneous element |
| $[X,Y]=XY-(-1)^{|X||Y|}YX$ | the graded commutator, the sign rule |
| $\mathrm{ad}_X(Y)=[X,Y]$ | the adjoint action |
| $\mathrm{ad}_{E_i}\subseteq E_{j+|X|}$ | compatibility with the grading |
| $\mathrm{ad}_X^{*}=\mathrm{ad}_{X^{\dagger}}$ | the adjoint of the adjoint action |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the graded algebras with involution and the adjoint actions.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the adjoint representation, the derivations and the Jacobi identity.
- Werner Greub, *Multilinear Algebra* (Springer, second edition, 1978), for the graded algebras, the graded commutators and the supertrace.
- Victor Kac, *Graded Lie Algebras and Lie Superalgebras* (Advances in Mathematics 26, 1977), for the graded Lie algebras, the sign rule and the adjoint action.
