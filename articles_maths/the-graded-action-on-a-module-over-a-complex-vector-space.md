
# __The Graded Action on a Module over a Complex Vector Space__

## Introduction

Let $V$ be a complex vector space with a Hermitian form $h$ and let $T$ be a **unitary self-adjoint involution** of $V$; the involution grades the space, $V = V_0\oplus V_1$, and its conjugation grades the endomorphism algebra, $E = \operatorname{End}_{\mathbb C}(V) = E_0\oplus E_1$. A module $M$ over $E$ is **graded** when it too is graded, $M = M_0\oplus M_1$, and the action respects the two gradings,
$$
E_i\,M_j \subseteq M_{i+j} \qquad (i, j \in \{0,1\});
$$
the action is then the module-level form of the sign carried by the signed operators, an element of $E_0$ preserving the two parts of the module and an element of $E_1$ exchanging them, and the compatibility is the statement that the action commutes with the two grade involutions up to the parity sign. The grading has a geometric reading: because $T$ is unitary, the two parts $V_0, V_1$ are orthogonal and the unitary elements of $E$ that preserve the grading — the centraliser of $T$ in the unitary group — act on the graded module by isometries, and the odd unitary elements are the isometric isomorphisms that exchange the two parts. The compatibility carries no sign in the action itself; the sign rule that the article records is the Koszul sign of the graded structure, $(-1)^{|m||n|}$ wherever two odd objects are exchanged, and it is the sign of *Superalgebras and Graded Structures* and *The Exterior Algebra*, named here and not defined.

The article has three sections: the graded modules and the compatible action; the canonical example and the induced involution; and the sign rule and the Hermitian reading. *Involutions of a Graded Linear Space* supplies the grading of $V$ and of $E$, the grade involution and the parity of endomorphisms; *The Signed Sandwich on a Complex Vector Space* and *The Signed Left Multiplication on a Complex Vector Space* supply the signed operators; *Modules over an Involutive Ring* supplies the module theory over a ring with involution; and *Superalgebras and Graded Structures* owns the sign rule and the general theory of graded modules over graded algebras, which is named here and not used. The grading by a unitary involution and the Hermitian form are *Involutive Linear Spaces*, *The Involution on a Complex Vector Space* and *Hermitian Geometry and the Unitary Group*.

Throughout, $V$ is a finite-dimensional complex vector space with a positive-definite Hermitian form $h$, $T$ is a unitary self-adjoint involution, $V = V_0\oplus V_1$ is its grading with grade involution $\alpha$, $\alpha(X) = TXT$ on $E = \operatorname{End}_{\mathbb C}(V) = E_0\oplus E_1$, $M = M_0\oplus M_1$ is a graded left $E$-module with grade involution $\beta$ equal to $+\mathrm{id}$ on $M_0$ and $-\mathrm{id}$ on $M_1$, and $\rho_X$ is the action of $X \in E$ on $M$.

## Graded Modules and the Compatible Action

**Definition.** The action of the graded algebra $E$ on the graded module $M$ is **compatible** with the gradings when
$$
E_i\,M_j \subseteq M_{i+j} \qquad (i, j \in \{0,1\}),
$$
that is when every even endomorphism preserves the two parts of $M$ and every odd endomorphism carries $M_0$ to $M_1$ and $M_1$ to $M_0$. A graded left $E$-module with a compatible action is a **graded module over $E$**.

**Proposition (the equivalent form).** The action is compatible if and only if for every homogeneous $X \in E_i$ and every $m \in M$,
$$
X\,\beta(m) = (-1)^{i}\,\beta(X\,m),
$$
equivalently $\beta(Xm) = (-1)^i X\beta(m)$; the two grade involutions therefore satisfy $\beta\circ\rho_X = (-1)^i\,\rho_X\circ\beta$ on the homogeneous part $E_i$.

**Proof.** If $m \in M_j$ and $X \in E_i$, then $Xm \in M_{i+j}$, so $\beta(Xm) = (-1)^{i+j}Xm = (-1)^iX((-1)^jm) = (-1)^iX\beta(m)$; conversely the identity for all homogeneous $m$ forces $X(M_j)\subseteq M_{i+j}$, since for $m \in M_j$ one has $\beta(Xm) = (-1)^{i+j}Xm$, which is the homogeneity statement.

**Proposition (the Hermitian reading).** The grading involution $T$ is unitary, so the two parts of $V$ are orthogonal, $h(V_0,V_1) = 0$, and $V_i = \ker(T \mp \mathrm{id})$. The even part $E_0$ and the odd part $E_1$ of the endomorphism algebra are the centraliser and the anticentraliser of $T$ up to the $T$-conjugation, $E_0 = \{X : XT = TX\}$, $E_1 = \{X : XT = -TX\}$; a **unitary** element $X$ lying in $E_0$ is an isometry of $V$ preserving the grading, and a unitary element lying in $E_1$ is an isometry exchanging the two parts.

**Proof.** Orthogonality of the eigenspaces of a self-adjoint involution is the computation of *Reflections as Signed Two-Sided Operators on a Complex Vector Space*; $X \in E_0$ means $\alpha(X) = X$, that is $TXT = X$, i.e., $XT = TX$, and $X \in E_1$ means $TXT = -X$, i.e., $XT = -TX$. A unitary $X$ is an isometry, and its parity decides whether it preserves or exchanges the $T$-eigenspaces, which are the graded parts.

**Corollary (the module as a graded module over a graded algebra).** The pair $(M, \beta)$ with the compatible action is a graded module over the graded algebra $(E, \alpha)$; the even part $E_0$ acts on each $M_j$ and the odd part $E_1$ maps $M_0$ to $M_1$ and $M_1$ to $M_0$, and the action is determined by the two even restrictions $E_0\times M_j\to M_j$ and the two odd restrictions $E_1\times M_j\to M_{1-j}$.

**Proof.** The inclusions $E_iM_j\subseteq M_{i+j}$ and the associativity of the action are the axioms of a graded module; the description of the parts is the definition of the inclusions.

## The Canonical Example and the Induced Involution

**Proposition (the space as its own graded module).** $M = V$ with the grading $V = V_0\oplus V_1$, the grade involution $\beta = \alpha$ with $\alpha(v) = Tv$, and the evaluation action $X\cdot v = Xv$ is a graded $E$-module: the inclusions $E_iV_j\subseteq V_{i+j}$ hold because an even endomorphism preserves the two parts and an odd one exchanges them.

**Proof.** The action is associative and unital by the definition of composition, and the inclusions are the parity statement: $X \in E_i$ satisfies $X(V_j)\subseteq V_{i+j}$ because $XT = (-1)^iTX$ and the $V_j$ are the $T$-eigenspaces. This is *Involutions of a Graded Linear Space*.

**Proposition (the induced involution on the module endomorphisms).** The algebra $\operatorname{End}_E(M)$ of module endomorphisms is graded by
$$
\operatorname{End}_E(M)_i = \{f : f(M_j)\subseteq M_{i+j}\},
$$
with grade involution $\gamma(f) = \beta f \beta$; the same holds for the algebra $\operatorname{End}_{\mathbb C}(M)$ of all complex-linear endomorphisms of $M$ when $M$ is a complex vector space.

**Proof.** The composition of endomorphisms adds parities, and conjugation by $\beta$ is an automorphism of order two with the two eigenspaces $f(M_j)\subseteq M_j$ and $f(M_j)\subseteq M_{1-j}$. This is the computation of *Involutions of a Graded Linear Space* for the endomorphism algebra of a graded space.

**Remark (the Hermitian module).** When $M$ carries a Hermitian form for which $\beta$ is unitary and self-adjoint, the two graded parts of $M$ are orthogonal, and the induced involution $\gamma$ on the module endomorphisms is again the conjugation by a unitary self-adjoint involution; the graded module endomorphisms of even parity are then the isometries preserving the grading and those of odd parity the isometric isomorphisms exchanging the two parts. The grading of a module is thus a parity attached to a unitary symmetry, and the compatible action is the action of the graded algebra on the graded Hermitian module.

## The Sign Rule

**Definition.** The **sign rule** of the graded structure is the Koszul sign $(-1)^{|m||n|}$: it is the factor by which the flip of two homogeneous elements is corrected,
$$
\tau(m\otimes n) = (-1)^{|m||n|}\,n\otimes m ,
$$
and it is the factor in the graded Leibniz rule of a homogeneous derivation of parity $|D|$,
$$
D(mn) = (Dm)\,n + (-1)^{|D||m|}\,m\,(Dn) .
$$

**Proposition (the sign rule is the parity of the action).** Let $X \in E_i$ act on the graded module $M$ by $\rho_X$, and suppose $M$ is an algebra on which $E$ acts by derivations. Then $X$ acts as a graded derivation of parity $i$,
$$
\rho_X(mn) = \rho_X(m)\,n + (-1)^{i|m|}\,m\,\rho_X(n) ,
$$
and the sign is the Koszul sign of the two odd objects $X$ and $m$.

**Proof.** The compatibility $\beta\rho_X = (-1)^i\rho_X\beta$ says that the action of $X$ is even or odd according to $i$; an action of parity $i$ that is a derivation of the algebra $M$ is a graded derivation of parity $i$, which is exactly the displayed rule. The rule is not an extra axiom of the graded action; it is the parity of the graded structure, and its own theory is *Superalgebras and Graded Structures*.

**Remark (the deferred sign rule).** The compatibility $E_iM_j\subseteq M_{i+j}$ carries no sign: the grade involutions commute or anticommute on the homogeneous parts, and no sign enters the action itself. The sign rule that makes the tensor product of two graded modules a graded module with the Koszul flip belongs to *Superalgebras and Graded Structures* and to *The Exterior Algebra*, where the graded-commutative product $\alpha\wedge\beta = (-1)^{|\alpha||\beta|}\beta\wedge\alpha$ realises it; it is named here because the graded actions of the later articles refer to it, and it is not defined or used.

**Example (the exterior algebra of a Hermitian space).** Let $G$ be the unitary group of $V$ and $M = \Lambda V$ the exterior algebra, graded by the parity of the degree; the action of $G$ extends to $\Lambda V$ and preserves each degree, so it is a graded action, and the Koszul sign is the sign of the wedge product. The fixed submodule of the even subgroup — the special unitary group, which preserves the degree — is the span of the volume element in each degree where an invariant form exists, and this is the geometric instance of the graded action of the category.

## Summary

A grading of a complex vector space by a unitary self-adjoint involution $T$ makes $V = V_0\oplus V_1$ an orthogonal decomposition and grades the endomorphism algebra $E = \operatorname{End}_{\mathbb C}(V) = E_0\oplus E_1$ with $E_0$ the centraliser and $E_1$ the anticentraliser of $T$; a graded module $M = M_0\oplus M_1$ over $E$ carries a compatible action exactly when $E_iM_j\subseteq M_{i+j}$, equivalently when the two grade involutions satisfy $\beta\rho_X = (-1)^i\rho_X\beta$ on the homogeneous part $E_i$, and then $E_0$ preserves the two parts of $M$ and $E_1$ exchanges them, the action being determined by the two even restrictions and the two odd ones. The canonical example is the space itself, $M = V$ with $\beta = \alpha$, $v\mapsto Tv$; the module endomorphisms are graded by $\operatorname{End}_E(M)_i = \{f : f(M_j)\subseteq M_{i+j}\}$ with grade involution $\gamma(f) = \beta f\beta$, and the unitary even and odd elements act as isometries preserving and exchanging the graded parts. The sign rule is the Koszul sign $(-1)^{|m||n|}$, appearing in the flip $\tau(m\otimes n) = (-1)^{|m||n|}n\otimes m$ and in the graded Leibniz rule $D(mn) = (Dm)n + (-1)^{|D||m|}m(Dn)$; it is the parity of the graded structure and not an independent axiom, and its theory is *Superalgebras and Graded Structures* and *The Exterior Algebra*. The signed operators are *The Signed Sandwich on a Complex Vector Space* and *The Signed Left Multiplication on a Complex Vector Space*; the adjoint action on the endomorphism module is the group `- * Operator Theory`.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V=V_0\oplus V_1$, $T$, $\alpha$ | the graded Hermitian space, its unitary involution and grade involution |
| $E=\operatorname{End}_{\mathbb C}(V)=E_0\oplus E_1$ | the graded endomorphism algebra |
| $M=M_0\oplus M_1$, $\beta$ | the graded module and its grade involution |
| $E_iM_j\subseteq M_{i+j}$ | the compatibility of the action |
| $\beta\rho_X=(-1)^i\rho_X\beta$ on $E_i$ | the equivalent form |
| $\operatorname{End}_E(M)_i$, $\gamma(f)=\beta f\beta$ | the graded module endomorphisms and their involution |
| $\tau(m\otimes n)=(-1)^{|m||n|}n\otimes m$ | the Koszul flip; the sign rule |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for graded modules and algebras.
- Pierre Deligne and John W. Morgan, *Notes on Supersymmetry (following Joseph Bernstein)*, in *Quantum Fields and Strings* (American Mathematical Society, 1999), for graded modules and parity.
- Werner Greub, *Multilinear Algebra* (Springer, second edition, 1978), for the exterior algebra, its Koszul sign and the action of the unitary group.
- Yuri I. Manin, *Gauge Field Theory and Complex Geometry* (Springer, second edition, 1997), for the linear algebra of graded spaces and modules.
