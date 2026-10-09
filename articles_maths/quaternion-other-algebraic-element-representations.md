
# __Quaternion Other Algebraic Element Representations__

## Introduction

The quaternion algebra has several algebraic realizations that do not have an article of their own: the spinor representation on two-component complex vectors, the identification with a Clifford algebra and with the even part of a Clifford algebra, and the module structure of the algebra over itself and over its subalgebras. This article collects them, states the identifications precisely, and records the role of the choices involved. It is the quaternion member of the family's residual-representation pair; its counterpart is *The Clifford Algebra Representation*, and it supplies the realizations that the dedicated articles on the four-vector, regular, $2\times2$ and operator representations leave aside.

The article depends on *Quaternion Algebra* for the basis and the relations, on *Quaternion Norm and Invertibility* for the quaternion norm, and on *Quaternion 2x2 Matrix Element Representation* for the realization of the algebra. The Clifford identifications use the conventions of *Clifford Algebras in Finite Dimensions* for $\mathrm{Cl}(V,\tilde q)$ and $\mathrm{Cl}_{p,\tilde q}$, and the spinor realization is the representation theory of the unit group $Sp(1)$ from *Quaternion Rotations and Reflections*. No physical vocabulary is used: in particular the spinors below are the vectors of a module for $Sp(1)$, not the spinors of a field.

The corpus's default base is a commutative ring with identity; the Clifford identifications are stated over $\mathbb{R}$ and after complexification over $\mathbb{C}$, and the module statements hold over any base in which the relevant subalgebra is defined.

Throughout, $\mathbb{H}$ is the quaternion algebra with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$; a quaternion is $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ with conjugate $\tilde{q}^{\natural}$ and norm $N(\tilde q) = \tilde q\tilde{q}^{\natural}$; the unit group is $\mathbb{H}^{\times} = \mathbb{H}\setminus\{0\}$ and the unit sphere is $Sp(1)\cong S^3$. The Clifford algebra of a quadratic space $(V,\tilde q)$ is written $\mathrm{Cl}(V,\tilde q)$ and its real signature form $\mathrm{Cl}_{p,\tilde q}$, and the even subalgebra is $\mathrm{Cl}^0$.

## The Spinor Representation

**Definition.** The **spinor representation** of the quaternion algebra is the action of $\mathbb{H}$ on the two-component complex vectors $\mathbb{C}^2$ by the matrix realization $\iota$ of *Quaternion 2x2 Matrix Element Representation*:

$$
\tilde q\cdot v = \iota(\tilde q)\,v, \qquad v\in\mathbb{C}^2 .
$$

**Theorem.** The spinor representation is a faithful $\mathbb{R}$-linear representation of $\mathbb{H}$ by complex-linear maps of $\mathbb{C}^2$; restricted to the unit group it is the defining two-dimensional unitary representation of $Sp(1)\cong SU(2)$.

*Proof.* The action is a representation because $\iota$ is multiplicative, and it is faithful because $\iota$ is injective. For a unit $u$, $\iota(u)$ is unitary by *Quaternion 2x2 Matrix Element Representation*, so the restriction is a unitary representation; its dimension is two and it is irreducible, since any $\mathbb{C}$-linear map of $\mathbb{C}^2$ is in $M_2(\mathbb{C}) = \iota(\mathbb{H}\otimes\mathbb{C})$ and the algebra acts transitively on non-zero vectors.

**Proposition.** The spinor representation is the fundamental representation of $Sp(1)$ and is the source of the double cover $Sp(1)\to SO(3)$: the adjoint (three-dimensional) representation is the symmetric square of the spinor representation, and the tensor square decomposes as $\mathbb{C}^2\otimes\mathbb{C}^2\cong\mathrm{Sym}^2\oplus\Lambda^2$, of dimensions three and one.

*Proof.* The twofold symmetric square of the defining representation of $SU(2)$ is the three-dimensional irreducible representation, which is the adjoint representation on $\operatorname{Im}\mathbb{H}\otimes\mathbb{C}$; the alternating square is one-dimensional and trivial because the invariant antisymmetric form $\epsilon = i\sigma_2$ exists.

**Corollary.** The spinor representation is complex and of complex dimension two, so it is not equivalent to any real representation of $\mathbb{H}$; the quaternionic multiplication by $e_1,e_2,e_3$ supplies the three complex structures on $\mathbb{C}^2$ that make it a quaternionic line.

*Proof.* If the module were real of dimension two, the representation would be an injective homomorphism $\mathbb{H}\to M_2(\mathbb{R})$, which does not exist by *Quaternion 2x2 Matrix Element Representation*. The three images $\iota(e_k)$ satisfy $\iota(e_k)^2 = -I$ and pairwise anticommute, so they are three complex structures on $\mathbb{C}^2$.

## The Clifford Algebra Identification

**Definition.** The **Clifford algebra** $\mathrm{Cl}(V,\tilde q)$ of a quadratic space is the quotient of the tensor algebra by the relations $v^2 = \tilde q(v)$; its real signature forms are written $\mathrm{Cl}_{p,\tilde q}$.

**Theorem.** The quaternion algebra is the Clifford algebra of the negative definite real plane,

$$
\mathbb{H}\cong\mathrm{Cl}_{0,2},
$$

and it is also the even part of the Clifford algebra of the negative definite real three-space,

$$
\mathbb{H}\cong\mathrm{Cl}^0_{0,3}.
$$

*Proof.* Let $f_1,f_2$ generate $\mathrm{Cl}_{0,2}$, so $f_k^2 = -1$ and $f_1f_2 = -f_2f_1$. Setting $e_1 = f_1$, $e_2 = f_2$, $e_3 = f_1f_2$ gives $e_3^2 = -1$ and $e_1e_2 = e_3$, so the four elements $1,e_1,e_2,e_3$ satisfy the quaternion relations and form a basis of the four-dimensional algebra $\mathrm{Cl}_{0,2}$; hence $\mathbb{H}\cong\mathrm{Cl}_{0,2}$. For the second identification, the even subalgebra $\mathrm{Cl}^0_{0,3}$ is generated by the products $f_if_j$ with $i<j$, and these three elements satisfy the quaternion relations, giving $\mathrm{Cl}^0_{0,3}\cong\mathbb{H}$.

**Corollary.** Under the identification $\mathbb{H}\cong\mathrm{Cl}_{0,2}$ the scalar subspace is the degree-zero part, and the vector subspace is the sum of the degree-one and degree-two parts, because $e_1,e_2$ are the degree-one generators while $e_3 = e_1e_2$ is degree two; quaternion conjugation is the Clifford conjugation $\alpha\circ\tau$, the composition of the grade involution with reversion, which is the identity on the scalar part and the negation on each positive-degree part, hence negates the vector part.

*Proof.* The generators $e_1,e_2$ span the degree-one part and $e_3 = e_1e_2$ spans the degree-two part, so $1$ is degree zero and the vector subspace is the sum of the two positive-degree parts. The grade involution $\alpha$ negates the degree-one part and fixes the even part, while reversion $\tau$ fixes the degree-zero and degree-one parts and negates the degree-two part; their composition $\alpha\tau$ is therefore $+1$ on $1$ and $-1$ on each of $e_1,e_2,e_3$, which is quaternion conjugation.

## The Even Clifford Algebra by Complexification

**Theorem.** After complexification the Clifford identifications become the matrix identifications

$$
\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathrm{Cl}_2(\mathbb{C})\cong M_2(\mathbb{C}), \qquad
\mathrm{Cl}^0_{3,0}\cong M_2(\mathbb{R}), \qquad \mathrm{Cl}^0_{3,0}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C})\cong\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}.
$$

*Proof.* Complexifying $\mathrm{Cl}_{0,2}$ gives the complex Clifford algebra $\mathrm{Cl}_2(\mathbb{C})$, which is $M_2(\mathbb{C})$; the even part of the positive definite real algebra $\mathrm{Cl}_{3,0}$ is $\mathrm{Cl}_{2,0}\cong M_2(\mathbb{R})$, and its complexification is $M_2(\mathbb{C})$. Both are the complexification of $\mathbb{H}$ by the first identification.

**Remark.** The two real forms obtained this way — $\mathbb{H}$ itself and $\mathrm{Cl}^0_{3,0}\cong M_2(\mathbb{R})$ — have the same complexification but are not isomorphic over $\mathbb{R}$: one is a division algebra and the other a full matrix algebra. This is the manifestation, in the Clifford language, of the fact that $\mathbb{H}$ and $M_2(\mathbb{R})$ are distinct real forms of $M_2(\mathbb{C})$.

## The Module Structure

**Definition.** The **regular module** of $\mathbb{H}$ is the algebra regarded as a left module over itself by left multiplication, written ${}_{\mathbb{H}}\mathbb{H}$.

**Theorem.** The regular module is simple, its endomorphism ring is the opposite algebra $\operatorname{End}_{\mathbb{H}}({}_{\mathbb{H}}\mathbb{H})\cong\mathbb{H}^{\mathrm{op}}\cong\mathbb{H}$, and it is the unique simple left module up to isomorphism.

*Proof.* A submodule of ${}_{\mathbb{H}}\mathbb{H}$ is a left ideal, and the only left ideals are $0$ and $\mathbb{H}$, so the module is simple. An endomorphism is determined by its value at $1$ and is right multiplication by that value, so $\operatorname{End}_{\mathbb{H}}({}_{\mathbb{H}}\mathbb{H})\cong\mathbb{H}^{\mathrm{op}}$, which is isomorphic to $\mathbb{H}$ through conjugation, an anti-automorphism. Uniqueness is Schur's lemma together with the classification of simple modules over the division algebra $\mathbb{H}$.

**Theorem (module over a subalgebra).** For a root of $-1$, $\xi\in\{\xi : \xi^2 = -1\}$, let $\mathbb{C}_\xi = \mathbb{R}[\xi]\cong\mathbb{C}$ be the subalgebra generated by $\xi$. Then $\mathbb{H}$ is a free module of rank two over $\mathbb{C}_\xi$, and it is a free module of rank four over $\mathbb{R}$ and of rank one over itself.

*Proof.* The subalgebra $\mathbb{C}_\xi$ has dimension two, and $\mathbb{H}$ has dimension four over $\mathbb{R}$, so it has dimension two over $\mathbb{C}_\xi$; a finite-dimensional module over a division algebra is free, and its rank is the dimension quotient. The ranks over $\mathbb{R}$ and over $\mathbb{H}$ are the dimensions four and one.

**Corollary.** The choice of a root $\xi$ makes $\mathbb{H}$ a two-dimensional complex vector space, and different roots give different, conjugate, complex structures on the same underlying real space; the module structure over $\mathbb{C}_\xi$ is the algebraic content of the complex structure $L_\xi$ of *Quaternion Roots of Minus One*.

## The Role of Choices

**Proposition.** Each of the identifications above depends on a choice: the Clifford identification $\mathbb{H}\cong\mathrm{Cl}_{0,2}$ on the choice of an orthonormal basis $(f_1,f_2)$ of the negative plane; the spinor representation on the choice of the isomorphism $\iota$; and the complex module structure on the choice of root $\xi$.

*Proof.* An orthonormal basis of the negative plane determines the generators $f_1,f_2$ and hence the identification; the matrix realization $\iota$ is fixed by a specific choice of the images of $e_1,e_2,e_3$; and $\mathbb{C}_\xi$ depends on $\xi$.

**Theorem.** Two choices in any of these three lists differ by the action of the compact group $Sp(1)$ (equivalently $SO(3)$ on the imaginary subspace), and all the structural statements of the article are invariant under this action.

*Proof.* A change of orthonormal basis of the negative plane is a rotation of $\operatorname{Im}\mathbb{H}$, and every rotation is the adjoint action of a unit quaternion, so the generators change by conjugation by a unit; the matrix realization changes by conjugation by the corresponding unitary matrix; and the root $\xi$ changes to $u\xi u^{-1}$ under the adjoint action. Each of the invariants — the quaternion norm, the trace, the determinant, the module ranks — is unchanged.

## Relation to the Biquaternion Representations

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ inherits each of the realizations by scalar extension. Its Clifford identification is the complex one, $\mathbb{B}\cong\mathrm{Cl}_2(\mathbb{C})\cong M_2(\mathbb{C})$, already an isomorphism without a separate complexification; its spinor module is the same $\mathbb{C}^2$, now a complex module with a second, commuting action of the central unit $i$; and its regular module is the direct sum of two minimal left ideals, in contrast with the simple regular module of the division algebra $\mathbb{H}$. The passage from the real to the complex quaternion algebra therefore doubles the module theory without changing the spinor module: the central unit $i$ commutes with the action and splits the complexified regular module, while the spinor module remains irreducible.

## Summary

The spinor representation of the quaternion algebra is the action on two-component complex vectors by the matrix realization $\iota$; it is faithful, its restriction to $Sp(1)$ is the defining unitary representation, and its symmetric square is the adjoint representation, so it is the source of the double cover $Sp(1)\to SO(3)$. The module carries three anticommuting complex structures $\iota(e_1),\iota(e_2),\iota(e_3)$ and is therefore a quaternionic line.

The Clifford identifications are $\mathbb{H}\cong\mathrm{Cl}_{0,2}$ and $\mathbb{H}\cong\mathrm{Cl}^0_{0,3}$, with the scalar subspace as the degree-zero part and the vector subspace as the sum of the degree-one and degree-two parts of the first; after complexification they become $\mathbb{H}\otimes\mathbb{C}\cong\mathrm{Cl}_2(\mathbb{C})\cong M_2(\mathbb{C})$, and the even algebra $\mathrm{Cl}^0_{3,0}\cong M_2(\mathbb{R})$ is a distinct but complexification-equivalent real form and not isomorphic to $\mathbb{H}$ over $\mathbb{R}$.

The regular module of $\mathbb{H}$ is simple, with endomorphism ring $\mathbb{H}^{\mathrm{op}}\cong\mathbb{H}$ and no other simple left module; over a complex subalgebra $\mathbb{C}_\xi$ generated by a root of $-1$ the algebra is free of rank two, over $\mathbb{R}$ free of rank four, over itself free of rank one. Every identification depends on a choice, and the choices are acted on by $Sp(1)$ with the structural invariants fixed. The biquaternion case inherits all of this after scalar extension and doubles the module theory through the central unit.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Basis, $e_k^2 = -e_0$ |
| $\iota : \mathbb{H}\to M_2(\mathbb{C})$ | Matrix realization, used for the spinor action |
| $\tilde q\cdot v = \iota(\tilde q)v$, $v\in\mathbb{C}^2$ | Spinor representation |
| $Sp(1)\cong SU(2)$ | Unit quaternions, the spin group |
| $\mathrm{Sym}^2,\Lambda^2$ | Symmetric and alternating squares of the spinor module |
| $\mathrm{Cl}(V,\tilde q)$, $\mathrm{Cl}_{p,\tilde q}$, $\mathrm{Cl}^0$ | Clifford algebra, real signature form, even part |
| $\mathbb{H}\cong\mathrm{Cl}_{0,2}\cong\mathrm{Cl}^0_{0,3}$ | Clifford identifications |
| $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathrm{Cl}_2(\mathbb{C})\cong M_2(\mathbb{C})$ | Complexified identification |
| $\mathrm{Cl}^0_{3,0}\cong M_2(\mathbb{R})$ | The other real form, not isomorphic to $\mathbb{H}$ |
| ${}_{\mathbb{H}}\mathbb{H}$ | Regular module, simple, $\operatorname{End}\cong\mathbb{H}^{\mathrm{op}}$ |
| $\mathbb{C}_\xi = \mathbb{R}[\xi]$, $\xi^2 = -1$ | Complex subalgebra; $\mathbb{H}$ free of rank two over it |
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, complex Clifford form |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the Clifford identifications of the quaternion algebra and the spinor representations.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for Clifford algebras, spinor modules and the spin groups.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the regular module and the endomorphism ring of a division algebra.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for simple modules over division rings and Schur's lemma.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quaternion algebra among the normed division algebras.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the classification of real and complex Clifford algebras.
