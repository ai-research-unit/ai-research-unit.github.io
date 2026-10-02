# __The Signed Action on a Clifford Module__

## Introduction

A Clifford module is a vector space on which the Clifford algebra acts; the module structure is one-sided, the algebra multiplying on the left. Twisting that action by the grade involution — letting $x$ act as $\alpha(x)$ acts, or equivalently attaching the sign $(-1)^{|x|}$ to an odd element — defines the **signed action**. This article is about that twist: what it does to the module, and how it is read by the grading.

Two facts decide the answer. First, attaching the grade involution to the acting element is the same as twiddling the module by the automorphism $\alpha$ of the algebra, so the signed action makes the module $S$ into a new module $S^{\alpha}$ whose isomorphism type is a property of the automorphism $\alpha$: equivalent to $S$ when $\alpha$ is an inner automorphism, and different when it is not. Second, whether $\alpha$ is inner is decided by the parity of the dimension. In **even** dimension the volume element is even, it implements the grade involution by conjugation, and it is the chirality operator of the spinor module; so the signed action is the ordinary action conjugated by the chirality, and the twisted module is isomorphic to the original. In **odd** dimension the volume element is the central element $\omega$, the conjugation by it is the identity, and $\alpha$ is the outer automorphism exchanging the two simple modules; so the signed action carries each spinor module to the other.

The Clifford algebra and its grading are *Clifford Algebras* and *Clifford Algebras in Finite Dimensions*; the modules, the minimal left ideals and the number of simple modules are *Left Multiplication and the Clifford Module Structure*, *The One-Sided Action and the Spin Representation* and *Spin Representations and Clifford Modules with Inner Conjugation*; the operators twisted by the grading are *The Graded Multiplication Operators*; the volume element, the chirality and the two simple modules in odd dimension are *The Low-Dimensional Classification* and *Bott Periodicity and the Classification*. Those are cited. The base is a field $F$ of characteristic not $2$, $q$ is non-degenerate and $\alpha$ is the grade involution.

## Clifford Modules and the Signed Action

**Definition.** A **Clifford module** is a vector space $S$ with an action of $\mathrm{Cl}(V,q)$ by $F$-linear maps, $x\otimes s\mapsto x\cdot s$, respecting the algebra structure. Its **signed action** is

$$
x \cdot_{\alpha} s = \alpha(x)\cdot s, \qquad x \in \mathrm{Cl}(V,q),\ s \in S .
$$

**Proposition.** The signed action makes $S$ into a Clifford module, denoted $S^{\alpha}$ and called the **twist** of $S$ by $\alpha$, and the identity map on the underlying space is an isomorphism of $F$-vector spaces carrying the signed action to the ordinary one. On a homogeneous element the signed action is $x\cdot_{\alpha} s = (-1)^{|x|}x\cdot s$.

**Proof.** Since $\alpha$ is an algebra automorphism, $x\mapsto \alpha(x)$ composed with the given action is again an action; the sign statement is the definition of $\alpha$ on a homogeneous element.

**Proposition (fixed points and the even part).** Under the signed action the even part of the algebra acts as it did before, and the odd part acts with the opposite sign. In particular an element of $S$ that is annihilated by the whole algebra is annihilated in either action, and for $x$ even the operators of $x$ in $S$ and in $S^{\alpha}$ coincide.

**Proof.** For $x$ even, $\alpha(x) = x$; for $x$ odd, $\alpha(x) = -x$.

**Remark (the twist of a module is not new data).** The signed action uses exactly the same linear maps of the algebra, only relabelled by $\alpha$; the module $S^{\alpha}$ is the module $S$ with the labels of the acting elements changed. Everything structural about $S^{\alpha}$ is therefore a question about the automorphism $\alpha$, and the next section answers it.

## The Twist by an Automorphism

**Definition.** For an algebra automorphism $\theta$ of $\mathrm{Cl}(V,q)$ and a module $S$, the **twist** $S^{\theta}$ is the module with the action $x\cdot_{\theta}s = \theta(x)\cdot s$.

**Proposition (the criterion for isomorphism).** The twist $S^{\theta}$ is isomorphic to $S$ for every module $S$ if $\theta$ is inner, that is $\theta = \mathrm{Ad}_u$ for a unit $u$; the isomorphism is the operator of $u$ on $S$. If $\theta$ is not inner, there are modules for which $S^{\theta}$ is not isomorphic to $S$; and if $\theta$ fixes the isomorphism classes of the simple modules, it acts on the set of those classes.

**Proof.** If $\theta(x) = uxu^{-1}$ then $\theta(x)\cdot s = u\cdot(x\cdot(u^{-1}\cdot s))$, so the operator of $u^{-1}$ intertwines the two actions. The converse and the outer case are the standard module theory of an automorphism.

**Corollary (the signed action is a twist).** The signed action is the twist by $\alpha$: $S^{\alpha}$ is the twist of $S$ by the grade involution. So the question "is the signed action equivalent to the ordinary one?" is the question "is $\alpha$ inner?".

## Compatibility with the Grading

### The Even Dimension

**Theorem.** Let $\dim V = n$ be **even**, and let $\omega = e_1\cdots e_n$ be the volume element. Then $\omega$ is even, it is a unit with $\omega^{2} = (-1)^{n(n-1)/2}\prod_{i}q(e_i) \in F^{\times}$, and it implements the grade involution:

$$
\alpha(x) = \omega\,x\,\omega^{-1} \qquad \text{for every } x \in \mathrm{Cl}(V,q).
$$

Consequently $\alpha$ is an inner automorphism in even dimension, the signed action is the ordinary action conjugated by the operator of $\omega$ on the module, and $S^{\alpha}\cong S$ for every Clifford module $S$. For the spinor module the operator of $\omega$ is the **chirality operator** $\Gamma_S$, and the signed action is $\Gamma_S\,x\,\Gamma_S^{-1}$.

**Proof.** For a vector $v$, $\omega v\omega^{-1} = (-1)^{n-1}v = -v$ because $n$ is even, so $v\omega = -\omega v$ and $\omega v\omega^{-1} = -v$; since $v\mapsto -v$ extends to the unique automorphism $\alpha$ and both sides of the identity are automorphisms agreeing on the generators, they agree everywhere. The unit condition and the isomorphism are the preceding criterion, and the identification with the chirality is the definition of the chirality operator of a spinor module.

**Corollary (the grading is internal in even dimension).** In even dimension the graded structure of every Clifford module is detected by an operator of the algebra: the chirality $\Gamma_S = \omega\big|_S$ commutes with the even part, is invertible, and satisfies $\Gamma_S^{2} = \omega^{2}$, a scalar. Where that scalar is a square the eigenspaces of $\Gamma_S$ are the two chiral halves of $S$; in general the chirality grades the module over the extension of $F$ in which $\omega^{2}$ has a square root, and the signed action is the conjugation by this grading operator, so the sign rule of the graded operators is implemented inside the module and not merely declared.

### The Odd Dimension

**Theorem.** Let $n$ be **odd** and let $\omega$ be the volume element. Then $\omega$ is central and odd, it lies in the centre $F\oplus F\omega$, and $\alpha(\omega) = -\omega$. The conjugation by $\omega$ is the identity on the algebra and hence does **not** implement $\alpha$; the grade involution is an **outer** automorphism, and it exchanges the two simple modules of $\mathrm{Cl}(V,q)$, sending a minimal left ideal $I$ to a minimal left ideal $I^{\alpha}$ carrying the other simple module.

**Proof.** $\omega$ is central in odd dimension by *Clifford Algebras in Finite Dimensions*, and $\alpha(\omega) = (-1)^{n}\omega = -\omega$. If $\alpha = \mathrm{Ad}_u$ then $\mathrm{Ad}_u(\omega) = \omega$ because $\omega$ is central, but $\alpha(\omega) = -\omega \neq \omega$, so $\alpha$ is not inner. The simple modules of the centre are distinguished by the scalar by which $\omega$ acts, and when $\omega^{2} = 1$ these scalars are the two signs $\pm1$; twisting by $\alpha$ changes the sign of that scalar and therefore exchanges the classes, and when the centre $F\oplus F\omega$ is a field the corresponding statement is the exchange of the two embeddings of that field.

**Corollary (the signed action in odd dimension switches chirality).** In odd dimension the signed action on a simple module is not isomorphic to the ordinary action on that module, but to the ordinary action on the other simple module: $S^{\alpha}\cong S'$, where $S, S'$ are the two simple modules. So the signed action is the map that exchanges the two chiral halves in odd dimension, where the exchange cannot be realised by an operator of the algebra.

## Worked Cases

### The Even Case $\mathrm{Cl}_{1,1}(\mathbb{R})$

With $e_1^{2} = 1$, $e_2^{2} = -1$ the algebra is $M_2(\mathbb{R})$ and $\omega = e_1e_2$ has $\omega^{2} = -1$. For a vector $v$, $\omega v\omega^{-1} = -v$; the endomorphism $\omega$ of the module $\mathbb{R}^2$ has square $-1$, so it has no real eigenspaces and the chiral halves appear over $\mathbb{C}$, where the two eigenspaces of $\omega$ split the complexified module. The signed action is the conjugation by that endomorphism, hence isomorphic to the ordinary action.

### The Odd Case $\mathrm{Cl}_{0,3}(\mathbb{R})$

With $e_j^{2} = -1$ the volume element $\omega = e_1e_2e_3$ is central with $\omega^{2} = 1$, and $\alpha(\omega) = -\omega$. The algebra is $\mathbb{H}\oplus\mathbb{H}$ and the two simple modules are distinguished by $\omega$ acting as $+1$ and as $-1$; twisting by $\alpha$ sends the module with $\omega = 1$ to the module with $\omega = -1$, so the signed action exchanges the two chiral halves.

### The Even Dimension Four

In $\mathrm{Cl}_{3,1}(\mathbb{R})$ with $e_1^{2} = e_2^{2} = e_3^{2} = 1$ and $e_4^{2} = -1$ the volume element $\omega = e_1e_2e_3e_4$ is even and satisfies $\omega^{2} = -1$; on the Dirac spinor module it is the chirality operator $\Gamma$ with $\Gamma^{2} = -1$, so over $\mathbb{R}$ it has no eigenspaces and the half-spin spaces are its eigenspaces over $\mathbb{C}$, where $\Gamma$ acts as $+1$ on one and $-1$ on the other. The signed action is the conjugation by $\Gamma$.

## Summary

The **signed action** on a Clifford module is $x\cdot_{\alpha}s = \alpha(x)\cdot s$; it makes the module into the twist $S^{\alpha}$ by the grade involution and equals the ordinary action with the sign $(-1)^{|x|}$ on an odd element; it agrees with the ordinary action on the even part. Whether $S^{\alpha}$ is isomorphic to $S$ is decided by whether $\alpha$ is inner. It is inner in **even** dimension: the volume element $\omega$ is even with $\omega v\omega^{-1} = -v$, so $\alpha = \mathrm{Ad}_{\omega}$, the signed action is the conjugation by the **chirality operator** $\Gamma_S = \omega\big|_S$, and the twisted module is isomorphic to the original. It is outer in **odd** dimension: $\omega$ is central and odd with $\alpha(\omega) = -\omega$, so no unit implements $\alpha$, and the signed action **exchanges the two simple modules**, which are distinguished by the sign of $\omega$. This is the compatibility of the signed action with the grading: in even dimension the grading is an operator inside the module and the signed action is its conjugation, while in odd dimension the grading is the centre and the signed action permutes the two chiralities instead of conjugating one of them. The module theory is *Left Multiplication and the Clifford Module Structure* and *The One-Sided Action and the Spin Representation*; the graded operators are *The Graded Multiplication Operators*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S$, $x\cdot s$ | Clifford module and its action |
| $x\cdot_{\alpha}s = \alpha(x)\cdot s$ | Signed action |
| $S^{\alpha}$ | Twist of $S$ by the grade involution |
| $\alpha = \mathrm{Ad}_{\omega}$ (even $n$) | The grade involution is inner in even dimension |
| $\Gamma_S = \omega\big|_S$ | Chirality operator of a spinor module |
| $\omega$, $F\oplus F\omega$ (odd $n$) | Volume element, centre; $\alpha$ is outer |
| $S \mapsto S^{\alpha}$ | Exchange of the two simple modules in odd dimension |

## Further Reading

- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the volume element, the chirality and the twisting of a Clifford module.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the chirality operator and the half-spin modules.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the centre of a Clifford algebra and the inner automorphisms.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the twist of a module by an automorphism.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the volume element in the low-dimensional algebras.
