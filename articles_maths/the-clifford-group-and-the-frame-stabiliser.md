# __The Clifford Group and the Frame Stabiliser__

## Introduction

A gamma frame is a choice. The Clifford relations fix the algebra, not the five matrices: any conjugate $U\gamma^\mu U^{-1}$ by an invertible $U$ is another frame, and the frames form a homogeneous space. Two subgroups of $GL_4(\mathbb{C})$ measure the freedom. The **stabiliser of the frame** is the set of $U$ that fix each gamma; it is the group of scalars $\mathbb{C}^{\times}I$. The **Clifford group** is the set of $U$ that preserve the span of the gammas up to a Lorentz transformation; it is larger, of dimension seven, and its even part is the scalars times the spin group. The quotient of the Clifford group by the scalars is the orthogonal group $O(4,\mathbb{C})$.

The distinction is the exact content of the phrase "the frame is not canonical". The Clifford relations are invariant under the Clifford group; the five-element subset is invariant only under the scalars. The spin group is the even part of Pin and the double cover of $SO(4,\mathbb{C})$; in the biquaternion picture its two factors are the left and right copies of $\mathbb{B}$ inside $M_4(\mathbb{C})$. The finite group of the two-sided matrices is a discrete subgroup of the Clifford group, of order $32$, and its image in the orthogonal group is the group of sign changes of the frame.

This article fixes the stabilisers, proves the exact sequence, computes the Lie algebra and the dimensions, identifies the spin group and its two biquaternion factors, and places the finite extraspecial group inside the Clifford group. The frame and the five gammas are *The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$*; the finite group is *The Extraspecial Group of the Two-Sided Matrices of $M_4(\mathbb{C})$*; the real Pin group is *The Pin Group of the Gamma Frame*; the versor group and the double cover are *Biquaternion Versors and the Orthogonal Group*.

## The Action on Frames

**The action.** Let $\gamma^0,\gamma^1,\gamma^2,\gamma^3$ be a frame in $M_4(\mathbb{C})$, satisfying
$$
\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I,\qquad
g=\operatorname{diag}(1,-1,-1,-1).
$$
For $U\in GL_4(\mathbb{C})$, put
$$
U\cdot\gamma^\mu=U\gamma^\mu U^{-1}.
$$
The conjugated matrices satisfy the same relations, because conjugation preserves anticommutators and the identity. The action is a left action of $GL_4(\mathbb{C})$ on the set of frames.

**The orbit.** Over $\mathbb{C}$, any two representations of $\mathrm{Cl}(4,\mathbb{C})$ of dimension four are equivalent; the frames form a single orbit. The frame space is therefore the homogeneous space
$$
\mathcal{F}\cong GL_4(\mathbb{C})/\operatorname{Stab}(\gamma),
$$
where $\operatorname{Stab}(\gamma)$ is the stabiliser of the ordered tuple.

**The stabiliser of the tuple.** The five gammas generate $M_4(\mathbb{C})$: the sixteen antisymmetrised products are a basis. If $U$ commutes with all five, it commutes with the whole algebra, hence lies in its centre:
$$
\operatorname{Stab}(\gamma^0,\dots,\gamma^3)
=\mathbb{C}^{\times}I .
$$
This is the exact stabiliser. It has complex dimension one, and the frame space has dimension $16-1=15$.

**The reading.** The scalars are the only freedom that fixes the frame pointwise. A scalar multiple of all the gammas is the same frame in the projective sense; the phase is the kernel of the action. The frame is a section of a bundle whose fibre is the Clifford group modulo the scalars.

## The Clifford Group

**The definition.** The **Clifford group** of the frame is
$$
\Gamma=\{U\in GL_4(\mathbb{C}):U\gamma^\mu U^{-1}=\Lambda^{\mu}_{\ \nu}\gamma^\nu
\text{ for some }\Lambda\in O(4,\mathbb{C})\}.
$$
It is the stabiliser of the **span**
$$
V_\gamma=\operatorname{span}_{\mathbb{C}}\{\gamma^0,\gamma^1,\gamma^2,\gamma^3\},
$$
not of the tuple.

**The map to the orthogonal group.** The assignment $U\mapsto\Lambda$ is a group homomorphism
$$
\pi:\Gamma\longrightarrow O(4,\mathbb{C}).
$$
It is surjective: every orthogonal transformation of $V_\gamma$ is a product of reflections, and each reflection is implemented by a vector of $V_\gamma$, which lies in $\Gamma$. Its kernel is the set of $U$ acting trivially on $V_\gamma$, which is the stabiliser of the tuple:
$$
\ker\pi=\mathbb{C}^{\times}I .
$$

**The exact sequence.** Therefore
$$
\boxed{\;1\longrightarrow\mathbb{C}^{\times}\longrightarrow\Gamma
\longrightarrow O(4,\mathbb{C})\longrightarrow1\;}
$$
is exact. The sequence does not split canonically: the spin group is a double cover of $SO(4,\mathbb{C})$, not a subgroup mapping isomorphically.

**The dimension.** The orthogonal group $O(4,\mathbb{C})$ has dimension $6$, and the kernel has dimension one; hence
$$
\dim_{\mathbb{C}}\Gamma=7 .
$$
The Clifford group is a complex algebraic group of dimension seven.

**The biquaternion form.** Over $\mathbb{C}$, the Clifford group is the product of the scalars with the Pin group,
$$
\Gamma=\mathbb{C}^{\times}\cdot\mathrm{Pin}(4,\mathbb{C}),
$$
and its even part is
$$
\Gamma^{+}=\mathbb{C}^{\times}\cdot\mathrm{Spin}(4,\mathbb{C}).
$$
The scalars are the kernel; the Pin group is the norm-one part. In the real Lorentzian case the corresponding group is $\mathbb{R}^{\times}\cdot\mathrm{Pin}(1,3)$, and the spin group is $\mathrm{Spin}(1,3)\cong\mathbb{B}^{\times}_1$.

## The Lie Algebra

**The Lie algebra of the Clifford group.** An element $X\in\mathfrak{gl}_4(\mathbb{C})$ is in the Lie algebra of $\Gamma$ when
$$
[X,\gamma^\mu]\in V_\gamma
$$
for every $\mu$. The solutions are the scalars and the bivectors:
$$
\boxed{\;\operatorname{Lie}\Gamma=\mathbb{C}I\oplus\Lambda^{2}V_\gamma\;}
$$
of dimension $1+6=7$.

**The proof.** The bivectors satisfy
$$
[\gamma^{\mu\nu},\gamma^\rho]
=2\bigl(g^{\nu\rho}\gamma^\mu-g^{\mu\rho}\gamma^\nu\bigr)\in V_\gamma,
$$
so $\Lambda^{2}V_\gamma$ is in the Lie algebra. The scalars commute with everything. Conversely, write $X=X_0+X_1+X_2+X_3+X_4$ in the Clifford basis. The grade-4 part of $[X,\gamma^\mu]$ comes from $X_3$, so $X_3=0$; the grade-3 part comes from $X_4$, so $X_4=0$. With $X=X_0+X_1+X_2$, the grade-0 part of $[X,\gamma^\mu]$ is $2g(X_1,\gamma^\mu)$, which vanishes for all $\mu$ only if $X_1=0$. The remaining terms are the scalar $X_0$ and the bivector $X_2$, both of which give grade-1 commutators. $\square$

**The structure.** The Lie algebra is the direct sum of the centre $\mathbb{C}I$ and the semisimple $\Lambda^{2}V_\gamma\cong\mathfrak{so}(4,\mathbb{C})$. The bracket of two bivectors is a bivector, and the centre is central. The Lie algebra is reductive, not semisimple: the centre is one-dimensional.

**The even and odd parts.** The even part of the Clifford group has Lie algebra
$$
\operatorname{Lie}\Gamma^{+}=\mathbb{C}I\oplus\Lambda^{2}V_\gamma,
$$
of dimension seven, and the spin group has Lie algebra $\Lambda^{2}V_\gamma$, of dimension six. The odd part of the Clifford group is a coset of the even part, not a subgroup; its tangent space at a point is $V_\gamma$, of dimension four, but it is not a Lie algebra, because the bracket of two vectors is a bivector.

## The Spin Group

**The theorem.** The even part of the Clifford group is the scalars times the spin group, and
$$
\mathrm{Spin}(4,\mathbb{C})\cong SL_2(\mathbb{C})\times SL_2(\mathbb{C}),
$$
of complex dimension six. It is the double cover of $SO(4,\mathbb{C})$.

**The biquaternion factors.** The complexified even Clifford algebra is
$$
\mathrm{Cl}^{+}(4,\mathbb{C})\cong M_2(\mathbb{C})\oplus M_2(\mathbb{C}),
$$
and its two simple ideals are two copies of $\mathbb{B}$. The spin group is the norm-one part of the product of their unit groups,
$$
\mathrm{Spin}(4,\mathbb{C})\cong\bigl(B^{\times}_1\times B^{\times}_1\bigr)/\{\pm1\},
$$
the quotient by the simultaneous sign. In the Kronecker factorisation $M_4(\mathbb{C})\cong\mathbb{B}\otimes\mathbb{B}$, the two copies are realized by the left and right multiplication images
$$
M_2\otimes I\quad\text{and}\quad I\otimes M_2 .
$$
The left factor is the Lorentz action on the spinor; the right factor is the chirality action. The mass block mixes the two; it is the off-diagonal block of *The Rank-Two Split of $M_4(\mathbb{C})$*.

**The real case.** For the real Lorentzian algebra, the even part is the single biquaternion algebra, and
$$
\mathrm{Spin}(1,3)\cong\mathbb{B}^{\times}_1\cong SL_2(\mathbb{C}),
$$
of real dimension six. The double cover of $SO^{+}(1,3)$ is the versor map $b\mapsto(\eta\mapsto b\eta b^{*})$ of *Biquaternion Versors and the Orthogonal Group*. The complex case doubles the factor because the complexification splits the even part into two copies.

**The double cover.** The map
$$
\mathrm{Spin}(4,\mathbb{C})\longrightarrow SO(4,\mathbb{C})
$$
is two-to-one with kernel $\{\pm1\}$. In the biquaternion form the kernel is the image of the simultaneous sign $(-1,-1)$ under the quotient by $\{\pm1\}$.

## The Stabilisers

**The three groups.** The frame has three nested stabilisers:
$$
\mathbb{C}^{\times}I
\;\subset\;
\Gamma
\;\subset\;
GL_4(\mathbb{C}),
$$
with
$$
\operatorname{Stab}(\gamma)=\mathbb{C}^{\times}I,\qquad
\operatorname{Stab}(V_\gamma)=\Gamma .
$$
The first fixes the five matrices; the second fixes their span up to an orthogonal transformation; the third fixes nothing.

**The dimensions.**

| group | condition | dimension |
|---|---|---|
| $\operatorname{Stab}(\gamma)$ | $U\gamma^\mu U^{-1}=\gamma^\mu$ | $1$ |
| $\Gamma$ | $U\gamma^\mu U^{-1}=\Lambda^\mu_{\ \nu}\gamma^\nu$ | $7$ |
| $GL_4(\mathbb{C})$ | — | $16$ |
| $O(4,\mathbb{C})$ | $\Lambda$ orthogonal | $6$ |
| $\mathrm{Spin}(4,\mathbb{C})$ | even part, norm one | $6$ |

**The projective quotients.** The projective Clifford group is
$$
P\Gamma=\Gamma/\mathbb{C}^{\times}I\cong O(4,\mathbb{C}),
$$
of dimension six. The projective frame stabiliser is trivial: a frame is a point of $GL_4/\mathbb{C}^{\times}I$. The projective spin group is $SO(4,\mathbb{C})$, and the spin group is its double cover.

**The finite subgroup.** The thirty-two matrices $\pm T_{\mu\nu}$ form a finite subgroup
$$
G\subset\Gamma,\qquad |G|=32,
$$
extraspecial $Q_8\circ Q_8$. Its image in $O(4,\mathbb{C})$ is the group of sign changes of the four gammas,
$$
\pi(G)\cong(\mathbb{Z}/2)^{4},\qquad |\pi(G)|=16,
$$
and its kernel is $\{\pm I\}$. Every element has determinant $1$, so $G\subset SL_4(\mathbb{C})$. The finite group is a discrete shadow of the continuous Clifford group: it preserves the frame up to signs, not up to a general Lorentz transformation.

**The even part of the finite group.** The subgroup of $G$ whose image in $O(4,\mathbb{C})$ has an even number of sign changes has order $16$; its image is the order-eight group of even sign changes, which lies in $SO(4,\mathbb{C})$. It is a finite subgroup of the even Clifford group, and its spinor action is by left multiplication.

## The Physical Reading

**The frame is a choice.** The Clifford relations are the invariant object; the five gammas are a section. A change of frame is a conjugation by $GL_4(\mathbb{C})$, and the physics that depends only on the Clifford relations is invariant under the Clifford group. The five-element subset is invariant only under the scalars.

**The symmetry groups.** The Clifford group is the symmetry of the Clifford relations; the spin group is the Lorentz symmetry of the spinor; the scalars are the phase freedom of the frame. The three have different dimensions and different actions, and conflating them is the common error.

**The gauge group.** The Standard Model gauge group is not a subgroup of the Clifford group. It is an external structure on the spinor module, not a conjugation of the frame. The Clifford group contains the Lorentz group and the phase, and no more. This is the exact sense in which the gauge layer is an import; the replacement of the Clifford notation by the biquaternion calculus does not change it.

**The biquaternion reading.** The spin group is the norm-one biquaternion group; the Clifford group adds the scalars; the frame stabiliser is the scalars alone. The two chiral factors of the complex spin group are the left and right copies of $\mathbb{B}$; the mass block is the off-diagonal mixing. The finite extraspecial group is the discrete skeleton of the two-sided basis.

## Summary

The frame is a single orbit of $GL_4(\mathbb{C})$ with stabiliser $\mathbb{C}^{\times}I$, of dimension one. The Clifford group $\Gamma$, the stabiliser of the span of the gammas, fits in the exact sequence
$$
1\longrightarrow\mathbb{C}^{\times}\longrightarrow\Gamma\longrightarrow O(4,\mathbb{C})\longrightarrow1,
$$
has dimension seven, and has Lie algebra $\mathbb{C}I\oplus\Lambda^{2}V_\gamma$. Its even part is $\mathbb{C}^{\times}\cdot\mathrm{Spin}(4,\mathbb{C})$, and the spin group is $SL_2(\mathbb{C})\times SL_2(\mathbb{C})$, the double cover of $SO(4,\mathbb{C})$, of dimension six. The two factors are the left and right copies of $\mathbb{B}$ inside $M_4(\mathbb{C})$. The finite group $G=\{\pm T_{\mu\nu}\}$ of order $32$ is a subgroup of $\Gamma$; its image in $O(4,\mathbb{C})$ is the sign group $(\mathbb{Z}/2)^4$ of order $16$, and its determinant is $1$. The frame stabiliser is the scalars; the even Clifford group is the scalars times the spin group, and the full Clifford group is the scalars times the Pin group; the spin group is the biquaternion versor group in the real case and the product of the two biquaternion factors in the complex case.

| object | value |
|---|---|
| frame space | $GL_4(\mathbb{C})/\mathbb{C}^{\times}I$, dimension $15$ |
| frame stabiliser | $\mathbb{C}^{\times}I$, dimension $1$ |
| Clifford group | $\Gamma$, dimension $7$ |
| exact sequence | $1\to\mathbb{C}^{\times}\to\Gamma\to O(4,\mathbb{C})\to1$ |
| Lie algebra | $\mathbb{C}I\oplus\Lambda^{2}V_\gamma$, dimension $7$ |
| even Clifford group | $\mathbb{C}^{\times}\cdot\mathrm{Spin}(4,\mathbb{C})$, dimension $7$ |
| spin group | $SL_2(\mathbb{C})\times SL_2(\mathbb{C})$, dimension $6$ |
| real spin group | $\mathbb{B}^{\times}_1\cong SL_2(\mathbb{C})$, dimension $6$ |
| projective Clifford group | $O(4,\mathbb{C})$, dimension $6$ |
| finite subgroup | $G=\{\pm T_{\mu\nu}\}$, order $32$ |
| image of $G$ | $(\mathbb{Z}/2)^4$, order $16$ |
| determinant of $G$ | $1$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\gamma^\mu$ | the four gammas of the frame |
| $V_\gamma$ | the span of the four gammas |
| $\Gamma$ | the Clifford group of the frame |
| $\Gamma^{+}$ | its even part |
| $\mathrm{Spin}(4,\mathbb{C})$ | the spin group, the even part of Pin |
| $\mathrm{Pin}(4,\mathbb{C})$ | the pin group of the complex space |
| $O(4,\mathbb{C})$ | the complex orthogonal group |
| $T_{\mu\nu}$ | the two-sided operator $L_\mu R_\nu$ |
| $G$ | the finite group $\{\pm T_{\mu\nu}\}$ |
| $\mathbb{B}^{\times}_1$ | the norm-one biquaternion group |

## Further Reading

- [The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$](the-gamma-frame-and-the-complexified-dirac-algebra-of-m4c.html), for the frame, the Clifford relations and the action of $GL_4$.
- [The Extraspecial Group of the Two-Sided Matrices of $M_4(\mathbb{C})$](the-extraspecial-group-of-the-two-sided-matrices-of-m4c.html), for $G\cong Q_8\circ Q_8$ and its representations.
- [The Pin Group of the Gamma Frame](the-pin-group-of-the-gamma-frame.html), for the real Pin group and the finite gamma group.
- [Biquaternion Versors and the Orthogonal Group](biquaternion-versors-and-the-orthogonal-group.html), for the spin group as a biquaternion group and the double cover.
- [The Star and the Conjugate-Linear Operators of $M_4(\mathbb{C})$](the-star-and-the-conjugate-linear-operators-of-m4c.html), for the two Clifford dictionaries.
- [The Kronecker Factorisation $M_4(\mathbb{C})\cong M_2(\mathbb{C})\otimes M_2(\mathbb{C})$](the-kronecker-factorisation-of-m4c.html), for the left and right copies of $\mathbb{B}$.
- [The Rank-Two Split of $M_4(\mathbb{C})$](the-rank-two-split-of-m4c.html), for the chiral blocks and the mass block.
- [The $\mathbb{Z}$-Grading and the Odd Slot of $M_4(\mathbb{C})$](the-z-grading-and-the-odd-slot-of-m4c.html), for the five gammas inside the two-sided basis.
