# __The Graded Action on a Module over a Linear Space__

## Introduction

The endomorphism algebra $E = \operatorname{End}_F(V)$ is graded by the eigenspaces of the grade involution, $E = E_0\oplus E_1$, and a module over $E$ is **graded** when it too is graded and the action respects the two gradings, $E_iM_j \subseteq M_{i+j}$. Such an action is the module-level form of the sign carried by the signed operators: an element of $E_0$ preserves the two parts of the module and an element of $E_1$ exchanges them, and the compatibility is exactly the statement that the action commutes with the two grade involutions up to the parity sign. This article defines the graded module, states the compatibility in its equivalent forms, records the canonical example, in which the module is $V$ itself, and defers the sign rule of the graded tensor product to its owner.

*Involutions of a Graded Linear Space* supplies the grading of $V$ and of $E$, the grade involution and the parity of endomorphisms; *The Signed Sandwich on a Linear Space* and *The Signed Left Multiplication on a Linear Space* supply the signed operators; *Modules over an Involutive Ring* supplies the module theory over a ring with involution; and *Superalgebras and Graded Structures* owns the sign rule and the general theory of graded modules over graded algebras, which is named here and not used.

Throughout, $F$ is a field with $2 \neq 0$, $V = V_0\oplus V_1$ is a graded linear space with grade involution $\alpha$, $E = \operatorname{End}_F(V) = E_0\oplus E_1$ is its graded endomorphism algebra, and $M = M_0\oplus M_1$ is a graded left $E$-module with grade involution $\beta$, $\beta = +\mathrm{id}$ on $M_0$ and $-\mathrm{id}$ on $M_1$. No form, norm or topology is used.

## Graded Modules and the Compatible Action

**Definition.** The action of $E$ on the graded module $M$ is **compatible** with the gradings when

$$
E_i\,M_j \subseteq M_{i+j} \qquad (i,j \in \{0,1\}) ,
$$

that is, when the even endomorphisms preserve the two parts of $M$ and the odd endomorphisms exchange them.

**Proposition (the equivalent form).** The action is compatible if and only if for every homogeneous $X \in E_i$ and every $m \in M$,

$$
X\,\beta(m) = (-1)^{i}\,\beta(X\,m) ,
$$

equivalently $\beta(Xm) = (-1)^i X\beta(m)$; the two grade involutions therefore satisfy $\beta\circ \rho_X = (-1)^i \rho_X\circ\beta$ on the homogeneous part $E_i$, where $\rho_X$ is the action of $X$.

**Proof.** If $m \in M_j$ and $X \in E_i$, then $Xm \in M_{i+j}$, so $\beta(Xm) = (-1)^{i+j}Xm = (-1)^i X((-1)^j m) = (-1)^iX\beta(m)$; conversely this identity for all homogeneous $m$ forces $X(M_j)\subseteq M_{i+j}$, since for $m \in M_j$ one has $\beta(Xm) = (-1)^{i+j}Xm$, which is the homogeneity statement.

**Corollary (the module as a graded module over a graded algebra).** The pair $(M,\beta)$ with the compatible action is a graded module over the graded algebra $(E,\alpha)$; the even part $E_0$ acts on each $M_j$ and the odd part $E_1$ maps $M_0$ to $M_1$ and $M_1$ to $M_0$, and the action is determined by its two restrictions $E_0\times M_j\to M_j$ and $E_1\times M_j\to M_{1-j}$.

**Proof.** The inclusions $E_iM_j\subseteq M_{i+j}$ and the associativity of the action are the axioms of a graded module; the description of the two parts is the definition of the inclusions.

## The Canonical Example and the Induced Involution

**Proposition (the space as its own graded module).** $M = V$ with the grading $V = V_0\oplus V_1$, the grade involution $\beta = \alpha$, and the evaluation action $X\cdot v = Xv$ is a graded $E$-module; the inclusions $E_iV_j\subseteq V_{i+j}$ hold because an even endomorphism preserves the two parts and an odd one exchanges them.

**Proof.** The action is associative and unital by the definition of composition, and the inclusions are the parity statement of *Involutions of a Graded Linear Space*.

**Proposition (the induced involution on the module endomorphisms).** The algebra $\operatorname{End}_E(M)$ of module endomorphisms is graded by $\operatorname{End}_E(M)_i = \{f : f(M_j)\subseteq M_{i+j}\}$, with grade involution $\gamma(f) = \beta f \beta$; the same holds for the algebra $\operatorname{End}_F(M)$ of all linear endomorphisms of $M$ when $M$ is a linear space.

**Proof.** The composition of endomorphisms adds parities, and conjugation by $\beta$ is an automorphism of order two with the two eigenspaces $f(M_j)\subseteq M_j$ and $f(M_j)\subseteq M_{1-j}$. This is the computation of *Involutions of a Graded Linear Space* for the endomorphism algebra of a graded space.

**Remark (the deferred sign rule).** The compatibility above carries no sign: the grade involutions commute or anticommute on the homogeneous parts, and no sign enters the action itself. The sign rule that makes the tensor product of two graded modules a graded module with the twisted flip belongs to *Superalgebras and Graded Structures*; it is named here because the graded actions of the later articles refer to it, and it is not defined or used.

## Summary

A graded left module $M = M_0\oplus M_1$ over the graded endomorphism algebra $E = E_0\oplus E_1$ of a graded linear space carries a compatible action exactly when $E_iM_j\subseteq M_{i+j}$, equivalently when the two grade involutions satisfy $\beta\rho_X = (-1)^i\rho_X\beta$ on the homogeneous part $E_i$; then $E_0$ preserves the two parts of $M$ and $E_1$ exchanges them, and the action is determined by the two even restrictions and the two odd ones. The canonical example is the space itself, $M = V$ with $\beta = \alpha$; the module endomorphisms are graded by $\operatorname{End}_E(M)_i=\{f: f(M_j)\subseteq M_{i+j}\}$ with grade involution $\gamma(f)=\beta f\beta$. The sign rule of the graded tensor product and the general theory of graded modules over graded algebras are *Superalgebras and Graded Structures*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V=V_0\oplus V_1$, $\alpha$ | the graded space and its grade involution |
| $E=\operatorname{End}_F(V)=E_0\oplus E_1$ | the graded endomorphism algebra |
| $M=M_0\oplus M_1$, $\beta$ | the graded module and its grade involution |
| $E_iM_j\subseteq M_{i+j}$ | the compatibility of the action |
| $\beta\rho_X=(-1)^i\rho_X\beta$ on $E_i$ | the equivalent form |
| $\operatorname{End}_E(M)_i$ | the graded module endomorphisms |
| $\gamma(f)=\beta f\beta$ | the grade involution on endomorphisms |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for graded modules and algebras.
- Pierre Deligne and John W. Morgan, *Notes on Supersymmetry (following Joseph Bernstein)*, in *Quantum Fields and Strings* (American Mathematical Society, 1999), for graded modules and parity.
- Yuri I. Manin, *Gauge Field Theory and Complex Geometry* (Springer, 2nd ed. 1997), for the linear algebra of graded spaces and modules.
