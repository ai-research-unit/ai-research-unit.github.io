
# __The Involution on the Translation Operators__

## Introduction

The translation operators $T_a f(x) = f(a^{-1}x)$ are the action of the group on its own functions, and an **involution** $\sigma$ of the group acts on them by $T_a \mapsto T_{\sigma(a)}$. For the involution $\sigma(a) = a^{-1}$ the operator it produces is exactly the **adjoint**: $T_a^{*} = T_{a^{-1}}$, by the invariance of the Haar measure. The passage to the adjoint is therefore the operator form of the inversion of a group element, and the operator that implements the inversion geometrically — the **reversing symmetry** — is the one induced by the inversion map $x \mapsto x^{-1}$, which is an anti-automorphism of the group and swaps the left and the right translations. On an abelian group the inversion is an automorphism, the involution on the elements and the adjoint on the operators coincide, and the identity of the two-structures theorem of *The Adjoint of a Symmetry Operator* holds; on a nonabelian group the inversion is an anti-automorphism, and the identity is the statement that the adjoint realises the inversion on the operators, not the agreement of an automorphism with the adjoint.

The article treats the translation operators and their adjoint, the involution they carry, the reversing symmetry, and the worked cases. The translation operators, their invariance and their convolution algebra are *The Translation Operator on a Symmetry Group*, the operator whose adjoint is computed; the adjoint of a single operator and the two-structures theorem are *The Adjoint of a Symmetry Operator*; the unitary operators and the regular representation are *Unitary Operators of a Symmetry Group*, the second article of this group; the Haar measure and its invariance are *Locally Compact Groups and Haar Measure*; the Fourier analysis of the abelian case is *The Fourier Transform and Conjugate Symmetry* and *Convolution Operators*; and the characters and the nonabelian case are *Noncommutative Harmonic Analysis* and *The Plancherel Theorem*, all in Part III or Part II and cited. The adjoint of the general signed operator is *The Signed Adjoint Sandwich on a Symmetry Group*, the next article; the involution on the elements of the group was the previous group `- * Theory`.

The article has four sections: the translation operators and their adjoint; the involution on the translations; the reversing symmetry; and the worked cases. Throughout, $G$ is a locally compact group, $dx$ a left Haar measure, $L^2(G)$ the space of square-integrable functions, $T_a f(x) = f(a^{-1}x)$ the left translation and $S_a f(x) = f(xa)$ the right translation, and $\sigma$ an involution of $G$.

## The Translation Operators and Their Adjoint

### The Operators

**Definition.** The **translation operator** by $a$ is the operator on the functions of the group

$$
T_a : L^2(G) \longrightarrow L^2(G), \qquad (T_a f)(x) = f(a^{-1}x),
$$

and the right translation is $S_a f(x) = f(xa)$; the assignment $a \mapsto T_a$ is the left regular representation and $a \mapsto S_a$ the right one, of *The Translation Operator on a Symmetry Group*.

**Proposition.** The translations satisfy $T_a T_b = T_{ab}$, $S_a S_b = S_{ab}$, they commute, $T_a S_b = S_b T_a$, and the inverses are $T_a^{-1} = T_{a^{-1}}$, $S_a^{-1} = S_{a^{-1}}$; each is unitary for the invariant measure when $G$ is unimodular.

**Proof.** The composition and inverse rules are associativity in $G$; the commutation is $T_a S_b f(x) = f(a^{-1}xb) = S_b T_a f(x)$; unitarity is the invariance of the Haar measure, *The Translation Operator on a Symmetry Group*.

### The Adjoint

**Theorem.** The adjoint of the left translation is the left translation by the inverse,

$$
T_a^{*} = T_{a^{-1}} = T_a^{-1}, \qquad\text{and}\qquad S_a^{*} = S_{a^{-1}},
$$

with respect to the invariant inner product of $L^2(G)$.

**Proof.** $\langle T_a f, h\rangle = \int f(a^{-1}x)\overline{h(x)}\,dx$; the change of variable $y = a^{-1}x$ gives $dx = dy$ by left invariance, so $= \int f(y)\overline{h(ay)}\,dy = \langle f, T_{a^{-1}}h\rangle$, hence $T_a^{*} = T_{a^{-1}}$; the right case is the same computation. This is a special case of *The Adjoint of a Symmetry Operator* for the isometry $T_a$.

## The Involution on the Translations

### The Induced Involution

**Definition.** An involution $\sigma$ of $G$ induces the operator on the translations

$$
\tau_{\sigma} : T_a \longmapsto T_{\sigma(a)},
$$

and it extends to the algebra they generate by linearity; when $\sigma$ is inner, $\sigma = \operatorname{Ad}_h$, the induced map is the conjugation by $T_h$.

**Proposition.** The map $\tau_{\sigma}$ is well defined on the translation operators, it is the identity exactly when $\sigma = \mathrm{id}$, and it is an involution of the family $\{T_a\}$ exactly when $\sigma$ is an involution of $G$; it preserves the group law of the translations precisely when $\sigma$ is an automorphism, $\tau_{\sigma}(T_aT_b) = T_{\sigma(a)\sigma(b)} = T_{\sigma(ab)} = \tau_{\sigma}(T_{ab})$.

**Proof.** The well-definedness is that $a = b$ implies $\sigma(a) = \sigma(b)$; the involution property is $\tau_{\sigma}^2 = \mathrm{id}$ from $\sigma^2 = \mathrm{id}$; the preservation of the law is the multiplicativity of an automorphism. For an anti-automorphism $\sigma$ the composition reverses, $\tau_{\sigma}(T_aT_b) = T_{\sigma(b)\sigma(a)}$.

### The Inversion

**Proposition.** The **inversion** $\iota(a) = a^{-1}$ induces the map $T_a \mapsto T_{a^{-1}} = T_a^{-1}$ on the translations, which is the **operator inversion**; it is an involution of the family, it reverses the composition law,
$$
\tau_{\iota}(T_aT_b) = T_{(ab)^{-1}} = T_{b^{-1}a^{-1}} = T_{b^{-1}}T_{a^{-1}} = \tau_{\iota}(T_b)\,\tau_{\iota}(T_a),
$$
and it is an automorphism of the family exactly when $G$ is abelian.

**Proof.** The inversion is an anti-automorphism of $G$, $(ab)^{-1} = b^{-1}a^{-1}$, so the induced map reverses the composition; it is an automorphism exactly when $G$ is abelian, since an anti-automorphism is an automorphism exactly then. This is the elementary group theory of the inversion of a group.

**Remark.** The inversion is the only involution of the group that is natural for the translation operators, and it is the operator instance of the general fact that the adjoint of an isometry is its inverse: the involution $\iota$ on the elements corresponds to the inversion of the operator on the operators, and the two agree through the adjoint below.

## The Adjoint and the Reversing Symmetry

### The Adjoint Realises the Inversion

**Theorem (the two structures for translations).** The adjoint of the left translation is the image of the inversion involution on the operator,

$$
T_a^{*} = T_{a^{-1}} = \tau_{\iota}(T_a),
$$

so the involution of the elements and the adjoint on the operators **coincide** for the translation operators with the inversion: the identity $\rho(\sigma(a)) = \rho(a)^{*}$ of *The Adjoint of a Symmetry Operator* holds with $\rho = T$ and $\sigma = \iota$. When $G$ is abelian the inversion is an automorphism and the identity is the abelian case of the two-structures theorem; when $G$ is nonabelian the inversion is an anti-automorphism and the identity holds as an equation of operators, realising the inversion on the operators rather than matching an automorphism with the adjoint.

**Proof.** The operator identity is the adjoint theorem above; the comparison with the two-structures criterion $\rho(g\sigma(g)) = \operatorname{id}$ is $T_aT_{a^{-1}} = T_e = \operatorname{id}$, which holds always, and the abelian obstruction of the theorem — that an automorphic $\sigma$ forces an abelian image — is consistent because for nonabelian $G$ the map $\iota$ is not an automorphism.

### The Reversing Symmetry

**Definition.** The **reversing symmetry** is the operator on the functions induced by the inversion of the group,
$$
C : L^2(G) \longrightarrow L^2(G), \qquad (Cf)(x) = f(x^{-1}),
$$
which is an involution, $C^2 = \mathrm{id}$.

**Proposition.** The reversing symmetry swaps the left and the right translations,
$$
C\,T_a\,C = S_a, \qquad C\,S_a\,C = T_a,
$$
because the inversion is an anti-automorphism; it is unitary when the bi-invariant measure exists ($G$ unimodular) and has $\lVert C\rVert = 1$ in general; and it intertwines the inversion on the translations, $C\,T_a = S_a\,C$.

**Proof.** $(C T_a C f)(x) = (T_a C f)(x^{-1}) = (Cf)(a^{-1}x^{-1}) = f((a^{-1}x^{-1})^{-1}) = f(xa) = (S_a f)(x)$; the other identity is the same with $a$ replaced by $a^{-1}$. The unitarity is the invariance of the measure under the inversion, which holds exactly for a unimodular group, *Locally Compact Groups and Haar Measure*.

**Remark.** The reversing symmetry is the geometric reason the adjoint of a translation is the translation by the inverse: the inversion of the group contragredient to the left multiplication is the right multiplication, and its composition with the left translation realises the inverse. On the function space, the inversion is the "reversal" of the argument, and it is the simplest **reversing symmetry** — a symmetry that reverses the sense of a one-parameter flow, the operator form of the time reversal of *Time Reversal and the Transfer Operator*.

### The Abelian Case

**Proposition.** On an abelian group the translations $T_a = S_a$ coincide with the right translations, the reversing symmetry satisfies $C T_a C = T_a$, and the Fourier transform diagonalises the translations: on the character $\chi$ the operator $T_a$ acts by the scalar $\chi(a)^{-1}$, and its adjoint by the conjugate scalar $\chi(a)$,
$$
\widehat{T_a f}(\chi) = \chi(a)^{-1}\hat f(\chi), \qquad \widehat{T_a^{*} f}(\chi) = \chi(a)\hat f(\chi) = \overline{\chi(a)^{-1}}\,\hat f(\chi),
$$
so the inversion involution corresponds to the complex conjugation of the Fourier multiplier.

**Proof.** On an abelian group the left and right translations coincide by commutativity; the Fourier transform diagonalises the translations by the characters of the dual group, and the adjoint multiplies by the complex conjugate scalar, *The Fourier Transform and Conjugate Symmetry* and *Convolution Operators*. The inversion of the group sends the character $\chi$ to its conjugate $\bar\chi$, which is the conjugation of the multiplier.

## Worked Cases

**Example (the line and the plane).** Let $G = \mathbb{R}^n$ with the Lebesgue measure; the translation $T_a f(x) = f(x-a)$ has adjoint $T_a^{*} = T_{-a} = T_a^{-1}$, the reversing symmetry is $Cf(x) = f(-x)$, and the Fourier transform diagonalises $T_a$ by the character $e^{-i a\cdot\xi}$, so the adjoint multiplies by $e^{+ia\cdot\xi}$, the complex conjugate. The example is the original and simplest case.

**Example (the circle).** Let $G = \mathbb{T} = \mathbb{R}/\mathbb{Z}$ with the rotations; the translations are the rotations of the circle, the adjoint of the rotation by $\theta$ is the rotation by $-\theta$, and on the Fourier basis $e^{2\pi i n x}$ the operator $T_\theta$ acts by $e^{-2\pi in\theta}$, the adjoint by $e^{+2\pi in\theta}$. The inversion sends $\theta$ to $-\theta$ and the Fourier coefficient to its conjugate; the example is the compact abelian case.

**Example (the finite cyclic group).** Let $G = \mathbb{Z}/n$; the translation $T_a$ is the cyclic shift, its adjoint is the shift by $-a$, and the discrete Fourier transform diagonalises the family; the inversion is the reflection of the group, and the adjoint is the conjugate transpose of the circulant matrix of the shift. The example is the finite abelian case, the discrete form of the line.

**Example (a nonabelian group).** Let $G$ be nonabelian and $\rho = T$ the left regular representation; the adjoint of $T_a$ is $T_{a^{-1}}$ still, but the inversion $\iota(a) = a^{-1}$ is **not** an automorphism, so the involution of the elements it defines is an anti-automorphism and the two-structures identity is the operator identity $T_a^{*} = \tau_{\iota}(T_a)$ rather than the matching of an automorphism with the adjoint. The reversing symmetry swaps the left and right regular representations, and the nonabelian Fourier analysis is *Noncommutative Harmonic Analysis* and *The Plancherel Theorem*. The example is the boundary the abelian two-structures case does not cross.

## Summary

The left translation $T_a f(x) = f(a^{-1}x)$ has adjoint $T_a^{*} = T_{a^{-1}}$, by the invariance of the Haar measure, and the right translation the same; an involution $\sigma$ of the group induces the map $\tau_{\sigma}(T_a) = T_{\sigma(a)}$ on the translations, which is an involution of the family exactly when $\sigma$ is an involution of the group and preserves the composition law exactly when $\sigma$ is an automorphism. The natural involution is the **inversion** $\iota(a) = a^{-1}$, an anti-automorphism, and the adjoint realises it, $T_a^{*} = \tau_{\iota}(T_a)$, so the involution of the elements and the adjoint on the operators **coincide** for the translation operators; on an abelian group the inversion is an automorphism and this is the abelian case of the two-structures theorem of *The Adjoint of a Symmetry Operator*, while on a nonabelian group the identity holds as the operator form of the inversion. The **reversing symmetry** $Cf(x) = f(x^{-1})$ implements the inversion, is unitary for a unimodular group, and swaps the left and right translations, $C T_a C = S_a$; on an abelian group the Fourier transform diagonalises the translations and the adjoint is the conjugate multiplier. The adjoint of the general signed operator is the next article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_a f(x) = f(a^{-1}x)$ | the left translation operator |
| $S_a f(x) = f(xa)$ | the right translation operator |
| $T_a T_b = T_{ab}$, $T_a^{-1} = T_{a^{-1}}$ | the group law and the inverse |
| $T_a^{*} = T_{a^{-1}}$ | the adjoint of a translation |
| $\sigma$, $\tau_{\sigma}(T_a) = T_{\sigma(a)}$ | an involution and the induced operator on the translations |
| $\iota(a) = a^{-1}$ | the inversion; an anti-automorphism |
| $T_a^{*} = \tau_{\iota}(T_a)$ | the adjoint realises the inversion |
| $Cf(x) = f(x^{-1})$ | the reversing symmetry |
| $C T_a C = S_a$ | the reversing symmetry swaps left and right translations |
| $\widehat{T_a f}(\chi) = \chi(a)^{-1}\hat f$ | the abelian Fourier diagonalisation |

## Further Reading

- Lynn H. Loomis, *An Introduction to Abstract Harmonic Analysis* (Van Nostrand, 1953), for the translation operators, the Haar measure and the adjoint of a translation.
- Walter Rudin, *Fourier Analysis on Groups* (Interscience, 1962), for the abelian Fourier transform, the characters and the adjoint as the conjugate multiplier.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis I* (Springer, 1963), for the left and right translations, the modular function and the inversion.
- Sigurdur Helgason, *Groups and Geometric Analysis* (Academic Press, 1984), for the translation operators, the convolution algebra and the invariant differential operators.
- Anthony W. Knapp, *Representation Theory of Semisimple Groups* (Princeton University Press, 1986), for the left and right regular representations and their intertwiners.
