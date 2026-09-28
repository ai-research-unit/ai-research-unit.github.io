
# __Split-Biquaternion Representation Theory__

## Introduction

The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$ is a finite-dimensional real algebra, and its representation theory is governed by a single structural fact: it is isomorphic to the product $\mathbb{H} \oplus \mathbb{H}$ of two copies of the quaternion division algebra. This makes it a **semisimple** but **not simple** algebra, with exactly two isomorphism classes of simple modules, in contrast to the biquaternion algebra $\mathbb{B}$, which is simple. This article records the representations of the algebra and of its group of units, the form of Schur's lemma, the intertwiners, the real and split complex forms, the tensor products, and the comparison with the biquaternion case. The structural facts about the algebra are assumed from *Split-Biquaternion Algebra*, and the ideals and the splitting from *Split-Biquaternion Ideals and Peirce Decomposition*.

The treatment is purely mathematical. No physics is invoked. The general theory of finite-dimensional associative algebras — Wedderburn's theorem, the Jacobson radical, Schur's lemma — is used as standard, and the module theory is that of the companion articles on modules and on algebras.

## The Algebra and Its Ground Fields

The algebra $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ is free of rank $4$ over the split complex algebra $\mathbb{D}$, which is its centre. Since $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$ is not a field, the two natural ground structures are:

- the real numbers $\mathbb{R}$, over which $\mathbb{H}_{\mathbb{D}}$ has dimension $8$;
- the split complex algebra $\mathbb{D}$, over which it is a free module of rank $4$ and a $\mathbb{D}$-algebra.

The idempotents $\tilde\Pi_\pm = \tfrac{1}{2}(1 \pm j)$ of the centre give the **Peirce decomposition** of every module, and are the key to the whole theory. Because $\tilde\Pi_+ + \tilde\Pi_- = 1$ and $\tilde\Pi_+ \tilde\Pi_- = 0$, the algebra splits as a product

$$
\varphi : \mathbb{H}_{\mathbb{D}} \longrightarrow \mathbb{H} \oplus \mathbb{H} , \qquad \varphi(\tilde{Q}) = (\tilde{Q}_+, \tilde{Q}_-) ,
$$

and every left $\mathbb{H}_{\mathbb{D}}$-module $M$ splits as

$$
M = \tilde\Pi_+ M \oplus \tilde\Pi_- M ,
$$

with $\tilde\Pi_\pm$ acting as the two projections. On $\tilde\Pi_+ M$ the algebra acts through the first factor $\mathbb{H}$, and on $\tilde\Pi_- M$ through the second.

## Representations over the Split Complex Numbers

**Theorem.** A left $\mathbb{H}_{\mathbb{D}}$-module is the same thing as a pair $(M_+, M_-)$ of left $\mathbb{H}$-modules, and the passage to the pair is by $M \mapsto (\tilde\Pi_+ M, \tilde\Pi_- M)$.

**Proof.** For a left $\mathbb{H}_{\mathbb{D}}$-module $M$, the central idempotents $\tilde\Pi_\pm$ act as commuting projections with $\tilde\Pi_+ + \tilde\Pi_- = 1$, giving the direct sum decomposition, and each piece is stable under the algebra, which acts through the corresponding factor of $\mathbb{H} \oplus \mathbb{H}$. Conversely two $\mathbb{H}$-modules $M_+, M_-$ form an $\mathbb{H}_{\mathbb{D}}$-module $M_+ \oplus M_-$ with $(\tilde{Q}_+, \tilde{Q}_-)(m_+, m_-) = (\tilde{Q}_+ m_+, \tilde{Q}_- m_-)$, and the two constructions are inverse.

Since the quaternion algebra $\mathbb{H}$ is a division algebra, every $\mathbb{H}$-module is free: the category $\mathbb{H}\text{-}\mathrm{Mod}$ is the category of free $\mathbb{H}$-modules, and its simple objects are the one-dimensional $\mathbb{H}$-modules, isomorphic to $\mathbb{H}$ itself.

**Theorem.** The algebra $\mathbb{H}_{\mathbb{D}}$ is semisimple, with Jacobson radical zero and composition length two as a module over itself. It has exactly two isomorphism classes of simple left modules,

$$
S_+ = (\mathbb{H}, 0) , \qquad S_- = (0, \mathbb{H}) ,
$$

each of real dimension $4$, and each isomorphic as an $\mathbb{H}$-module to $\mathbb{H}$.

**Proof.** The category of modules is the product $\mathbb{H}\text{-}\mathrm{Mod} \times \mathbb{H}\text{-}\mathrm{Mod}$ by the previous theorem; the simple objects of a product category are the simple objects of one factor with the other factor zero, which are $S_+$ and $S_-$. A product of division algebras has zero radical, and the module $\mathbb{H}_{\mathbb{D}} = S_+ \oplus S_-$ over itself shows the length.

The **regular representation** is therefore the regular bimodule $\mathbb{H}_{\mathbb{D}}$, which as a left module is $S_+ \oplus S_-$. By Wedderburn's theorem the algebra is isomorphic to the product of the endomorphism rings of its simple modules, $\mathbb{H} \oplus \mathbb{H}$, which is the splitting already used.

The two minimal two-sided ideals $\mathbb{H}\tilde\Pi_\pm$, viewed as left $\mathbb{D}$-modules, are projective but not free: each is a direct summand of the free $\mathbb{D}$-module $\mathbb{H}_{\mathbb{D}}$, while the annihilator of $\mathbb{H}\tilde\Pi_+$ contains $j-1$ and that of $\mathbb{H}\tilde\Pi_-$ contains $j+1$, so neither is free, a free $\mathbb{D}$-module being faithful.

## Schur's Lemma and Intertwiners

**Theorem (Schur).** For simple $\mathbb{H}_{\mathbb{D}}$-modules $S, T$, every nonzero homomorphism $S \to T$ is an isomorphism, and $\operatorname{End}_{\mathbb{H}_{\mathbb{D}}}(S)$ is a division ring. Here

$$
\operatorname{Hom}_{\mathbb{H}_{\mathbb{D}}}(S_+, S_-) = \operatorname{Hom}_{\mathbb{H}_{\mathbb{D}}}(S_-, S_+) = 0 , \qquad \operatorname{End}_{\mathbb{H}_{\mathbb{D}}}(S_\pm) \cong \mathbb{H}^{\mathrm{op}} \cong \mathbb{H} .
$$

**Proof.** Schur's lemma is standard. Because a homomorphism preserves the action of the central idempotents, it must carry $\tilde\Pi_+ T$ to $\tilde\Pi_+ T$ and vanishes on the other summand; hence a homomorphism $S_+ \to S_-$ vanishes, and one $S_+ \to S_+$ is an $\mathbb{H}$-linear endomorphism of the free rank-one module $\mathbb{H}$, that is right multiplication by a quaternion, which is $\mathbb{H}^{\mathrm{op}}$.

The division ring $\operatorname{End}(S_\pm) \cong \mathbb{H}$ is the analogue of the field $\mathbb{C}$ appearing in the biquaternion case through $\mathbb{B} \cong M_2(\mathbb{C})$. The non-isomorphism of the two simple modules is the module-theoretic expression of the fact that $\tilde\Pi_+ \mathbb{H}_{\mathbb{D}} \tilde\Pi_- = 0$.

**Corollary.** The algebra is a product of two division algebras and is therefore **not simple**: each of the two simple modules spans a distinct two-sided ideal, and these are the two minimal two-sided ideals $\mathbb{H} \tilde\Pi_+$ and $\mathbb{H} \tilde\Pi_-$ of *Split-Biquaternion Ideals and Peirce Decomposition*.

## Real Representations

The **real representations** of $\mathbb{H}_{\mathbb{D}}$ are its representations on real vector spaces, that is its left modules; by the structure theorem these decompose into copies of $S_+$ and $S_-$. A real representation of dimension $n$ is described by a pair of non-negative integers $(a, b)$ with $4(a+b) = n$, the multiplicities of $S_+$ and $S_-$:

$$
M \cong a\, S_+ \oplus b\, S_- , \qquad \dim_{\mathbb{R}} M = 4(a+b) .
$$

The regular representation corresponds to $(a,b) = (1,1)$. The endomorphism ring of such a module is $M_a(\mathbb{H}) \times M_b(\mathbb{H})$, a product of two matrix algebras over the division ring $\mathbb{H}$.

Because the centre is $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$, a real representation is irreducible precisely when $(a,b) = (1,0)$ or $(0,1)$: irreducibility over $\mathbb{R}$ of a module for a product algebra means triviality on one factor. There is no representation irreducible over $\mathbb{D}$ that is not already one of the two simple modules.

## The Group of Units

**Theorem.** The group of units of $\mathbb{H}_{\mathbb{D}}$ is the direct product $\mathbb{H}^{\times} \times \mathbb{H}^{\times}$ under the isomorphism $\varphi$:

$$
\mathbb{H}_{\mathbb{D}}^{\times} \cong \left\{ (\tilde{Q}_+, \tilde{Q}_-) : \tilde{Q}_+ \neq 0, \tilde{Q}_- \neq 0 \right\} , \qquad \tilde{Q}^{\times} = \mathbb{H}^{\times} \times \mathbb{H}^{\times} .
$$

**Proof.** An element is a unit in a product ring exactly when both components are units, and the units of the division algebra $\mathbb{H}$ are its nonzero elements.

The unit group is a real Lie group of dimension $8$, connected because it is the square of the connected group $\mathbb{H}^{\times}$. By the polar form of the nonzero quaternions, $\mathbb{H}^{\times} \cong \mathbb{R}_{>0} \times S^3$, so that

$$
\mathbb{H}_{\mathbb{D}}^{\times} \cong \mathbb{R}_{>0}^2 \times S^3 \times S^3 ,
$$

a group whose compact part is $S^3 \times S^3 \cong \mathrm{Spin}(4)$. This is the group acting on the algebra in the rotation theory developed in *Split-Biquaternion Rotations and the Lorentz Group*, and it contrasts with the biquaternion unit group, which is $GL(2,\mathbb{C}) \cong (SL(2,\mathbb{C}) \times \mathbb{C}^{\times})/\{\pm 1\}$, with compact part $U(2)$.

The **norm-one group** — the elements whose split-biquaternion norm is the identity of $\mathbb{D}$ — is the kernel of $N$ restricted to the units. Since $N(\tilde{Q}) = N_+ N_-$ in components $N_\pm = |\tilde{Q}_\pm|^2$, the condition $N(\tilde{Q}) = 1$ is the pair of equations $|\tilde{Q}_+| = |\tilde{Q}_-| = 1$, so the norm-one group is

$$
\left\{ \tilde{Q} : N(\tilde{Q}) = 1 \right\} = S^3 \times S^3 \cong \mathrm{Spin}(4) .
$$

## Finite-Dimensional Representations

Since $\mathbb{H}_{\mathbb{D}}^{\times} \cong \mathbb{H}^{\times} \times \mathbb{H}^{\times}$ and $\mathbb{H}^{\times} \cong \mathbb{R}_{>0} \times S^3$ with $S^3 = SU(2)$, every finite-dimensional continuous representation of $\mathbb{H}_{\mathbb{D}}^{\times}$ is the exterior tensor product of one representation of the first copy of $\mathbb{H}^{\times}$ and one of the second:

$$
\rho = \rho_1 \boxtimes \rho_2 , \qquad \rho_i : \mathbb{H}^{\times} \to GL(V_i) .
$$

Each copy of $\mathbb{H}^{\times}$ is the product of the abelian factor $\mathbb{R}_{>0}$ and the compact factor $SU(2)$, so its irreducible finite-dimensional continuous representations are the tensor products $\chi \otimes \sigma$ of a continuous character $\chi(x) = x^{\lambda}$ of $\mathbb{R}_{>0}$, $\lambda \in \mathbb{C}$, and an irreducible representation $\sigma = \mathrm{Sym}^{n}(\mathbb{C}^2)$ of $SU(2)$ of spin $n/2$. The irreducible finite-dimensional continuous representations of the unit group are therefore indexed by a pair of a character exponent and a spin for each factor, with

$$
\rho = \left(\chi_{\lambda_1} \otimes \mathrm{Sym}^{n_1}(\mathbb{C}^2)\right) \boxtimes \left(\chi_{\lambda_2} \otimes \mathrm{Sym}^{n_2}(\mathbb{C}^2)\right) .
$$

Restricting to the representations that are trivial on the two positive rays, equivalently to the finite-dimensional representations of the compact part $S^3 \times S^3 = \mathrm{Spin}(4)$, the exponents are zero and the classification is by a pair $(n_1, n_2)$ of non-negative integers, with

$$
\rho_{(n_1,n_2)} = \mathrm{Sym}^{n_1}(\mathbb{C}^2) \boxtimes \mathrm{Sym}^{n_2}(\mathbb{C}^2) , \qquad \dim_{\mathbb{C}} = (n_1+1)(n_2+1) .
$$

The two positive rays are also the reason the unit group is non-compact and its representations need not be unitary; the whole classification is that of the Lie group $(\mathbb{R}_{>0} \times SU(2))^2$, whose compact part is $SU(2) \times SU(2)$.

## The Defining Representation

The **defining representation** of $\mathbb{H}_{\mathbb{D}}$ is the action on either simple module, $S_\pm \cong \mathbb{H}$, of real dimension $4$. Under $\varphi$ it is the representation $(\tilde{Q}_+, \tilde{Q}_-) \mapsto \tilde{Q}_+$ on the first factor (or $\tilde{Q}_-$ on the second). There is no faithful irreducible representation: any faithful module must have $a \geq 1$ and $b \geq 1$, hence dimension at least $8$, and the regular representation $S_+ \oplus S_-$ is the smallest faithful one.

This is a genuine difference from the biquaternion case. There the algebra $\mathbb{B} \cong M_2(\mathbb{C})$ has a single simple module $\mathbb{C}^2$, the defining representation is two-dimensional over $\mathbb{C}$, and it is faithful; the split biquaternion algebra has two four-dimensional simple modules over $\mathbb{R}$ and no faithful irreducible one.

## Tensor Products

For a non-commutative algebra the tensor product of two left modules is not naturally a left module, and the split biquaternion algebra is no exception. A tentative action of $\tilde{Q}$ on $S_+ \otimes_{\mathbb{R}} S_-$ would have to place the component $\tilde{Q}_+$ on the first factor and $\tilde{Q}_-$ on the second, but the resulting assignment

$$
\tilde{Q} \longmapsto \tilde{Q}_+ \otimes \tilde{Q}_-
$$

is bilinear rather than linear in $\tilde{Q}$: on a sum $\tilde{Q} = \tilde{Q}' + \tilde{Q}''$ the two sides $(\tilde{Q}'+\tilde{Q}'')_+ \otimes (\tilde{Q}'+\tilde{Q}'')_-$ and $\tilde{Q}'_+ \otimes \tilde{Q}'_- + \tilde{Q}''_+ \otimes \tilde{Q}''_-$ differ, since the assignment uses both components at once. Such a map therefore does not factor through the algebra and does not define a module structure. Consequently there is no decomposition of $S_\pm \otimes_{\mathbb{R}} S_\pm$ into simple modules, and no multiplicity statement of the form $S_+ \otimes_{\mathbb{R}} S_- \cong 4\,S_-$; the tensor-product decomposition that the biquaternion case reads off from the tensor square of its single simple module has no counterpart on the algebra side here.

The tensor products that are defined are those of the unit-group representations: the irreducible finite-dimensional representations $\rho_{(n_1,n_2)}$ form the tensor products of representations of the two $SU(2)$ factors, and their tensor product is computed factor by factor by the Clebsch–Gordan rule of $SU(2)$. The product of $\rho_{(n_1,n_2)}$ and $\rho_{(m_1,m_2)}$ is the direct sum of the $\rho_{(k_1,k_2)}$ with $|n_1-m_1| \leq k_1 \leq n_1+m_1$ and $|n_2-m_2| \leq k_2 \leq n_2+m_2$, the steps being two and each pair appearing once. This is the Clebsch–Gordan rule applied independently to two factors, in place of the single $SU(2)$ rule of the biquaternion case.

## The Relation to the Representation Theory of the Biquaternions

The biquaternion algebra $\mathbb{B} \cong M_2(\mathbb{C})$ is simple, with a single simple module $\mathbb{C}^2$, division ring $\mathbb{C}$, and regular representation of dimension $4$ over $\mathbb{C}$; its unit group is essentially $SL(2,\mathbb{C})$, whose finite-dimensional representations are the symmetric powers $\mathrm{Sym}^n(\mathbb{C}^2)$. The split biquaternion algebra is the product $\mathbb{H} \oplus \mathbb{H}$, with two simple modules, division ring $\mathbb{H}$, regular representation of dimension $8$ over $\mathbb{R}$, and unit group $\mathbb{H}^{\times} \times \mathbb{H}^{\times}$. The correspondence is by the idempotent decomposition: each biquaternion representation is transported to a pair of quaternionic representations through the Peirce decomposition, and the passage

$$
\mathbb{B} \longleftrightarrow \mathbb{H} \oplus \mathbb{H} , \qquad \mathbb{C} \longleftrightarrow \mathbb{H}
$$

is the replacement of the simple algebra $M_2(\mathbb{C})$ by the product of two division algebras. The representation rings are correspondingly the representation ring of $SL(2,\mathbb{C})$ on the one hand and that of $S^3 \times S^3$ on the other.

## Summary

The split biquaternion algebra is a free $\mathbb{D}$-module of rank $4$ and a real algebra of dimension $8$, isomorphic to the product $\mathbb{H} \oplus \mathbb{H}$ by the Peirce decomposition along its central idempotents $\tilde\Pi_\pm$. Its module category is the product of two copies of the category of $\mathbb{H}$-modules, so it is semisimple with zero radical, has composition length two over itself, and possesses exactly two simple left modules $S_\pm$, each of real dimension $4$ and isomorphic to $\mathbb{H}$. The two minimal ideals, viewed as $\mathbb{D}$-modules, are projective but not free. Schur's lemma gives intertwiners $\operatorname{Hom}(S_+,S_-) = 0$ and division ring $\operatorname{End}(S_\pm) \cong \mathbb{H}$, in place of the field $\mathbb{C}$ of the biquaternion case, and the algebra is not simple, its two minimal two-sided ideals being the spans of the simple modules. A real representation is classified by a pair of multiplicities $(a,b)$, irreducible only for $(1,0)$ and $(0,1)$, and the regular representation is $(1,1)$. The group of units is $\mathbb{H}^{\times} \times \mathbb{H}^{\times} \cong \mathbb{R}_{>0}^2 \times S^3 \times S^3$, and the norm-one group is $S^3 \times S^3 \cong \mathrm{Spin}(4)$; finite-dimensional representations of the unit group are the exterior tensor products of representations of the two copies of $\mathbb{R}_{>0} \times SU(2)$, indexed by a character exponent and a spin for each factor. The defining representation is the four-dimensional action on a simple module, and no faithful irreducible representation exists. The tensor product of two left modules is not naturally a left module, since the only candidate action is bilinear in the algebra element and fails to factor through it, so the tensor products belong to the unit group, where they follow the Clebsch–Gordan rule factor by factor on the two $SU(2)$'s. The whole theory is the biquaternion theory with the simple algebra $M_2(\mathbb{C})$ replaced by the product of two division algebras.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ | Split biquaternion algebra, $\cong \mathbb{H} \oplus \mathbb{H}$ |
| $\mathbb{D}, \mathbb{H}, \mathbb{R}$ | The split complex, quaternion and real ground structures |
| $\tilde\Pi_\pm = \tfrac{1}{2}(1 \pm j)$ | Central idempotents, the Peirce projections |
| $\varphi(\tilde{Q}) = (\tilde{Q}_+, \tilde{Q}_-)$ | Isomorphism to $\mathbb{H} \oplus \mathbb{H}$ |
| $S_+, S_-$ | The two simple left modules, each $\cong \mathbb{H}$, dimension $4$ |
| $M = a S_+ \oplus b S_-$ | Classification of real representations by multiplicities |
| $\operatorname{End}_{\mathbb{H}_{\mathbb{D}}}(S_\pm) \cong \mathbb{H}$ | Division ring of the simple module |
| $\mathbb{H}\tilde\Pi_\pm$ | Minimal two-sided ideals, projective but not free as $\mathbb{D}$-modules |
| $\mathbb{H}_{\mathbb{D}}^{\times} \cong \mathbb{H}^{\times} \times \mathbb{H}^{\times}$ | Group of units |
| $\{ \tilde{Q} : N(\tilde{Q}) = 1 \} = S^3 \times S^3$ | Norm-one group |
| $\rho_{(n_1,n_2)}$ | Irreducible unit-group representation, spin $(n_1/2, n_2/2)$ |
| $S_+ \otimes_{\mathbb{R}} S_-$ | Tensor product of simple modules; not a module here |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for Wedderburn's theorem, semisimple algebras and the module category.
- Irving Kaplansky, *Fields and Rings* (Chicago, 1972), for the structure of products of division algebras and their representations.
- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Wiley, 1962), for Schur's lemma, intertwiners and tensor products over a division ring.
- Jacques Dixmier, *Enveloping Algebras* (North-Holland, 1977), for the finite-dimensional representation theory of $SU(2)$ and the Clebsch–Gordan rule as used in the unit-group case.
