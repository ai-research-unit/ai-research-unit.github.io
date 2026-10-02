
# __The Graded Action on a Module over the Group Algebra__

## Introduction

The group algebra with a grade involution is a graded algebra, and a module over a graded algebra may be graded: its elements split into even and odd, the even part of the algebra preserves the degree, the odd part reverses it, and the whole structure is compressed into the single rule that conjugation by the grading involution of the module implements the grade involution of the algebra. On the group algebra this rule has an analytic content absent from the purely algebraic setting: the algebra is a Banach algebra, the module is a Banach module, the grading involution is an operator on a Banach space, and the twisted action which the rule produces is again a module structure, bounded with the same bound. This article fixes the graded module over the group algebra, proves the sign rule, constructs the twisted action, and describes the submodule and the invariant elements the grading fixes.

The article assumes the group, its Haar measure and the modular function from *Locally Compact Groups and Haar Measure*; the group algebra $L^1(G)$, its product and its norm from *The Convolution Algebra $L^1(G)$*; the convolution operators, their norms and composition laws from *Convolution on a Group* and *The Group Algebra as an Algebra of Operators*; the grade involution $\alpha$, the operator $\mathrm{A}f = \alpha(f)$, the eigenspaces $\mathcal{A}^\pm$, the signed sandwich and the signed left multiplication from *The Signed Sandwich on the Group Algebra* and *The Signed Left Multiplication on the Group Algebra*; the abstract graded module over an algebra and the homogeneity of an action from *The Graded Action on a Module over a Graded Algebra* and *The Graded Action on a Module over an Algebra*; the graded action of a topological group on a module, the sign rule and the twisted action from *The Graded Action on a Module over a Topological Group*; and the Banach algebras, the Banach modules and the bounded operators from *Topological Algebras and Banach Algebras* and *Operator Algebras*. The graded adjoint action is *The Graded Adjoint Action on a Module over the Group Algebra*, in the `- * Operator Theory` group of this category; the measure algebra is *The Involution on the Measure Algebra*, later. No adjoint is taken, and no Fourier theory occurs.

Throughout, $G$ is a locally compact Hausdorff group with left Haar measure $dx$ and identity $e$; $\mathcal{A} = L^1(G)$ is the group algebra with convolution $f*g$ and norm $\|f\|_1$; $\alpha$ is a continuous involutive automorphism of $\mathcal{A}$, $\mathrm{A}f = \alpha(f)$, and $\mathcal{A} = \mathcal{A}^+\oplus\mathcal{A}^-$ is the grading by the $\pm1$-eigenspaces, with $\mathcal{A}^i\mathcal{A}^j\subseteq\mathcal{A}^{\overline{i+j}}$; a **graded module** is a Banach space $M$ with a skew direct sum $M = M^+\oplus M^-$ (the **even** and the **odd** part) and a bounded left action of $\mathcal{A}$,

$$
\mathcal{A}\times M\to M, \qquad (a,m)\mapsto a\cdot m , \qquad \|a\cdot m\|\leq C\,\|a\|_1\,\|m\| ,
$$

satisfying $a\cdot(b\cdot m) = (a*b)\cdot m$, with the **homogeneity** $\mathcal{A}^i\cdot M^j\subseteq M^{\overline{i+j}}$. The **grading involution** of $M$ is the bounded involution $\varepsilon = +1$ on $M^+$, $\varepsilon = -1$ on $M^-$.

## The Graded Group Algebra

**Theorem (the grading recapped).** The eigenspace decomposition $\mathcal{A} = \mathcal{A}^+\oplus\mathcal{A}^-$ makes $\mathcal{A}$ a $\mathbb{Z}/2$-graded Banach algebra: $\mathcal{A}^+\mathcal{A}^+\subseteq\mathcal{A}^+$, $\mathcal{A}^+\mathcal{A}^-\subseteq\mathcal{A}^-$, $\mathcal{A}^-\mathcal{A}^+\subseteq\mathcal{A}^-$ and $\mathcal{A}^-\mathcal{A}^-\subseteq\mathcal{A}^+$, and the operator $\mathrm{A}$ is the grading automorphism, $\mathrm{A}|_{\mathcal{A}^\pm} = \pm\mathrm{id}$, with $\mathrm{A}(a*b) = \mathrm{A}a*\mathrm{A}b$.

**Proof.** This is the grading theorem of *The Signed Sandwich on the Group Algebra*, restated for the algebra alone; the multiplicativity of $\mathrm{A}$ is the multiplicativity of $\alpha$. $\square$

**Remark (the two instances of the grading).** The grade involution is the sign character or a group automorphism of the examples of *The Signed Sandwich on the Group Algebra*; for the sign character $\mathcal{A}^\pm$ are the functions of the two sign classes, and for a group automorphism $\mathcal{A}^\pm$ are the symmetric and antisymmetric functions. The grading is a structure of the algebra and is fixed before any module is considered; the article uses it and does not rebuild it.

## Graded Modules and the Sign Rule

**Definition.** A **graded action** of the graded algebra $\mathcal{A}$ on a graded module $M$ is a bounded left action that is homogeneous, $\mathcal{A}^i\cdot M^j\subseteq M^{\overline{i+j}}$. A **grading involution** of $M$ is a bounded linear involution $\varepsilon$ with $\varepsilon|_{M^+} = \mathrm{id}$ and $\varepsilon|_{M^-} = -\mathrm{id}$, which exists exactly when the two summands are closed.

**Theorem (the two descriptions of homogeneity).** A bounded module action of the graded group algebra $\mathcal{A}$ on $M = M^+\oplus M^-$ is homogeneous if and only if

$$
\varepsilon\,(a\cdot \varepsilon\,m) = \alpha(a)\cdot m \qquad \text{for all } a\in\mathcal{A},\ m\in M ,
$$

equivalently $\varepsilon\,(a\cdot)\,\varepsilon = \alpha(a)\cdot$ on $M$ for every $a$. When this holds, the assignment

$$
a\cdot_\alpha m := \varepsilon\,(a\cdot\varepsilon\,m) = \alpha(a)\cdot m
$$

defines a second bounded module action of $\mathcal{A}$ on $M$, the **$\alpha$-twisted action**.

**Proof.** Suppose the action is homogeneous. For $a = a_+ + a_-$ with $a_\pm\in\mathcal{A}^\pm$ and $m\in M^j$, homogeneity gives $a_+\cdot m\in M^j$ and $a_-\cdot m\in M^{\overline{j+1}}$, so $\varepsilon(a\cdot m) = (-1)^j a_+\cdot m + (-1)^{j+1}a_-\cdot m = (-1)^j(a_+ - a_-)\cdot m$; hence $\varepsilon(a\cdot\varepsilon m) = (-1)^j\varepsilon(a\cdot m) = (a_+ - a_-)\cdot m = \mathrm{A}a\cdot m = \alpha(a)\cdot m$. Conversely, if $\varepsilon(a\cdot)\varepsilon = \alpha(a)\cdot$ for all $a$, then for homogeneous $a$ of parity $i$ and $m\in M^j$ the identity $\varepsilon(a\cdot)\varepsilon = (-1)^i(a\cdot)$ read on $m$ gives $(-1)^j\varepsilon(a\cdot m) = (-1)^i a\cdot m$, that is $\varepsilon(a\cdot m) = (-1)^{i+j}a\cdot m$, so $a\cdot m\in M^{\overline{i+j}}$. The twisted assignment is a module action because it is $\varepsilon$-conjugate to the homogeneous one: $\varepsilon(a\cdot_\alpha(b\cdot_\alpha m)) = a\cdot\varepsilon(b\cdot_\alpha m) = (a*b)\cdot\varepsilon m$, hence $a\cdot_\alpha(b\cdot_\alpha m) = (a*b)\cdot_\alpha m$; it is bounded with the same constant as the given action. $\square$

**Corollary (the sign rule).** The grading involution interchanges the two actions,

$$
\varepsilon\,(a\cdot_\alpha m) = a\cdot \varepsilon\,m, \qquad \varepsilon\,(a\cdot m) = a\cdot_\alpha \varepsilon\,m ,
$$

so the twisted action is the given action transported by $\varepsilon$; in particular the two actions have the same operator norms and the same invariant subspaces under $\varepsilon$.

**Proof.** The first identity is $\varepsilon\varepsilon(a\cdot\varepsilon m) = a\cdot\varepsilon m$; the second is the first with $a$ replaced by $\alpha(a)$ and $\varepsilon^2 = \mathrm{id}$. $\square$

## The Twisted Action

**Theorem (when the two actions agree).** The homogeneous action and its $\alpha$-twist coincide, $a\cdot_\alpha m = a\cdot m$ for all $a, m$, if and only if the odd part of the algebra acts trivially,

$$
\mathcal{A}^-\cdot M = 0 ,
$$

and then the action factors through the even quotient $\mathcal{A}/\mathcal{A}^-$. In particular, if $\alpha = \mathrm{id}$ the two actions are equal for every module.

**Proof.** For $a = a_+ + a_-$, $a\cdot m - a\cdot_\alpha m = a\cdot m - \alpha(a)\cdot m = 2\,a_-\cdot m$, because $\alpha(a) = a_+ - a_-$; the difference vanishes for all $a, m$ exactly when $\mathcal{A}^-\cdot M = 0$. The action then descends to the quotient by $\mathcal{A}^-$, which is the even part up to the identification. The case $\alpha = \mathrm{id}$ has $\mathcal{A}^- = 0$. $\square$

**Proposition (the twisted action on the regular module).** On the regular module $M = \mathcal{A}$ with the grading $\mathcal{A} = \mathcal{A}^+\oplus\mathcal{A}^-$ and the action $a\cdot m = a*m$, the twisted action is

$$
a\cdot_\alpha m = \alpha(a)*m ,
$$

which is the signed left multiplication of *The Signed Left Multiplication on the Group Algebra* with the argument unchanged; the twisted action and the original action differ by the grade involution acting on the coefficient.

**Proof.** $\varepsilon = \mathrm{A}$ on $M = \mathcal{A}$, so $a\cdot_\alpha m = \mathrm{A}(a*\mathrm{A}m) = \alpha(a)*m$, using $\mathrm{A}^2 = \mathrm{id}$. This is $\Lambda_{\alpha(a)}$ applied to $m$, that is the signed left multiplication by $\alpha(a)$. $\square$

**Remark (the action on $L^p(G)$).** On $M = L^p(G)$ with the convolution action of $L^1(G)$ and the grading by the sign character, $M^\pm = \{\xi : \varepsilon\xi = \pm\xi\}$ and the homogeneity is the computation $\varepsilon(a*m) = (\varepsilon a)*(\varepsilon m)$, which is the sign rule for convolution; the twisted action is $a\cdot_\alpha m = \alpha(a)*m$, and the two actions agree exactly when the odd part of $L^1(G)$ convolves $L^p(G)$ to zero. The analytic structure — a Banach module over a Banach algebra — is what the group algebra adds to the discrete group-algebra picture of *The Graded Action on a Module over a Topological Group*.

## The Fixed Submodule and the Invariant Elements

**Definition.** The **fixed submodule** of the grading is the even part $M^+ = \{m : \varepsilon m = m\}$; the **invariant elements** of the twisted action are

$$
M^{\mathcal{A}^-} = \{m \in M : a\cdot m = 0 \ \text{for all}\ a\in\mathcal{A}^-\} = \{m : a\cdot_\alpha m = a\cdot m \ \text{for all}\ a\in\mathcal{A}\} .
$$

**Theorem (the fixed submodule is a module over the even part).** $M^+$ is a closed linear subspace and a module over the even subalgebra, $\mathcal{A}^+\cdot M^+\subseteq M^+$; the odd part satisfies $\mathcal{A}^+\cdot M^-\subseteq M^-$ and $\mathcal{A}^-\cdot M^+\subseteq M^-$, $\mathcal{A}^-\cdot M^-\subseteq M^+$; and $M^{\mathcal{A}^-}$ is a closed subspace contained in the common kernel of the odd operators.

**Proof.** The even part is closed as the $1$-eigenspace of the bounded involution $\varepsilon$, and the inclusions are the homogeneity of the action; the invariant set is the intersection of the closed kernels of the bounded maps $m\mapsto a\cdot m$ for $a\in\mathcal{A}^-$, hence closed, and the identification with the difference set is the theorem on the agreement of the actions. $\square$

**Corollary (the invariants vanish when the odd part contains a unit).** If $\mathcal{A}^-$ contains a unit $u$ of $\mathcal{A}$, then $M^{\mathcal{A}^-} = \{0\}$; if $G$ is discrete and the odd part contains a point mass $\delta_h$ with $\alpha(\delta_h) = -\delta_h$, then every invariant element is annihilated by $\delta_h$, that is, $M^{\mathcal{A}^-} = \{m : \delta_h\cdot m = 0\}$.

**Proof.** A unit $u\in\mathcal{A}^-$ acts by the invertible operator $m\mapsto u\cdot m$, whose kernel is $\{0\}$. For the point mass statement, the invariant set is the kernel of the single operator because $\mathcal{A}^-$ is spanned by the odd point masses and $\delta_h$ is a unit. $\square$

**Example (the trivial and the maximal grading).** If $\alpha = \mathrm{id}$ then $\mathcal{A}^- = 0$, $M^{\mathcal{A}^-} = M$, and the twisted action is the original one. If $M$ carries the trivial grading $M^- = 0$, every module action is homogeneous and the twisted action equals the original one on the even part of the algebra; the grading involution is the identity.

## Summary

A graded module over the group algebra $\mathcal{A} = L^1(G)$ with grade involution $\alpha$ is a Banach module $M = M^+\oplus M^-$ on which $\mathcal{A}$ acts with the homogeneity $\mathcal{A}^i\cdot M^j\subseteq M^{\overline{i+j}}$, and the whole homogeneity is equivalent to the sign rule $\varepsilon(a\cdot\varepsilon m) = \alpha(a)\cdot m$ for the grading involution $\varepsilon$; the rule produces the $\alpha$-twisted action $a\cdot_\alpha m = \varepsilon(a\cdot\varepsilon m) = \alpha(a)\cdot m$, again a bounded module action, $\varepsilon$-conjugate to the original and with the same operator norms. The two actions agree if and only if the odd part of the algebra acts trivially, $\mathcal{A}^-\cdot M = 0$; on the regular module with the convolution action the twisted action is the signed left multiplication $a\cdot_\alpha m = \alpha(a)*m$, and on $L^p(G)$ it is convolution by the twisted coefficient, the homogeneity being $\varepsilon(a*m) = (\varepsilon a)*(\varepsilon m)$. The fixed submodule $M^+$ is closed and is a module over the even subalgebra, the odd operators intertwine the two summands in the parity pattern of the grading, and the invariant elements of the twisted action form the closed set $M^{\mathcal{A}^-}$ killed by the odd part; if the odd part contains a unit the invariants vanish. The graded adjoint action is *The Graded Adjoint Action on a Module over the Group Algebra*, and the measure algebra is *The Involution on the Measure Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{A} = L^1(G)$, $\mathcal{A}^\pm$ | The graded group algebra and its even and odd parts |
| $\alpha$, $\mathrm{A}f = \alpha(f)$ | Grade involution and grading automorphism |
| $M = M^+\oplus M^-$ | Graded Banach module, even and odd parts |
| $\varepsilon$ | Grading involution of $M$, $+1$ on $M^+$, $-1$ on $M^-$ |
| $a\cdot m$, $\|a\cdot m\|\leq C\|a\|_1\|m\|$ | The bounded homogeneous action |
| $\mathcal{A}^i\cdot M^j\subseteq M^{\overline{i+j}}$ | Homogeneity |
| $\varepsilon(a\cdot\varepsilon m) = \alpha(a)\cdot m$ | The sign rule |
| $a\cdot_\alpha m = \alpha(a)\cdot m$ | The $\alpha$-twisted action |
| $\mathcal{A}^-\cdot M = 0$ | Criterion for the two actions to agree |
| $M^{\mathcal{A}^-} = \{m : \mathcal{A}^-\cdot m = 0\}$ | The invariant elements |
| $a\cdot_\alpha m = \alpha(a)*m$ on $M = \mathcal{A}$ | The twisted action on the regular module |

## Further Reading

- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for Banach modules over a Banach algebra and bounded module actions.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume I* (Cambridge University Press, 1994), for graded Banach algebras, their modules and the homogeneity of an action.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for graded modules, their endomorphism rings and the sign rule.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis I* (Springer, second edition, 1979), for $L^p(G)$ as a module over $L^1(G)$ and the Young inequalities.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the grading involution and the twisted action of a graded algebra on its modules.
