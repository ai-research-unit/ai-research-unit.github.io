# __The One-Sided Action and the Spin Representation__

## Introduction

A minimal left ideal of a Clifford algebra is a simple module, and the algebra acts on it by left multiplication. That action is a one-sided operator, and read as a representation it is the **spin representation**: the same left multiplication, restricted from the algebra to the spin group, is the representation that carries the spinors. This article keeps the operator and the representation in one place. The one-sided operator is the action of the algebra on the ideal; the spin representation is its restriction; and the irreducibility of the module is the irreducibility of the representation, with Schur's lemma supplying the commutant.

Two facts organise the article. First, of the two one-sided families only the left family preserves a left ideal, so the spin representation is intrinsically one-sided: a right multiplication by a rotor does not keep the ideal fixed, and the dual representation requires a minimal right ideal instead. Second, the ideal being simple, the action on it is irreducible and its commutant is a division algebra, so the spin representation has no invariant subspaces and its structure is that of a simple module over a division algebra.

The algebra and the minimal left ideals are *Left Multiplication and the Clifford Module Structure* and *Spinors as Minimal Left Ideals with Inner Conjugation*; the operator calculus of the left and the right multiplications is *One-Sided Operators on a Clifford Algebra*; the spinor module and its dimension, the chiral splitting and the complex spin representation are *Spin Representations and Clifford Modules with Inner Conjugation*; the spin group and the double cover are *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* and *The Two-Sided Operators and the Spin Group*. Those constructions are quoted, not repeated; what this article adds is the description of the representation as the one-sided action on a minimal left ideal, with its irreducibility and its commutant. The base is a field $F$ of characteristic not $2$, $q$ is non-degenerate, and the algebra is semisimple.

## The One-Sided Action on a Left Ideal

**Definition.** Let $I = \mathrm{Cl}(V,q)\pi$ be a minimal left ideal. The **one-sided action** of the algebra on $I$ is the restriction of the left multiplication,

$$
\rho_I : \mathrm{Cl}(V,q) \longrightarrow \mathrm{End}_F(I), \qquad \rho_I(x)\psi = x\,\psi , \qquad \psi \in I .
$$

It is the module action of the regular module on its submodule $I$, and it is an algebra homomorphism.

**Proposition.** $\rho_I$ is well defined – that is, $x\psi \in I$ for $x \in \mathrm{Cl}$ and $\psi \in I$ – precisely because $I$ is a left ideal; and $\rho_I(xz) = \rho_I(x)\rho_I(z)$, $\rho_I(1) = \mathrm{id}_I$.

**Proof.** $x\psi \in \mathrm{Cl}\psi \subseteq \mathrm{Cl}\,\mathrm{Cl}\pi \subseteq \mathrm{Cl}\pi = I$; the homomorphism properties are associativity and $1\psi = \psi$.

**Proposition (only the left family acts).** Let $R_y(\psi) = \psi y$ be the right multiplication. Then $R_y$ preserves $I$ for every $y$ only when $I$ is a two-sided ideal, which for a minimal left ideal of a simple algebra it is not. A right multiplication by a unit preserves a minimal *right* ideal, and the resulting action is the dual of $\rho_I$.

**Proof.** If $R_y(I) \subseteq I$ for all $y$ then $\mathrm{Cl}\pi\,\mathrm{Cl} \subseteq \mathrm{Cl}\pi$, so $\mathrm{Cl}\pi$ is two-sided, contrary to minimality in a simple algebra, where the only two-sided ideals are $0$ and the algebra. For a minimal right ideal $J = \pi'\mathrm{Cl}$, right multiplication by a unit $R$ satisfies $JR = \pi'\mathrm{Cl}R = \pi'\mathrm{Cl}$, since $\mathrm{Cl}R = \mathrm{Cl}$.

**Remark (the two actions on the ideal).** The left action of the algebra and the right action of the opposite algebra on the same ideal, the identification of the ideal with the exterior algebra of a Witt basis, and the fact that a left ideal is preserved by every left multiplication while a right ideal is preserved by every right multiplication, are *Spinors as Minimal Left Ideals with Inner Conjugation*; the operator-theoretic content of the present article is only the restriction of the left family, which is the module action.

## The Spin Representation

**Definition.** The **spin representation** attached to the module $I$ is the restriction of the one-sided action to the spin group,

$$
\rho : \mathrm{Spin}(V,q) \longrightarrow GL_F(I), \qquad \rho(x) = \rho_I(x)\big|_{\mathrm{Spin}(V,q)} .
$$

**Theorem (irreducibility).** Let $I$ be a minimal left ideal. Then the action $\rho_I$ of the algebra on $I$ is irreducible: $I$ has no proper nonzero submodule, and every nonzero element of $I$ is a cyclic vector. Equivalently, the only $F$-linear maps $T : I \to I$ with $T(x\psi) = xT(\psi)$ for every $x$ and $\psi$ are the multiplications by elements of the division ring $D = \mathrm{End}_{\mathrm{Cl}}(I)$, so the commutant is a division algebra and

$$
\rho_I\bigl(\mathrm{Cl}(V,q)\bigr) = \mathrm{End}_D(I)
$$

whenever the algebra is simple.

**Proof.** A submodule of the left ideal $I$ is a left ideal contained in $I$, and minimality leaves only $0$ and $I$; a nonzero $\psi \in I$ generates $\mathrm{Cl}\psi = I$. For the commutant, a $T$ commuting with the action is an endomorphism of the simple module, so Schur's lemma makes $D = \mathrm{End}_{\mathrm{Cl}}(I)$ a division ring; the density statement is the double centraliser theorem applied to the simple algebra.

**Theorem (the kernel on the group).** The representation $\rho$ satisfies $\rho(-1) = -\mathrm{id}_I \neq \mathrm{id}_I$, so $-1$ is **not** in the kernel. When the Clifford algebra is simple the action of the algebra on the irreducible module is faithful, so an element of the spin group acting as the identity on $I$ is the identity of the algebra, and the kernel of $\rho$ is trivial. When the algebra is a product $A \times A$, the irreducible module of one factor is annihilated by the other and the kernel is the nontrivial subgroup $\mathrm{Spin}(V,q) \cap (\{1\}\times A)$. In both cases $\rho$ does not descend to $SO(V,q)$: the element $-1$ is in the kernel of the projection $\mathrm{Spin} \to SO$ but acts as $-\mathrm{id}_I$ on the module.

**Proof.** The element $-1$ is the scalar $-1$ of the algebra and $I \neq 0$, so it acts as $-\mathrm{id}_I$. In the simple case the action of the algebra on its irreducible module is faithful, so the kernel on the spin group is trivial. The product case and the half-spin kernels are computed in *Spin Representations and Clifford Modules with Inner Conjugation*.

**Remark (odd dimension and the two simple modules).** In odd dimension the algebra has two simple modules, and a minimal left ideal carries one of them; the two are distinguished by the scalar by which the central volume element acts, and the spin representation attached to one of them is irreducible. Nothing new is needed: the uniqueness in even dimension and the pair in odd dimension are *Left Multiplication and the Clifford Module Structure*, and the concrete dimension of the module is *Spin Representations and Clifford Modules with Inner Conjugation*.

## The One-Sided Action and the Vector Action

**Proposition (the two actions are different).** Let $R$ be a rotor and $\psi \in I$. The **spin action** is left multiplication $\psi \mapsto R\psi$ and carries the half of the double cover that acts on the spinors; the **vector action** is the sandwich $v \mapsto RvR^{-1}$ and acts on $V$, not on $I$ in general. The two actions carry the two halves of the angle of the rotation, and they are not the same representation.

**Proof.** Left multiplication by $R$ is the module action; the sandwich is the two-sided operator of *The Sandwich on a Clifford Algebra*, which acts on $V$ by construction and does not preserve a general left ideal, as the explicit counterexample of *Spinors as Minimal Left Ideals with Inner Conjugation* shows.

**Remark (why the one-sided action is the right one for spinors).** A spinor is an element of the ideal, so the only operators that can act on it without leaving the ideal are the left multiplications. This is the operator-theoretic reason the spin representation is written as a one-sided action and not as a sandwich, and the reason the sandwich is reserved for the vector representation.

## Worked Cases

### A Minimal Left Ideal in $\mathrm{Cl}_{1,1}(\mathbb{R})$

With $e_1^{2} = 1$, $e_2^{2} = -1$ the algebra is $M_2(\mathbb{R})$, the idempotent $\pi = \tfrac12(1+e_1)$ generates the two-dimensional ideal $I = \mathbb{R}\pi \oplus \mathbb{R}e_2\pi$, and the left action of the algebra on $I$ is the defining two-dimensional representation of $M_2(\mathbb{R})$. It is irreducible, its commutant is $\mathbb{R}$, and $\rho(-1) = -\mathrm{id}_I$.

### A Minimal Left Ideal in $\mathrm{Cl}_{0,3}(\mathbb{R})$

With $e_j^{2} = -1$ the algebra is $\mathbb{H}\oplus\mathbb{H}$, and a minimal left ideal is four-dimensional over $\mathbb{R}$, carrying one of the two simple modules. The left action is irreducible, the central volume element $\omega$ acts by one of the two scalars $\pm1$, and the spin group acts by left multiplication with kernel $\{\pm1\}$ on this module. The two choices of sign give the two chiral halves.

### The Rotor and the Two Actions

In $\mathrm{Cl}_{0,2}(\mathbb{R})\cong\mathbb{H}$ with $R = e_1e_2$ and $I$ a minimal left ideal, left multiplication by $R$ acts on $I$ as an $F$-linear map of order $2$ up to the sign of the double cover, while the sandwich $v \mapsto RvR^{-1}$ acts on the two-dimensional space of vectors as the half-turn. The two operators are different, live on different spaces, and illustrate the two actions of the rotor.

## Summary

On a minimal left ideal $I = \mathrm{Cl}(V,q)\pi$ the **one-sided action** $\rho_I(x)\psi = x\psi$ is the module action of the algebra, and it is the left family alone: a right multiplication does not preserve a left ideal, so nothing two-sided acts on the spinors. The action is **irreducible**, because $I$ is a simple module; its commutant is the division algebra $D = \mathrm{End}_{\mathrm{Cl}}(I)$ and, over a simple algebra, the action exhausts $\mathrm{End}_D(I)$. The **spin representation** is the restriction of this action to $\mathrm{Spin}(V,q)$; it satisfies $\rho(-1) = -\mathrm{id}_I$, its kernel is trivial over a simple algebra and is the other factor over a product algebra, and it therefore does not descend to $SO(V,q)$ – the element $-1$ is invisible to $SO$ but acts as $-\mathrm{id}_I$ on the spinors. The action on the vectors by the sandwich is a different representation, on a different space, and the one-sided action is the correct one for spinors because only left multiplication stays in the ideal. The construction of the ideals, their dimension, the chirality and the concrete models are *Spinors as Minimal Left Ideals with Inner Conjugation* and *Spin Representations and Clifford Modules with Inner Conjugation*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $I = \mathrm{Cl}(V,q)\pi$ | Minimal left ideal, the spinor space |
| $\rho_I(x)$ | One-sided action, the left multiplication restricted to $I$ |
| $R_y(\psi) = \psi y$ | Right multiplication, which does not preserve $I$ |
| $\rho = \rho_I\big|_{\mathrm{Spin}}$ | Spin representation |
| $D = \mathrm{End}_{\mathrm{Cl}}(I)$ | Commutant, a division algebra |
| $\rho_I(\mathrm{Cl}) = \mathrm{End}_D(I)$ | Density over a simple algebra |
| $\rho(-1) = -\mathrm{id}_I$ | The sign of the double cover in the representation |
| $R\psi$, $RvR^{-1}$ | Spin action and vector action of a rotor |

## Further Reading

- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the spin representation as the action on a minimal left ideal.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for irreducible Clifford modules and the spin representation of the spin group.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the module theory and the density statement.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the double centraliser theorem and the commutant of a simple module.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the spinor spaces of the low-dimensional algebras.
