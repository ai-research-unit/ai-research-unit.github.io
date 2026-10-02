# __The Fundamental Symmetry__

## Introduction

Every indefinite inner product space carries, as soon as a fundamental decomposition is chosen, an operator $J$ of square one which turns the indefinite form into a positive definite one: the form of the space is recovered from the definite form by $[x,y] = \langle Jx,y\rangle$, and $J$ acts as $+\mathrm{id}$ on the positive part and as $-\mathrm{id}$ on the negative part. This operator is the **fundamental symmetry**, and it is the single device that lets the whole definite theory be imported into the indefinite one: an indefinite statement is a definite statement with every form occurrence conjugated by $J$.

Three properties make $J$ do this work. It is **involutive**, $J^{2} = \mathrm{id}$, so the space splits into its two eigenspaces, which are exactly the positive and the negative parts of the decomposition. It is **self-adjoint** for the indefinite form, $[Jx,y] = [x,Jy]$, which is what makes $\langle x,y\rangle = [Jx,y]$ Hermitian; and it is self-adjoint for the definite form as well, so it is an isometry of both. And the definite form it defines is **positive definite**, so the indefinite space acquires the structure of a Hilbert space and its topology.

The choice is not unique: when both parts are nonzero there are as many fundamental symmetries as there are maximal positive definite subspaces. The differences between two choices are encoded by an operator between the two negative parts, the **angular operator**, and the norms induced by the choices are all equivalent because the angular operator is a strict contraction. This article fixes the definition and the bridge, the eigenspace description of the decomposition, the isometry properties, the non-uniqueness with the angular operator, and the order structure $J$ induces.

The indefinite form and the fundamental decomposition are *Indefinite Inner Product Spaces*; the complete case is *Krein Spaces*; the finite rank of negativity is *Pontryagin Spaces*; the operators that $J$ makes available – the $J$-self-adjoint and $J$-unitary operators and the $J$-positive cone – are *J-Self-Adjoint and J-Unitary Operators*; the use of $J$ in the algebra is *Krein Algebras* and *Krein–von Neumann Algebras*. Those are cited. The base is $\mathbb{R}$ or $\mathbb{C}$ with its conjugation, the indefinite form is $[\cdot,\cdot]$, and $J$ always satisfies $J^{2} = \mathrm{id}$ and $[Jx,y] = [x,Jy]$.

## The Definition and the Bridge

**Definition.** A **fundamental symmetry** of an indefinite inner product space $V$ with form $[\cdot,\cdot]$ is an $F$-linear operator $J$ with

$$
J^{2} = \mathrm{id}, \qquad [Jx,y] = [x,Jy], \qquad [Jx,x] > 0 \text{ for } x \neq 0 .
$$

The last condition says that the form $\langle x,y\rangle = [Jx,y]$ is positive definite; it is called the **definite form induced by $J$**.

**Theorem (the bridge).** Let $J$ be a fundamental symmetry and put $\langle x,y\rangle = [Jx,y]$. Then $\langle\cdot,\cdot\rangle$ is a positive definite Hermitian form, $J$ is self-adjoint and involutive for it, and the indefinite form is recovered by

$$
[x,y] = \langle Jx,y\rangle .
$$

Conversely, every involutive and indefiniteness-self-adjoint operator $J$ for which $[Jx,x] > 0$ off zero arises from a fundamental decomposition. So the data of a fundamental symmetry and the data of a fundamental decomposition are the same, and an indefinite inner product space is a definite one together with $J$.

**Proof.** The Hermitian symmetry of $\langle\cdot,\cdot\rangle$ is the self-adjointness of $J$ for $[\,,\,]$; positivity is the third condition; the recovery is $J^{2} = \mathrm{id}$; and the converse is the spectral decomposition of $J$ into its $\pm1$-eigenspaces, which are then definite by the positivity.

**Proposition (both forms are isometric).** $J$ preserves the indefinite form and the definite form:

$$
[Jx,Jy] = [x,y], \qquad \langle Jx,Jy\rangle = \langle x,y\rangle .
$$

So $J$ is a unitary operator of the positive definite space and an isometry of the indefinite one, and it is the same operator in both roles.

**Proof.** $[Jx,Jy] = [x,J^{2}y] = [x,y]$; and $\langle Jx,Jy\rangle = [J^{2}x,Jy] = [x,Jy] = [Jx,y] = \langle x,y\rangle$.

## The Eigenspaces

**Proposition.** For a fundamental symmetry $J$ the eigenspaces

$$
V_{+} = \ker(J-\mathrm{id}), \qquad V_{-} = \ker(J+\mathrm{id})
$$

are the positive definite and the negative definite parts of a fundamental decomposition: $V = V_{+}\oplus V_{-}$, $V_{+}\perp V_{-}$, and the elements of $V_{+}$ are positive and those of $V_{-}$ negative.

**Proof.** An involutive operator has the two eigenspaces and their direct sum is $V$; for $x\in V_{+}$ the definite form gives $\langle x,x\rangle = [Jx,x] = [x,x]$, so $[x,x] > 0$, and for $x\in V_{-}$, $\langle x,x\rangle = -[x,x] > 0$, so $[x,x] < 0$; orthogonality follows from $[x_{+},x_{-}] = \langle Jx_{+},x_{-}\rangle = \langle x_{+},x_{-}\rangle = 0$.

**Corollary (the decomposition is read by $J$).** A fundamental decomposition is a pair of definite eigenspaces of an involutive operator; the signature of the space is $(\dim V_{+},\dim V_{-})$, and the operator $J$ is the fundamental symmetry of that decomposition.

**Proof.** Immediate from the proposition and the definition of the signature.

## Non-Uniqueness and the Angular Operator

**Theorem (parametrisation of the symmetries).** Let $V = V_{+}\oplus V_{-}$ be a fundamental decomposition with symmetry $J$. The fundamental symmetries of $V$ correspond bijectively to the maximal positive definite subspaces $\tilde V_{+}$, each of which is the **graph**
$$
M_T = \{\, x_{+} + Tx_{+} : x_{+}\in V_{+} \,\}
$$
of one and only one linear map $T : V_{+}\to V_{-}$; the symmetry of $M_T$ is $+\mathrm{id}$ on $M_T$ and $-\mathrm{id}$ on its orthogonal complement $M_T^{\perp}$, and $M_T$ is positive definite exactly when $T$ is a **strict contraction** for the norm $\|x\| = \langle x,x\rangle^{1/2}$,
$$
\|Tx_{+}\| < \|x_{+}\| \qquad \text{for } x_{+}\neq0 .
$$
Distinct $T$ give distinct symmetries, and the correspondence is a bijection.

**Proof.** Let $\tilde V_{+}$ be a maximal positive definite subspace and project it to $V_{+}$ along $V_{-}$. The projection is injective, since a nonzero element of $\tilde V_{+}\cap V_{-}$ would be both positive and negative, and it is surjective because $\dim\tilde V_{+} = \dim V_{+}$; so $\tilde V_{+}$ is the graph $M_T$ of a linear $T$. For $x = x_{+} + Tx_{+}$ one has $\langle x,x\rangle = [Jx,x] = [x_{+},x_{+}] + [Tx_{+},Tx_{+}] = \|x_{+}\|^{2} - \|Tx_{+}\|^{2}$, the two summands being orthogonal, and this is positive for every $x\neq0$ exactly when $\|Tx_{+}\| < \|x_{+}\|$ whenever $x_{+}\neq0$. The rest is the preceding proposition: $\tilde V_{+}$ definite and maximal makes $\tilde J = +\mathrm{id}$ on it and $-\mathrm{id}$ on its definite orthogonal complement a fundamental symmetry, and $\tilde V_{+}$ is recovered as the $+1$-eigenspace, so the map $T\mapsto M_T\mapsto\tilde J$ is a bijection.

**Definition.** The operator $T$ above is the **angular operator** between the two decompositions, and its contraction constant measures the opening between their positive parts: $T = 0$ exactly when the two positive parts coincide.

**Proposition (equivalence of the induced forms).** The definite forms induced by any two fundamental symmetries are equivalent, and the topology they define is the same.

**Proof.** Let $J'$ be the second symmetry and write $\langle x,x\rangle' = [J'x,x] = \langle JJ'x,x\rangle$. The operator $JJ'$ is bounded and self-adjoint for $\langle\cdot,\cdot\rangle$ and it is invertible, with $(JJ')^{-1} = J'J$ because $J^{2} = J'^{2} = \mathrm{id}$; its spectrum is therefore a compact subset of $(0,\infty)$, so there are constants $0 < c\leq C < \infty$ with $c\|x\|^{2}\leq\langle x,x\rangle'\leq C\|x\|^{2}$, and the two norms are equivalent.

**Remark (the non-uniqueness is genuine and bounded).** When both $p$ and $q$ are nonzero the fundamental symmetries are as many as the graphs $M_T$, so the choice is genuine; but the theorem shows the choice never changes the topology and only rotates the positive part inside its indefinite orthogonal complement, with an angle strictly less than $\pi/2$.

## $J$ as the Bridge

**Proposition (dictionary).** Through $J$ every notion of the definite theory transports to the indefinite one, and the transport is the conjugation by $J$:

| Indefinite notion | Definite notion under $J$ |
|---|---|
| $[x,y]$ | $\langle Jx,y\rangle$ |
| $[Ax,y] = [x,Ay]$ ($J$-self-adjoint $A$) | $JA$ self-adjoint for $\langle\cdot,\cdot\rangle$ |
| $[Ax,Ay] = [x,y]$ ($J$-unitary $A$) | $A$ unitary for $\langle\cdot,\cdot\rangle$ |
| $[Ax,x]\geq0$, $A = A^{\dagger}$ ($J$-positive) | $JA$ positive for $\langle\cdot,\cdot\rangle$ |
| $V_{+}\perp V_{-}$, signature $(p,q)$ | eigenspaces $\pm1$ of $J$ |

**Proof.** Each line is one substitution, using $[x,y] = \langle Jx,y\rangle$ and $J^{2} = \mathrm{id}$; the operator lines use that $\langle JAx,y\rangle = [Jx,Ay]$ etc.

**Proposition (the operators fixed by $J$).** The operators commuting with $J$ are exactly those preserving the decomposition $V = V_{+}\oplus V_{-}$, and among them the $J$-self-adjoint and the ordinary self-adjoint operators coincide. So on the operators that respect the chosen decomposition there is no difference between the indefinite and the definite theory; the difference is carried by the operators that do not commute with $J$.

**Proof.** An operator commutes with $J$ exactly when it preserves each eigenspace; on such an operator the equation $[Ax,y] = [x,Ay]$ becomes $\langle JAx,y\rangle = \langle JAy,x\rangle$, that is the ordinary self-adjointness of $JA$ on each definite summand.

**Remark (the order structure).** There are two orders, and only the operator one depends on $J$. On vectors the indefinite order is the one given by the scalar square, $x\geq0$ when $[x,x]\geq0$, and it is a property of the form alone; the set $\{x : [Jx,x]\geq0\}$ is all of $V$, since $[Jx,x] = \langle x,x\rangle$. On operators the order is the $J$-order of *J-Self-Adjoint and J-Unitary Operators*, $A\geq0$ when $A$ is $J$-self-adjoint and $[Ax,x]\geq0$ for every $x$, and this one does depend on $J$, because the adjoint operation does: $J$ itself is $J$-positive, and changing the symmetry changes the cone. The distinction matters as soon as the order is used in the algebra, as it is in *Krein Algebras*.

## Worked Cases

### The Plane $\mathbb{R}^{1,1}$

With $[x,y] = x^{1}y^{1}-x^{2}y^{2}$ the fundamental symmetry $J = \mathrm{diag}(1,-1)$ gives $\langle x,y\rangle$ the standard inner product. For $|t|<1$ the graph $M_{t} = \mathrm{span}(e_1+te_2)$ is positive definite, and the associated fundamental symmetry acts as $+\mathrm{id}$ on $e_1+te_2$ and as $-\mathrm{id}$ on the orthogonal vector $te_1+e_2$; in the standard basis it is $\frac{1}{1-t^{2}}\begin{pmatrix}1+t^{2} & -2t \\ 2t & -1-t^{2}\end{pmatrix}$. All choices give equivalent norms, and the angular operator is $T : e_1\mapsto te_2$.

### A Pontryagin Space

On $\ell^{2}\oplus-\mathbb{C}$ with $[x,y] = \sum x_{n}\bar y_{n}-x_{0}\bar y_{0}$ the fundamental symmetry $J = \mathrm{diag}(-1,1,1,\ldots)$ has the negative eigenspace of dimension one; the angular operators are bounded by the condition $|t| < 1$ in the negative direction, so the set of fundamental symmetries is the open unit ball of the negative part.

### The Bridge in Action

For $A$ an operator with $[Ax,y] = [x,Ay]$, the operator $JA$ is self-adjoint for the definite form; so the spectral theory of $A$ for the indefinite form is the spectral theory of $JA$ for the definite one, with the eigenvector equation $Ax = \lambda x$ becoming $JAx = \lambda x$. This is the single most used instance of the dictionary.

## Summary

A **fundamental symmetry** is an operator $J$ with $J^{2} = \mathrm{id}$ that is self-adjoint for the indefinite form and satisfies $[Jx,x] > 0$ off zero. Its **eigenspaces** are the two parts of a fundamental decomposition, so the data of a symmetry and of a decomposition coincide, and $\langle x,y\rangle = [Jx,y]$ is a positive definite form with $[x,y] = \langle Jx,y\rangle$: this is the **bridge** that turns an indefinite statement into a definite one conjugated by $J$. $J$ is an isometry of both forms and a unitary operator of the definite one. The choice of $J$ is **not unique** when both ranks are nonzero: the symmetries are parametrised by the **angular operators** $T$ from the positive to the negative part, the positive part being the graph $M_T$ of a strict contraction $\|Tx_{+}\| < \|x_{+}\|$, and all choices induce equivalent norms and the same topology. Through $J$ the dictionary is short: $J$-self-adjoint operators $A$ become ordinary self-adjoint operators $JA$, $J$-unitary operators become unitary operators, and the $J$-positive cone becomes the ordinary positive cone, while operators not commuting with $J$ are where the indefinite theory genuinely differs. The form and the decomposition are *Indefinite Inner Product Spaces* and *Krein Spaces*, the finite case *Pontryagin Spaces*, and the operators *J-Self-Adjoint and J-Unitary Operators*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J$ | Fundamental symmetry, $J^{2} = \mathrm{id}$, $[Jx,y] = [x,Jy]$ |
| $\langle x,y\rangle = [Jx,y]$ | Definite form induced by $J$ |
| $V_{+} = \ker(J-\mathrm{id})$, $V_{-} = \ker(J+\mathrm{id})$ | The two definite parts |
| $[Jx,Jy] = [x,y] = \langle Jx,Jy\rangle$ | $J$ is an isometry of both forms |
| $T$, $M_T = \{x_{+}+Tx_{+}\}$ | Angular operator; the general positive part |
| $\|Tx_{+}\| < \|x_{+}\|$ | The strict contraction condition on $T$ |
| $[Jx,x]\geq0$ | The $J$-positive cone |
| $\langle JAx,y\rangle$, $A$ unitary | The dictionary for operators |

## Further Reading

- János Bognár, *Indefinite Inner Product Spaces*, Ergebnisse der Mathematik und ihrer Grenzgebiete 78 (Springer, 1974), for the fundamental symmetry and the angular operator.
- Tomas Ya. Azizov and Iosif S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric* (Wiley, 1989), for the parametrisation of the fundamental symmetries.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the finite-dimensional case of the angular operator.
- Mark G. Krein, *Introduction to the Theory of Linear Non-Self-Adjoint Operators* (American Mathematical Society, 1969), for the bridge between the definite and the indefinite cases.
- Vladimir A. Khatskevich and David Shoiykhet, *Differentiable Operators and Nonlinear Equations* (Birkhäuser, 1994), for the equivalence of the induced topologies.
