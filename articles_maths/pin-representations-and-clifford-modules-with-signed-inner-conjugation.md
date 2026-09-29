# __Pin Representations and Clifford Modules with Signed Inner Conjugation__

## Introduction

The spin representations of *Spin Representations and Clifford Modules with Inner Conjugation* are the modules of the Clifford algebra restricted to the even part: the spin group lies in $\mathrm{Cl}^0$, its action on a Clifford module is the restriction of the algebra action, and the two-to-one cover survives in the representation because $-1$ acts as $-\mathrm{id}$. That construction stops at the even part. The Pin group contains odd elements as well, and the odd elements are precisely the ones that a description by the inner conjugation alone cannot handle: on a vector the inner conjugation gives $-\rho_u$ and the signed inner conjugation of *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation* gives $\rho_u$. This article supplies the module theory of the odd part.

A Clifford module is already a module over the whole algebra, so the action of $\mathrm{Pin}(V,q)$ on it is available without any new construction: it is the restriction of the algebra action to the group of units, and it is **one-sided**, a left multiplication. The pin representation is therefore the whole Clifford action read on the group, and the spin representation is its restriction to the even part. What the odd part adds is a parity: an odd element interchanges the two chiral halves of an even-dimensional module, so the pin representation is irreducible where the spin representation is not, and the two half-spin representations are exchanged rather than preserved.

The sign enters through the intertwining identity. The module action intertwines the algebra action with the inner conjugation, $\rho(x)\rho(v)\rho(x)^{-1}=\rho(\mathrm{Ad}_x(v))$ for $v\in V$, and since $\mathrm{Ad}_x=\varepsilon_x\mathrm{Ad}^{\alpha}_x$ with $\varepsilon_x=(-1)^{k}$ the parity sign, the geometric reflection appears in the module with the sign: for a vector $u$, $\rho(u)\rho(v)\rho(u)^{-1}=-\rho(\rho_u(v))$. The signed inner conjugation is thus the two-sided operator whose action on $V$ matches the module action up to that parity sign, and it is the operator that the pinor theory must use.

The Clifford algebra, its parity grading and the grade involution are from *Clifford Algebras* and *Clifford Algebras in Finite Dimensions*; the general theory of modules over an algebra, the simple and semisimple modules and the density theorem are from *Modules over an Algebra* and *Simple and Semisimple Modules*; the Clifford modules, the explicit spinor module, chirality and the eightfold table are *Spin Representations and Clifford Modules with Inner Conjugation*; the groups, the Clifford norm and the exact sequences are *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*; the two-sided operator and its sign are *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*; the one-sided factors are *One-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*; and the ideal description of a spinor is *Spinors as Minimal Left Ideals with Inner Conjugation*. Nothing owned by those entries is re-derived. The base is a field $F$ of characteristic not $2$, $q$ is non-degenerate of dimension $n$ on $V$, and for the definite real forms the notation is $\mathrm{Cl}_{p,q}$.

## The Pin Representation

**Definition.** Let $S$ be a Clifford module over $\mathrm{Cl}(V,q)$. The **pin representation** is the restriction of the algebra action to the Pin group,

$$
\rho\colon\mathrm{Pin}(V,q)\longrightarrow GL(S),\qquad \rho(x)s=x\,s ,
$$

and the **spin representation** is its restriction to $\mathrm{Spin}(V,q)=\mathrm{Pin}(V,q)\cap\mathrm{Cl}^0(V,q)$.

The action is one-sided by construction: the algebra acts on a module by left multiplication, so $\rho(x)$ is a left multiplication and there is no right factor to pair it with. The two-sided operators of the category act on the *algebra*, and it is through the intertwining identity below, not through a definition, that they govern the module action.

**Proposition (the basics).** The pin representation is a well-defined group representation, $\rho(1)=\mathrm{id}_S$, $\rho(xz)=\rho(x)\rho(z)$, and

$$
\rho(-1)=-\mathrm{id}_S ,
$$

because $S\neq0$ and $-1$ is the scalar $-1$ of the algebra. Hence the pin representation does not descend to $O(V,q)$, exactly as the spin representation does not descend to $SO(V,q)$.

*Proof.* The algebra action is associative, so $x(zs)=(xz)s$; $-1$ is central and acts as $-\mathrm{id}$ on every module with $S\neq0$; and $-1$ lies in the kernel of the projection of $\mathrm{Pin}$ to $O(V,q)$.

**Theorem (faithfulness and the kernel).** Suppose $S$ is irreducible. If $\mathrm{Cl}(V,q)$ is simple then the pin representation is faithful, and its restriction to $\mathrm{Spin}(V,q)$ is the spin representation. If $\mathrm{Cl}(V,q)\cong A\times A$ is a product of two simple algebras and $S$ is the irreducible module of the first factor, then the kernel of $\rho$ is

$$
\ker\rho=\mathrm{Pin}(V,q)\cap\bigl(\{1\}\times A\bigr).
$$

*Proof.* The annihilator of an irreducible module is a two-sided ideal, proper because $1$ acts as $\mathrm{id}_S$; over a simple algebra it vanishes and the action is faithful, and over a product the module of one factor is annihilated by the other. Restricting a faithful action to a subgroup is faithful.

**Remark.** The kernel of the pin representation is the same kind of object as the kernel of the spin representation, with $\mathrm{Pin}$ in place of $\mathrm{Spin}$; since $-1\in\mathrm{Spin}\subseteq\mathrm{Pin}$ in both cases, the two representations see the same double-cover sign, and the difference between them is entirely in the odd part, where the spin representation has nothing to say.

## The Parity of the Odd Part

**Proposition (chirality).** Suppose $n$ is even and $S=\Delta_+\oplus\Delta_-$ is the chiral decomposition, on which $\mathrm{Cl}^0$ acts preserving the summands and $\mathrm{Cl}^1$ acts interchanging them. Then every element of $\mathrm{Spin}(V,q)$ preserves $\Delta_\pm$ and every odd element of $\mathrm{Pin}(V,q)$ interchanges them.

*Proof.* The algebra action satisfies $\mathrm{Cl}^{i}\cdot S^{j}\subseteq S^{i+j}$, the exponent read modulo two; the even elements of the group lie in $\mathrm{Cl}^0$ and the odd ones in $\mathrm{Cl}^1$.

**Corollary (irreducibility of the pin representation).** If $S$ is an irreducible Clifford module of even dimension, the pin representation on $S$ is irreducible, while its restriction to $\mathrm{Spin}(V,q)$ is the sum of the two half-spin representations $\rho_\pm$ on $\Delta_\pm$, each irreducible over the even part.

*Proof.* The Clifford algebra is spanned by products of vectors, hence by $\mathrm{Pin}(V,q)$, so the $\mathrm{Pin}$-submodules of $S$ are the $\mathrm{Cl}(V,q)$-submodules and the irreducibility carries over. The restriction to the even part splits along $\Delta_\pm$ by the proposition, and each half is irreducible by *Spin Representations and Clifford Modules with Inner Conjugation*.

**Remark.** The corollary is the structural difference between spinors and pinors. A half-spinor is a vector of an irreducible module of the even part; a pinor is a vector of an irreducible module of the whole algebra, and its two chiral components are exchanged, not preserved, by the odd elements. Over $\mathbb{R}$ this is why the pinor module is the module of $\mathrm{Pin}$ and the half-spin modules are the modules of $\mathrm{Spin}$.

## The Sign in the Intertwining Identity

**Proposition.** Let $v\in V$ and let $x\in\mathrm{Pin}(V,q)$. Then

$$
\rho(x)\,\rho(v)\,\rho(x)^{-1}=\rho\bigl(\mathrm{Ad}_x(v)\bigr)=\rho\bigl(\varepsilon_x\,\mathrm{Ad}^{\alpha}_x(v)\bigr),
$$

with $\varepsilon_x=(-1)^{k}$ the parity sign of $x$. Equivalently,

$$
\rho\bigl(\mathrm{Ad}^{\alpha}_x(v)\bigr)=\varepsilon_x\,\rho(x)\,\rho(v)\,\rho(x)^{-1}.
$$

*Proof.* For $s\in S$, $\rho(x)\rho(v)\rho(x)^{-1}(s)=x\bigl(v(x^{-1}s)\bigr)=(xvx^{-1})s=\rho(xvx^{-1})(s)$, which is the first identity, and $\mathrm{Ad}_x=\varepsilon_x\mathrm{Ad}^{\alpha}_x$ by *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*.

**Corollary (the reflection in the module).** Let $u\in V$ with $q(u)\neq0$ and let $\rho_u$ be the reflection in $u^{\perp}$. Then for every $v\in V$

$$
\rho(u)\,\rho(v)\,\rho(u)^{-1}=-\rho\bigl(\rho_u(v)\bigr).
$$

So an odd element of $\mathrm{Pin}$, which is a product of vectors, conjugates the Clifford action by the negative of the reflection; and the signed inner conjugation is the two-sided operator whose restriction to $V$ removes that sign.

*Proof.* $\mathrm{Ad}_u=-\mathrm{Ad}^{\alpha}_u=-\rho_u$ by the propositions of the two-sided article, and the first identity above applies.

**Proposition (the odd elements are square roots).** For $u\in V$ one has $\rho(u)^{2}=\rho(u^{2})=q(u)\,\mathrm{id}_S$, and for $x=u_1\cdots u_k\in\mathrm{Pin}$, $\rho(x)^{2}=\prod_i q(u_i)\,\mathrm{id}_S$, an invertible scalar.

*Proof.* The algebra action is a representation of the algebra, so $\rho(u)^{2}=\rho(u^{2})=q(u)\rho(1)$.

**Remark.** The sign in the corollary is the whole reason the pin theory needs the signed member. On the even part $\varepsilon_x=1$ and the module action intertwines the inner conjugation itself, which is why the spin theory never meets the sign; on the odd part $\varepsilon_x=-1$, the module action intertwines the negative of the reflection, and it is the signed inner conjugation that restores the reflection and makes the action of $\mathrm{Pin}$ on $S$ and its action on $V$ agree up to that parity.

## Real Pin Modules

The pin modules over $\mathbb{R}$ are obtained from the spin modules by nothing more than
extending the group: the underlying Clifford module is the same, the classification is the
eightfold table of *Spin Representations and Clifford Modules with Inner Conjugation*, and the
only thing added is the action of the odd part of the group.

**Proposition.** Let $S$ be a real Clifford module. The restriction of the pin representation to
$\mathrm{Spin}(V,q)$ is the real spin representation, and for an odd $x\in\mathrm{Pin}(V,q)$ the
operator $\rho(x)$ reverses the chirality when $n$ is even. On an irreducible module over a simple
real Clifford algebra the pin representation is faithful, so the real pinor and the real spinor are
vectors of the same module and differ only in the group that is allowed to act on them.

*Proof.* The restriction statement is the definition; the parity statement is the chirality
proposition; faithfulness is the theorem on the kernel, applied with the classification of the real
Clifford algebras. 

**Remark (the definite case).** For a definite real form the standard module form of *Involutive
Clifford Algebras* makes each Clifford coefficient skew-adjoint, so an even element of $\mathrm{Pin}$
acts by an orthogonal operator and an odd element by a composition of an odd number of skew
operators, with $\rho(u)^{2}=q(u)\,\mathrm{id}_S$ a scalar of the sign of $q(u)$. The adjoint of
$\rho(x)$ and its relation to $\rho(x)^{-1}$ belong to the involutive layer and are not repeated
here.

## Worked Cases

### The Three-Dimensional Definite Algebra

In $\mathrm{Cl}_{0,3}(\mathbb{R})\cong\mathbb{H}\oplus\mathbb{H}$ with $e_j^{2}=-1$, the irreducible module is $S=\mathbb{H}$ with the action of the first factor, and $\mathrm{Pin}(3)$ acts on it by left multiplication. The even part is $\mathrm{Spin}(3)\cong Sp(1)$, the unit quaternions, and $\rho$ is faithful on the first factor; the odd elements are the products of an odd number of vectors, among them $e_1$, with $\rho(e_1)^{2}=q(e_1)\mathrm{id}=-\mathrm{id}$, so an odd element of $\mathrm{Pin}$ is a complex structure on the module. The kernel of $\rho$ is $\mathrm{Pin}(3)\cap(\{1\}\times\mathbb{H})$, the odd elements of the second factor included; the spin representation does not see those.

### The Sign on a Reflection

In the same algebra take $u=e_1$ and $v=e_2$. Then $\rho_{e_1}$ fixes $e_2$, so $\rho_{e_1}(e_2)=e_2$, and the corollary above predicts

$$
\rho(e_1)\,\rho(e_2)\,\rho(e_1)^{-1}=-\rho(e_2).
$$

This is verified with $e_1^{-1}=-e_1$: $\rho(e_1)\rho(e_2)\rho(e_1)^{-1}=e_1e_2(-e_1)=-e_1e_2e_1$, and $e_2e_1=-e_1e_2$ gives $e_1e_2e_1=e_2$, whence the value $-e_2=-\rho(e_2)$. The module computation therefore returns the negative of the vector on which the reflection acts trivially, and it is the signed inner conjugation, and not the inner conjugation, that returns $e_2$ itself.

### The Biquaternion Module

For $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ the irreducible module is the space of biquaternions with the action recorded in the biquaternion spinor module section of *Spin Representations and Clifford Modules with Inner Conjugation*, and the odd elements of $\mathrm{Pin}(1,3)$ act by the same one-sided left multiplication, interchanging the two chiral halves and conjugating the Clifford action by the negative of the reflection, exactly as above. The compatibility of that module with the Lorentz action is the subject of the applications layer, and nothing of it is used here.

## Summary

A **pin representation** is the restriction of the Clifford action on a Clifford module $S$ to the Pin group, $\rho(x)s=xs$, a one-sided left action by construction. It is defined for the whole algebra, so it requires no new module theory; it satisfies $\rho(-1)=-\mathrm{id}_S$, hence does not descend to $O(V,q)$, and it is faithful on an irreducible module over a simple Clifford algebra, with kernel $\mathrm{Pin}\cap(\{1\}\times A)$ when the algebra is a product. Its restriction to the even part is the spin representation, and on an even-dimensional module the **odd elements interchange the two chiral halves** while the even ones preserve them, so the pin representation is irreducible where the spin representation splits into the two half-spin representations.

The sign is carried by the intertwining identity, $\rho(x)\rho(v)\rho(x)^{-1}=\rho(\mathrm{Ad}_x(v))=\rho(\varepsilon_x\mathrm{Ad}^{\alpha}_x(v))$, with $\varepsilon_x=(-1)^{k}$; equivalently $\rho(\mathrm{Ad}^{\alpha}_x(v))=\varepsilon_x\rho(x)\rho(v)\rho(x)^{-1}$. For a vector it reads $\rho(u)\rho(v)\rho(u)^{-1}=-\rho(\rho_u(v))$, so the module action returns the negative of the reflection and the **signed inner conjugation** is the operator that removes the sign, which is why the pinor theory must use it. An odd element satisfies $\rho(u)^{2}=q(u)\mathrm{id}_S$ and, over a definite form, acts as a parity-reversing operator unitary up to the group inverse. Over $\mathbb{R}$ the construction is read off the definite and signature forms in the same way, with the reality conditions of the module taken from the reality article of the category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S$ | Clifford module; the pinor module when the whole Pin group acts |
| $\rho(x)s=xs$ | Pin representation, the one-sided left action |
| $\rho(-1)=-\mathrm{id}_S$ | The double-cover sign survives on the module |
| $S=\Delta_+\oplus\Delta_-$ | Chiral decomposition for even $n$ |
| $\mathrm{Cl}^0$ preserves, $\mathrm{Cl}^1$ interchanges | Even and odd elements on the halves |
| $\rho(x)\rho(v)\rho(x)^{-1}=\rho(\mathrm{Ad}_x(v))=\rho(\varepsilon_x\mathrm{Ad}^{\alpha}_x(v))$ | Intertwining identity and the sign |
| $\rho(\mathrm{Ad}^{\alpha}_x(v))=\varepsilon_x\rho(x)\rho(v)\rho(x)^{-1}$ | The signed operator up to the parity sign |
| $\rho(u)\rho(v)\rho(u)^{-1}=-\rho(\rho_u(v))$ | Reflection in the module, with the minus |
| $\rho(u)^{2}=q(u)\mathrm{id}_S$ | Square of an odd element |
| $\ker\rho=\mathrm{Pin}\cap(\{1\}\times A)$ | Kernel over a product of simple algebras |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the Pin and Spin groups and their modules through the whole Clifford algebra.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the Clifford action on a module, the chirality splitting and the action of the odd part.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the pin representations and the effect of the parity on the module.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the original construction of the pinor and spinor modules.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the action of an algebra on an irreducible module, its kernel and the two-sided ideals.
